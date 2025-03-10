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