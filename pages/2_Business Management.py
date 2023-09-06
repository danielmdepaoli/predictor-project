import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import plotly.express as px
import pycountry
import plotly.graph_objects as go

st.set_page_config(layout="centered")

st.title("Business Management Tool")
st.subheader("Data Visualization", divider="blue")

hotel = pd.read_csv("hotel_bookings.csv")
st.dataframe(hotel)



st.subheader("Monthly Report Analysis")
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

# st.sidebar.title("Monthly Metrics")
# st.sidebar.subheader("Summary")


col4, col5 = st.columns(2)

st.write("Analyze the revenue trend throughout the months of the year. This will show revenue per month to identify peak seasons and periods with low demand.")

with col4:
    distribution_channel_counts = hotel['distribution_channel'].value_counts()
    st.header("Distribution Channel Categories")
    st.bar_chart(distribution_channel_counts, use_container_width=True)

with col5:
    st.header("AVG Daily Rate/Month")
    monthly_adr = hotel.groupby("arrival_date_month")["adr"].mean().reset_index()

    # Convert month names to datetime objects
    monthly_adr['arrival_date_month'] = pd.to_datetime(monthly_adr['arrival_date_month'], format='%B')
    monthly_adr = monthly_adr.sort_values('arrival_date_month')

    st.line_chart(monthly_adr.set_index("arrival_date_month"))

st.write("---")


st.header("Country of Origin")
st.write("Analyze the revenue generated from different countries can help hotels identify their main customer segments and tailor marketing strategies accordingly.")
country_codes = hotel['country']
hotel['total_guests'] = hotel['adults'] + hotel['children'] + hotel['babies']
country_guests = hotel.groupby('country')['total_guests'].sum().reset_index()
country_names = []

for code in country_guests['country']:
    try:
        country = pycountry.countries.get(alpha_3=code)
        country_names.append(country.name)
    except Exception:
        country_names.append('Unknown')
country_guests['country_name'] = country_names
fig = px.choropleth(country_guests, locations='country_name', locationmode='country names',
                        color='total_guests', color_continuous_scale='blues',
                        title='Total Guests by Country',
                        labels={'total_guests': 'Total Guests', 'country_name': 'Country'})
st.plotly_chart(fig)


st.write("---")

st.header("Market Segment")
st.write("Analyze the different market segments that the hotel caters to. This identifies which segments bring in the most revenue.")

segment_counts = hotel["market_segment"].value_counts()

fig = go.Figure(data=[go.Pie(labels=segment_counts.index, values=segment_counts.values)])

fig.update_layout(showlegend=True)

st.plotly_chart(fig)






col6, col7 = st.columns(2)

with col6:
    st.header("Deposit Type Distribution")
    deposit_type_counts = hotel['deposit_type'].value_counts()
    st.bar_chart(hotel['deposit_type'].value_counts())

with col7:
    meal_customer_counts = pd.crosstab(hotel['meal'], hotel['customer_type'])
    meal_customer_percentages = meal_customer_counts.div(meal_customer_counts.sum(axis=1), axis=0) * 100
    st.header("Meal Type by Customer Type")
    st.markdown("(Percentage)")
    st.bar_chart(meal_customer_percentages, use_container_width=True)















