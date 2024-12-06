# import streamlit as st

'''
# TaxiFareModel front
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

# url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

import streamlit as st
import pandas as pd
from datetime import datetime
import requests

st.title("NY Taxi Fare Prediction")

st.markdown("Enter the ride details below to get a taxi fare estimate.")

date = st.date_input("Date of the ride", datetime.now().date())
time_of_day = st.time_input("Time of the ride", datetime.now().time())

pickup_latitude = st.number_input("Pickup Latitude", value=0.0, format="%.6f")
pickup_longitude = st.number_input("Pickup Longitude", value=0.0, format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", value=0.0, format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude", value=0.0, format="%.6f")

passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=1)

pickup_datetime = datetime.combine(date, time_of_day)

if st.button("Get Fare Prediction"):
    params = {
        "pickup_datetime": pickup_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count,
    }

    url = "https://taxifare.lewagon.ai/predict"

    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json().get("fare", "No prediction available")
        st.success(f"The predicted fare is: ${prediction:.2f}")
    else:
        st.error("Error in API call. Please try again.")
