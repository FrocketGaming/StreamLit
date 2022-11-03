import pyperclip
import streamlit as st
import PyQt5

st.set_page_config(
    page_title="=SQL Formatter",
)


def format_clipboard_query(value):
    return ", ".join(repr(s) for s in value.split("\n"))


value = st.text_area('Enter values to modify', height=500)

if st.button('Modify'):
    st.write(format_clipboard_query(value))
