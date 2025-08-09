import streamlit as st

st.set_page_config(page_title="ML Models Showcase", layout="centered")

# Title and subtitle
st.markdown("<h1 style='text-align: center;'>Welcome to my ML Models Showcase</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Your AI-powered tool for Flight Price and Customer Churn Prediction</h4>", unsafe_allow_html=True)
st.markdown("---")

# What is PredictX
st.markdown("### 🚀 What is this website?")
st.markdown("""
This is an **interactive, AI-driven web application** that brings the power of machine learning to your fingertips.

I created this platform to showcase my machine learning projects, some of which were originally developed as part of **Kaggle Competition Notebooks**.  
For the flight price prediction model and customer attrition model presented here, my scores were within **0.015-0.02 points** of the competition's top-ranked solutions.
""")
# What can you do
st.markdown("### 🎯 What Can You Do Here?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### ✈️ Flight Price Prediction")
    st.text('')
    st.text('')
    st.markdown("""
    Enter your travel details – like source, destination, airline, date, and duration – and get an instant price estimate for your flight ticket.  
    Powered by a **regression model** trained on real flight data.
    """)
    if st.button("Go to Flight Price Predictor"):
        st.switch_page("pages/1 Flight Price Prediction [Regression].py")
    
    st.text('')
    st.markdown("#### ✉️ E-Mail/SMS Spam Classification")
    st.markdown("""
                Paste your e-mail or SMS message, or upload a file, and instantly find out if it's spam or genuine.  
                Powered by a **classification model** trained to detect unwanted and fraudulent messages.
                """)
    if st.button("Go to E-Mail/SMS Spam Classifier"):
        st.switch_page("pages/3 E-Mail Spam Detector.py")

with col2:
    st.markdown("#### 🧍‍♂️ Customer Attrition Prediction")
    st.markdown("""
    Simulate customer profiles and predict whether a customer will churn or stay with a financial institution.  
    Powered by a **classification model** trained to detect behavior patterns.
    """)
    if st.button("Go to Customer Attrition Predictor"):
        st.switch_page("pages/2 Customer Attrition Prediction for a Financial Inst. [Classification].py")
    st.text('')

# Model Performance
st.markdown("### 📊 Model Performance (Behind the Scenes)")
with st.expander("🔍 Click to view model evaluation metrics"):
    st.markdown("#### 🟢 HistGradientBoosting Regressor (Flight Prices)")
    st.markdown("""
    - **Cross-Validation R² Score:** `0.97`
    - **Test R² Score:** `0.97`
    """)
    st.markdown("#### 🔵 Extreme Gradient Boost Classifier (Customer Attrition)")
    st.markdown("""
    - **Cross-Validation F1 Score:** `0.61`
    - **Test Accuracy Score:** `0.81`
    - **Test Precision Score:** `0.55`
    - **Test Recall Score:** `0.75`
    - **Test F1 Score:** `0.63`
    """)
    st.markdown("#### 🔴 Multinomial Naive Bayes (Spam Classification)")
    st.markdown("""
    - **Test Precision Score:** `0.99`
    - **Test Recall Score:** `0.91`
    """)

# How it works
st.markdown("### 🛠️ How Does It Work?")
st.markdown("""
- You input relevant details into a simple form.
- The pre-trained machine learning model processes the input.
- You instantly receive a smart prediction backed by data science.

No technical expertise required — just intuitive design and powerful results.
""")

# Privacy
st.markdown("### 🔒 Privacy Note")
st.markdown("""
We do not store any user input. Your data is used **only temporarily** during your session for prediction purposes.
""")

# Footer
st.markdown("---")
st.markdown("""
<p style='text-align: center;'>🔗 Built by Samyak Jain | Powered by Streamlit & scikit-learn<br>
<a href='https://github.com/SamyakJain-DS/end-to-end-machine-learning'>GitHub Repo</a> | <a href='https://www.linkedin.com/in/samyakjain-ds/'>LinkedIn</a> | 
<a href='mailto:samyakjain2411@gmail.com'>E-Mail</a></p>""", unsafe_allow_html=True)
