import streamlit as st
import requests


st.markdown('''
# Taxi Fare Predictor

Welcome to my incredibly accurate NY taxi fare predictor. I hope you know the exact lattitude and longitude of where you are going...
''')



taxi_date = st.date_input("Input date of taxi ride")
taxi_time = st.time_input("Input time of taxi ride")
taxi_datetime = f"{taxi_date} {taxi_time} UTC"

pickup_lon = st.number_input("Input pickup longitude", value=40.761)
pickup_lat = st.number_input("Input pickup lattitude", value=-73.979)
dropoff_lon = st.number_input("Input dropoff longitude", value=40.651)
dropoff_lat = st.number_input("Input dropoff lattitude", value=-73.880)

pass_count = st.number_input("Input number of passengers", min_value=0, value=1)

url = 'https://taximodel-vcr7nfhyda-ew.a.run.app/predict_fare/'
params = {
    "key": "2012-10-06 12:10:20.0000001",
    "pickup_datetime": taxi_datetime,
    "pickup_longitude": float(pickup_lon),
    "pickup_latitude": float(pickup_lat),
    "dropoff_longitude": float(dropoff_lon),
    "dropoff_latitude": float(dropoff_lat),
    "passenger_count": int(pass_count)
}

response = requests.get(
    url,params=params
).json()['prediction']

st.markdown('''
## Taxi Price:
''')

taxi_fare = f"${round(response, 2)}"

taxi_fare
