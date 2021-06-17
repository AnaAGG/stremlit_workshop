import pandas as pd

# Function to load the macroalgae data
def load_data():
    return pd.read_csv("data/macroalgae_final.csv")

# Function to load the macroalgae info
def load_info():
    return pd.read_csv("data/species_info.csv")

# Function to load create a list with all the species that we have in the dataset
def species_list():
    data = load_data()
    return tuple(data["species"].unique())