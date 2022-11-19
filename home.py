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
 st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["Jueves", "Viernes", "Sabado"],
    )

st.write('You selected:', option)
df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [7.11392, -73.1198],
    columns=['lat', 'lon'])

st.map(df)

