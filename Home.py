import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Amazon Sales Analysis")

st.write("This is a dashboard for analyzing Amazon sales data.")

st.write("Go to Dashboard page from the sidebar to get started.")

st.image("https://www.neoadviser.com/wp-content/uploads/2021/01/am.png")


df = pd.read_csv("cleaned_data.csv")

# Sidebar Filters
st.sidebar.header("Filters")

# Filter by Gender
gender_filter = st.sidebar.multiselect(
    'Select Gender', 
    df['Gender'].unique(), 
    default=df['Gender'].unique()
)
if not gender_filter:
    gender_filter = df['Gender'].unique()  # Default to all options
filtered_data = df[df['Gender'].isin(gender_filter)]

# Filter by Age Group
age_group_filter = st.sidebar.multiselect(
    'Select Age Group', 
    filtered_data['Age Group'].unique(), 
    default=filtered_data['Age Group'].unique()
)
if not age_group_filter:
    age_group_filter = filtered_data['Age Group'].unique()  # Default to all options
filtered_data = filtered_data[filtered_data['Age Group'].isin(age_group_filter)]

# Filter by State
state_filter = st.sidebar.multiselect(
    'Select State', 
    filtered_data['State'].unique(), 
    default=filtered_data['State'].unique()
)
if not state_filter:
    state_filter = filtered_data['State'].unique()  # Default to all options
filtered_data = filtered_data[filtered_data['State'].isin(state_filter)]

# Filter by Marital Status
marital_status_filter = st.sidebar.multiselect(
    'Select Marital Status', 
    filtered_data['Marital_Status'].unique(), 
    default=filtered_data['Marital_Status'].unique()
)
if not marital_status_filter:
    marital_status_filter = filtered_data['Marital_Status'].unique()  # Default to all options
filtered_data = filtered_data[filtered_data['Marital_Status'].isin(marital_status_filter)]

# Dataset Summary
st.info(f"""
### Dataset Summary
- **Total Records**: {filtered_data.shape[0]}
- **Total Orders**: {filtered_data['Orders'].sum()}

""")
st.success(f"""
- Total Sales: ₹{filtered_data['Amount'].sum():,.2f}
- Total Products: {filtered_data['Product_ID'].nunique()}
            """)



