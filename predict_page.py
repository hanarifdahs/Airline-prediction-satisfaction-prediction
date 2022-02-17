import streamlit as st
import pickle
import pandas as pd

# Cara 1 manggil model


def load_model():
    with open('model_xgb.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

# Cara 2 manggil model
open_model = open('model_xgb.pkl', 'rb')
load_model = pickle.load(open_model)


def show_predict_page():
    st.title("Airline Passenger Satisfaction Prediction")
    st.write(""" ### Rate these services""")

    cust_type = (
        'yes',
        'no'
    )

    travel_type = (
        'Personal Travel',
        'Business travel'
    )

    class_type = (
        'Eco Plus',
        'Business',
        'Eco'
    )

    cust = st.radio('Do you often travel with this airline?', cust_type)
    travel = st.selectbox('Type of travel', travel_type)
    class_t = st.selectbox('Type of cabin class', class_type)
    distance = st.slider('How far was your trip? (km)', 0, 10000)
    delay = st.slider('How long was the departure delay in minutes?', 0, 2000)

    booking = st.slider('Ease of online booking', 0, 5)
    boarding = st.slider('Online boarding', 0, 5)
    checkin = st.slider('Checkin service', 0, 5)
    departure = st.slider('Departure/Arrival time convinient', 0, 5)

    wifi = st.slider('Inflight Wifi Service', 0, 5)
    clean = st.slider('Cleanliness', 0, 5)
    food = st.slider('Food and drink', 0, 5)
    inflight = st.slider('Inflight service', 0, 5)
    seat = st.slider('Seat comfort', 0, 5)
    ent = st.slider('Inflight Entertainment', 0, 5)
    onboard = st.slider('On-board service', 0, 5)
    baggage = st.slider('Baggage Service', 0, 5)
    leg = st.slider('Leg room service', 0, 5)

    pred = st.button("Predict Satisfaction")

    # Change customer type answer
    if cust == 'yes':
        cust_real = 'Loyal Customer'
    else:
        cust_real = 'disloyal Customer'

    # Predict
    if pred:
        X = pd.DataFrame({
            'Customer Type': [cust_real],
            'Type of Travel': [travel],
            'Class': [class_t],
            'Flight Distance': [distance],
            'Inflight wifi service': [wifi],
            'Departure/Arrival time convenient': [departure],
            'Ease of Online booking': [booking],
            'Food and drink': [food],
            'Online boarding': [boarding],
            'Seat comfort': [seat],
            'Inflight entertainment': [ent],
            'On-board service': [onboard],
            'Leg room service': [leg],
            'Baggage handling': [baggage],
            'Checkin service': [checkin],
            'Inflight service': [inflight],
            'Cleanliness': [clean],
            'Departure Delay in Minutes': [delay]
        })

        # Predict dengan model
        satisfaction = load_model.predict(X)

        if satisfaction == 1:
            st.subheader("This passenger is satisfied")
        else:
            st.subheader("This passenger is neutral or dissatisfied")
