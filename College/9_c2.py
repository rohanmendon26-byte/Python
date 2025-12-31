import plotly.express as px
df=px.line.data().gapminder().query("Continent=='Asia'")
fig=px.line_3d(df,)