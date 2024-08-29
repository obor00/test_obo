import numpy as np
import plotly.graph_objs as go
import plotly
import pandas as pd
import json
from plotly.subplots import make_subplots
import plotly.express as px

# reading the data from the file
with open('perfmes.result') as f:
    data = f.read()

# reconstructing the data as a dictionary
#js = json.loads(data)
js = eval (data)
#x = js['queues']
#y = js['read_iops']
#y2 = js['write_iops']

print("Data type after reconstruction : ", type(js))
print(js)

#fig = plotly.tools.make_subplots(rows=1,cols=1)

colors = ['#3f3f3f', '#00bfff', '#ff7f00']
#fig = make_subplots(
#    rows=3, cols=2,
#    column_widths=[0.55, 0.45],
#    row_heights=[1., 1., 1.],
#    specs=[[{"type": "scatter"}, {"type": "xy"}],
#           [{"type": "scatter"}, {"type": "xy", "rowspan": 2}],
#           [{"type": "scatter"},            None           ]],
#    )
specs_list = list()
row_heigh = list()
for key in js:
    #specs_list.append([{"type": "scatter"}, {"type": "xy"}])
    specs_list.append([{"type": "xy"}, ])
    row_heigh.append( 10 )

fig = make_subplots(
    rows=len(js), cols=1,
    #column_widths=[0.55, 0.45],
    row_heights= row_heigh,
    #subplot_titles = js.keys(),
    specs= specs_list,
    x_title="queues",
    y_title="iops"
    )

num = 1
for key in js:
    sj = js[key]
    x = ['hello'] + sj['queues']
    y = ['y'] + sj['read_iops']
    df = pd.DataFrame.from_dict(sj)

    trace1 = go.Scatter( x = x, y = y, name = 'read iops')
    #data = Data([trace1])
#    layout = go.Layout(
#            showlegend=True,
#            scene=go.Scene(
#                xaxis=go.XAxis(title='x axis title'),
#                yaxis=go.YAxis(title='y axis title'),
#                )
#            )
    fig.append_trace(trace1, num, 1)
    #fig.add_trace(go.Scatter(data_frame=df),  num, 1)
    #fig.append_trace(go.Scatter( df, x = 'queues', y = 'read iops'),num,1)
    #fig.append_trace(go.Scatter( x = x, y = y, name = 'read iops'), num, 1)
    #fig.append_trace(go.Scatter(x = x, y = y2, opacity = 0.75, name = 'write iops'),num,1)
    num += 1


#fig.append_trace(go.Scatter(x = x, y = y2, opacity = 0.75, name = 'write iops'),1,1)
#fig.append_trace(go.Scatter(x = x, y = y2, opacity = 0.75, name = 'write iops'),1,2)
fig['layout'].update(height=3000)
fig.layout.update(go.Layout(barmode = 'overlay',))

plotly.offline.plot(fig)
#plotly.offline.plot(fig, filename='test.html')

