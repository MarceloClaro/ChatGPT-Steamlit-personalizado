import os
import streamlit as st
import openai

# Instala o pacote openai
os.system('pip install openai')

# Define a chave da API da OpenAI
openai.api_key = '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'

# Define as mensagens iniciais
messages = [
    {"role": "system", "content": "Você é um especialista em prompts de artigos científicos com citações e referências."},
]

# Define o título da página
st.title('Chat com OpenAI GPT-3')

# Cria a caixa de texto para o usuário digitar sua mensagem
user_input = st.text_input('User :')

# Se o usuário digitou uma mensagem, adiciona a mensagem à lista de mensagens
if user_input:
    messages.append({"role": "user", "content": user_input})
    
    # Envia as mensagens para o modelo GPT-3 da OpenAI e recebe a resposta
    chat = openai.Completion.create(
        model="text-davinci-002",
        prompt=" ".join([message["content"] for message in messages]),
        max_tokens=4000, # Definindo o valor máximo de tokens para 4000
        temperature=0.5, # Define a "criatividade" da resposta
    )
    
    # Extrai a resposta do objeto retornado pelo modelo
    reply = chat.choices[0].text
    
    # Adiciona a resposta à lista de mensagens
    messages.append({"role": "assistant", "content": reply})

# Mostra as mensagens em uma caixa de texto grande
st.text_area("ChatGPT:", value="\n".join([f'{msg["role"]}: {msg["content"]}' for msg in messages]), height=200)
