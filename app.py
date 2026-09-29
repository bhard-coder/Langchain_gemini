import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="centered"
)

# Application title
st.title("🤖 AI Study Assistant")
st.write("Ask a question and get an AI-generated explanation using LangChain and Google Gemini.")

# User input
question = st.text_area(
    "Enter your question:",
    placeholder="Example: Explain machine learning in simple terms."
)

# Generate answer
if st.button("Generate Answer"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        try:
            # Initialize Gemini
            llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)

            # Create LangChain prompt
            prompt = ChatPromptTemplate.from_template(
                """
                You are a helpful study assistant.
                Explain the following question clearly and simply.
                Use examples when useful.

                Question:
                {question}
                """
            )

            # Create LangChain chain
            chain = prompt | llm

            # Generate response
            response = chain.invoke({
                "question": question
            })

            # Display response
            st.subheader("Gemini Response")
            st.write(response.text)

        except Exception as e:
            st.error(f"An error occurred: {e}")