import requests

API_KEY = "8ee55bcb9519fd2c6b5e78d09ce52d89"
cidade = "São Paulo"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp'] - 273.15
print(f"PREVISÃO DO TEMPO\n --SÃO PAULO--\n\nClima: {descricao}\nTemperatura: {temperatura:.2f}ºC\n")
