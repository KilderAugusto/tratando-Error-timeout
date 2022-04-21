import requests
import json
try:    req = requests.get("http://54.205.129.122:5000/params", timeout=1)
except requests.exceptions.ConnectionError:
    print('TEMPO ESGOTADO!')
else:
    print('CHAMADA COM SUCESSO!')

    print(req.json())

    with open('dados.json','w',encoding='utf-8') as dados_file:

        json.dump(req.json(), dados_file)  #salva o json da api consumida

    dados_file.close()  #fecha o arquivo








