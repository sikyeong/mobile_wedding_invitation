import streamlit as st
import home

st.set_page_config(
    page_title="Mobile Wedding Invitation",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="collapsed"
    )

home.app()