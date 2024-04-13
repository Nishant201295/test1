import streamlit as st
import subprocess
import importlib.util

def install_package(package):
    st.write(f"Installing {package}...")
    subprocess.run(["pip", "install", package])
    st.write(f"Successfully installed {package}")

def is_package_installed(package_name):
    spec = importlib.util.find_spec(package_name)
    return spec is not None

def main():
    st.title("NSElib Package Installer and Data Retrieval")

    # Step 1: Install nselib package
    st.header("Step 1: Install nselib Package")
    if st.button("Install nselib Package"):
        install_package("nselib")
        st.success("nselib package installed successfully!")
        st.info("Click the button below to begin Step 2.")

    # Step 2: Retrieve option chain data and other functionalities
    if st.button("Begin Step 2"):
        if is_package_installed("nselib"):
            from nselib import capital_market, derivatives

            st.header("Step 2: Retrieve Option Chain Data and Other Functionalities")

            data_section = st.sidebar.selectbox("Select Data Section", ("Capital Market", "Derivative"))

            if data_section == "Capital Market":
                # Code for Capital Market data retrieval
                pass
            elif data_section == "Derivative":
                # Code for Derivative data retrieval
                pass
        else:
            st.warning("Please install the nselib package first.")

if __name__ == "__main__":
    main()
