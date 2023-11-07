import streamlit as st
import pandas as pd

# add title for the app
st.title("Exploratory Data Analysis")

# sidebar title
st.sidebar.title("Upload Data")

# add tabs
tab1, tab2, tab3 = st.tabs(["DataFrame", "Numeric Features", "Categorical Features"])

# add file-uploader widget in sidebar
uploaded_data = st.sidebar.file_uploader("Choose a CSV file")

@st.cache_data
def load_data(file_name):
  # read CSV file
  data = pd.read_csv(file_name)
  # change date columns datatype to "datetime"
  data['Date'] = pd.to_datetime(data['Date'])
  return data

if uploaded_data is not None:
  # read csv
  df = load_data(uploaded_data)

with tab1:
  if uploaded_data is not None:
    # extract meta-data from the uploaded dataset
    st.header("Dataframe")

    row_count = df.shape[0]

    column_count = df.shape[1]
    
    # Use the duplicated() function to identify duplicate rows
    duplicates = df[df.duplicated()]
    duplicate_row_count =  duplicates.shape[0]

    missing_value_row_count = df[df.isna().any(axis=1)].shape[0]

    table_markdown = f"""
      | Description | Value | 
      |---|---|
      | Number of Rows | {row_count} |
      | Number of Columns | {column_count} |
      | Number of Duplicated Rows | {duplicate_row_count} |
      | Number of Rows with Missing Values | {missing_value_row_count} |
      """

    st.markdown(table_markdown)

