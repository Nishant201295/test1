import streamlit as st
import subprocess

# Run installation script
st.write("Installing nselib...")
subprocess.run(["python", "install_nselib.py"])

# Importing necessary functions
from nselib import capital_market, derivatives

# Define functions to fetch data
def get_equity_data(symbol, from_date, to_date):
    return capital_market.price_volume_and_deliverable_position_data(symbol=symbol, from_date=from_date, to_date=to_date)

def get_derivative_data(symbol, instrument, from_date, to_date):
    return derivatives.future_price_volume_data(symbol=symbol, instrument=instrument, from_date=from_date, to_date=to_date)

# Streamlit app
st.title('NSE Data App')

st.sidebar.header('Choose Data Type')
data_type = st.sidebar.selectbox('Select Data Type', ['Equity', 'Derivative'])

if data_type == 'Equity':
    st.sidebar.subheader('Equity Data')
    symbol = st.sidebar.text_input('Enter Symbol (e.g., SBIN):')
    from_date = st.sidebar.text_input('Enter From Date (DD-MM-YYYY):')
    to_date = st.sidebar.text_input('Enter To Date (DD-MM-YYYY):')

    if st.sidebar.button('Get Equity Data'):
        equity_data = get_equity_data(symbol, from_date, to_date)
        st.write('### Equity Data')
        st.write(equity_data)

elif data_type == 'Derivative':
    st.sidebar.subheader('Derivative Data')
    symbol = st.sidebar.text_input('Enter Symbol (e.g., SBIN):')
    instrument = st.sidebar.selectbox('Select Instrument Type', ['FUTSTK', 'FUTIDX', 'OPTSTK', 'OPTIDX'])
    from_date = st.sidebar.text_input('Enter From Date (DD-MM-YYYY):')
    to_date = st.sidebar.text_input('Enter To Date (DD-MM-YYYY):')

    if st.sidebar.button('Get Derivative Data'):
        derivative_data = get_derivative_data(symbol, instrument, from_date, to_date)
        st.write('### Derivative Data')
        st.write(derivative_data)
