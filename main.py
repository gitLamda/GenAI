# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 09:45:06 2024

@author: User
"""
import os
import json
import streamlit as st
from groq import Groq

# streamlit page configuratin 
st.set_page_config(
    page_title = "LambdaQ",
    page_icon = "💬",
    layout = "centered",
    )

GROQ_API_KEY = "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"

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = Groq()

# initialize the chat history as streamlit session state of not present already
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# streamlit page title
st.title("🐺 LambdaQ 3.1. ChatBot")

# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# input field for user's message:
user_prompt = st.chat_input("Ask Lambda...")

if user_prompt:

    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # sens user's message to the LLM and get a response
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        *st.session_state.chat_history
    ]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # display the LLM's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
