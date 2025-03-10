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
### Using a slide for date range selection
# Load Data
```python
import streamlit as st
import pandas as pd
df = pd.read_csv("trips_data_2024.csv")
df['pickup_time'] = pd.to_datetime(df['pickup_time'])
df['trip_date'] = df['pickup_time'].dt.date  # Extract only the date

# Define min and max date
min_date = df['trip_date'].min()
max_date = df['trip_date'].max()

# Create date range slider
start_date, end_date = st.slider(
    "Select Date Range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date),  # Default to full range
    format="YYYY-MM-DD"
)

# Filter dataframe based on selected dates
filtered_df = df[(df['trip_date'] >= start_date) & (df['trip_date'] <= end_date)]

# Display results
st.write(f"Showing data from **{start_date}** to **{end_date}**")
st.write(filtered_df)
```
