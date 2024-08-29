import pandas as pd
import plotly.express as px

data= {'fname': ['4k1','4k1', '4k1'], 'queues' : [16,32,8] , 'read_iops': [ 217425, 216766, 212657] }

df = pd.DataFrame.from_dict( data)
print(df)
fig = px.line(df, x="queues", y="read_iops", color='fname', title='title')
fig.show()

