import pandas as pd

temps = pd.DataFrame()
temps['Year'] = ('2012', '2022')
temps['Temperature'] = (24.2,27.2)

import plotly.graph_objects as go

fig = go.Figure(data=[
                go.Table(header=dict(values=['Year', 'Temperature'],
                                line_color='darkslategray',
                                fill_color='lightskyblue',
                                align='left'),
                        cells=dict(values=[temps['Year'], temps['Temperature']],
                                line_color='darkslategray',
                                fill_color='lightcyan',
                                align='left')
                                )])
                    


fig.show()
