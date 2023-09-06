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

st.title("Market Segment")
st.write("Analyze the different market segments that the hotel caters to. This identifies which segments bring in the most revenue.")

segment_counts = hotel["market_segment"].value_counts()

fig = go.Figure(data=[go.Pie(labels=segment_counts.index, values=segment_counts.values)])

fig.update_layout(showlegend=True)

st.plotly_chart(fig)