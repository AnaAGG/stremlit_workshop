import streamlit as st
from PIL import Image

from src.support import species_list

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


# Insert images in streamlit, using one column
#imagen = Image.open("Images/portada1.jpg")
#st.image(imagen, use_column_width=True)

st.write(""" 
## List of species that you could find in this page""")

x_options = species_list()

col1, col2, col3 = st.beta_columns(3)
with col1:
    st.table(x_options[:5])
with col2:
    st.table(x_options[5:10])

with col3:
    st.table(x_options[10:15])