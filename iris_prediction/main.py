import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from src.support import user_input_features, load_data

st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

#we create a sidebar on the left of the page
st.sidebar.header('User Input Parameters')

df = user_input_features()

st.subheader('User Input parameters')
st.table(df)

st.dataframe(load_data())