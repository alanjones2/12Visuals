#12 visuals 5 line
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

weather =  pd.read_csv('data/london2018.csv')

# Create a mean value
weather['Tmean'] = (weather['Tmax'] + weather['Tmin'])/2

st.subheader("Weather data table")
st.table(weather)

st.subheader("A Plot of the mean temperature")
fig, ax = plt.subplots()
ax = weather.plot.line(x='Month', y = 'Tmean', ax=ax)
st.pyplot(fig)

st.subheader("A plot of the mean, max and min temperatures")
ax = weather.plot.line(x='Month', y = 'Tmax', color = 'lightgrey', ax=ax)
ax = weather.plot.line(x='Month', y = 'Tmin',  color = 'lightgrey', ax=ax)

st.pyplot(fig)

st.subheader("A plot of the mean with shaded area between max and min")
plt.fill_between(weather['Month'], 
                 weather['Tmax'],
                 weather['Tmin'], 
                 color='lightgrey')

ax.get_legend().set_visible(False)
ax.set_ylabel('Temperature Range °C')

st.pyplot(fig)