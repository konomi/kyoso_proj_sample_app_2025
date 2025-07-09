import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Donation 💰")

st.sidebar.success("Select a demo above.")

df = pd.read_csv('data.csv')
df
s =df.describe()
s

