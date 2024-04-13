import streamlit as st
from nselib.derivatives import nse_live_option_chain

# Set title and page layout
st.title('Nifty Option Chain Viewer')
st.sidebar.header('Options Configuration')

# Define input parameters
expiry_date = st.sidebar.date_input('Select Expiry Date')
strike_price_range = st.sidebar.slider('Select Strike Price Range', min_value=0, max_value=20000, value=(10000, 12000))

# Fetch Nifty option chain data based on input parameters
option_chain_data = nse_live_option_chain(expiry_date=expiry_date, strike_price_range=strike_price_range)

# Display option chain data
st.subheader('Nifty Option Chain Data')
st.write(option_chain_data)
