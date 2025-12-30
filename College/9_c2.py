import plotly.express as px
df=px.data.gapminder().query("continent=='Asia'")
fig=px.line_3d(df,x="gdpPercap",y="pop",z="year",color="country",title="Economic evolution of asian countries over time")
fig.show()