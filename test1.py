import streamlit as st

# Try to import nselib module
try:
    import nselib
except ImportError:
    st.error("Error: Unable to import nselib module. Please make sure it's installed correctly.")
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
