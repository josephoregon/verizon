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
  
  st.title("**♟**Explore E-com dashboard**♟**")
  st.write("Here, you can see the demo of a simple web-app dashboard."
  "It will show you general information such as your sales and revenue for a specific "
  "ecom-platform on which you sell your products.")
  
main()
