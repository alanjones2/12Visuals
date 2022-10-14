#12 visuals 7 bar
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

medals =  pd.read_csv('data/2022WinterOlympics.csv')

st.subheader("Olympic medals table")
st.table(medals)

fig, ax = plt.subplots()
medals.plot.bar(x='Country', y='Total', xlabel='', ax=ax)
st.pyplot(fig)

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

st.subheader('The zero baseline problem')

fig, ax = plt.subplots()
plt.bar(x=['Now','Then'], height = [35.0,39.6], color = 'darkorange')
ax.set_ylim([34,42])
ax.text(0, 35.5, '35%',
        verticalalignment='top', horizontalalignment='center',
        color='black', fontsize=12)
ax.text(1, 40, '39.6%',
        verticalalignment='top', horizontalalignment='center',
        color='black', fontsize=12)
st.pyplot(fig)

fig, ax = plt.subplots()
plt.bar(x=['Now','Then'], height = [35.0,39.6], color = 'darkorange')
ax.text(0, 33.5, '35%',
        verticalalignment='top', horizontalalignment='center',
        color='white', fontsize=12)
ax.text(1, 38, '39.6%',
        verticalalignment='top', horizontalalignment='center',
        color='white', fontsize=12)
st.pyplot(fig)