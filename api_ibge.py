import requests, json

nome = input("Qual é seu nome? ")
resultado = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/" + nome)

json_dados = json.loads(resultado.text)

print(json_dados[0]["res"][0])