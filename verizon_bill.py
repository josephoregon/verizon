#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import streamlit as st

from plotly import tools
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go


@st.cache
def get_data():

    df = pd.read_csv('VERIZON_BILL_CSV.csv')

    df['Charge Amount'] = df['Charge Amount'].str.replace('\t', '')
    df['Charge Amount'] = df['Charge Amount'].str.replace('$', '')
    df['Charge Amount'] = df['Charge Amount'].str.replace('(', '-')
    df['Charge Amount'] = df['Charge Amount'].str.replace(')', '')

    df['Charge Amount'] = pd.to_numeric(df['Charge Amount'])
    
    df['Charge Amount'] = round(df['Charge Amount'], 2)

    return df

group_by_list = ['Person', 'Device', 'Charge Description', 'Charge Type']
graph_list = st.sidebar.multiselect('Group By', group_by_list, key='Person')
    
def main():
    
    st.markdown("<h1 style='text-align: center;'>Eckhardt Verizon\xf0\x9f\x93\xb1</h1>"
                , unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Breakdown of the Verizon billing for everyone to see!</h3>"
                , unsafe_allow_html=True)
    
    df = get_data()

    st.markdown('---')
    
    grouped_df = df.groupby(graph_list)['Charge Amount'].sum().sort_values()
    grouped_df = grouped_df.rename('Charge Amount').reset_index()
    grouped_df['Charge Amount'] = grouped_df['Charge Amount'].map('${:,.2f}'.format)
    
    
    fig = \
        go.Figure(data=[go.Table(header=dict(values=list(grouped_df.columns),
                  fill_color='light blue', align='center'),
                  cells=dict(values=[grouped_df.Person,
                  grouped_df['Charge Amount']], fill_color='light gray',
                  align='center'))])

    fig.update_layout(width=600, height=400)
    
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('---')
    st.markdown('<i class="material-icons">by Joseph Rosas</i>', unsafe_allow_html=True)


main()

