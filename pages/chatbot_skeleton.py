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
