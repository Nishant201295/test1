import streamlit as st
import requests

def get_option_chain(cookie):
    headers = {
        'Cookie': cookie,
    }
    url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    st.title('Nifty Option Chain Extractor')
    cookie = st.text_input('Enter your cookie:', type='password')
    nifty_option_chain = None
    
    if st.button('Get Option Chain') and cookie:
        nifty_option_chain = get_option_chain(cookie)
        
    if nifty_option_chain:
        st.write(nifty_option_chain)
    elif st.button('Show Example'):
        st.write("Example option chain will appear here.")
        # You can add an example of the option chain here.

if __name__ == '__main__':
    main()
