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
  
  df.groupby('Person').Charge.sum().sort_values()
  
  st.title("Eckhardt Verizon Dashboard**📱**")
  st.write("Breakdown of the Verizon billing for everyone to see!")
  
  <details>
  <summary>Data Dictionary</summary>

  ## Data Dictionary

  - Variable 1: this is variable 1
  - Variable 2: this is variable 2

  </details>
  
  st.write("<i>by Joseph Rosas</i>")
  
main()
