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

distribution_channel_counts = hotel['distribution_channel'].value_counts()
st.header("Distribution Channel Categories")
st.bar_chart(distribution_channel_counts, use_container_width=True)
