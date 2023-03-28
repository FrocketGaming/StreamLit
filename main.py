import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import json
from sql_formatter.core import format_sql
import re
from st_btn_select import st_btn_select
import textwrap
import xml.etree.ElementTree as ET

st.set_page_config(
    page_title="SQL Formatter",
    page_icon=":shark:")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("streamlit.css")

selected = option_menu(
    menu_title=None,
    options=["SQL Formatter", "JSON Formatter",
             "XML Formatter", "CRON Placeholder"],
    icons=["code", "braces", "bricks"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0px",
                      "display": "grid",
                      "margin": "0!important",
                      "background-color": "#212121"
                      },
        "icon": {"color": "#bd93f9", "font-size": "14px"},
        "nav-link": {
            "font-size": "14px",
            "text-align": "center",
            "margin": "auto",
            "background-color": "#262626",
            "height": "30px",
            "width": "13rem",
            "color": "#edff85",
            "border-radius": "5px"
        },
        "nav-link-selected": {
            "background-color": "#212121",
            "font-weight": "300",
            "color": "#f7f8f2",
            "border": "1px solid #e55381"
        }
    }
)


def pretty_json(text):
    new_text = json.loads(text)
    return json.dumps(new_text, indent=4, sort_keys=True)


def pretty_xml(user_text):
    new_text = ET.XML(user_text)
    ET.indent(new_text)
    return ET.tostring(new_text, encoding='unicode')


def sql_data_format(user_text, checked):
    if checked == True:
        updated_text = "(" + ", ".join(repr(s)
                                       for s in user_text.replace(',', "").split()) + ")"
        return textwrap.fill(updated_text, 65)

    elif checked == False:
        if ',' in user_text or ', ' in user_text:
            user_text.replace(',', ' ')
            updated_text = ','.join(
                repr(s) for s in user_text.split(','))
            return textwrap.fill(updated_text, 65)
        elif not ', ' in user_text or ',' in user_text:
            updated_text = ", ".join(
                repr(s) for s in user_text.replace(',', "").split())
            return textwrap.fill(updated_text, 65)


def java_extract(user_text):
    new_text = """"""

    new_text += re.sub(
        '(String sql = ")|^.*(append.")|(?:\+ ")|(?:" \+)|["]', '', user_text)

    return new_text


def xml_formatter():
    st.header("XML Formatter")

    st.caption('Paste the XML data below to format')

    column = st.columns(2)

    with column[1]:
        placeholder = st.empty()
        with placeholder.container():
            st.code('')

    with column[0]:
        user_text = st.text_area(
            'xml', height=450, placeholder="Paste here", label_visibility='hidden')

        if st.button('Format'):
            try:
                with placeholder.container():
                    st.code(pretty_xml(user_text), language='xml')
            except:
                st.text("Error: Please provide xml data.")


def json_formatter():
    st.header("JSON Formatter")

    st.caption('Paste the JSON data below to format')

    column = st.columns(2)

    with column[1]:
        placeholder = st.empty()
        with placeholder.container():
            st.code('')

    with column[0]:
        user_text = st.text_area(
            'json', height=450, placeholder="Paste here", label_visibility='hidden')

        if st.button('Format'):
            try:
                with placeholder.container():
                    st.code(pretty_json(user_text), language='json')
            except:
                st.text("Error: Please provide JSON data.")


def column_formatter():
    st.header("SQL Formatter")

    st.caption("Enter a list of items to format for a SQL query, an entire query to format for readability,\nor java code containing a query to remove the java and format the query")
    column = st.columns(2)

    with column[1]:
        placeholder = st.empty()
        with placeholder.container():
            st.code('')

    with column[0]:

        user_text = st.text_area(
            'txt', height=450, placeholder='Paste here', label_visibility='hidden')

        checked = False
        if st.checkbox("Add Parathesis (Only for Format Data)"):
            checked = True

        selection = st.radio(
            'None', ("Format Data", "Format Query", "Remove Java"), label_visibility='hidden')

    if st.button('Run'):
        with column[1]:
            if selection == "Format Data":
                try:
                    with placeholder.container():
                        st.code(sql_data_format(
                            user_text, checked), language='sql')
                except:
                    st.text("Error: Please provide data for formatting.")
            elif selection == "Remove Java":
                with placeholder.container():
                    st.code(format_sql(java_extract(user_text)), language='sql')
            elif selection == "Format Query":
                with placeholder.container():
                    st.code(format_sql(user_text), language='sql')


if selected == "SQL Formatter":
    column_formatter()
elif selected == "JSON Formatter":
    json_formatter()
if selected == "XML Formatter":
    xml_formatter()
