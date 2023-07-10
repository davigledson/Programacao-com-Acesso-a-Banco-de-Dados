#Projeto de interface gráfica com ChatGPT-3
from senha import  API_KEY
import requests
import json

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type":"application/json"}
link = 'https://api.openai.com/v1/chat/completions'
modelo_id = 'gpt-3.5-turbo'
body_mensagem = {
    'model': modelo_id,
    'messages': [{'role':'user','content':'escreva um bom dia como se fosse um a garota de anime'}]
}
body_mensagem = json.dumps(body_mensagem)
requisicao = requests.post(link , headers=headers, data=body_mensagem)

print(requisicao)
#print(requisicao.text)
resposta = requisicao.json()
mensagem = resposta['choices'][0]['message']['content']
print(mensagem)