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

st.title("Country of Origin")
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
