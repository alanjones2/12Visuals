import pandas as pd
temps = pd.DataFrame()
temps['Year'] = ('2012', '2022')
temps['Temperature'] = (24.2,27.2)
temps

import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(header=dict(values=['Year', 'Temperature']),
cells=dict(values=[temps['Year'], temps['Temperature']]))
])

fig.update_layout(width=500, height=250)

fig
