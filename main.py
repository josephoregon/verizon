import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title='Family Verizon Bill', layout='centered')

st.header('Verizon Bill Amount')


def main(name):
    """ Main Application """

    actual_amount = 321.81

    data = [

        ['Joe', 'iPhone', 'Debit', 'Base_Plan', 30.00],
        ['Joe', 'iPhone', 'Debit', 'Tax', 2.82],
        ['Joe', 'iPhone', 'Debit', 'Tax', 1.35],

        ['Joe', 'iWatch', 'Debit', 'Base_Plan', 10.00],
        ['Joe', 'iWatch', 'Debit', 'Tax', 2.48],
        ['Joe', 'iWatch', 'Debit', 'Tax', 1.14],

        ['Joe', 'iPad', 'Debit', 'Base_Plan', 10.00],
        ['Joe', 'iPad', 'Debit', 'Tax', .08],

        ['Debbie', 'iPhone', 'Debit', 'Base_Plan', 30.00],
        ['Debbie', 'iPhone', 'Debit', 'Tax', 2.67],
        ['Debbie', 'iPhone', 'Debit', 'Tax', 1.26],

        ['Lindsay', 'iPhone', 'Debit', 'Base_Plan', 30.00],
        ['Lindsay', 'iPhone', 'Debit', 'Tax', 2.67],
        ['Lindsay', 'iPhone', 'Debit', 'Tax', 1.26],

        ['Tanner', 'iPhone', 'Debit', 'Base_Plan', 30.00],
        ['Tanner', 'iPhone', 'Debit', 'Tax', 2.67],
        ['Tanner', 'iPhone', 'Debit', 'Tax', 1.26],

        ['Jenny', 'iPhone', 'Debit', 'Base_Plan', 30.00],
        ['Jenny', 'iPhone', 'Debit', 'Tax', 2.67],
        ['Jenny', 'iPhone', 'Debit', 'Tax', 1.26],

        ['Katie', 'iPhone', 'Debit', 'Base_Plan', 30.00],
        ['Katie', 'iPhone', 'Debit', 'Tax', 2.67],
        ['Katie', 'iPhone', 'Debit', 'Tax', 1.26],

        ['Verizon', 'iPhone', 'Debit', 'Distribute', 20.00],
        ['Verizon', 'iPhone', 'Debit', 'Distribute', 36.66],
        ['Verizon', 'iPhone', 'Debit', 'Distribute', 36.66],
        ['Verizon', 'General', 'Debit', 'Distribute', .97],
        ['Verizon', 'iPhone', 'Credit', 'Distribute', -10.00],
        ['Verizon', 'iPad', 'Credit', 'Distribute', -10.00],
        ['Verizon', 'iPhone', 'Credit', 'Distribute', -33.33],
        ['Verizon', 'iPhone', 'Credit', 'Distribute', -33.33]

    ]

    # Create Initial Dataframe
    df = pd.DataFrame(data, columns=['person', 'device', 'type', 'description', 'amount'])

    # Filter Base Charges Only
    base_charges = df[(df['description'] == 'Base_Plan') | (df['description'] == 'Tax')]

    # Overall Total Bill Amount
    bill_amount = df[df['type'] == 'Debit']['amount'].sum()

    # Actual Bill Against Calculated Bill
    bill_diff = (actual_amount - bill_amount).round(2)

    # iPhone Upgrade Charges (for those who upgraded)

    share_charges = df[df['person'] == 'Verizon']

    iphone_charge_list = ['Lindsay', 'Jenny', 'Debbie', 'Joe']

    iphone_charge_count = len(iphone_charge_list)

    iphone_share_debits = share_charges[
        (share_charges['type'] == 'Debit')
        & (share_charges['device'] == 'iPhone') |
        (share_charges['device'] == 'General')].reset_index(drop=True)

    debit_to_split = iphone_share_debits.amount.sum()
    debit_to_split = (debit_to_split / iphone_charge_count)

    group_df = base_charges.groupby('person')['amount'].sum().to_frame(
        name='amount').reset_index()

    data = [[iphone_charge_list[3], debit_to_split],
            [iphone_charge_list[1], debit_to_split],
            [iphone_charge_list[2], debit_to_split],
            [iphone_charge_list[0], debit_to_split]]

    dfcharge = pd.DataFrame(data, columns=['person', 'amount'])
    final_charges_per_person = pd.concat(
        [group_df, dfcharge],
        axis=0).groupby('person')['amount'].sum().to_frame().reset_index()

    final_charges_per_person = final_charges_per_person.sort_values(by='amount', ascending=False)

    calculated_charge = final_charges_per_person['amount'].sum()

    st.write(final_charges_per_person)
    st.subheader('Total Charge Amount: ${}'.format(bill_amount.round(2)))

    data = [
        ['JUN', '2020', 119.10],
        ['JUL', '2020', 119.59],
        ['AUG', '2020', 118.47],
        ['SEP', '2020', 118.47],
        ['OCT', '2020', 108.36],
        ['NOV', '2020', 119.22],
        ['DEC', '2020', 632.47],
        ['JAN', '2021', 321.81],
        ['FEB', '2021', 321.81]
    ]

    historical_charges = pd.DataFrame(data, columns=['MONTH', 'YEAR', 'TOTAL'])

    fig = px.line(historical_charges, x="MONTH", y="TOTAL")

    annotations = []

    # labeling the left_side of the plot
    annotations.append(dict(x='DEC', y=632.47,
                            xanchor='right', yanchor='middle',
                            text='Family Joins Verizon Plan',
                            font=dict(family='Arial', size=16),
                            showarrow=True))

    # labeling the left_side of the plot
    annotations.append(dict(x='JAN', y=historical_charges['TOTAL'][7],
                            xanchor='right', yanchor='middle',
                            text='${}'.format(historical_charges['TOTAL'][7]),
                            font=dict(family='Arial', size=16),
                            showarrow=True))

    # labeling the left_side of the plot
    annotations.append(dict(x='NOV', y=historical_charges['TOTAL'][5],
                            xanchor='right', yanchor='middle',
                            text='${}'.format(historical_charges['TOTAL'][5]),
                            font=dict(family='Arial', size=16),
                            showarrow=True))

    fig.update_layout(annotations=annotations)

    st.plotly_chart(fig)

    # st.write("Calculated Charge: ${}".format(calculated_charge))
    # st.write("Actual vs Calculated Difference: ${}".format((actual_amount - calculated_charge)))


if __name__ == '__main__':
    main('PyCharm')
