import requests

# projeto com api aloma
API_KEY = "9bf7a05caa2d1eebc8f72ace157554a2"
cidade = "São paulo"
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados["main"]["temp"]
    descricao = dados["weather"][0]["description"]
    print(f"Temperatura atual em {cidade}: {temperatura}°C")
    print(f"Condição: {descricao}")
else:
    print("Erro ao consultar a API de clima.")
