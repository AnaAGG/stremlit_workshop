import streamlit as st
from PIL import Image
from src.support import species_list, load_data, load_info, maps, plots_year, plots_month, pie_chart_family


# to write a title in our streamlit page we can use the magic command `write`
st.write ("""
# Biodiversity Heritage Library
""")

st.text('''In this app you will find the basic information and distribution of most 
important seaweed species. Species, distribution and characteristics''')


# Insert images in streamlit, using two columns
col1, col2 = st.columns(2)
with col1:
    imagen = Image.open("Images/portada1.jpg")
    st.image(imagen, use_column_width=True)
with col2:
    imagen = Image.open("Images/portada2.jpg")
    st.image(imagen, use_column_width=True)


#now, ask to the user what you want to see in our application
st.write(""" 
### List of species that you could find in this page""")

x_options = species_list()

col3, col4, col5 = st.columns(3)
with col3:
    st.table(x_options[:5])
with col4:
    st.table(x_options[5:10])
with col5:
    st.table(x_options[10:15])


st.plotly_chart(pie_chart_family())


#Now we have report the basic information for a given species

st.write("### Which species would you like to see?")
list_species = species_list()
x_axis = st.selectbox("Select species", ["Choose and option"] + list_species )

if len(x_axis) == 0 or x_axis == "Choose and option":    
        st.write("We need that you pass a species")
else:
    #load coordinates info
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
    st.text("Map of the global distribution")
    maps(data2)

    #get some conclusions of the data
    st.plotly_chart(plots_year(data, x_axis))
    st.plotly_chart(plots_month(data, x_axis))
