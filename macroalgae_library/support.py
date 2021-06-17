import pandas as pd
import folium
from streamlit_folium import folium_static
from folium import Choropleth, Circle, Marker, Icon, Map
import plotly.express as px

# Function to load the macroalgae data
def load_data():
    return pd.read_csv("data/macroalgae_final.csv", index_col=0)

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

    icono = Icon(color = "blue",
                    prefix = "fa",
                    icon = "home",
                    icon_color = "black"
        )

    loc = {"location":[40.4146, -3.7004],
                "tooltip": "Mi ubicación"}
        
    marker_ = Marker(**loc, icon = icono).add_to(map_sby)

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

def plots (df, x_axis):
    df = df.groupby(['species', 'year'])['year'].agg(['count']).reset_index()
    df = df[df["species"]== f"{x_axis}"]
    return px.line(df, x='year', y = "count")
    