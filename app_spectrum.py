import streamlit as st
import pandas as pd
import matplotlib
import datetime
from datetime import datetime
import matplotlib.pyplot as plt
from app_stock_prediction import stock_prediction_lstm

matplotlib.use("Agg")
st.set_option("deprecation.showPyplotGlobalUse", False)


def upload_csv_file():
    st.success("Please upload the stocks dataset...")
    uploaded_file = st.file_uploader("", type=["csv"])
    if uploaded_file is not None:
        st.code(f'"{uploaded_file.name}" uploaded successfully!')
        df = pd.read_csv(uploaded_file)
        return df


def price_trend(df):
    plt.figure(figsize=(12, 6))
    df["Close"].plot(color="green")
    plt.title(f"Price Trend")
    plt.xlabel(None)
    plt.ylabel("Closing Price")
    plt.grid(True)
    plt.tight_layout()
    st.pyplot()


def volume_trend(df):
    plt.figure(figsize=(12, 6))
    df["Volume"].plot(color="blue")
    plt.title(f"Volume Distribution")
    plt.xlabel(None)
    plt.ylabel("Volume")
    plt.grid(True)
    plt.tight_layout()
    st.pyplot()


def ema_trend(df):
    ema_day = [8, 21, 55]
    for ema in ema_day:
        column_name = f"EMA for {ema} days"
        df[column_name] = df["Close"].ewm(span=ema, adjust=False).mean()

    df[["Close", "EMA for 8 days", "EMA for 21 days", "EMA for 55 days"]].plot(
        figsize=(12, 6)
    )
    plt.title("Exponential Moving Average Trend")
    plt.xlabel(None)
    plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()
    st.pyplot()


def deviation(df):
    rolling_mean = df["Close"].rolling(window=30).mean()
    rolling_std = df["Close"].rolling(window=30).std()
    plt.figure(figsize=(12, 6))
    plt.plot(df["Close"], label="Original")
    plt.plot(rolling_mean, label="Rolling Mean", color="r")
    plt.plot(rolling_std, label="Rolling Std", color="g")
    plt.legend(loc="best")
    plt.title("Rolling Mean & Standard Deviation")
    plt.xlabel(None)
    plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()
    st.pyplot()


def daily_trade(df):
    features = ["Open", "Close", "High", "Low"]
    axes = df[features].plot(figsize=(11, 9), subplots=True)
    for ax in axes:
        ax.set_ylabel("Daily trade")


def spectrum():
    st.title("Analysis & Prediction")
    st.markdown("")

    try:
        # 1. uploading the csv file
        df = upload_csv_file()
        if df is not None:
            df["Date"] = pd.to_datetime(df.Date, format="%Y-%m-%d")
            df.index = df["Date"]
            st.write(df)
            st.markdown("")

            st.info("1. Price w.r.t Time")
            with st.expander("Closing Price"):
                price_trend(df)
            st.markdown("")
            st.markdown("")

            st.info("2. Volume w.r.t Time")
            with st.expander("Volume"):
                volume_trend(df)
            st.markdown("")
            st.markdown("")

            st.info("3. EMA w.r.t Time")
            with st.expander("Exponential Weighted Average"):
                ema_trend(df)
            st.markdown("")
            st.markdown("")

            st.info("4. Rolling Mean & SD w.r.t Time")
            with st.expander("Rolling Mean & Standard Deviation"):
                deviation(df)
            st.markdown("")
            st.markdown("")

            st.info("5. Daily Trade w.r.t Time")
            with st.expander("Daily Trade"):
                st.pyplot(daily_trade(df))
            st.markdown("")
            st.markdown("")

            st.error("Stocks Price Prediction with LSTM")
            with st.expander("Stocks Price Prediction"):
                stock_prediction_lstm(df)

    except:
        pass
