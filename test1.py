import subprocess
import sys
import streamlit as st

# Function to install nselib using pip
def install_nselib():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nselib"])

# Check if nselib is already installed
try:
    import nselib
except ImportError:
    st.write("nselib not found. Installing...")
    install_nselib()
    import nselib

st.title('NSE Data Fetcher')

# Sidebar for selecting data type
data_type = st.sidebar.selectbox(
    'Select Data Type',
    ('Trading Holiday Calendar', 'Capital Market', 'Derivatives')
)

# Rest of the code remains the same as the previous example...
