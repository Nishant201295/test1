import streamlit as st
import requests
import pandas as pd

def get_symbols():
    url = "https://www.nseindia.com/api/option-chain-indices"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['records']['expiryDates']

def get_option_chain(symbol, expiry_date):
    url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}&expiryDate={expiry_date}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['records']['data']

def main():
    st.title('NSE Option Chain Extractor for Nifty')

    # Select symbol
    symbols = get_symbols()
    selected_symbol = st.selectbox('Select Symbol', symbols)

    # Select expiry date
    expiry_dates = get_option_chain(selected_symbol, '')
    selected_expiry_date = st.selectbox('Select Expiry Date', expiry_dates)

    # Fetch option chain
    option_chain = get_option_chain(selected_symbol, selected_expiry_date)

    if option_chain:
        # Convert data to DataFrame
        df = pd.DataFrame(option_chain)
        
        # Select strike price
        strike_price = st.selectbox('Select Strike Price', df['strikePrice'].unique())

        # Filter data based on selected strike price
        filtered_df = df[df['strikePrice'] == strike_price]
        
        # Display DataFrame
        st.write(filtered_df)
    else:
        st.write('Data not available')

if __name__ == "__main__":
    main()
