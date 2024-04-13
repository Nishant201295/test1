import streamlit as st
import subprocess

def install_packages(packages):
    for package in packages:
        st.write(f"Installing {package}...")
        subprocess.run(["pip", "install", package])
        st.write(f"Successfully installed {package}")

def main():
    st.title("Package Installer")

    packages = [
        "pandas>=2.0.0",
        "requests>=2.31.0",
        "xlrd>=2.0.1"
    ]

    st.write("This app installs the following packages:")
    for package in packages:
        st.write(f"- {package}")

    if st.button("Install Packages"):
        install_packages(packages)

if __name__ == "__main__":
    main()
