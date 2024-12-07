import streamlit as st
import pandas as pd

# Load Data
st.title(":orange[This is conclusions of Amazon sales data.]")
df = pd.read_csv("cleaned_data.csv")


# Dataset Summary
st.sidebar.info(f"""
### Dataset Summary
- **Total Records**: {df.shape[0]}
- **Total Orders**: {df['Orders'].sum()}
- **Total Amount**: ₹{df['Amount'].sum():,.2f}
- **Total Products**: {df['Product_ID'].nunique()}
- **Age Groups Present**: {df['Age Group'].unique()}
""")



# Static Conclusion
st.success("""
### Complete Conclusion
From the complete data, we can conclude the following:
- Most buyers are from IT, Healthcare, and Aviation.
- Significant customers are in the 36-45 age group.
- Married women from UP, Maharashtra, and Karnataka dominate the buyer segment.
- Popular categories are Clothing, Food, Electronics, and Footwear.
""")

