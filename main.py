import streamlit as st
from PIL import Image

from src.support import species_list, load_data, load_info, maps

# to write a title in our streamlit page we can use the magic command `write`
st.write ("""
# Learning streamlit

## in this workshop we will learn how to create a streamlit page
""")
st.text('This is some text.')


# Insert images in streamlit, using two columns
col1, col2 = st.beta_columns(2)
with col1:

    imagen = Image.open("Images/portada1.jpg")
    st.image(imagen, use_column_width=True)
with col2:
    imagen = Image.open("Images/portada2.jpg")
    st.image(imagen, use_column_width=True)


#now 
st.write(""" 
## List of species that you could find in this page""")

x_options = species_list()

col3, col4, col5, col6 = st.beta_columns(4)
with col3:
    st.table(x_options[:5])
with col4:
    st.table(x_options[5:10])
with col5:
    st.table(x_options[10:15])
with col6:
    st.table(x_options[15:20])



#Now we have report the basic information for a given species

st.header("Which species would you like to see?")
x_axis = st.text_input("Buscador:")

if len(x_axis) == 0:    
        st.write("We need that you pass a species")
else:
    #load coordinates information
    data = load_data()
    data2 = data[data["species"] == f'{x_axis}']
    st.dataframe(data2)

    #load species info
    z = load_info()
    z.reset_index(inplace = True)
    t = z[z["species"]== f"{x_axis}"]
    t.drop(["species"], axis = 1, inplace = True)
    st.table(t)

    # create a map with the species presences
    maps(data2)

