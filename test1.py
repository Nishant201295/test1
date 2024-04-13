import streamlit as st
import requests
import pandas as pd

def get_option_chain(symbol):
    url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['records']['data']

def main():
    st.title('NSE Option Chain Extractor for Nifty')

    # Input symbol
    symbol = st.text_input('Enter Nifty symbol (e.g., NIFTY)', 'NIFTY')

    # Fetch option chain
    option_chain = get_option_chain(symbol)

    if option_chain:
        # Convert data to DataFrame
        df = pd.DataFrame(option_chain)
        
        # Display DataFrame
        st.write(df)
    else:
        st.write('Data not available')

if __name__ == "__main__":
    main()
