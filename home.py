import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title="Vintrash Electronic",
    page_icon="🔆",
    layout="wide",
    initial_sidebar_state="expanded"
)

image = Image.open('default.png')
st.image(image)

st.title('Jueves Vintrash Electronic/Latino 🔆')
st.write("BUCARALAND")

choice = st.radio(
        "Te regalamos un Free Pass en Vintrash 👉",       
        options=["Jueves", "Viernes", "Sabado"],
    )



