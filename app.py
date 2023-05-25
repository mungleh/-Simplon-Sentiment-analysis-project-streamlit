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

data = {"review": "nothing"}
user_input = st.text_input("Entrez la phrase que vous voulez analysez")
data["review"] = user_input
st.write(user_input)
btn = st.button("test")
if btn:
    response = requests.get('http://127.0.0.1:8000/predict', headers=headers, data=f'{data}')
    st.write(response.text)