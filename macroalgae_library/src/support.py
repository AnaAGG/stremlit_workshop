import pandas as pd
import folium
from streamlit_folium import folium_static
from folium import Choropleth, Circle, Marker, Icon, Map
import plotly.express as px


def load_data():
    """
    Function to load the macroalgae data
    Args: 
        non receive parameters
    Returns:
        The dataset with the species coordinates cleaned
    """
    df = pd.read_csv("data/macroalgae_final.csv", index_col=0)
    df = df.drop(["kingdom", "class", "family", "genus",  "new"], axis = 1)
    df.dropna(inplace= True)
    return df.drop_duplicates(["lon", "lat"])


def load_info():
    """
    Function to load the macroalgae info
    Args: 
        non receive parameters
    Returns:
        The dataset with the species info 
    """
    return pd.read_csv("data/species_info.csv", index_col=0)


def species_list():
    """
    Function to load create a list with all the species that we have in the dataset
    Args: 
        non receive parameters
    Returns:
        A list with the unique species finded in the dataset 
    """
    data = load_data()
    return list(data["species"].unique())

def maps(df):
    """
    Function to create a folium map with the species presences
    Args: 
        df: dataframe
    Returns:
        A folium map
    """
    #showing the maps
    map_sby = folium.Map(tiles="OpenStreetMap", location=[40.4146, -3.7004], zoom_start=2)

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
    """
    Function to create a plot to represent the evolution of data through the years
    Args: 
        df: dataframe
        x_axis: target species that you are interested in 
    Returns:
        A plotly line plot
    """
    df = df.groupby(['species', 'year'])['year'].agg(['count']).reset_index()
    df = df[df["species"]== f"{x_axis}"]
    return px.line(df, x='year', y = "count")

def plots_month(df, x_axis):
    """
    Function to create a plot to represent the evolution of data through the months
    Args: 
        df: dataframe
        x_axis: target species that you are interested in 
    Returns:
        A plotly bar plot
    """
    df = df.groupby(['species', 'month'])['month'].agg(['count']).reset_index()
    df = df[df["species"]== f"{x_axis}"]
    return px.bar(df, x='month', y = "count")
    