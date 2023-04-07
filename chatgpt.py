import streamlit as st
import openai

openai.api_key = 'sk-HThZaAIVEoWVSAAPztTT3BlbkFJGMCtUzsYlebJFxty7JbC'

messages = [ 
    {"role": "system", "content": "Você é um especialista em prompts de artigos científicos com citações e referências."},
]

st.title("Chatbot com GPT-3.5 Turbo")

while True:
    message = st.text_input("Você : ")
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=2000 # Definindo o valor máximo de tokens para 4000
        )
    
        reply = chat.choices[0].message.content
        st.write("ChatGPT:", reply)
        messages.append({"role": "assistant", "content": reply})
