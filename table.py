import pandas as pd
import matplotlib.pyplot as plt 

temps = pd.DataFrame()
temps['Day'] = ('Yesterday', 'Today')
temps['Temperature'] = (24,29)

fig, ax = plt.subplots()

ax.axis('off')
ax.table(cellText=temps.values, 
         colLabels=temps.columns, 
         colColours =["lightgrey"]*2, 
         loc='upper left').scale(0.95, 7)
plt.show()