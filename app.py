import streamlit as st

# add title for the app
st.title("Exploratory Data Analysis")

# sidebar title
st.sidebar.title("Upload Data")

# add tabs
tab1, tab2, tab3 = st.tabs(["DataFrame", "Numeric Features", "Categorical Features"])