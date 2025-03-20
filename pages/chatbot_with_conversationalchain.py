import streamlit as st
import pandas as pd
from langchain_community.llms import HuggingFaceHub
from langchain_core.prompts import PromptTemplate

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("datasets/trips_data_1000.csv")
    df['pickup_time'] = pd.to_datetime(df['pickup_time'])
    return df

df = load_data()

# Sidebar for API key
st.sidebar.header("🔑 Enter Hugging Face API Key")
api_key = st.sidebar.text_input("Hugging Face API Key", type="password")

if not api_key:
    st.warning("Please enter a Hugging Face API key to use the chatbot.")
    st.stop()

# Initialize Hugging Face LLM
llm = HuggingFaceHub(
    repo_id="tiiuae/falcon-7b-instruct",
    huggingfacehub_api_token=api_key
)

# Streamlit UI
st.title("🚖 Car Sharing Data Chatbot")
st.write("Ask me about trips, revenue, distances, and more!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
query = st.chat_input("Ask a question about the dataset...")

if query:
    # Add user query to chat history
    st.session_state.messages.append({"role": "user", "content": query})

    # Define cleaner prompt for LLM
    prompt = PromptTemplate.from_template("""
    You have access to car-sharing trip data. Answer the question accurately based on the dataset.
    Here is a small preview of the data for context:
    {data}

    Question: {question}
    Answer:
    """)

    # Format the input with a small data preview
    formatted_prompt = prompt.format(data=df.head(5).to_string(), question=query)

    # Get chatbot response
    response = llm.invoke(formatted_prompt)

    # Display bot response
    with st.chat_message("assistant"):
        st.write(response.strip())  # Ensure clean output

    # Add response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.strip()})
