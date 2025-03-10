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

## Chatbot with Streamlit 
### A very basic  chatbot with Streamlit
It receives a text from the user and writes the same text 
```python
import streamlit as st

st.title("A Simple Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_query = st.chat_input("Say something...")

if user_query:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_query})

    # Simple bot response (Echo bot)
    bot_response = f"You said: {user_query}"

    # Store and display bot response
    with st.chat_message("assistant"):
        st.write(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
```

### A basic chatbot to retrieve metrics from a data set
This chatbot has a limited number of metrics related questions it can answer from a car sharing dataset

```python
import streamlit as st
import pandas as pd

# Load Data
df = pd.read_csv("datasets/trips_data_1000.csv")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chatbot UI
st.title("Trip Data Chatbot")
st.write("Ask me about trips, revenue, or average trip distance! (e.g., 'What is the total revenue')")

# User Input
user_query = st.chat_input("Type your question...")

if user_query:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_query})

    # Default response
    response = "Sorry, I didn't understand your question."

    # Check for total revenue queries
    if "total revenue" in user_query.lower():
        total_revenue = df["revenue"].sum()
        response = f"Total revenue was **${round(total_revenue, 2):,}**."

    # Check for total trips queries
    elif "total trips" in user_query.lower():
        total_trips = len(df)
        response = f"There were **{total_trips:,} trips** recorded in the dataset."

    # Check for average distance queries
    elif "average trip distance" in user_query.lower():
        avg_distance = df['distance'].mean()
        response = f"The average trip distance was **{round(avg_distance, 2)} km**."

    # Store and display chatbot response
    with st.chat_message("assistant"):
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
```