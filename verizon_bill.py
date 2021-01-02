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

  df['Charge'] = df['Charge'].str.replace('\t', '')
  df['Charge'] = df['Charge'].str.replace('$', '')
  df['Charge'] = df['Charge'].str.replace('(', '-')
  df['Charge'] = df['Charge'].str.replace(')', '')

  df['Charge'] = pd.to_numeric(df['Charge'])

  return df


def main():
  
  df = get_data()
  
  st.markdown("<h1 style='text-align: center;'>Eckhardt Verizon📱</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: center;'>Breakdown of the Verizon billing for everyone to see!</h3>", unsafe_allow_html=True)
  
  st.markdown("---")
  
  # view total charges by person
  charge_by_person = df.groupby('Person').Charge.sum().sort_values()
  charge_by_person = charge_by_person.rename('Charges').reset_index()
  
  
  # view total charges by person

  # view total charges by person

  df = df[df["Person"] != "General Charges"]

  charge_by_person = df.groupby("Person").Charge.sum().sort_values()
  charge_by_person = charge_by_person.rename("Charge").reset_index()
  charge_by_person['Charge'] = round(charge_by_person['Charge'], 2)

  visul_df = charge_by_person.copy()
  visul_df['Charge'] = visul_df['Charge'].map("${:,.2f}".format)

  fig = go.Figure(data=[go.Table(
      header=dict(values=list(visul_df.columns),
                  fill_color='light blue',
                  align='center'),
      cells=dict(values=[visul_df.Person, visul_df.Charge],
                 fill_color='light gray',
                 align='center'))
  ])
  fig.update_layout(width=600, height=400)
  
  st.plotly_chart(fig, use_container_width=True)
  
  st.markdown("---")
  
  st.markdown('<i class="material-icons">by Joseph Rosas</i>', unsafe_allow_html=True)
  
main()
