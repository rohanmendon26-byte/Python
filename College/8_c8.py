import numpy as np
from bokeh.plotting import figure, output_file, show
from math import pi

x = np.linspace(0, 2*pi, 100)
y = np.sin(x)

p = figure()

# circles MUST have size or radius
p.circle(x, y, size=6, legend_label='sin(x)')
p.line(x, y, legend_label='sin(x)')

# correct multiplier and legend
p.line(x, 2*y, legend_label='2*sin(x)', line_color='green')

p.legend.location = 'bottom_left'

output_file("Rectangle.html")
show(p)
