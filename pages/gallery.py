import streamlit as st
import os
from PIL import Image

def app():
    st.title("Our Gallery")

    # Load gallery images from data/gallery_images/
    gallery_dir = "data/gallery_images"
    gallery_images = [str(p.path) for p in os.scandir(gallery_dir) if p.is_file() and not p.path.endswith('.json')]

    result_container = st.container()
    column_cnt = 4
    recognition_result_container = result_container.columns(column_cnt)
    for i, comp_img in enumerate(gallery_images):
        recognition_result_container[i % column_cnt].image(
            f"{comp_img}", use_column_width=True
        )

if __name__ == "__main__":
    app()