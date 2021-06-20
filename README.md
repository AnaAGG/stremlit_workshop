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

## 1. Macroalgae library

This example shows interactive and data-driven web apps to visualize macroalgael distribution patterns and characteristics. 

All the information contained in this application has been downloaded using different data sources through different python tools:
   - Species presences -> API GBIF
   - Species characteristics -> obtained from the [Marlin website](https://www.marlin.ac.uk/species/detail/1487) using Selenium 


## 2. Iris species predictive model

This example shows interactive and data-driven web apps to predict what iris species we have. The Iris dataset was used in Fisher’s classic 1936 paper, it includes three iris species with 50 samples each as well as some properties about each flower. In this repo, I will use the sklearn and streamlit libraries from Python to predict the species class of various Iris flowers and create a friendly app to predict the species of a given new species. 



Streamlit also allows to introduce POWERBI reports, [here](https://analyticsindiamag.com/embedding-powerbi-dashboard-in-a-streamlit-web-app-deploying-on-heroku/) some documentation to do it!
