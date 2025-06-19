# 📈 Apple Stock Price Forecast App

A web application to forecast Apple's stock prices for the next 30 business days using the **SARIMA time series model**. Built with **Python**, **Streamlit**, and deployed via **Streamlit Community Cloud**.

---

## 🚀 Live Demo

👉 [Click here to view the app](https://apple-stock-price-forecast-fhxjtaxfl2tyybnpjjaa8x.streamlit.app/)

---

## 📌 Features

- 📅 Forecasts Apple stock closing prices for 30 future business days
- 🔍 SARIMA model trained on historical data from **2012–2019**
- 📊 Interactive line chart comparing historical and forecasted prices
- 📋 Clean and responsive table of forecast results
- 📥 Option to **download the forecast as CSV**
- 💡 Lightweight, fast, and intuitive UI via Streamlit

---

## 🧠 Model Used

**SARIMA (Seasonal ARIMA)**  
Model order: `(5, 1, 0)(1, 1, 1, 12)`

- `p=5`: Autoregressive terms  
- `d=1`: Differencing for stationarity  
- `q=0`: No moving average terms  
- Seasonal: 12-monthly periodicity

---

## 🗂️ Files in this Repo

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit application |
| `AAPL.csv` | Apple historical stock data (2012–2019) |
| `requirements.txt` | Python dependencies for deployment |
| `README.md` | You're reading it! |

---
