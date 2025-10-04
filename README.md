# Internet Speed Test Web App

This project is a **Streamlit-based web application** that allows users
to run internet speed tests directly from their browser. It measures
download, upload, and ping speeds, then stores the results for history
and visualization.
Live Demo: https://oluwatomi-omotoso-netpulse.streamlit.app/

---

## Features

- Runs internet speed tests (download, upload, ping).
- Displays results in real-time using Streamlit UI.
- Saves results in `history.csv` for persistent storage.
- Plots speed history using line charts.

---

## Requirements

- Python 3.8+
- Streamlit
- Speedtest-cli
- Pandas

Install dependencies with:

```bash
pip install streamlit speedtest-cli pandas
```

---

## How to Run

1.  Clone this project or download the code.
2.  Run the app with:

```bash
streamlit run app.py
```

3.  The app will open in your browser automatically.

---

## File Structure

    .
    ├── app.py          # Main application file
    ├── history.csv     # Stores speed test history
    └── README.md       # Documentation (this file)

---

## Deployment

This app can be deployed on **Streamlit Cloud** for free.\
When hosted, Streamlit Cloud keeps the `history.csv` persistent during
the session, but resets if the app restarts. For long-term storage,
consider connecting to a database (like SQLite or Firebase).

---

## Example Output

- Download Speed: 45.23 Mbps
- Upload Speed: 10.87 Mbps
- Ping: 34 ms

---

## Author

Oluwatomi Omotoso

Developed for **CSC 334 (Python programming II)** Assignment.
