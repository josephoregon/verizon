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

    return df


def charges_by_person(df):
    """Display table that shows total charge for each individual"""

    charge_by_person = df.groupby('Person')['Charge Amount'].sum().sort_values()
    charge_by_person = charge_by_person.rename('Charges').reset_index()

    df = df[df['Person'] != 'General Charges']

    charge_by_person = df.groupby('Person')['Charge Amount'].sum().sort_values()
    charge_by_person = charge_by_person.rename('Charge Amount').reset_index()
    charge_by_person['Charge Amount'] = round(charge_by_person['Charge Amount'], 2)

    charge_by_person['Charge Amount'] = charge_by_person['Charge Amount'
            ].map('${:,.2f}'.format)

    fig = \
        go.Figure(data=[go.Table(header=dict(values=list(charge_by_person.columns),
                  fill_color='light blue', align='center'),
                  cells=dict(values=[charge_by_person.Person,
                  charge_by_person.Charge], fill_color='light gray',
                  align='center'))])

    fig.update_layout(width=600, height=400)
    
    return st.plotly_chart(fig, use_container_width=True)

def main():
    
    df = get_data()
    
    group_by_list = list(df.columns)
    graph_list = st.sidebar.multiselect('Group By', group_by_list)

    st.markdown("<h1 style='text-align: center;'>Eckhardt Verizon\xf0\x9f\x93\xb1</h1>"
                , unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Breakdown of the Verizon billing for everyone to see!</h3>"
                , unsafe_allow_html=True)

    st.markdown('---')

    charges_by_person(df)


    grouped_df = df.groupby(graph_list)['Charge Amount'].sum()
    st.write(grouped_df)

    st.markdown('---')
    st.markdown('<i class="material-icons">by Joseph Rosas</i>', unsafe_allow_html=True)


main()

