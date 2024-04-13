import streamlit as st
import subprocess

# Check if nselib module is installed
try:
    import nselib
except ImportError:
    st.warning("nselib module not found. Installing...")
    
    # Install nselib using pip
    subprocess.run(["pip", "install", "nselib"])

    # Check if installation was successful
    try:
        import nselib
        st.success("nselib module installed successfully.")
    except ImportError:
        st.error("Error: Unable to install nselib module. Please install it manually.")
        st.stop()

# Check if nselib.derivatives module is available
if hasattr(nselib, 'derivatives'):
    # Check if nse_live_option_chain function is available
    if hasattr(nselib.derivatives, 'nse_live_option_chain'):
        st.success("nselib module and nse_live_option_chain function imported successfully.")
    else:
        st.error("Error: nse_live_option_chain function not found. Please check the nselib package.")
else:
    st.error("Error: nselib.derivatives module not found. Please check the nselib package.")
