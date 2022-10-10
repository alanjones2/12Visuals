#12 visuals 12 square area
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Percentage of population who will suffer from bowel cancer
# total population: 100
# cancer sufferers: 6
# cancer sufferers who eat bacon in excess: 1

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
colorbar.set_ticklabels(['Cancer-free','Cancer by chance','Bacon Eater'])

st.pyplot(fig)