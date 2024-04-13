import streamlit as st
import subprocess
from nselib import capital_market, derivatives

def install_packages(packages):
    for package in packages:
        st.write(f"Installing {package}...")
        subprocess.run(["pip", "install", package])
        st.write(f"Successfully installed {package}")

def main():
    st.title("NSElib Package Installer and Data Retrieval")

    prerequisite_package = "nselib"

    st.write(f"This app installs {prerequisite_package} package and provides options for data retrieval.")

    if st.button("Install Package"):
        install_packages([prerequisite_package])

    if st.checkbox("Retrieve Trading Holiday Calendar"):
        trading_holidays = nselib.trading_holiday_calendar()
        st.write("Trading Holiday Calendar:")
        st.write(trading_holidays)

    data_section = st.sidebar.selectbox("Select Data Section", ("Capital Market", "Derivative"))

    if data_section == "Capital Market":
        capital_market_option = st.sidebar.selectbox("Select Data Type", ("Price, Volume, and Deliverable Position Data",
                                                                         "Price Volume Data",
                                                                         "Deliverable Position Data",
                                                                         "Bulk Deal Data",
                                                                         "Block Deals Data",
                                                                         "Short Selling Data",
                                                                         "Bhav Copy with Delivery",
                                                                         "Bhav Copy Equities",
                                                                         "Equity List",
                                                                         "F&O Equity List",
                                                                         "Nifty50 Equity List",
                                                                         "India VIX Data",
                                                                         "Index Data",
                                                                         "Market Watch All Indices",
                                                                         "FII/DII Trading Activity"))

        if st.sidebar.button("Get Data"):
            if capital_market_option == "Price, Volume, and Deliverable Position Data":
                symbol = st.text_input("Enter Symbol:")
                from_date = st.text_input("Enter From Date (DD-MM-YYYY):")
                to_date = st.text_input("Enter To Date (DD-MM-YYYY):")
                data = capital_market.price_volume_and_deliverable_position_data(symbol=symbol, from_date=from_date, to_date=to_date)
                st.write("Price, Volume, and Deliverable Position Data:")
                st.write(data)
            # Add other options and corresponding data retrieval logic

    elif data_section == "Derivative":
        derivative_option = st.sidebar.selectbox("Select Data Type", ("Future Price Volume Data",
                                                                      "Option Price Volume Data",
                                                                      "F&O Bhav Copy",
                                                                      "Participant-wise Open Interest",
                                                                      "Participant-wise Trading Volume",
                                                                      "Expiry Dates Future",
                                                                      "Expiry Dates Option Index",
                                                                      "NSE Live Option Chain",
                                                                      "FII Derivatives Statistics"))

        if st.sidebar.button("Get Data"):
            if derivative_option == "Future Price Volume Data":
                symbol = st.text_input("Enter Symbol:")
                instrument = st.text_input("Enter Instrument (FUTSTK or FUTIDX):")
                from_date = st.text_input("Enter From Date (DD-MM-YYYY):")
                to_date = st.text_input("Enter To Date (DD-MM-YYYY):")
                data = derivatives.future_price_volume_data(symbol=symbol, instrument=instrument, from_date=from_date, to_date=to_date)
                st.write("Future Price Volume Data:")
                st.write(data)
            # Add other options and corresponding data retrieval logic

if __name__ == "__main__":
    main()
