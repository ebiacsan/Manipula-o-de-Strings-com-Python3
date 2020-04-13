import re

test1 = "Meu numero é 1234-5678"
test2 = "Fale comigo em 2345-6789"
test3 = "Duvidas? 3456-7890 posso te ajudar"
test4 = "Entre em contato no seguinte número: 9999-2222"
test5 = "Esse é meu celular: 99877-6657 ou ligue no fixo: 36286965"

patern = "[0-9]{4,5}[-]*[0-9]{4}"

# result = re.search(patern, test5) #search retorna a primeira ocorrência
result = re.findall(patern, test5) #findAll retorna tudo que atende a RegEx
print(result)