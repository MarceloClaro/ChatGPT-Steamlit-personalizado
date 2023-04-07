import streamlit as st
import openai

openai.api_key = 'sk-HThZaAIVEoWVSAAPztTT3BlbkFJGMCtUzsYlebJFxty7JbC'

messages = [ 
    {"role": "system", "content": "Olá, sou um chatbot com conhecimento em diversos assuntos. Tente me perguntar alguma coisa!"},
]

st.set_page_config(page_title="Chatbot com GPT-3.5 Turbo", page_icon=":robot_face:")

st.title("Chatbot com GPT-3.5 Turbo")

form = st.form(key='my-form')

message = form.text_input(label='Você:')

submit_button = form.form_submit_button(label='Enviar')

if submit_button:
    messages.append({"role": "user", "content": message})
    chat = openai.Completion.create(
        engine="davinci",
        prompt=f"Conversation with the chatbot:\nUser: {message}\nBot:",
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n", " User:", " Bot:"]
    )
    reply = chat.choices[0].text.strip()
    st.write("Chatbot: ", reply)
    messages.append({"role": "assistant", "content": reply})
