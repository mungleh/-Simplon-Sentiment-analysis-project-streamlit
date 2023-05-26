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


if 'data' not in st.session_state:
    st.session_state['data'] = {"review": "nothing", "input" : "nothing", "istrue":"nothing"}


data = {"review": "nothing"}
user_input = st.text_input("Entrez la phrase que vous voulez analysez")
data["review"] = user_input


btn_pred = st.button("Prediction")
btn_del = st.button("Delete")
btn_true = st.button("True")
btn_false =  st.button("False")



if btn_pred:
   response = requests.get('https://matdreamteam.azurewebsites.net/predict',
                           headers=headers, json=data)
   st.session_state.data = response.json()
   st.session_state.data["input"] = user_input
   

if btn_true :
   st.session_state.data["istrue"] = 1
   requests.post('https://matdreamteam.azurewebsites.net/add', 
                        headers= headers, json = st.session_state.data)

if btn_false :
   st.session_state.data["istrue"] = 0
   requests.post('https://matdreamteam.azurewebsites.net/add', 
                        headers= headers, json = st.session_state.data)


if btn_del :
   delete = requests.post('https://matdreamteam.azurewebsites.net/del', 
                        headers= headers)