import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

#df = pd.DataFrame(dict(
#    x = [1, 3, 2, 4],
#    y = [1, 2, 3, 4]
#))
df = pd.DataFrame({ 'this is x': [1, 3, 2, 4], 'yyy': [1, 2, 3, 4] })
df2 = pd.DataFrame({ 'namex': [1, 3, 2, 4], 'iiyyy': [1, 2, 3, 4] })

#fig = px.line(df, x="x", y="y", title="Unsorted Input") 
#fig.show()

df = df.sort_values(by="this is x")
fig = px.line(df, x="this is x", y="yyy", title="Sorted Input") 
fig2 = px.line(df2, x="namex", y="iiyyy", title="Sorted Input") 
#fig.show()
#fig.write_image('fig.png', engine='kaleido')
fig = go.Figure(data = fig.data + fig2.data)
fig.show()
