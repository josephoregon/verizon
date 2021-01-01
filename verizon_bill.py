import pandas as pd

df = pd.read_csv('VERIZON_BILL_CSV.csv')

df['Charge'] = df['Charge'].str.replace('\t', '')
df['Charge'] = df['Charge'].str.replace('$', '')
df['Charge'] = df['Charge'].str.replace('(', '-')
df['Charge'] = df['Charge'].str.replace(')', '')

df['Charge'] = pd.to_numeric(df['Charge'])

df.groupby('Person').Charge.sum().sort_values()
