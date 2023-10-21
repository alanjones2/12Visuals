import pandas as pd
import matplotlib.pyplot as plt

gwdec = pd.read_csv('./tempbydecade.csv', delimiter=' ')
gwdec=gwdec.set_index('Year')

import seaborn as sns
fig, ax = plt.subplots()
sns.heatmap(gwdec)
fig
      