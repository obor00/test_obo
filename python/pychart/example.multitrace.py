import numpy as np
import plotly.graph_objs as go
import plotly

a = np.random.normal(0,1,100)
b = np.random.normal(-2,5,100)

c = np.random.normal(0,1,100)
d = np.random.normal(-2,5,100)
x = np.linspace(0, 1, 100)

fig = plotly.tools.make_subplots(rows=2,cols=1)

fig.append_trace(go.Scatter(x = x, y = b, opacity = 0.75, name = 'benign'),1,1)
fig.append_trace(go.Scatter(x = x, y = a, opacity = 0.75, name = 'malignant'),1,1)
fig.layout.update(go.Layout(barmode = 'overlay',))

plotly.offline.plot(fig)
