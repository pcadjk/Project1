import streamlit as st
import pandas as pd

st.set_page_config(page_title="Vintrash Electronic",
    page_icon="🔆",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title('Jueves Vintrash Electronica/Latino 🔆')
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
