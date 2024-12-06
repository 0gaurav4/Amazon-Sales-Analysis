import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Amazon Sales Analysis")

st.write("This is a dashboard for analyzing Amazon sales data.")

st.write("Go to Dashboard page from the sidebar to get started.")

st.image("https://www.neoadviser.com/wp-content/uploads/2021/01/am.png")




# Load Data
df = pd.read_csv("cleaned_data.csv")

# Sidebar Filters
st.sidebar.header("Filters")

try:
    gender_filter = st.sidebar.multiselect('Select Gender', df['Gender'].unique(), default=df['Gender'].unique())
    filtered_data = df[df['Gender'].isin(gender_filter)]

    age_group_filter = st.sidebar.multiselect('Select Age Group', filtered_data['Age Group'].unique(), default=filtered_data['Age Group'].unique())
    filtered_data = filtered_data[filtered_data['Age Group'].isin(age_group_filter)]

    marital_status_filter = st.sidebar.multiselect('Select Marital Status', filtered_data['Marital_Status'].unique(), default=filtered_data['Marital_Status'].unique())
    filtered_data = filtered_data[filtered_data['Marital_Status'].isin(marital_status_filter)]

except:
    st.error("Please select at least one filter")

# Dataset Summary
st.header("Dataset Summary")
st.write("Total Sales: ", filtered_data['Amount'].sum())
st.write("Total Products: ", filtered_data['Product_ID'].nunique())


