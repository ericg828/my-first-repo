# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/126GvxKaYYSCfRFWvHgB9vVjTca_Uf5TS
"""

import streamlit as st

# Create sliders for RGB values
st.title("Background Color Changer")

red = st.slider("Red", 0, 255, 127)
green = st.slider("Green", 0, 255, 127)
blue = st.slider("Blue", 0, 255, 127)

# Convert the RGB values to hex format
hex_color = f'#{red:02x}{green:02x}{blue:02x}'

# Add background color CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {hex_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.write(f"Selected color: {hex_color}")