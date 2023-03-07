# -*- coding: utf-8 -*-
"""Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Msy_qHYObmSmZRMDeTTK8CPvBbYjf1Um
"""

import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv('Advertising.csv')

st.write("""
# Number of Sales Prediction App
This app predicts the **Number of Sales**!
""")


st.sidebar.header('User Input Parameters')

def user_input_features():
    tv_value = st.sidebar.slider('TV Value', 0, 150, 300)
    radio_value = st.sidebar.slider('Radio Value', 2.0, 4.4, 3.4)
    newspaper_value = st.sidebar.slider('Newspaper Value', 1.0, 6.9, 1.3)
    data = {'TV Value': tv_value,
            'Radio Value': radio_value,
            'Newspaper Value': newspaper_value}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

sales = datasets.load_sales()
X = sales.data
Y = sales.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
