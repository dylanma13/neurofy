import streamlit as st
import openai

# Set up the Streamlit app
st.title("Neurofy")
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

