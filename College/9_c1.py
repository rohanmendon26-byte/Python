import plotly.graph_objects as go
import numpy as np

# Create X and Y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Create 2D grid
X, Y = np.meshgrid(x, y)

# Compute Z values
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create 3D surface plot
fig = go.Figure(
    data=[go.Surface(x=X, y=Y, z=Z)]
)

# Update layout
fig.update_layout(
    scene=dict(
        xaxis_title='xAxis',
        yaxis_title='yAxis',
        zaxis_title='zAxis'
    ),
    margin=dict(l=0, r=0, b=0, t=40),
    title='3D surface plot of sin(sqrt(x² + y²))'
)

fig.show()
