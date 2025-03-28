import streamlit as st
from openai import OpenAI
api_key = "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"
# api_key = "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"

client = OpenAI(api_key=api_key)

st.title("Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("What's up?"):
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = [
                {"role": m["role"], "content":m["content"]}
                for m in st.session_state.messages
            ])
        assistant_response = response.choices[0].message.content
        st.markdown(assistant_response)

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_response}
    )