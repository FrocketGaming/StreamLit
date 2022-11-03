import pyperclip
import streamlit as st


def format_clipboard_query():
    return ", ".join(repr(s) for s in pyperclip.paste().split("\r\n"))


if st.button('Covert Clipboard'):
    format_clipboard_query()
    st.write("Done!")
