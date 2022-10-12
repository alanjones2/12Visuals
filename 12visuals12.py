#12 visuals 12 square area
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.header('Square area chart')
st.write('Comparing bar, stacked bar and square area chart')
st.write('''
There have been scare stories in the press about an increase in the risk of bowel cancer in those who eat processed meat. 
The percentage of the general population who will suffer from bowel cancer is around 6% and of those the processed meat 
eaters are around 1%.
Here's how we might represent this increased risk.
''')

# total population: 100
# cancer sufferers: 6
# cancer sufferers who eat bacon in excess: 1

st.subheader('First a vertical bar chart')

fig, ax = plt.subplots(figsize=(8,5))

plt.bar(['Cancer-free','Contracted cancer by chance','Contracted cancer and is a Bacon Eater'],[94,6,1])
plt.xticks(rotation = 45)

ax.set_ylabel('Percentage')
ax.set_title('Occurance of Bowel Cancer in a Population')

st.pyplot(fig)

st.subheader('Second, a stacked bar that serves as an area chart')

fig, ax = plt.subplots()
ax.bar('Instances of Cancer', 94,label='Cancer-Free')
ax.bar('Instances of Cancer', 6, label='Contracted cancer by chance')
ax.bar('Instances of Cancer', 1, label='Contracted cancer and is a Bacon Eater')
st.pyplot(fig)

st.subheader('Last, a square area chart')
# construct a 2D array of 0s - total pop
a = [0]*100
b = np.array(a).reshape((10,10))

# add a 2 by 3 rectangle of 1s representing csncer sufferers
for i in range(8,10):
    for j in range(7,10):
        b[i,j] = 1

# add a single cell with value 2
# representing the number of cancer sufferers 
# who eat too much bacon
b[9,9] = 2

# Plot the grid as a heat map in Seaborn
fig, ax = plt.subplots(figsize=(8,5))
sns.heatmap(b, 
            linewidths=0.5, 
            yticklabels=False,
            xticklabels=False, 
            cmap=['lightblue','royalblue','midnightblue'],
            ax=ax)

# Customize legend
colorbar = ax.collections[0].colorbar 
colorbar.set_ticks([0.5,1,1.5])
colorbar.set_ticklabels(['Cancer-free','Contracted cancer by chance','Contracted cancer and is a Bacon Eater'])

ax.set_title('Occurance of Bowel Cancer in a Population')
st.pyplot(fig)