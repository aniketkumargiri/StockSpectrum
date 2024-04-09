import streamlit as st


def header():
    st.markdown(
        "<h1 style='color: Chartreuse;'>StockSpectrum</h1>", unsafe_allow_html=True
    )


def banner():
    st.image("images/page.png", use_column_width=True)


def footer():
    footer_html = """
        <style>
            .footer {
                position: fixed;
                bottom: 0;
                text-align: center;
                padding: 5px;
                color: #42f5f5;
            }
        </style>
        <div class="footer">Made with ❤️ by team DataMinds</div>
    """
    # Footer
    st.markdown(footer_html, unsafe_allow_html=True)


def home():

    # 1. header component
    header()

    # 2. banner field
    banner()

    # 3. footer component
    footer()
