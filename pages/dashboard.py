import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
st.title(":orange[This is a dashboard for analyzing Amazon sales data.]")
df = pd.read_csv("cleaned_data.csv")

# Sidebar Filters
st.sidebar.header("Filters")

# Filter by Gender
gender_filter = st.sidebar.multiselect('Select Gender', df['Gender'].unique(), default=df['Gender'].unique())
filtered_data = df[df['Gender'].isin(gender_filter)]

# Filter by Age Group
age_group_filter = st.sidebar.multiselect('Select Age Group', filtered_data['Age Group'].unique(), default=filtered_data['Age Group'].unique())
filtered_data = filtered_data[filtered_data['Age Group'].isin(age_group_filter)]

# Filter by State
state_filter = st.sidebar.multiselect('Select State', filtered_data['State'].unique(), default=filtered_data['State'].unique())
filtered_data = filtered_data[filtered_data['State'].isin(state_filter)]

# Filter by Marital Status
marital_status_filter = st.sidebar.multiselect('Select Marital Status', filtered_data['Marital_Status'].unique(), default=filtered_data['Marital_Status'].unique())
filtered_data = filtered_data[filtered_data['Marital_Status'].isin(marital_status_filter)]

# Dataset Summary
st.info(f"""
### Dataset Summary
- **Total Records**: {filtered_data.shape[0]}
- **Total Orders**: {filtered_data['Orders'].sum()}
- **Total Amount**: ₹{filtered_data['Amount'].sum():,.2f}
""")

# Display Filtered Dataset
st.success("### Dataset Preview")
st.write(filtered_data)

# Charts Section
st.write("### Data Visualizations")

# 1. Orders by Product Category
st.info(f'Order Count of {filtered_data.shape[0]} records')
order_count = filtered_data['Product_Category'].value_counts().reset_index()
order_count.columns = ['Product_Category', 'orderCount']
fig1 = px.bar(order_count, x='Product_Category', y='orderCount', title='Orders by Product Category', color='Product_Category')
st.plotly_chart(fig1)

# 2. Gender Distribution
st.info(f'Male Count: {filtered_data[filtered_data["Gender"] == "M"].shape[0]}, Female Count: {filtered_data[filtered_data["Gender"] == "F"].shape[0]}')
fig2 = px.pie(filtered_data, names='Gender', title='Gender Distribution')
st.plotly_chart(fig2)

# 3. Age Distribution
st.info(f'Age Group Count: {filtered_data["Age Group"].value_counts().to_dict()}')
fig3 = px.pie(filtered_data, names='Age Group', title='Age Distribution', color='Age Group')
st.plotly_chart(fig3)

# 4. Orders vs Amount
st.info(f'Age Group with the highest orders and amount: {filtered_data.groupby("Age Group")["Orders"].sum().idxmax()} and Total Orders: {filtered_data["Orders"].sum()}')
orders_amount = filtered_data.groupby('Age Group')[['Orders', 'Amount']].sum().reset_index()
fig4 = px.bar(orders_amount, x='Age Group', y='Amount', title='Orders vs Amount', color='Age Group')
st.plotly_chart(fig4)

# 5. Amount by State
st.info(f'State with the highest spending: {filtered_data.groupby("State")["Amount"].sum().idxmax()}')
fig5 = px.bar(filtered_data, x='State', y='Amount', title='Amount by State', color='State')
st.plotly_chart(fig5)

# 6. Marital Status Distribution
st.info(f'Marital Status Count: 0 (Unmarried) & 1 (Married): {filtered_data["Marital_Status"].value_counts().to_dict()}' )
fig6 = px.pie(filtered_data, names='Marital_Status', title='Marital Status Distribution')
st.plotly_chart(fig6)

# 7. Orders Distribution
st.info(f'Orders Count: {filtered_data["Orders"].value_counts().to_dict()}')
fig7 = px.pie(filtered_data, names='Orders', title='Orders Distribution')
st.plotly_chart(fig7)

# 8. Age vs Amount
st.info(f'Age Group with the highest amount: {filtered_data.groupby("Age Group")["Amount"].sum().idxmax()}')
fig8 = px.scatter(filtered_data, x='Age', y='Amount', title='Age vs Amount', color='Age Group')
st.plotly_chart(fig8)

# 9. Product Category Distribution
st.info(f'Highest Product Category: {filtered_data["Product_Category"].value_counts().idxmax()} and Lowest Product Category: {filtered_data["Product_Category"].value_counts().idxmin()}')
fig9 = px.pie(filtered_data, names='Product_Category', title='Product Category Distribution')
st.plotly_chart(fig9)

# 10. Amount Distribution (Histogram)
st.info(f'Age Group with the highest spending: {filtered_data.groupby("Age Group")["Amount"].sum().idxmax()}')
fig10 = px.histogram(filtered_data, x='Amount', title='Amount Distribution', color='Age Group')
st.plotly_chart(fig10)

# 11. Amount by Occupation
st.info(f'Occupation with the highest spending: {filtered_data.groupby("Occupation")["Amount"].sum().idxmax()}')
occupation_amount = filtered_data.groupby('Occupation')['Amount'].sum().reset_index()
fig11 = px.bar(occupation_amount, x='Occupation', y='Amount', title='Amount by Occupation', color='Occupation')
st.plotly_chart(fig11)

# 12. Orders by State
st.info(f'State with the highest orders: {filtered_data.groupby("State")["Orders"].sum().idxmax()}')
state_orders = filtered_data.groupby('State')['Orders'].sum().reset_index()
fig12 = px.bar(state_orders, x='State', y='Orders', title='Orders by State', color='State')
st.plotly_chart(fig12)

# 13. Orders by Gender
st.info(f'Gender with the highest orders: {filtered_data.groupby("Gender")["Orders"].sum().idxmax()}')
fig13 = px.bar(filtered_data.groupby('Gender')['Orders'].sum().reset_index(), x='Gender', y='Orders', title='Orders by Gender', color='Gender')
st.plotly_chart(fig13)

# 14. Total Spending by Age Group
st.info(f'Age Group with the highest spending: {filtered_data.groupby("Age Group")["Amount"].sum().idxmax()}')
fig14 = px.bar(filtered_data.groupby('Age Group')['Amount'].sum().reset_index(), x='Age Group', y='Amount', title='Spending by Age Group', color='Age Group')
st.plotly_chart(fig14)

# Static Conclusion
st.success("""
### Complete Conclusion
From the complete data, we can conclude the following:
- Most buyers are from IT, Healthcare, and Aviation.
- Significant customers are in the 36-45 age group.
- Married women from UP, Maharashtra, and Karnataka dominate the buyer segment.
- Popular categories are Clothing, Food, Electronics, and Footwear.
""")

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
