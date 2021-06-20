import pandas as pd
from pygbif import species
from pygbif import occurrences as occ
from geopy.geocoders import Nominatim

def get_species_name_from_codes(splist):
    '''
    Receive a list o scientific names to extract the GBIF codes
    
    Args:
        splist(list) the list of target species    
    
    Returns
        Dictionary with the scientific name and their GBIF codes.
        List with the specific codes
    '''
    keys = [species.name_backbone(x)['usageKey'] for x in splist ]
    species_codes = dict(zip(splist, keys))
    sp_list = list(species_codes.values())
    return  sp_list, species_codes

def get_coordinates (sp):
    '''
    Extracts the taxonomic information of each species and the coordinates for each one of them.
    Args:
        List with the codes of the species that we want to download from the database
    Returns: 
        Dataframe with 11 columns: long, lat, locality, year, month, kingdom, class, family, genus,
        species, common_name
    '''
    
    long, lat, month, year_list, kingdom, class_, family, genus, species_, verna, locality  = [], [], [], [], [], [], [], [], [], [], []
   
    
    years = range(1900, 2021)

    for year in years:
        data = occ.search(taxonKey = sp, year = str(year))
    
        for i in data["results"]:
            long.append(i.get("decimalLongitude"))
            lat.append(i.get("decimalLatitude")) 
            month.append(i.get("month"))            
            year_list.append(i.get("year"))
            species_.append(i.get("scientificName"))
            kingdom.append(i.get("kingdom")) 
            genus.append(i.get("genus"))
            family.append(i.get("family"))
            class_.append(i.get("class"))
            locality.append(i.get("locality"))
        
     
                
    df = pd.DataFrame(list(zip(long,lat, locality, year_list, month, kingdom, class_, family, genus,  species_)),
                      columns=[ "lon", "lat","locality", "year", "month", "kingdom", "class", "family", "genus", "species"])
       

    return df

def clean (x):
    x.dropna(subset = ["lon", "lat"], inplace = True)
    x["lon"] = x["lon"].round(4)
    x["lat"] = x["lat"].round(4)
    return x

def divide_species(df, coll):
    df['new_coll'] = df[coll].str.split(' ').str[:2]
    df['species'] = [' '.join(map(str, l)) for l in df['new_coll']]
    df.drop(["new_coll"], axis = 1, inplace = True)
    return df


def clean_species(df2, coll):
       #Drop unwanted rows
    
    df2['new_coll'] = df2[coll].str.split(' ').str[:2]
    df2['species'] = [' '.join(map(str, l)) for l in df2['new_coll']]
    df2.drop(["new_coll"], axis = 1, inplace = True)
    
    replace_values = {'Ulva fasciata' :'Ulva lactuca', 'Laminaria stenophylla' : 'Laminaria digitata', 
                     'Rhodymenia palmata': 'Palmaria palmata', 'Fucus platycarpus' : 'Fucus spiralis', 
                      'Alaria musaefolia': 'Alaria esculenta', 'Alaria dolichorhachis': 'Alaria esculenta', 
                      'Fucus nodosus':  'Ascophyllum nodosum', 'Fucus mytili': 'Fucus vesiculosus', 
                     'Fucus inflatus' : ''}                                                                                          

    df2 = df2.replace({"species": replace_values})
    
    to_remove = ['BOLD:AAB0883','BOLD:AAD7070','Ascophyllum mackaii','Fucus rotundatus','Halidrys Lyngbye,','Halidrys dioica',
    'Palmaria mollis', 'Laminaria flexicaulis', 'Alaria grandifolia']
    df2 = df2[df2['species'].isin(to_remove)== False]
    
 
    return df2

def get_community(x):
    '''
    Extract the community of given coordinates.
    Receive:
        Column from the dataframe
    Returns:
        The community information for each of the coordinates of the dataframe
    '''

    
    try:
        locator = Nominatim(user_agent="myGeocoder", timeout=10)

        location = locator.reverse(x)

        data = location.raw
        
        locality = data["address"]["village"]
        state = data["address"]["state"]
        country = data["address"]["country"]
        return locality, state, country
    
    except: 
        return "unknown"