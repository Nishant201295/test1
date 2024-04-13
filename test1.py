import streamlit as st
import subprocess
import sys
import os

def install_nselib():
    st.write("Installing nselib...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "nselib"])
        st.write("nselib installed successfully!")
    except subprocess.CalledProcessError:
        st.error("Error installing nselib. Please check your internet connection and try again.")
        sys.exit(1)

def main():
    st.title("Install nselib and Code Editor")

    if st.button("Install nselib"):
        install_nselib()

    if os.path.exists("nselib"):
        st.write("nselib is installed.")
        st.code("import nselib")

        # Provide a code editor
        st.subheader("Code Editor")
        code = st.text_area("Enter your code here", "# Write your code here")
        st.write("You entered:")
        st.code(code, language="python")

if __name__ == "__main__":
    main()
