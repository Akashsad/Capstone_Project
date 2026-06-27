import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Human Mobility During UK Lockdowns")

url = "https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv"
df = pd.read_csv(url, parse_dates=["date"])

country = st.sidebar.selectbox("Select Country", df['country_region'].unique())
filtered = df[df['country_region'] == country]

st.write("Preview of data:", filtered.head())

fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(data=filtered, x="date", y="workplaces_percent_change_from_baseline", ax=ax)
st.pyplot(fig)
