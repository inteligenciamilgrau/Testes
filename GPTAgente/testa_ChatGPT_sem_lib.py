import openai # pip install openai

# Inicializa a chave da API
openai.api_key = "sua_api_key"

def generate_answer(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": messages}],
            max_tokens=1000,
            temperature=0.9
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Erro", e)
        return e
pergunta = "Bom dia"
answer = generate_answer(pergunta)
print("Pergunta:", pergunta)
print("ChatGPT:", answer)
