#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import streamlit as st
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go
from plotly import tools

st.set_page_config(
        page_title="Verizon Bill",
        page_icon="📱",
        layout="centered",
        initial_sidebar_state="expanded"
    )

st.markdown("<h1 style='text-align: center;'>Eckhardt Verizon</h1>"
            , unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Breakdown of the Verizon billing.</h3>"
            , unsafe_allow_html=True)

@st.cache
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

    charge_by_user = df[df["Person"] != "General Account"]

    charges_per_user = (
        charge_by_user.groupby("Person")["Charge Amount"]
        .sum()
        .sort_values()
        .reset_index(name="Charge")
    )

    st.dataframe(charges_per_user)
    
    st.markdown('---')
     
    col_list = ['Person', 'Device', 
                'Charge Amount', 
                'Charge Description']

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(col_list),
                    fill_color='dark gray',
                    align='left'),
        cells=dict(values=[df.Person, df.Device, df['Charge Amount'], df['Charge Description']],
                   fill_color='light gray',
                   align='left'))
    ])

    st.plotly_chart(fig)

    st.markdown('---')
    
    st.markdown('<i class="material-icons">by Joseph Rosas</i>', unsafe_allow_html=True)
    
main()

