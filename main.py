import pyperclip
import streamlit as st
import PyQt5


def format_clipboard_query(paste):
    return ", ".join(repr(s) for s in paste.split("\r\n"))


paste = st.text_input('Paste Your Values', '')

if st.button('Copy'):
    format_clipboard_query(paste)
