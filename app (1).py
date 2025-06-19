import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Load and clean data
df = pd.read_csv('AAPL.csv', parse_dates=['Date'], dayfirst=True)
df.set_index('Date', inplace=True)

# Clean and prepare
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df.dropna(subset=['Close'], inplace=True)
df.sort_index(inplace=True)
df.index = pd.to_datetime(df.index)
df = df.asfreq('B')  # ✅ Ensures proper frequency for time series

# Streamlit UI
st.title("📈 Apple Stock Price Forecast (Next 30 Days)")

if st.button("Predict"):
    st.info("Generating forecast...")

    try:
        # Use data excluding last 30 days for training
        train_data = df['Close'][:-30]

        # Create future business dates
        last_date = df.index[-1]
        future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=30, freq='B')

        # Fit SARIMA model
        model = SARIMAX(train_data, order=(5, 1, 0), seasonal_order=(1, 1, 1, 12))
        results = model.fit(disp=False)

        # Forecast
        forecast = results.forecast(steps=30)
        forecast_df = pd.DataFrame({'Forecast': forecast.values}, index=future_dates)

        # Display forecast table
        st.subheader("📊 Forecasted Closing Prices")
        forecast_df_display = forecast_df.copy()
        forecast_df_display.index = forecast_df_display.index.strftime('%Y-%m-%d')

        st.dataframe(forecast_df_display.style.format("{:.2f}"))


        # Plot forecast
        st.subheader("📈 Forecast Chart")
        plt.figure(figsize=(12, 5))
        plt.plot(df['Close'][-90:], label='Actual Price')
        plt.plot(forecast_df['Forecast'], label='Forecasted Price', color='red')
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)

        # Optional: Download forecast
        csv = forecast_df.to_csv().encode('utf-8')
        st.download_button("📥 Download Forecast as CSV", csv, "forecast.csv", "text/csv")

    except Exception as e:
        st.error(f"⚠️ Forecasting failed: {e}")
