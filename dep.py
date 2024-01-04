import streamlit as st
import numpy as np
from pickle import load

st.title("Classification Model")
st.write('Bankruptcy Prevention')

with st.form("prediction_form"):
    industrial = st.sidebar.radio("Enter the Industrial Risk", [0.0, 0.5, 1.0])
    management = st.sidebar.radio("Enter the Management Risk", [0.0, 0.5, 1.0])
    financial = st.sidebar.radio("Enter the Financial Flexibility", [0.0, 0.5, 1.0])
    credible = st.sidebar.radio("Enter the Credibility", [0.0, 0.5, 1.0])
    competitive = st.sidebar.radio("Enter the competitiveness", [0.0, 0.5, 1.0])
    operating = st.sidebar.radio("Enter the Operating Risk", [0.0, 0.5, 1.0])

    submit_button = st.form_submit_button("Predict")

if submit_button:
    x = [industrial, management, financial, credible, competitive, operating]
    x = np.array(x).reshape(1, -1)

    model = load(open('clsf.pkl', 'rb'))
    prediction = model.predict(x)

    if prediction == 0:
        st.write("This Company will go Bankrupt")
    else:
        st.write("This Company will  not go Bankrupt")

        