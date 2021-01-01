import numpy as np
import pandas as pd
import streamlit as st

from plotly import tools
import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go


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
  
  st.title("Eckhardt Verizon Dashboard**📱**")
  st.write("Breakdown of the Verizon billing for everyone to see!")
  
  st.markdown("---")
  
  # view total charges by person
  charge_by_person = df.groupby('Person').Charge.sum().sort_values()
  st.write(charge_by_person)
  
  st.markdown("---")
  
  st.markdown('<i class="material-icons">by Joseph Rosas</i>', unsafe_allow_html=True)
  
main()
