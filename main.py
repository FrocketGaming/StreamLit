import pyperclip
import streamlit as st


def format_clipboard_query(paste):
    return ", ".join(repr(s) for s in paste.split("\r\n"))


paste = st.text_input('Paste Your Values', '')

format_clipboard_query(paste)
