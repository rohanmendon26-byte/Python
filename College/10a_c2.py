import pandas as pd 
import plotly.express as px

runs_scored=pd.read_csv("AusVsInd.csv")

fig=px.line(runs_scored,x="Overs",y=["IND","AUS"],markers=True)
fig.update_layout(title="Australia vs india ODI Match",xaxis_title="OVERS",yaxis_title="RUNS",legend_title="Country")
fig.show()