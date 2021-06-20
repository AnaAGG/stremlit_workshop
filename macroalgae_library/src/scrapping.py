from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from functools import reduce

import time
import pandas as pd

def species_scrap(opciones , param, driver):   
    description = {}
    distribution = {}
    features = {}
    for i in param: 

        try:
            url2 = f"https://www.marlin.ac.uk/species/search?q={i}"
            driver3 = webdriver.Chrome(driver, options = opciones)
        except:
            print(f"sorry, we don`t have information about {i} ")
        
        try:

            #driver3 = webdriver.Chrome(executable_path="./chromedriver")
            driver3.get(url2)
            driver3.implicitly_wait(10)
            driver3.find_element_by_xpath('//*[@id="search_results"]/li[1]/b/a').click()
            driver3.implicitly_wait(10)
            desc = driver3.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[4]/div[1]/div/div/p")
            driver3.implicitly_wait(10)
            distr = driver3.find_element_by_xpath('//*[@id="searchable"]/div[4]/div[3]/div')
            time.sleep(5)
            feature = driver3.find_element_by_xpath('//*[@id="searchable"]/div[4]/div[6]/div')
            time.sleep(5)


            description[i] = desc.text
            distribution[i] = distr.text
            features[i] = feature.text
            driver3.quit()
            time.sleep(5)
        except:
            print("Sorry we dont have data")
        
    #creating the dataframe
    df1 = pd.DataFrame.from_dict(description, orient = "index").reset_index()
    df1.columns =  ["species", "description"]
        
    df2 = pd.DataFrame.from_dict(features, orient = "index").reset_index()
    df2.columns =  ["species", "features"]
        
    df3 = pd.DataFrame.from_dict(distribution, orient = "index").reset_index()
    df3.columns =  ["species", "distribution"]

    data_frames = [df1, df2, df3]
    df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['species'],
                                            how='outer'), data_frames)
        
    return df_merged

def cleaning (df):
    df['species'] = df['species'].apply(lambda x: x.replace('+', ' '))
    df['features'] = df['features'].apply(lambda x: x.replace('\n', ' '))
    df['features'] = df['features'].apply(lambda x: x.replace('Identifying features', ''))
    df['features'] = df['features'].apply(lambda x: x.replace('\n', ' '))
    df['distribution'] = df['distribution'].apply(lambda x: x.replace('See additional information.', ''))
    return df