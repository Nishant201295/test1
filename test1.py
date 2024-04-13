import streamlit as st
import subprocess

# Install dependencies
def install_dependencies():
    subprocess.run(["pip", "install", "beautifulsoup4", "requests"])

# Check if dependencies are installed, if not, install them
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    st.write("Installing dependencies...")
    install_dependencies()
    import requests
    from bs4 import BeautifulSoup

def get_option_chain(symbol):
    url = f"https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol={symbol}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Fetching the webpage
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        st.error("Failed to fetch data")
        return None

    # Parsing the HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting data
    tables = soup.find_all("table")
    if len(tables) < 2:
        st.error("No option chain data found")
        return None

    # Extracting the option chain table
    option_chain_table = tables[1]

    # Extracting headers
    headers = [th.text.strip() for th in option_chain_table.find_all('th')]

    # Extracting rows
    rows = []
    for row in option_chain_table.find_all('tr'):
        rows.append([td.text.strip() for td in row.find_all('td')])

    return headers, rows

# Streamlit app
st.title("NSE Option Chain Data Extractor")

symbol = st.text_input("Enter symbol (e.g., SBIN):")
if st.button("Get Option Chain"):
    if symbol:
        headers, option_chain_data = get_option_chain(symbol)
        if option_chain_data:
            st.write("Option Chain Headers:", headers)
            st.write("Option Chain Data:", option_chain_data)
