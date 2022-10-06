#12 visuals 6 slopegraph
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("Slope graph")

st.subheader("Here is the data")
df = pd.DataFrame()
df['year']=[2012,2022]
df['London']=(24.2,27.2)
df['Wick']=(14.8,17.3)

st.table(df)

st.subheader("A Slopegraph as a line graph")
fig, ax = plt.subplots()

ax = df.plot(x='year', color = ('red', 'blue'), ax=ax)
ax = df.plot.scatter(x='year',y='London', color= 'red', ax=ax)
df.plot.scatter(x='year',y='Wick', color = 'blue', ax=ax)

plt.xlim(2010,2024)
plt.xticks(df['year'])
ax.set_ylabel('')
st.pyplot(fig)

st.subheader("A more conventionally styled Slopegraph")
ax.text(df.year[0] -5, df.London[0], df.columns[1])
ax.text(df.year[0] -2.5,df.London[0], f'{df.London[0]}°C')
ax.text(df.year[1] +1, df.London[1],f'{df.London[1]}°C')
ax.text(df.year[0] -5, df.Wick[0], df.columns[2])
ax.text(df.year[0] -2.5, df.Wick[0],f'{df.Wick[0]}°C')
ax.text(df.year[1] +1, df.Wick[1],f'{df.Wick[1]}°C')

ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.xaxis.grid(visible=True, color = 'black')
ax.get_yaxis().set_visible(False)

ax.get_legend().set_visible(False)

st.pyplot(fig)

