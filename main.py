import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import json
from sql_formatter.core import format_sql
# import sqlparse
import re
from st_btn_select import st_btn_select

st.set_page_config(
    page_title="SQL Formatter",
    page_icon=":shark:")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("streamlit.css")

with st.container():
    def column_formatter():
        def sql_data_format(user_text, checked):
            if checked == True:
                return "(" + ", ".join(repr(s) for s in user_text.replace(',', "").split()) + ")"
            elif checked == False:
                updated_text = ", ".join(
                    repr(s) for s in user_text.replace(',', "").split())

                final_text = ""
                for i, letter in enumerate(updated_text):
                    if i % 80 == 0 and i != ',':
                        final_text += '\n'
                    final_text += letter
                return final_text

        def java_extract(user_text):
            if 'StringBuilder()' in user_text:
                user_text = user_text.split('\n', 1)[-1]
                new_text = """"""
                for line in user_text.splitlines():
                    new_text += re.sub('^.*(.append.")', '',
                                       line).replace('")', '').replace('sql =', '')
            else:
                new_text = """"""

                for line in user_text.splitlines():
                    new_text += re.sub('^.*(\+)', '',
                                       line).replace('"', '').replace('sql =', '')
            return new_text

        st.header("SQL Formatter")

        user_text = st.text_area(
            'Enter a list of items to format for a SQL query, an entire query to format for readability,\nor java code containing a query to remove the java and format the query', height=500)

        checked = False
        if st.checkbox("Add Parathesis (Only for Format Data)"):
            checked = True

        selection = st.radio(
            'None', ("Format Data", "Format Query", "Remove Java"), label_visibility='hidden')

        if st.button('Run'):
            if selection == "Format Data":
                try:
                    st.code(sql_data_format(user_text, checked))
                except:
                    st.text("Error: Please provide data for formatting.")
            elif selection == "Remove Java":
                st.code(format_sql(java_extract(user_text)))
            elif selection == "Format Query":
                st.code(format_sql(user_text))

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
