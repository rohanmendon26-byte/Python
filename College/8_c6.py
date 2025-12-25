from bokeh.plotting import figure,output_file,show
p=figure(min_width=800,min_height=400)
x=[1,2,5,7,9]
y1=[2,5,4,6,8]
y2=[5,9,11,12,15]
p.varea(x=x,y1=y1,y2=y2)
output_file('area.html')
show(p)