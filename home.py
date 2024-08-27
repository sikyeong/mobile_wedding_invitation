import streamlit as st
import json
from pages import friends_comment, gallery, bank_account, location

def app():
    st.title("Welcome to Our New day")
    st.write("We are excited to invite you to our special day!")



    # Add comment section
    location.app()
    st.write("---")
    friends_comment.app()
    st.write("---")
    gallery.app()
    st.write("---")
    bank_account.app()


if __name__ == "__main__":
    app()