import pandas as pd
import numpy as np
import streamlit as st


# load data
LAST_VISIT_DATE_COLUMN = 'date'
DATA = ('streamlit_data.csv')

def load_data(nrows):
    data = pd.read_csv(DATA, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[LAST_VISIT_DATE_COLUMN] = pd.to_datetime(data[LAST_VISIT_DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
# @st.cache
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

# title
st.title('Active Patient Report')
#subheader
st.subheader('Raw data')
st.write(data)



