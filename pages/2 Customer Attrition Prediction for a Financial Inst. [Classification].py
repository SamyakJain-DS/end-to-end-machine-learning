import numpy as np
import pandas as pd
import pickle
import streamlit as st

data = pd.read_csv(r'E:\Machine Learning Project\Customer Attrition\attrition_data.csv')
with open(r'E:\Machine Learning Project\Customer Attrition\attrition_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open(r'E:\Machine Learning Project\Customer Attrition\attrition_pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)
order = ['country', 'gender', 'credit_score', 'age', 'tenure', 'acc_balance', 'prod_count', 'has_card', 'is_active', 'estimated_salary']

st.subheader("Please Enter the Following Details of Your Customer:")
st.write('')
with st.form("prediction_form"):
    one, two = st.columns(2, gap='large')
    with one:
        age = st.slider("Age", min_value=18)
        gender = st.selectbox("Gender", ('Male', 'Female'))
        st.write('')
        prod_count = st.slider("Products Owned", min_value=0, max_value=4)
        has_card = 1 if st.selectbox("Do They Own Your Credit Card", ('Yes', 'No')) == 'Yes' else 0
        is_active = 1 if st.selectbox("Have They Been Active Recently?", ("Yes", "No")) == 'Yes' else 0
    with two:
        country = st.selectbox("Country", ('France','Germany','Spain'))
        st.write('')
        tenure = st.slider("Member For (Years)", min_value=0)
        acc_balance = st.number_input("Account Balance", min_value=0.00, step=0.01)
        st.write('')
        credit_score = st.number_input("Credit Score", min_value=0.00, step=0.01)
        estimated_salary = st.number_input("Estimated Salary", min_value=0.00, step=0.01)

    submit = st.form_submit_button("Predict")

st.subheader("Output:")
st.write('')
if submit:
    query = {
        'country': country,
        'gender': gender,
        'credit_score': credit_score,
        'age': age,
        'tenure': tenure,
        'acc_balance': acc_balance,
        'prod_count': prod_count,
        'has_card': has_card,
        'is_active': is_active,
        'estimated_salary': estimated_salary
    }
    query = pd.DataFrame([query])
    query = pipeline.transform(query)
    prediction = model.predict(query)
    if prediction[0] == 0:
        st.error("The Customer Has High Chances Of Leaving.")
    else:
        st.success("The Customer Shows No Signs Of Leaving!")

# Footer
st.markdown("---")
st.markdown("""
<p style='text-align: center;'>
🔗 Built by Samyak Jain | Powered by Streamlit & scikit-learn <br>
<a href='https://www.kaggle.com/code/kiiroisenkoxx/predicting-customer-attrition-for-financial-inst'>Kaggle Notebook</a> | 
<a href='https://github.com/SamyakJain-DS/end-to-end-machine-learning'>GitHub Repo</a> | 
<a href='https://www.linkedin.com/in/samyakjain-ds/'>LinkedIn</a> | 
<a href='mailto:samyakjain2411@gmail.com'>E-Mail</a>
</p>""", unsafe_allow_html=True)