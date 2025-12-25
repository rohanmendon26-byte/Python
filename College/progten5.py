import json
import pandas as pd
import plotly.express as px

# Load GeoJSON
with open("states_india.geojson", "r") as f:
    india_states = json.load(f)

# Load CSV
df = pd.read_csv("india_census.csv")

# Create state name → id mapping
state_id_map = {}

for feature in india_states["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]

# Clean density column
df["Density"] = df["Density[a]"].apply(
    lambda x: int(str(x).split("/")[0].replace(",", ""))
)

# Map state names to ids
df["id"] = df["state or union territory"].apply(
    lambda x: state_id_map.get(x)
)

print(df.head())

# Plot choropleth
fig = px.choropleth(
    df,
    geojson=india_states,
    locations="id",
    color="population",
    hover_name="state or union territory",
    hover_data=["Density", "sex ratio", "population"],
    title="India Population State-wise"
)

fig.update_geos(fitbounds="locations", visible=False)
fig.show()
