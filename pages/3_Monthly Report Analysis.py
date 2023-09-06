import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import plotly.express as px
import pycountry
import plotly.graph_objects as go

hotel = pd.read_csv("hotel_bookings.csv")

st.title("Monthly Report Analysis")
st.write("Analyze the cancellation trend throughout the months of the year, associated with the total guests staying in the hotel in those same months. Based on this information, this plot can assist management to calculate revenue.")

month_options = hotel["arrival_date_month"].unique()
month_options = sorted(month_options, key=lambda x: pd.to_datetime(x, format='%B'))

month = st.selectbox("Select a Month", month_options, 0)

selected_month_data = hotel[hotel['arrival_date_month'] == month]

guests_per_month = selected_month_data['adults'] + selected_month_data['children'] + selected_month_data['babies']
total_guests = guests_per_month.sum()

cancellations_per_month = selected_month_data['is_canceled'].sum()

chart_data = {'Total Guests': total_guests,'Cancellations': cancellations_per_month}

st.bar_chart(chart_data, use_container_width=True, color=["#0000ff"])

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Guests", total_guests)

with col2:
    st.metric("Cancellations", cancellations_per_month)

with col3:
    if cancellations_per_month > 0:
        cancellation_percentage = (cancellations_per_month / total_guests) * 100
        st.metric("Cancellation Rate", cancellation_percentage, f"{cancellation_percentage:.2f}%", delta_color="inverse")

st.title("AVG Daily Rate/Month")
st.write("Analyze the revenue trend throughout the months of the year. This will show average daily rate per month to identify peak seasons and periods with low demand.")
monthly_adr = hotel.groupby("arrival_date_month")["adr"].mean().reset_index()
monthly_adr['arrival_date_month'] = pd.to_datetime(monthly_adr['arrival_date_month'], format='%B')
monthly_adr = monthly_adr.sort_values('arrival_date_month')
st.line_chart(monthly_adr.set_index("arrival_date_month"))