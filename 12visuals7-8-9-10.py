#12 visuals 7 bar
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

medals =  pd.read_csv('data/2022WinterOlympics.csv')

st.subheader("Olympic medals table")
st.table(medals)

# Note this does not make sense, of course
st.subheader("A Plot of the mean temperature")
fig, ax = plt.subplots()
medals[medals['Country']=='Norway'].plot.bar(x='Country', ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
medals.plot.bar(x='Country', ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
medals.plot.barh(x='Country', ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
medals.plot.bar(x='Country', stacked = True, ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
medals.plot.barh(x='Country', stacked = True, ax=ax)
st.pyplot(fig)
