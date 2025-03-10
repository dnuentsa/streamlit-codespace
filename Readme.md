A simple app to demonstrate the power of Streamlit and CodeSpace

# Code Snippets
## Date Range Selection and Filtering
### Using a date_input for date range selection
The following Python snippet allows users to **select a date range** and dynamically filter the trip dataset:

```python
import streamlit as st
import pandas as pd


df = pd.read_csv("dataset.csv")
df['pickup_time'] = pd.to_datetime(df['pickup_time'])
df['trip_date'] = df['pickup_time'].dt.date  # Extract date for filtering

# Create date range input
start_date, end_date = st.date_input(
    "Select Date Range", 
    [df['trip_date'].min(), df['trip_date'].max()],  # Default to full range
    min_value=df['trip_date'].min(), 
    max_value=df['trip_date'].max()
)

# Filter dataframe based on selected dates
filtered_df = df[(df['trip_date'] >= start_date) & (df['trip_date'] <= end_date)]

# Display results
st.write(f"Showing data from **{start_date}** to **{end_date}**")
st.write(filtered_df)
``` 
### Showcase the metric delta variation

```python
import streamlit as st
import pandas as pd

# Load Data
df = pd.read_csv("trips_data_2024.csv")
df['pickup_time'] = pd.to_datetime(df['pickup_time'])
df['trip_month'] = df['pickup_time'].dt.to_period("M")  # Extract month (Year-Month format)

# Get Unique Months for Selection
available_months = df['trip_month'].astype(str).unique()

# Select a Month
selected_month = st.selectbox("Select a Month", available_months, index=len(available_months)-1)

# Convert to Period format for filtering
selected_period = pd.Period(selected_month)

# Filter Data for Selected Month and Previous Month
current_month_df = df[df['trip_month'] == selected_period]
previous_month_df = df[df['trip_month'] == (selected_period - 1)]

# Compute Metrics
current_revenue = round(current_month_df['revenue'].sum(), 2)
previous_revenue = round(previous_month_df['revenue'].sum(), 2) if not previous_month_df.empty else 0
revenue_delta = current_revenue - previous_revenue

# Display Metrics in Streamlit
st.metric(label=f"Total Revenue for {selected_month}", value=f"${current_revenue:,}", delta=f"${revenue_delta:,}")
```
