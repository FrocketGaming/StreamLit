import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

st.set_page_config(
    page_title="SQL Formatter",
    page_icon=":shark:"
)

with st.container():
    def column_formatter():
        def format_sql(user_text, checked):
            if checked == True:
                return "(" + ", ".join(repr(s) for s in user_text.split()) + ")"
            elif checked == False:
                return ", ".join(repr(s) for s in user_text.replace(',', "").split())

        st.header("Column Formatter")

        user_text = st.text_area(
            'Enter the data you wish to modify', height=500)

        checked = False
        if st.checkbox("Add Parathesis"):
            checked = True
        if st.button('Modify'):
            st.code(format_sql(user_text, checked))


selected = option_menu(
    menu_title=None,
    options=["Column Formatter", "Ftr Feature",
             "Ftr Feature"],
    icons=["columns", "bricks", "bricks"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0px",
                      "display": "grid",
                      "margin": "0!important"
                      },
        "icon": {"color": "#f1fa8c", "font-size": "14px"},
        "nav-link": {
            "font-size": "14px",
            "text-align": "center",
            "margin": "auto",
            "background-color": "#282a36",
            "height": "30px",
            "color": "#6272a4",
            "border-radius": "0px"
        },
        "nav-link-selected": {
            "background-color": "#282a36",
            "font-weight": "300",
            "color": "#f8f8f2",
            "border": "1px solid #ff79c6"
        }
    }
)

if selected == "Column Formatter":
    column_formatter()
if selected == "Ftr Feature":
    pass
