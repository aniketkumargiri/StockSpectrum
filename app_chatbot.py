import streamlit as st
import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import unicodedata
import nltk

nltk.download("vader_lexicon")
analyzer = SentimentIntensityAnalyzer()


# Function to get sentiment label
def get_sentiment_label(score):
    if score > 0.1:
        return "Positive"
    elif score < -0.015:
        return "Negative"
    else:
        return "Neutral"


# Function to calculate sentiment scores
def get_sentiment_scores(text):
    sentence_i = unicodedata.normalize("NFKD", text)
    sentiment = analyzer.polarity_scores(sentence_i)
    sentiment_label = get_sentiment_label(sentiment["compound"])
    return sentiment["neg"], sentiment["neu"], sentiment["pos"], sentiment_label


# Function to display sentiment analysis results
def display_sentiment_analysis_results(text):
    negative_score, neutral_score, positive_score, sentiment_label = (
        get_sentiment_scores(text)
    )
    st.success(f"Sentiment: {sentiment_label}")
    # st.code(f"Negative Score: {negative_score}")
    # st.code(f"Neutral Score: {neutral_score}")
    # st.code(f"Positive Score: {positive_score}")


def chatbot():
    st.title("Stocks Sentiment Analysis Chatbot")
    st.write("")

    input_text = st.chat_input("Please enter text...")
    if input_text:
        with st.chat_message("user"):
            st.write(input_text)

        with st.spinner("Getting Sentiment Response .."):
            time.sleep(1)
            display_sentiment_analysis_results(input_text)
