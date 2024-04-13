import streamlit as st
import requests

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
    symbol = st.text_input('Enter Nifty symbol (e.g., NIFTY)', 'NIFTY')

    # Select expiry date
    expiry_date = st.text_input('Enter expiry date (e.g., 31MAR2022)', '31MAR2022')

    # Fetch option chain
    option_chain = get_option_chain(symbol, expiry_date)

    if option_chain:
        # Display option chain data
        st.write(option_chain)
    else:
        st.write('Data not available')

if __name__ == "__main__":
    main()
