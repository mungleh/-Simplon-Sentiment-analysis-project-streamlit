import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import requests 
import streamlit.components.v1 as components
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

df = pd.DataFrame(requests.get('https://matdreamteam.azurewebsites.net',
                           headers=headers).json())



st.title("Sentiment analysis")
st.subheader("The purpose here is to test an AI on a text who predict if the global sentiment is positive or negative")

col10,col20 = st.columns([1,3.6])

with col10 :
   
   user_input = st.text_input("Enter a sentence to analyse")


col1,col2,col3,col4,col5 = st.columns([1.5,1,1,1,16])


with col1 :
   
   
   if st.button("Prediction") :
      
      
      data["review"] = user_input
      response = requests.get('https://matdreamteam.azurewebsites.net/predict',
                              headers=headers, json=data)
      st.session_state.data = response.json()
      st.session_state.data["input"] = user_input
      
      predict = response.json()["prediction"]
      if predict == 1 :
         predict = "positive"
      elif predict != 1 : 
         predict = "negative"
         
      probability = np.round(response.json()["probability"],2)*100
      
      st.write(f"The text '{user_input}' is {predict} with a probability of {probability}%")
      

with col2 :
   if st.button("True") :
      st.session_state.data["istrue"] = 1
      requests.post('https://matdreamteam.azurewebsites.net/add', 
                           headers= headers, json = st.session_state.data)
with col3 :
   if st.button("False") :
      st.session_state.data["istrue"] = 0
      requests.post('https://matdreamteam.azurewebsites.net/add', 
                           headers= headers, json = st.session_state.data)

with col4 :
   if st.button("Delete") :
      delete = requests.post('https://matdreamteam.azurewebsites.net/del', 
                           headers= headers)
      


try :
   stat = np.round(df["istrue"].value_counts()[1] / df["istrue"].count()*100, 2)

   
   st.write(f"Your model is good {stat}% of the time")
except :
   pass
st.dataframe(df)

page_bg_img = f"""
<style>

[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1622559650168-61fa8ee44bf4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}



[data-baseweb="base-input"] {{
background: rgba(0,0,0,0);
}}

div.stButton > button:first-child {{
background: rgba(0,0,0,0);
color:white;
font-color:white;
border-color:white;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
# st.markdown(
# """
# <style>
# .square-set {
#   color: WHITE;
#   background: darkgrey;
#   height: 600px;
#   position: absolute;
#   border-radius: 15px;
#   font:  Helvetica ;
#   width: 400px;
#   top: 50px;
#   left:0px
  
# }
# .square {
#   background: green;
#   height: 80px;
#   position: absolute;
#   width: 80px;
#   border-radius: 15px;
#   line-height: 60px;
#   top:1500px;
#   right:5px
# }
# </style>

# <div class="square-set">

# """, unsafe_allow_html= True)