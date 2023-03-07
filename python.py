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

st.write(df)

st.sidebar.header('User Input Parameters')
