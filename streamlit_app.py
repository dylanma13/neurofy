from openai import OpenAI
import streamlit as st

st.title("Neurofy")

client = OpenAI(api_key="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")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4.0"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
