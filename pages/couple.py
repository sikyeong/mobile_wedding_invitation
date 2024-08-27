import streamlit as st
import json

def app():
    st.title("Our Couple")

    # Load couple information from data/couple_info.json
    with open("data/couple_info.json", "r") as f:
        couple_info = json.load(f)

    # Display couple information
    col1, col2 = st.columns(2)
    with col1:
        st.image("assets/images/bride.png", use_column_width=True)
        st.write(f"**{couple_info['bride']['name']}**")
        st.write(couple_info['bride']['bio'])

    with col2:
        st.image("assets/images/groom.jpg", use_column_width=True)
        st.write(f"**{couple_info['groom']['name']}**")
        st.write(couple_info['groom']['bio'])

if __name__ == "__main__":
    app()