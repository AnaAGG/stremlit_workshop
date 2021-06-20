import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

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



def model(df,x,y):
    clf = RandomForestClassifier()
    clf.fit(x, y)
    
    prediction = int(clf.predict(df))
    prediction_proba = clf.predict_proba(df)

    dict_pred = {0 : "Iris setosa", 
                1 : "Iris versicolor", 
                2 : "Iris virginica"}

    pred = dict_pred[prediction]

    pred_proba = prediction_proba

    return pred, pred_proba