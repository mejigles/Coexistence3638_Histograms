import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import pandas as pd
import plotly.offline as pyo

fileName= 'C:\Users\local.Iglesias\PycharmProjects\PlotHistograms\PlotHistograms_Radius.csv'
data_df = pd.read_csv(fileName)
dt_col = list(data_df.columns.values)

x0 = data_df['IntLevel_50kmRadius']
x1 = data_df['IntLevelOutsideRadius']
#x2 = data_df['V'alues_40km']

trace0 = go.Histogram(
    x=-x0,
    histnorm='percent',
    xbins=dict(
        start=0,
        end=70,
        size=1
    ),
    name='Sectors inside a 5 km radius',
    marker=dict(
        color='RGB(182,202,79)',
    ),
    opacity=0.75
)

trace1 = go.Histogram(
    x=-x1,
    histnorm='percent',
    xbins=dict(
        start=0,
        end=70,
        size=1
    ),
    name='Sectors outside a 5 km radius',
    marker=dict(
        color='RGB(15,158,177)',
    ),
    opacity=0.75
)

#trace2 = go.Histogram(
#    x=-x2,
#    histnorm='percent',
#    xbins=dict(
#        start=0,
 ##       end=70,
 #       size=1
 #   ),
#    name='Values in 20 - 40 km buffer',
#    marker=dict(
#        color='RGB(129,39,94)',
#    ),
#    opacity=0.75
#)


data = [trace0, trace1]#, trace2]

layout = go.Layout(
    autosize=False,
    width=1000,
    height=500,
    barmode = 'overlay',
    xaxis=dict(
        title='Interference margin value (dB)'
    ),
    yaxis=dict(
        title='No. failed sectors'
    ),
    legend=dict(
        x=0,
        y=1,
        traceorder='normal',
        font=dict(
            family='sans-serif',
            size=14,
            color='#000'
        ),
        #bgcolor='#E2E2E2',
        #bordercolor='#FFFFFF',
        #borderwidth=2
    ),

)

fig = go.Figure(data=data, layout=layout)


pyo.plot(fig, filename='HistogramIntMargin_Radius_25102018.html')