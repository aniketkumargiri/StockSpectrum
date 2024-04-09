import streamlit as st
import datetime
from app_home import home
from app_spectrum import spectrum
from app_chatbot import chatbot


def main():
    st.set_page_config(page_title="StockSpectrum", page_icon="images/banner.png")
    st.markdown("")

    # # Date Component
    # date = datetime.datetime.now().strftime("%Y-%m-%d")
    # st.sidebar.success(f"Date: {date}")

    # Adding a clock component
    time = datetime.datetime.now().strftime("%H:%M:%S")
    st.sidebar.info(f"Time: {time}")

    # Navigation bar
    navbar = st.sidebar.radio("Sidebar", ["Home", "App", "Chatbot"])

    if navbar == "Home":
        home()

    elif navbar == "App":
        spectrum()

    elif navbar == "Chatbot":
        chatbot()


if __name__ == "__main__":
    main()
