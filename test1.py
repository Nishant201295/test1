import subprocess
import sys
import streamlit as st

# Install nselib if not already installed
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import nselib
except ImportError:
    st.write("Installing nselib...")
    install("nselib")
    import nselib

st.title('NSE Data Fetcher')

# Sidebar for selecting data type
data_type = st.sidebar.selectbox(
    'Select Data Type',
    ('Trading Holiday Calendar', 'Capital Market', 'Derivatives')
)

# Functions to fetch data
def fetch_trading_holiday_calendar():
    return nselib.trading_holiday_calendar()

def fetch_capital_market(symbol, from_date, to_date, period):
    if period:
        return nselib.capital_market.price_volume_and_deliverable_position_data(symbol=symbol, period=period)
    else:
        return nselib.capital_market.price_volume_and_deliverable_position_data(symbol=symbol, from_date=from_date, to_date=to_date)

def fetch_derivatives(symbol, instrument, from_date, to_date, period):
    if period:
        return nselib.derivatives.future_price_volume_data(symbol=symbol, instrument=instrument, period=period)
    else:
        return nselib.derivatives.future_price_volume_data(symbol=symbol, instrument=instrument, from_date=from_date, to_date=to_date)

# Main content based on selected data type
if data_type == 'Trading Holiday Calendar':
    data = fetch_trading_holiday_calendar()
    st.write("Trading Holiday Calendar Data:", data)

elif data_type == 'Capital Market':
    st.subheader('Capital Market Data')
    symbol = st.text_input('Enter Symbol')
    from_date = st.text_input('From Date (DD-MM-YYYY)')
    to_date = st.text_input('To Date (DD-MM-YYYY)')
    period = st.text_input('Period (e.g., 1M for 1 month)')
    if symbol:
        data = fetch_capital_market(symbol, from_date, to_date, period)
        st.write("Capital Market Data:", data)

elif data_type == 'Derivatives':
    st.subheader('Derivatives Data')
    symbol = st.text_input('Enter Symbol')
    instrument = st.selectbox('Select Instrument Type', ('FUTIDX', 'FUTSTK', 'OPTIDX', 'OPTSTK'))
    from_date = st.text_input('From Date (DD-MM-YYYY)')
    to_date = st.text_input('To Date (DD-MM-YYYY)')
    period = st.text_input('Period (e.g., 1M for 1 month)')
    if symbol:
        data = fetch_derivatives(symbol, instrument, from_date, to_date, period)
        st.write("Derivatives Data:", data)
