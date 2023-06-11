from GPTAgent.GPTAgent import GPTAgent # pip install GPTAgent

# criar um arquivo 'chat_key.json' com a chave no formato json {"api_key": "coloque_aqui_sua_api_key_da_OpenAI"}

agente = GPTAgent(name="Bob", estilo="Você é engraçado e positivo.")
print(agente.perguntar("Bom dia!"))
