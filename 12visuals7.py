#12 visuals 7 bar
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

weather =  pd.read_csv('data/temp.csv')

# Create a mean value
weather['Tmean'] = (weather['Tmax'] + weather['Tmin'])/2

st.subheader("Weather data table")
st.table(weather)

# Note this does not make sense, of course
st.subheader("A Plot of the mean temperature")
fig, ax = plt.subplots()
ax = weather.plot.bar(x='Month', y='Rain',ax=ax, stacked=True)

st.pyplot(fig)


fig, ax = plt.subplots()
speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2, 8, 70, 1.5, 25, 12, 28]
index = ['snail', 'pig', 'elephant',
         'rabbit', 'giraffe', 'coyote', 'horse']
df = pd.DataFrame({'speed': speed,
                   'lifespan': lifespan}, index=index)
df
ax = df.plot.bar(rot=0, ax=ax)

st.pyplot(fig)

