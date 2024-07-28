import streamlit as st
from openai import OpenAI


f = open("C:/Users/mitra/Desktop/INNOMATICS(MITRABHANU PANDA)/GEN AI (ADVANCE)/6. PROJECTS/2. AI CODE REVIEWER/KEY/openai_api_key.txt")
OPENAI_API_KEY = f.read()

client = OpenAI(api_key = OPENAI_API_KEY)

st.header(" 🗯 AN AI CODE REVIEWER")



prompt = st.text_area("Enter your Python Code", height=15)

def chatgpt(prompt):
    response = client.chat.completions.create(
                      model="gpt-4o-mini",
                      messages=[
                          {"role": "system", "content": """You are a AI Assistant for python code who assist the user's written code. if the user's code is wrong then you need to explain user  where they done mistakes by using the bold heading BUG IN THE CODE always write the bugs in a list and fix the bugs by using the bold heading FIXED CODE. if the user's code is right then do not give any reply only say THE CODE IS RIGHT & DO NOT HAVE ANY MISTAKES.if user do not write anything then donot message."""},
                          {"role": "user", "content": prompt}
                      ]
                )
    return response.choices[0].message.content
if st.button("Generate"):

    st.write(chatgpt(prompt))