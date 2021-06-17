import streamlit as st
import pandas as pd
from sklearn import datasets

def load_data():
     data =  datasets.load_iris()
     df = pd.DataFrame(data.data, columns = data.feature_names)

     df2 = pd.DataFrame(data.target, columns = ["target"])

     return df.join(df2)

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4) # the sidebar.slider magic function receive the max, min and default value in out sidebar
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}

    return pd.DataFrame(data, index=[0])

