pip install openai
import streamlit as st
import openai

# Set up the Streamlit app
st.title("Neurofy Chatbot")
st.write("Welcome to Neurofy! Start chatting below:")

# OpenAI API key
openai.api_key = "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"

# User input
user_input = st.text_input("Your message:", "")

# Function to get a response from the OpenAI GPT endpoint
def get_gpt_response(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Neurofy, a helpful chatbot."},
                {"role": "user", "content": message}
            ]
        )
        # Extract and return the GPT response
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Display the response if user has input a message
if user_input:
    response = get_gpt_response(user_input)
    st.text_area("Neurofy's response:", value=response, height=200)

