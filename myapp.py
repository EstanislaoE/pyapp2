from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os 
import google.generativeai as genai 

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(inp):
    answer = model.generate_content(inp)
    return answer.text 

#Build teh UI on streamLit 
st.header("My first App")
input_1 = st.text_input("Ask your question", key="input_1")
submit = st.button("Click to Submit Q")

if submit: 
    answer_1 = get_gemini_response(input_1)
    st.write("Ai answer is: ")
    st.write(answer_1)
