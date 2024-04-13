import streamlit as st
import pandas as pd

def load_data(file):
    data = pd.read_csv(file)
    return data

def highlight_changes(old_df, new_df):
    changes_df = pd.concat([old_df, new_df]).drop_duplicates(keep=False)
    return changes_df

def main():
    st.title('Dataset Changes Analyzer')

    st.sidebar.header('Upload Files')
    old_file = st.sidebar.file_uploader('Upload old dataset (CSV)', type='csv')
    new_file = st.sidebar.file_uploader('Upload new dataset (CSV)', type='csv')

    if old_file and new_file:
        st.sidebar.success('Files uploaded successfully!')
        old_data = load_data(old_file)
        new_data = load_data(new_file)

        st.header('Old Dataset')
        st.write(old_data)

        st.header('New Dataset')
        st.write(new_data)

        st.header('Changes Highlighted')
        changes = highlight_changes(old_data, new_data)
        st.write(changes)

if __name__ == '__main__':
    main()
