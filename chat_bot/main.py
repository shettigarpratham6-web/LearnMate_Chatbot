from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.7
)


if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful assistant and your name is LearnMate")
    ]

st.title("LearnMate Chatbot")


for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)


prompt = st.chat_input("Type your message...")

if prompt:
   
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

  
    response = model.invoke(st.session_state.messages)

    
    with st.chat_message("assistant"):
        st.write(response.content)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )