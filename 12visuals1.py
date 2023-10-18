#12 visuals 1 simple text

import streamlit as st
import matplotlib.pyplot as plt

# Set up variables
years = ['2012','2022']
temps = [24.2,27.2]
caption = f"The maximum temperature in July 2022 was {temps[1]}°C"
caption2 =  f"That's {temps[1]-temps[0]}° up from 2012"

st.title("London Maximum Temperatures in July - 2022 v. 2012")

# Create a bar chart
st.markdown("## _Data rendered as a bar chart_")
fig, ax = plt.subplots()
plt.bar(years,temps)
plt.suptitle(caption, fontweight = 'bold')
plt.title(caption2)
st.pyplot(fig)

st.markdown("---")


st.markdown("## _Data rendered in Streamlit metric_")
col3, col4 = st.columns([1,4])
col3.metric("Temperature", temps[1],temps[0])
col4.markdown(f"#### {caption}")
col4.markdown(caption2)

st.markdown("---")

st.markdown("## _Data rendered as text in columns using markdown_")
col1, col2 = st.columns([1,4])
col1.markdown(f"# {temps[1]}")
col2.markdown(f"#### {caption}")
col2.markdown(caption2)

st.markdown("---")

st.markdown("## _Data rendered as text in columns using markdown 2_")

st.markdown(f"# {temps[1]}")
st.markdown(f"#### {caption}")
st.markdown(caption2)

st.markdown("---")


st.markdown("## _Data rendered as text in a matplotlib chart_")

fig2, ax2 = plt.subplots(figsize=(5,1))

ax2.text(0, 0.9, temps[1],
        verticalalignment='top', horizontalalignment='left',
        color='red', fontsize=18, fontweight = 'bold')
ax2.text(0.2, 0.9, caption,
        verticalalignment='top', horizontalalignment='left',
        color='Black', fontsize=10)
ax2.text(0.2, 0.55, caption2,
        verticalalignment='top', horizontalalignment='left',
        color='darkgrey', fontsize=6)

ax2.axis('off')

st.pyplot(fig2)

st.markdown("---")

st.markdown("## _Data rendered as text in an different matplotlib chart_")
fig3, ax3 = plt.subplots(figsize=(4,2))

ax3.text(0.5, 0.9, temps[1],
        verticalalignment='top', horizontalalignment='center',
        color='darkblue', fontsize=64, fontweight = 'bold')
ax3.text(0.5, 0.3, caption,
        verticalalignment='top', horizontalalignment='center',
        color='blue', fontsize=8)
ax3.text(0.5, 0.2, caption2,
        verticalalignment='top', horizontalalignment='center',
        color='lightblue', fontsize=6)

ax3.axis('off')

st.pyplot(fig3)

st.markdown("---")

st.markdown("## _Data rendered as text in an different matplotlib chart_")
fig3, ax3 = plt.subplots(figsize=(4,2))

ax3.text(0.5, 0.9, '63,000,000',
        verticalalignment='top', horizontalalignment='center',
        color='darkblue', fontsize=32, fontweight = 'bold')
ax3.text(0.5, 0.4, "Earth's Orbit in miles",
        verticalalignment='top', horizontalalignment='center',
        color='blue', fontsize=12)
ax3.text(0.5, 0.2, "That's a lot of miles",
        verticalalignment='top', horizontalalignment='center',
        color='lightblue', fontsize=10)

ax3.axis('off')

st.pyplot(fig3)