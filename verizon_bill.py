#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import streamlit as st
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go
from plotly import tools

st.markdown("<h1 style='text-align: center;'>Eckhardt Verizon</h1>"
            , unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Breakdown of the Verizon billing.</h3>"
            , unsafe_allow_html=True)

def get_data():
    """Clean Incoming Data"""
    # Import
    df = pd.read_csv('VERIZON_BILL_CSV.csv')
    # Remove special characters 
    df['Charge Amount'] = df['Charge Amount'].str.replace('\t', '')
    df['Charge Amount'] = df['Charge Amount'].str.replace('$', '')
    df['Charge Amount'] = df['Charge Amount'].str.replace('(', '-')
    df['Charge Amount'] = df['Charge Amount'].str.replace(')', '')
    # Change data type
    df['Charge Amount'] = pd.to_numeric(df['Charge Amount'])
    # Round charte amounts to two decimals
    df['Charge Amount'] = round(df['Charge Amount'], 2)
    return df

df = get_data()

def main():
    st.dataframe(df)
    
    st.markdown('---')
     
    
    
    st.markdown('---')
    
    st.markdown('<i class="material-icons">by Joseph Rosas</i>', unsafe_allow_html=True)
    
main()
