import streamlit as st
import datetime
import pickle
import pandas as pd
from xgboost import XGBClassifier
import xgboost as xgb
import numpy as np

customer_mapping = {"Transient":0,"Contract":1,"Transient Party":2,"Group":3}

deposit_mapping = {"No Deposit":0,"Refundable":1,"Non Refundable":2}

meal_mapping = {"Bed & Breakfast":0,"Full Board":1,"Half Board":2,"Self Catering":3, "Undefined":4}

market_mapping = {"Direct":0,"Corporate":1,"Online Travel Agent":2,"Offline Travel Agent":3, "Complementary":4,
                  "Groups":5,"Undefined":6,"Aviation":7}

distribution_mapping = {"Direct":0,"Corporate":1,"Travel Agent/Tour Operator":2,"Undefined":3, "GDS":4}

guest_mapping = {"Yes":0, "No":1}

st.set_page_config(page_title="Hotel Booking Cancellation Predictor", page_icon=":airplane_departure:", layout="wide") # or centered


st.title("Booking Cancellation Predictor")
image_url = 'https://www.hotellinksolutions.com/images/blog/avt.jpg'
st.image(image_url, use_column_width=True)

st.header("Welcome to our Hotel Booking Web App!", divider="blue")
st.subheader("Our primary goal is to help hotels optimize their operations and revenue.")

st.write("With our 98% accurate booking cancellation predictor app, hotels can gain valuable insights into guest cancellation patterns, and optimize their operations by dynamically adjusting inventory, staff scheduling, and resource allocation. This enables your business to avoid overbooking, reduce no-shows, and minimize revenue loss. This app helps hotels make data-driven decisions, enhance your booking strategies, while improving overall revenue management, leading to better customer satisfaction and increased profitability.")
st.write("---") # line to separate (aestethic only)


st.subheader("Booking Information")

col1, col2, col3 = st.columns(3)
with col1:
    adults = st.number_input("Adults:", min_value=0)
    st.write("")
    children = st.number_input("Children:", min_value=0)
    st.write("")
    babies = st.number_input("Babies:", min_value=0)

with col2:
    adr = st.number_input("AVG Daily Rate:", min_value=0)
    customer_type = st.selectbox("Customer Type:", list(customer_mapping.keys()))
    customer_type = customer_mapping[customer_type]
    st.write("")
    deposit_type = st.selectbox("Deposit Type:", list(deposit_mapping.keys()))
    deposit_type = deposit_mapping[deposit_type]



with col3:
     required_car_parking_spaces = st.number_input("Required Parking Spaces:", min_value=0)
     st.write("")
     total_of_special_requests = st.number_input("Number of Special Requests:", min_value=0)
     st.write("")
     booking_changes = st.number_input("Changes made to the booking:", min_value=0)








st.write("---")

st.subheader("Reservation Details")

col4, col5, col6 = st.columns(3)

with col4:
    lead_time = st.number_input("Lead Time (in days):", min_value=0)
    st.write("")
    reservation_day = st.selectbox("Day of the month the reservation was made:", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                                                                       11, 12, 13, 14, 15, 15, 16, 17, 18,
                                                                                       19, 20, 21, 22, 23, 24, 25, 25, 26,
                                                                                        27, 28, 29, 30, 31])
    st.write("")
    reservation_month = st.selectbox("Month of the year the reservation was made:",[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                                                                       11, 12])

with col5:
    arrival_date_day_of_month = st.selectbox("Day of the month the guest will arrive:", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                                                                       11, 12, 13, 14, 15, 15, 16, 17, 18,
                                                                                       19, 20, 21, 22, 23, 24, 25, 25, 26,
                                                                                        27, 28, 29, 30, 31])
    st.write("")
    stays_in_week_nights = st.number_input("Week nights guest will be at the hotel:", min_value=0)
    st.write("")
    meal = st.selectbox("Meal Type:", list(meal_mapping.keys()))
    meal = meal_mapping[meal]





with col6:
    is_repeated_guest = st.radio("Is this a repeated guest?", list(guest_mapping.keys()))
    is_repeated_guest = guest_mapping[is_repeated_guest]
    st.write("")
    previous_cancellations = st.slider("Number of previously cancellated bookings:", 0, 100)
    st.write("")
    previous_bookings_not_canceled = st.slider("Number of previous bookings:", 0, 100)









col7, col8 = st.columns(2)

with col7:
     market_segment = st.selectbox("Market Segment:", list(market_mapping.keys()))
     market_segment = market_mapping[market_segment]

with col8: 
    distribution_channel = st.selectbox("Distribution Channel:", list(distribution_mapping.keys()))
    distribution_channel = distribution_mapping[distribution_channel]














def load_model():
    with open("cancellation_model.p", "rb") as model_file:
        model = pickle.load(model_file)
    return model

def predict_cancellation(user_input, model):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)
    
    return prediction

model = load_model()

if st.button("Submit"):
    user_input = {"lead_time": lead_time, "adr": adr, "adults": adults, "children": children, "babies": babies, "meal": meal, 
            "market_segment": market_segment, "distribution_channel": distribution_channel, "deposit_type": deposit_type, "customer_type": customer_type,
            "reservation_month": reservation_month, "reservation_day": reservation_day, "arrival_date_day_of_month": arrival_date_day_of_month, 
            "stays_in_week_nights": stays_in_week_nights, "is_repeated_guest": is_repeated_guest, "previous_cancellations": previous_cancellations,
            "previous_bookings_not_canceled": previous_bookings_not_canceled, "booking_changes": booking_changes, "required_car_parking_spaces": required_car_parking_spaces,
            "total_of_special_requests": total_of_special_requests}
    

    df_input = pd.DataFrame.from_dict(user_input, orient="index").T
    df_input = df_input[['meal', 'market_segment', 'distribution_channel', 'deposit_type', 'customer_type', 'reservation_month', 
                         'reservation_day', 'lead_time', 'arrival_date_day_of_month', 'stays_in_week_nights', 'adults', 'children', 'babies',
                        'is_repeated_guest', 'previous_cancellations', 
                         'previous_bookings_not_canceled', 'booking_changes', 'adr', 'required_car_parking_spaces', 'total_of_special_requests']]
    #emp = np.array(list(user_input.values()))
    #prediction = predict_cancellation(df_input, model)
    model = load_model()
    prediction = model.predict(df_input)
    if prediction[0] == 1:
        st.write("The booking is predicted to be cancelled.")
    else:
        st.write("The booking is predicted to not be cancelled.")






import streamlit as st
import pandas as pd
import pickle
import base64

def main():
    uploaded_file = st.file_uploader("Upload your business CSV file to obtain a prediction:", type=["csv"])

    if uploaded_file is not None:
        user_data = pd.read_csv(uploaded_file)

        model = load_model()

        if st.button("Predict"):
            predictions = predict_cancellation(user_data, model)
            user_data['Prediction'] = predictions 
            st.write("0 = Predicted not to be cancelled")
            st.write("1 = Predicted to be cancelled")
            st.write("Predictions:")
            st.write(user_data)
            st.markdown(get_csv_download_link(user_data), unsafe_allow_html=True)

def load_model():
    # Load your machine learning model using pickle or any other method
    with open('cancellation_model.p', 'rb') as file:
        model = pickle.load(file)
    return model

def predict_cancellation(data, model):
    predictions = model.predict(data) 
    return predictions

def get_csv_download_link(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  
    href = f'<a href="data:file/csv;base64,{b64}" download="predicted_data.csv">Download CSV</a>'
    return href

if __name__ == "__main__":
    main()










