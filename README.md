# Learning streamlit

<p align="center">
  <img src="https://github.com/AnaAGG/stremlit_workshop/blob/main/Images/streamlit.png" />
</p>


In this repo we are going to learn how to create a web application using [streamlit](https://streamlit.io/). 

**Streamlit** is an open Python package that will help us to create interactive web applications without any knowledge of html or CSS, i.e. Python will be the only thing we will need!

To do this example I used a worldwide seaweed information with the objetive to characterice their distribution and introduce a little description of each species cointained in the dataset. 

In this repo you can see two examples of streamlit app: 

1. The macroalgae library -> in this folder we find the basic concepts to get started with streamlit
   
2. Iris species predictive model -> an example of how to create and load a machine learning model in streamlit. 
   
   
> Both folders follow the same structure. In each of them you will find:
   > - **src folder** --> where you find different .py files with all the function used in the project
   >
   > - **data folder** --> all the data needed to perform the project
   >
   > - **images folder** --> used images in the streamlit app
   >
   > - **Noteboooks folder** --> where I execute the main code to get the data
   >
   > - **main.py file** --> the stremlit app

## 1. Macroalgae library

This example shows interactive and data-driven web apps to visualize macroalgael distribution patterns and characteristics. 

All the information contained in this application has been downloaded using different data sources through different python tools:
   - Species presences -> [API GBIF](https://www.gbif.org/es/developer/summary)
  
   - Species characteristics -> obtained from the [Marlin website](https://www.marlin.ac.uk/species/detail/1487) using Selenium 


## 2. Iris species predictive model

This example shows interactive and data-driven web apps to predict what iris species we have. The Iris dataset includes three iris species with 50 samples each as well as some properties about each flower. 

In this repo, I will use the [sklearn](https://scikit-learn.org/stable/) and streamlit libraries from Python to predict the species class of various Iris flowers and create a friendly app to predict the species of a given new species. 



 ⚠️ **NOTE** ⚠️ Streamlit can give some issues with python 3.9. Ideally, use versions < 3.9.


