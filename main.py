from ExtratorArgumentosURL import ExtratorArgumentosURL

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedAdestino=dolar&valor=1000"
url2 = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedAdestino=dolar&valor=1500"

argumentoURL = ExtratorArgumentosURL(url)
argumentoURL2 = ExtratorArgumentosURL(url)
moeda_origem, moeda_destino = argumentoURL.extrai_argumentos()
valor = argumentoURL.extrai_valor()

print(moeda_origem, moeda_destino, valor)

#print(id(argumentoURL))
#print(id(argumentoURL2))
#print(argumentoURL == argumentoURL2)