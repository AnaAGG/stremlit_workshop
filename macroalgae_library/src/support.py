import pandas as pd
import folium
from streamlit_folium import folium_static
from folium import Choropleth, Circle, Marker, Icon, Map
import plotly.express as px

# Function to load the macroalgae data
def load_data():
    df = pd.read_csv("data/macroalgae_final.csv", index_col=0)
    df = df.drop(["kingdom", "class", "family", "genus",  "new"], axis = 1)
    return df.drop_duplicates(["lon", "lat"])

# Function to load the macroalgae info
def load_info():
    return pd.read_csv("data/species_info.csv", index_col=0)

# Function to load create a list with all the species that we have in the dataset
def species_list():
    data = load_data()
    return list(data["species"].unique())

def maps(df):
    #showing the maps
    map_sby = folium.Map(tiles="OpenStreetMap", location=[40.4146, -3.7004], zoom_start=2)
    #design for the app


    for i,row in df.iterrows():
                
        icon = Icon(color = "green",
                    prefix = "fa",
                    icon = "fa-map-marker",
                    icon_color = "black"
        )

        location_ = {"location" : [row["lat"],row["lon"]],
                     "tooltip" : row["locality"]}
                
       

        marker_2 = Marker(**location_, icon = icon).add_to(map_sby)

    return folium_static(map_sby)

def plots_year (df, x_axis):
    df = df.groupby(['species', 'year'])['year'].agg(['count']).reset_index()
    df = df[df["species"]== f"{x_axis}"]
    return px.line(df, x='year', y = "count")

def plots_month(df, x_axis):
    df = df.groupby(['species', 'month'])['month'].agg(['count']).reset_index()
    df = df[df["species"]== f"{x_axis}"]
    return px.bar(df, x='month', y = "count")
    