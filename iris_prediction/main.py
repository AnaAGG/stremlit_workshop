import streamlit as st
import pandas as pd
from PIL import Image

from sklearn.ensemble import RandomForestClassifier
from src.support import user_input_features, load_data, model

st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

imagen = Image.open("images/flor.png")
st.image(imagen, use_column_width=True)


#we create a sidebar on the left of the page
st.sidebar.header('User Input Parameters')

df = user_input_features()

st.subheader('User Input parameters')
st.table(df)

st.dataframe(load_data())

iris = load_data()

x = iris.drop(["target"], axis = 1)
y = iris["target"]

pred, prob_pred = model (df, x, y)


st.subheader('Prediction')
st.write(pred)
   

st.subheader('Prediction Probability')
st.table(prob_pred)
