import numpy as np
import pandas as pd
import streamlit as st

import altair as alt

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
  
  st.bar_chart(df, x)
  
main()
