import streamlit as st
import pandas as pd
import streamlit_calendar as st_calendar
from streamlit_gsheets import GSheetsConnection

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
st.bar_chart(df)
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

st_calendar.calendar() 


# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
    