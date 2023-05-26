import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import requests 

#create the page of the web app
st.set_page_config(page_title = "Sentiment analyse",
                   layout = "wide", 
                   )

headers = {
   'accept': 'application/json',
   'Content-Type': 'application/json',
}

data = {"review": "nothing", "input" : "nothing", "istrue":"nothing"}
user_input = st.text_input("Entrez la phrase que vous voulez analysez")
data["review"] = user_input

st.text(data)
btn_pred = st.button("Prediction")
btn_del = st.button("Delete")
btn_true = st.button("True")
btn_false =  st.button("False")

if btn_pred:
   response = requests.get('https://matdreamteam.azurewebsites.net/predict',
                           headers=headers, json=data)
   dict_data = response.json()
   dict_data["input"] = user_input
   st.write(dict_data)
    
if btn_true :
   dict_data["istrue"] = 1
   add = requests.post('https://matdreamteam.azurewebsites.net/add', 
                        headers= headers, json = dict_data)

if btn_false :
   dict_data["istrue"] = 0
   add
   
if btn_del :
   delete = requests.post('https://matdreamteam.azurewebsites.net/del', 
                        headers= headers)