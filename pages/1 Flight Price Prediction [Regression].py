from datetime import datetime, timedelta
import numpy as np
import os
import pandas as pd
import pickle
import streamlit as st

st.title("Flight Price Prediction Regression Model")

root_dir = os.getcwd()
data = pd.read_csv(os.path.join(root_dir,'Flight Price Prediction','cleaned_flights.csv'))
with open(os.path.join(root_dir,'Flight Price Prediction','flight_model.pkl'), 'rb') as f:
    model = pickle.load(f)
with open(os.path.join(root_dir,'Flight Price Prediction','flight_pipeline.pkl'), 'rb') as f:
    x_pipeline = pickle.load(f)
with open(os.path.join(root_dir,'Flight Price Prediction','flight_y_pipeline.pkl'), 'rb') as f:
    y_pipeline = pickle.load(f)
q1 = data['price'].quantile(0.25)
q3 = data['price'].quantile(0.75)

st.subheader("Please Enter the Following Details of Your Flight:")
st.write('')

with st.form("prediction_form"):
    one, two, three = st.columns(3)
    with one:
        departure_date = st.date_input('Date of Departure',
                                       value="today",
                                       min_value="today",
                                       max_value=datetime.today().date() + timedelta(days=365))
        destination = st.selectbox('Destination', data['destination'].unique())
        airline = st.selectbox('Airline', data['airline'].unique())

    with two:
        source = st.selectbox('Source', data['source'].unique())
        arrival_time = st.selectbox('Arrival Time', data['arrival'].unique())
        stops = st.selectbox('Number of Stops', data['stops'].unique())

    with three:
        departure_time = st.selectbox('Departure Time', data['departure'].unique())
        class_ = st.selectbox('Flight Class', data['class'].unique())
        duration = st.number_input('Duration of Flight in Hours', value=0.0, min_value=0.0, step=0.01)

    submit = st.form_submit_button('Predict')

st.subheader("Output:")
st.write('')

if submit:
    days_left = (departure_date - datetime.today().date()).days
    query = {
        'duration':duration,
        'airline':airline,
        'source':source,
        'departure':departure_time,
        'stops':stops,
        'arrival':arrival_time,
        'destination':destination,
        'class': class_,
        'days_left': days_left
    }
    query = pd.DataFrame([query])
    query = x_pipeline.transform(query)
    prediction = model.predict(query)
    prediction = np.round(y_pipeline.inverse_transform(prediction.reshape(-1, 1))[0][0],2)

    if prediction <= q1:
        st.success(f'Predicted Range of Price For Your Flight: ₹{np.round(prediction - 997.04,2):,} - ₹{np.round(prediction + 1348.94,2):,}')
    elif (prediction > q1) and (prediction <= q3):
        st.warning(f'Predicted Range of Price For Your Flight: ₹{np.round(prediction - 997.04,2):,} - ₹{np.round(prediction + 1348.94,2):,}')
    else:
        st.error(f'Predicted Range of Price For Your Flight: ₹{np.round(prediction - 997.04,2):,} - ₹{np.round(prediction + 1348.94,2):,}')

# Footer
st.markdown("---")
st.markdown("""
<p style='text-align: center;'>
🔗 Built by Samyak Jain | Powered by Streamlit & scikit-learn <br>
<a href='https://www.kaggle.com/code/kiiroisenkoxx/flight-ticket-price-prediction-model'>Kaggle Notebook</a> | 
<a href='https://github.com/SamyakJain-DS/end-to-end-machine-learning'>GitHub Repo</a> | 
<a href='https://www.linkedin.com/in/samyakjain-ds/'>LinkedIn</a> | 
<a href='mailto:samyakjain2411@gmail.com'>E-Mail</a>
</p>""", unsafe_allow_html=True)