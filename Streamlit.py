import streamlit as st  # Import Streamlit library
import pandas as pd  # Import Pandas for data handling
import numpy as np  # Import NumPy for generating sample data
import matplotlib.pyplot as plt  # Import Matplotlib for plotting

# Set page title and layout
st.set_page_config(page_title='Sample Dashboard', layout='wide')

# Title of the dashboard
st.title('📊 Sample Streamlit Dashboard')

# Generate sample data
# Creating a DataFrame with random values for demonstration purposes
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],  # Categories
    'Value': np.random.randint(10, 100, 5)  # Random values between 10 and 100
})

# Display key metrics using Streamlit columns
col1, col2, col3 = st.columns(3)  # Creating three columns
col1.metric("Total Items", len(data))  # Display total number of categories
col2.metric("Max Value", data['Value'].max())  # Display maximum value in dataset
col3.metric("Min Value", data['Value'].min())  # Display minimum value in dataset

# Display table of data
st.subheader("📋 Data Table")  # Section header
st.dataframe(data)  # Show data in a tabular format

# Display bar chart representation
st.subheader("📊 Bar Chart Representation")  # Section header
fig, ax = plt.subplots()  # Create a Matplotlib figure
ax.bar(data['Category'], data['Value'], color=['red', 'blue', 'green', 'orange', 'purple'])  # Bar chart
ax.set_xlabel("Category")  # X-axis label
ax.set_ylabel("Value")  # Y-axis label
ax.set_title("Category-wise Values")  # Chart title
st.pyplot(fig)  # Display chart in Streamlit

# Add an interactive slider to filter data
def update_chart(val):
    """Filters and displays data based on slider input"""
    filtered_data = data[data['Value'] > val]  # Filter rows where value > slider input
    st.dataframe(filtered_data)  # Show filtered data

# Create slider for value filtering
slider_value = st.slider("Filter values greater than:", min_value=int(data['Value'].min()), max_value=int(data['Value'].max()), value=int(data['Value'].min()))
update_chart(slider_value)  # Call function to update table based on slider value
