import streamlit as st
import json
import folium
from streamlit_folium import folium_static

def app():
    st.title("Wedding Location")

    # Load location data from data/location_data.json
    with open("data/location_data.json", "r") as f:
        location_data = json.load(f)

    # Display location information
    st.write(f"**{location_data['venue_name']}**")
    st.write(location_data['address'])

    lat = location_data["coordinates"]["lat"]
    lon = location_data["coordinates"]["lon"]
    map = folium.Map(location=[lat, lon], zoom_start=16)

    st_map = folium_static(map)

if __name__ == "__main__":
    app()