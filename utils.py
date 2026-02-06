import streamlit as st
import base64


def load_openai_api() -> str:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    if not openai_api_key:
        st.error("未設定 OpenAI API 金鑰，請設置環境變數 OPENAI_API_KEY")
        st.stop()
    return openai_api_key


def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
