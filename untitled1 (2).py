# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/126GvxKaYYSCfRFWvHgB9vVjTca_Uf5TS
"""

import streamlit as st
import pandas as pd

# Sample data for cat breeds
cats_data = [
    {"Breed Name": "Persian", "Fur Coat Color": "Gray", "Success Rate in Hunts (%)": 85, "Active": "Night"},
    {"Breed Name": "Siamese", "Fur Coat Color": "Cream", "Success Rate in Hunts (%)": 75, "Active": "Day"},
    {"Breed Name": "Maine Coon", "Fur Coat Color": "Brown", "Success Rate in Hunts (%)": 65, "Active": "Day"},
    {"Breed Name": "Bengal", "Fur Coat Color": "Spotted", "Success Rate in Hunts (%)": 90, "Active": "Night"},
    {"Breed Name": "Sphynx", "Fur Coat Color": "Hairless", "Success Rate in Hunts (%)": 50, "Active": "Night"},
]

# Convert the list to a DataFrame
df = pd.DataFrame(cats_data)

# Set the background to a cute cat picture
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://example.com/cute-cat.jpg'); /* Replace with a URL of a cute cat picture */
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("Cute Cat Breeds Info")

# Dropdown menu for sorting
sort_option = st.selectbox(
    "Sort data by:",
    ("Breed Name", "Fur Coat Color", "Success Rate in Hunts (%)", "Active")
)

# Sort the DataFrame based on the selected option
if sort_option == "Success Rate in Hunts (%)":
    sorted_df = df.sort_values(by=sort_option, ascending=False)
else:
    sorted_df = df.sort_values(by=sort_option)

# Display the sorted DataFrame
st.write(sorted_df)