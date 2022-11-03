import pyperclip
import streamlit as st
import PyQt5


def format_clipboard_query():
    return ", ".join(repr(s) for s in pyperclip.paste().split("\r\n"))


if st.button('Copy to Clipboard'):
    format_clipboard_query()
