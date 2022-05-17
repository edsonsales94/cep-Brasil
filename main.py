import requests
from acesso_cep import BuscaEndereço

cep = 69099100
objeto_cep = BuscaEndereço(cep)
objeto_cep.acesso_via_cep()
logradouro, bairro, cidade, uf = objeto_cep.acesso_via_cep()
print(logradouro,'-', bairro ,'/' ,cidade,uf)

r = requests.get("https://viacep.com.br/ws/69099260/json/")
