import streamlit as st
import requests

def get_option_chain(cookie):
    url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
    headers = {'Cookie': cookie}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error retrieving option chain: {e}")
        return None

def main():
    st.title('Nifty Option Chain Extractor')
    
    # Get user's cookie input
    cookie = st.text_input('Enter your cookie:', type='password')
    
    # Retrieve and display option chain
    if st.button('Get Option Chain') and cookie:
        option_chain = get_option_chain(cookie)
        if option_chain:
            st.write(option_chain)

if __name__ == '__main__':
    main()
