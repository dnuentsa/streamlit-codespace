import streamlit as st
import pandas as pd
import numpy as np

st.title("Manipulate Streamlit Chart")

# Generate random data 
bar_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(bar_data)


# Generate random data for line chart
line_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(line_data)

# Generate random data for scatter chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.scatter_chart(chart_data)



































#st.title("User CSV File Viewer")

# Request the user to Upload the File 
# uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.write("Here is the preview of the Uploaded CSV: ")
#     st.dataframe(df.head())

#     # Chart 1: Bar chart of customers by country
#     st.subheader("Customers by City")
#     country_counts = df['customer_city'].value_counts()
#     st.write(country_counts)
#     st.bar_chart(country_counts)

#     # Chart 2: Line chart of subscriptions over time
#     st.subheader("Trips Over Time")
#     df['Trip Date'] = pd.to_datetime(df['pickup_time']).dt.date
#     subscriptions_by_date = df.groupby('Trip Date').size().reset_index(name='Count')
#     st.line_chart(subscriptions_by_date.set_index('Trip Date'))




