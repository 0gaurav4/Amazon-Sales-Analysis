import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
st.title(":orange[This is a dashboard for analyzing Amazon sales data.]")
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


# Display Filtered Dataset
st.success("### Dataset Preview")
st.write(filtered_data)

# Charts Section
st.write("### Data Visualizations")

# 1. Orders by Product Category
order_count = filtered_data['Product_Category'].value_counts().reset_index()
order_count.columns = ['Product_Category', 'orderCount']
fig1 = px.bar(order_count, x='Product_Category', y='orderCount', title='Orders by Product Category', color='Product_Category')
st.plotly_chart(fig1)

# 2. Gender Distribution
fig2 = px.pie(filtered_data, names='Gender', title='Gender Distribution')
st.plotly_chart(fig2)

# 3. Age Distribution
fig3 = px.pie(filtered_data, names='Age Group', title='Age Distribution', color='Age Group')
st.plotly_chart(fig3)

# 4. Orders vs Amount
orders_amount = filtered_data.groupby('Age Group')[['Orders', 'Amount']].sum().reset_index()
fig4 = px.bar(orders_amount, x='Age Group', y='Amount', title='Orders vs Amount', color='Age Group')
st.plotly_chart(fig4)

# 5. Amount by State
fig5 = px.bar(filtered_data, x='State', y='Amount', title='Amount by State', color='State')
st.plotly_chart(fig5)

# 6. Marital Status Distribution
fig6 = px.pie(filtered_data, names='Marital_Status', title='Marital Status Distribution')
st.plotly_chart(fig6)

# 7. Orders Distribution
fig7 = px.pie(filtered_data, names='Orders', title='Orders Distribution')
st.plotly_chart(fig7)

# 8. Age vs Amount
fig8 = px.scatter(filtered_data, x='Age', y='Amount', title='Age vs Amount', color='Age Group')
st.plotly_chart(fig8)

# 9. Product Category Distribution
fig9 = px.pie(filtered_data, names='Product_Category', title='Product Category Distribution')
st.plotly_chart(fig9)

# 10. Amount Distribution (Histogram)
fig10 = px.histogram(filtered_data, x='Amount', title='Amount Distribution', color='Age Group')
st.plotly_chart(fig10)

# 11. Amount by Occupation
occupation_amount = filtered_data.groupby('Occupation')['Amount'].sum().reset_index()
fig11 = px.bar(occupation_amount, x='Occupation', y='Amount', title='Amount by Occupation', color='Occupation')
st.plotly_chart(fig11)

# 12. Orders by State
state_orders = filtered_data.groupby('State')['Orders'].sum().reset_index()
fig12 = px.bar(state_orders, x='State', y='Orders', title='Orders by State', color='State')
st.plotly_chart(fig12)

# 13. Orders by Gender
fig13 = px.bar(filtered_data.groupby('Gender')['Orders'].sum().reset_index(), x='Gender', y='Orders', title='Orders by Gender', color='Gender')
st.plotly_chart(fig13)

# 14. Total Spending by Age Group
fig14 = px.bar(filtered_data.groupby('Age Group')['Amount'].sum().reset_index(), x='Age Group', y='Amount', title='Spending by Age Group', color='Age Group')
st.plotly_chart(fig14)


# Dynamic Conclusion
dynamic_conclusion = f"""
### Dynamic Conclusion
Based on the applied filters:
- The dataset contains **{filtered_data.shape[0]} records**.
- The total orders are **{filtered_data['Orders'].sum()}**, amounting to ₹**{filtered_data['Amount'].sum():,.2f}**.
- The most common product category is **{filtered_data['Product_Category'].value_counts().idxmax()}**.
- The age group with the highest orders is **{filtered_data.groupby('Age Group')['Orders'].sum().idxmax()}**.
- The state with the highest spending is **{filtered_data.groupby('State')['Amount'].sum().idxmax()}**.
"""
st.info(dynamic_conclusion)