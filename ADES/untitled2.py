# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:23:08 2023

@author: kavya
"""

import streamlit as st
import pandas as pd
import openpyxl as oxl
from PIL import Image
import numpy as np
import plotly.express as px



df= pd.read_excel(
      io= r"C:\Users\kavya\OneDrive\Desktop\kavya work\farmers_data.xlsx",
      engine='openpyxl',
      sheet_name='Farmer-Data',
      #skiprows=,
      usecols='A:K',
      nrows=503,
    )  
print(df.head())





st.markdown("<h1 style='text-align: center; color: white;'>Dashboard Ordinato</h1>", unsafe_allow_html=True)
# st.title(':bar_chart: Dashboard Ordinato')
st.markdown("""---""")

# --------SIDERBAR-----------
st.sidebar.header("Farmer-Info")

names = st.sidebar.multiselect('name:', options=df["Farmers Name"].unique(), default="OLDLINE")
products = st.sidebar.multiselect('crop name:', options=df["Product Name"].unique())
quantity = st.sidebar.multiselect('Product quantity:', options=df["Product QTY"].unique())
farm_size = st.sidebar.multiselect('farm size of each farmer:', options=df["Farm Size"].unique())
country = st.sidebar.multiselect('country belong to:', options=df["Country/Division"].unique())
city = st.sidebar.multiselect('cities:', options=df["Town/City"].unique())
contact = st.sidebar.multiselect('contact directly:', options=df["Contact Number"].unique())


#-----FILTRI------
df_selection = df.query(
    "Farmer Name == @names & Product Name == @products & Product QTY == @quantity & Farm Size == @farm_size & Country/Division == county & Town/City == city ^ Contact Number == contact"
)
st.dataframe(df_selection)


st.markdown("""---""")