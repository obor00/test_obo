
import numpy as np
import plotly.graph_objs as go
import plotly
import pandas as pd
import json
from plotly.subplots import make_subplots
import plotly.express as px

gname = 'RW70_TYrandrw'
title = gname

# reading the data from the file
with open('perfmes.result') as f:
    data = f.read()

js = eval (data)
print("Data type after reconstruction : ", type(js))

gdata = dict()
for key in js:
    if gname in key:
        newdata = js[key]
        for subkey in newdata:   #name, queues ...
            for elt in newdata[subkey]:
                if subkey not in gdata: gdata[subkey] = list()
                print(elt)
                gdata[subkey].append(elt)

print (gdata)
df = pd.DataFrame.from_dict( gdata )
df.sort_values( by=['queues'], inplace = True )
print (df)

fig = px.line(df, x="queues", y="read_iops", color='name', title=title, markers = True)
#fig.show()
fig.update_layout(
    autosize=False,
    width=600,
    height=400,)

with open('p_graph.html', 'w') as f:
    f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fig.to_html(full_html=False, include_plotlyjs='cdn'))
