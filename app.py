import streamlit as st
import pandas as pd

st.title("CSV File viewer")

df = pd.read_csv("datasets/trips_data.csv")
st.write(" Preview Uploaded data")
st.dataframe(df.head())



































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




