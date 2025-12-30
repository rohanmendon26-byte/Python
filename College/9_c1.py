import plotly.graph_objects as go
import numpy as np

x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
x,y=np.meshgrid(x,y)
z=np.sin(np.sqrt(x**2+y**2))

fig=go.Figure(data=[go.Surface(x=x,y=y,z=z)])

fig.update_layout(scene=dict(xaxis_title="x axis",yaxis_title="y axis",zaxis_title="z axis"),margin=dict(l=0,r=0,b=0,t=0),title="3D surface plot of sin(sqrt(x**2+y**2))")
fig.show()