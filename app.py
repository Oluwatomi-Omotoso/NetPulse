import streamlit as st
import speedtest, time
from datetime import datetime
import os
import pandas as pd


HISTORY_FILE = "speed_results.csv"


# Speed test
def check_speed():
    for attempt in range(3):
        try:
            stt = speedtest.Speedtest()
            server = stt.get_best_server()
            download_speed = stt.download() / 1_000_000
            upload_speed = stt.upload()
            ping = stt.results.ping
            return download_speed, upload_speed, ping, server
        except Exception as e:
            if attempt < 2:
                time.sleep(2)
                continue
            else:
                return None, None, None, None


# Save results
def save_results(download, upload, ping):
    data = {
        "time": [datetime.now().strftime("%Y-%m-%d %H:%S")],
        "download": [download],
        "upload": [upload],
        "ping": [ping],
    }
    df = pd.DataFrame(data)

    if not os.path.exists(HISTORY_FILE):
        df.to_csv(HISTORY_FILE, index=False)
    else:
        df.to_csv(HISTORY_FILE, mode="a", header=False, index=False)


# Load history
def load_history():
    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE)
    return pd.DataFrame(columns=["time", "download", "upload", "ping"])


# UI
st.set_page_config(
    page_title="Wifi Speed & Bandwidth Checker", page_icon="", layout="centered"
)
st.title("📡 WiFi Speed & Bandwidth Checker")

if st.button("Run Speed Test"):
    with st.spinner("Running test... this might take a few seconds"):
        download, upload, ping, server = check_speed()
    if download is None:
        st.error("Could not connect to Speedtest server. Please try again.")
    else:
        st.success("Test complete!")
        col1, col2, col3 = st.columns(3)
        col1.metric("Download Speed", f"{download:.2f} Mbps")
        col2.metric("Upload Speed", f"{upload:.2f} Mbps")
        col3.metric("Ping", f"{ping:.2f} ms")

    if download > 50:
        st.success("Excellent connection!")
    elif download > 20:
        st.info("Good Connection")
    elif download > 5:
        st.warning("Fair connection")
    else:
        st.error("Poor connection")

    # Server info
    lat = float(server.get("lat", 0))
    lon = float(server.get("lon", 0))
    st.write(
        f"Server: {server['host']} ({server['country']}) - {round(lat,2)}, {round(lon,2)}"
    )

    # save results
    save_results(download, upload, ping)

# History
st.subheader("Speed Test History")
history = load_history()

if not history.empty:
    st.dataframe(history.tail(10))
    st.line_chart(history.set_index("time")[["download", "upload"]])
else:
    st.write("No history yet. Run a test to start tracking.")
