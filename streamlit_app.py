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
            model="gpt-4-mini",
            messages=[
                {"role": "system", "content": "You are Neurofy, a helpful chatbot."},
                {"role": "user", "content": message}
            ]
        )
        # Extract and return the GPT response
        return response.choices[0].message["content"]
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Display the response if user has input a message
if user_input:
    response = get_gpt_response(user_input)
    st.text_area("Neurofy's response:", value=response, height=200)

