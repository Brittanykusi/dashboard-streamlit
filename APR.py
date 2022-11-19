import pandas as pd
import numpy as np
import streamlit as st


# load data
LastMDVisit = 'lastmdvisit'
RAW_DATA = ('streamlit_data.csv')

def load_data(nrows):
    data = pd.read_csv(RAW_DATA, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[LastMDVisit] = pd.to_datetime(data[LastMDVisit])
    return data

# Load 10,000 rows of data into the dataframe.
data = load_data(5000)

# title
st.title('Active Patient Report')
#subheader
st.subheader('Raw data')
st.write(data)

#subheader
st.subheader('Number of appts by day of the month')
# generate histogram
hist_values = np.histogram(data[LastMDVisit].dt.day, 
        bins=31, range=(0,31))[0]
# draw histogram
st.bar_chart(hist_values)

#subheader
st.subheader('Gender Counts')
chart_data = st.bar_chart(data=data['gender'], width=0, 
        height=0, use_container_width=True)


