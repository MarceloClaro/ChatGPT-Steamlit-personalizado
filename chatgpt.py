import openai
import streamlit as st

# Defina sua chave de API
openai.api_key = "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"

# Defina o modelo que será usado para gerar as respostas
model_engine = "text-davinci-002"

# Define a função para gerar uma resposta com base em uma pergunta
def generate_answer(question):
    prompt = f"Eu gostaria de saber {question}. A resposta é:"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Cria a interface do Streamlit
def main():
    st.title("Gerador de respostas usando OpenAI")

    # Obtém a pergunta do usuário
    question = st.text_input("Faça uma pergunta:")
    if not question:
        return

    # Gera a resposta com base na pergunta
    with st.spinner("Gerando resposta..."):
        answer = generate_answer(question)

    # Mostra a resposta para o usuário
    st.write(answer)

if __name__ == "__main__":
    main()
