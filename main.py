import streamlit as st
import pyperclip
import io


def format_clipboard_query():
    return ", ".join(
        repr(s.strip()) for s in io.StringIO(pyperclip.paste()))


if st.button('Covert Clipboard'):
    format_clipboard_query()
    st.write("Done!")
