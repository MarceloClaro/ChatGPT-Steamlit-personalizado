import streamlit as st
import openai

openai.api_key = "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"

st.title('Chat com OpenAI GPT-3 - Prof. marcelo Claro')

user_input = st.text_input('User :')

if user_input:
    messages = [{"role": "user", "content": user_input}]
    prompt = " ".join([message["content"] for message in messages])

    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text.strip()
    messages.append({"role": "assistant", "content": message})

    st.text_area("ChatGPT:", value=message, height=200)
