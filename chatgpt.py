# -*- coding: utf-8 -*-
"""Untitled43.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A0IU9gCEDRYCmsfjESTc4RZ_WwbzvzBx
"""

pip install -q openai
pip install streamlit

import streamlit as st
import openai

openai.api_key = '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'

messages = [ 
    {"role": "system", "content": "Você é um especialista em prompts de artigos científicos com citações e referências."},
]

st.title('Chat com OpenAI GPT-3')

user_input = st.text_input('User :')

if user_input:
    messages.append({"role": "user", "content": user_input})
    chat = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=" ".join([message["content"] for message in messages]),
        max_tokens=4000 # Definindo o valor máximo de tokens para 4000
    )
    
    reply = chat.choices[0].message.content
    st.text_area("ChatGPT:", value=reply, height=200)
    messages.append({"role": "assistant", "content": reply})
