#12 visuals 2 table
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


temps = pd.DataFrame()
temps['Year'] = ('2012', '2022')
temps['Temperature'] = (24.2,27.2)

st.subheader("st.table")
st.table(temps)

st.subheader("st.table in a narrow column")
col1,col2 = st.columns((5,10))
col1.table(temps)

st.subheader("st.dataframe")
st.dataframe(temps)
