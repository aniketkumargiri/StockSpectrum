import warnings
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Ignore all warnings
warnings.filterwarnings("ignore")


def stock_prediction_lstm(df):
    # Preprocessing the dataset
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
    df.index = df["Date"]
    df = df[["Close"]]
    df.dropna(inplace=True)

    # Scaling the dataset using the same scaler used for training
    data = df.values
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)

    # Creating sequences for the dataset
    x = []
    time_steps = 90
    for i in range(time_steps, len(scaled_data)):
        x.append(scaled_data[i - time_steps : i, 0])
    x = np.array(x)

    # Pad sequences to match expected length of 180
    x = pad_sequences(x, maxlen=180, dtype="float32", padding="pre", truncating="pre")

    # Loading the trained LSTM model
    loaded_model = load_model("lstm_stock_prediction_model.h5")

    # Making predictions using the loaded model
    prediction = loaded_model.predict(x)

    # Inverse transform the predictions to get actual stock prices
    prediction = scaler.inverse_transform(prediction)

    # Create a new DataFrame for validation with predicted prices
    validation = df[time_steps:].copy()
    validation["Predicted_Price"] = prediction

    # # Creating DataFrames for validation and predictions
    # df_validation_pred = pd.DataFrame(
    #     {"Actual": validation["Close"].values, "Predicted": prediction.flatten()}
    # )

    # # Printing the Comparison DataFrame
    # st.dataframe(df_validation_pred)

    # Plotting actual vs predicted prices
    plt.figure(figsize=(12, 6))
    plt.plot(validation.index, validation["Close"], label="Actual Price", color="blue")
    plt.plot(validation.index, prediction, label="Predicted Price", color="red")
    plt.title("Actual vs Predicted Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    st.pyplot()
