import pyperclip
import streamlit as st
import PyQt5


def format_clipboard_query(value):
    return ", ".join(repr(s) for s in value.split("\r\n"))


value = st.text_area('Enter values to modify')

if st.button('Modify'):
    st.write('Output:', format_clipboard_query(value))
