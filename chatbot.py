from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#creating my prompts

prompt = ChatPromptTemplate.from_messages(
  [
("system", 'You are helpful assistart, please respond to the question asked'), 
 ("user", "Question: {question}")
  ]
 )

#streamlit framework
st.title('My GPT')
input_text = st.text_input('What question do you have in mind')

#Let's create LLM chain system
#Ollama  LLAMA2 model
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
