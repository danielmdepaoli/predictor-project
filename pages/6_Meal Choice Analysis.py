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

meal_customer_counts = pd.crosstab(hotel['meal'], hotel['customer_type'])
meal_customer_percentages = meal_customer_counts.div(meal_customer_counts.sum(axis=1), axis=0) * 100
st.title("Meal Type by Customer Type")
st.markdown("(Percentage)")
st.bar_chart(meal_customer_percentages, use_container_width=True)