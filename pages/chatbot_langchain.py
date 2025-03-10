import streamlit as st
import pandas as pd
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.chat_history import HumanMessage

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("datasets/trips_data_1000.csv")
    df['pickup_time'] = pd.to_datetime(df['pickup_time'])
    return df

df = load_data()

# Initialize chatbot model (using Ollama)
model = ChatOllama(model="mistral")  # Make sure you have Ollama installed and running

# Streamlit UI
st.title("🚖 Car Sharing Data Chatbot")
st.write("Ask me about trips, revenue, distances, and more!")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display past chat_history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
query = st.chat_input("Ask a question about the dataset...")

if query:
    # Add user query to chat history
    st.session_state.chat_history.append({"role": "user", "content": query})

    # Define prompt for LLM
    prompt = PromptTemplate.from_template("""
    You are a data analyst assistant. Answer user queries based on the following dataset:
    {data}
    
    Question: {question}
    Answer:
    """)

    # Format the input with data preview
    formatted_prompt = prompt.format(data=df.head(5).to_string(), question=query)

    # Get chatbot response
    response = model.invoke([HumanMessage(content=formatted_prompt)]).content

    # Display bot response
    with st.chat_message("assistant"):
        st.write(response)

    # Add response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})
