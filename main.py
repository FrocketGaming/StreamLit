import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import json

st.set_page_config(
    page_title="SQL Formatter",
    page_icon=":shark:")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


with st.container():
    def column_formatter():
        def format_sql(user_text, checked):
            if checked == True:
                return "(" + ", ".join(repr(s) for s in user_text.replace(',', "").split()) + ")"
            elif checked == False:
                return ", ".join(repr(s) for s in user_text.replace(',', "").split())

        st.header("SQL Formatter")

        user_text = st.text_area(
            'Enter column data or a series of data you wish to format', height=500, placeholder="""Data, Data, Data

OR

Data
Data
Data""")

        checked = False
        if st.checkbox("Add Parathesis"):
            checked = True
        if st.button('Modify'):
            try:
                st.code(format_sql(user_text, checked))
            except:
                st.text("Error: Please provide data for formatting.")

    def json_formatter():
        def pretty_json(text):
            text = json.loads(text)
            return json.dumps(text, indent=4, sort_keys=True)

        st.header("JSON Formatter")

        user_text = st.text_area(
            'Paste the JSON data to format', height=500, placeholder="""[{"id":11111,"name":"Data","Codes":["Text","Text","Text"],"bool":true}]""")

        if st.button('Format'):
            try:
                st.code(pretty_json(user_text))
            except:
                st.text("Error: Please provide JSON data.")

local_css("streamlit.css")

selected = option_menu(
    menu_title=None,
    options=["SQL Formatter", "JSON Formatter",
             "Ftr Feature"],
    icons=["columns", "bricks", "bricks"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0px",
                      "display": "grid",
                      "margin": "0!important",
                      "background-color": "#23212c"
                      },
        "icon": {"color": "#8bff80", "font-size": "14px"},
        "nav-link": {
            "font-size": "14px",
            "text-align": "center",
            "margin": "auto",
            "background-color": "#23212c",
            "height": "30px",
            "width": "13rem",
            "color": "#7970a9",
            "border-radius": "5px"
        },
        "nav-link-selected": {
            "background-color": "#454158",
            "font-weight": "300",
            "color": "#f7f8f2",
            "border": "1px solid #fe80bf"
        }
    }
)

if selected == "SQL Formatter":
    column_formatter()
elif selected == "JSON Formatter":
    json_formatter()
if selected == "Ftr Feature":
    pass


# Background Color - #23212c
# Comment Color - #7970a9
# Selection Color - #454148
# Foreground Color - #f7f8f2
# Cyan Color - #80ffea
# Green Color - #8bff80
# Orange Color - #ffc97f
# Pink Color - #fe80bf
# Purple Color - #9580FF
# Red Color - #fe947f
# Yellow Color - #ffff80
