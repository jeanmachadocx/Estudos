import requests
# -*- coding: utf-8 -*-

print("Bem vindo ao sistema de cotação de moedas")
print("------------------------------------------")
print("Moedas disponíveis: USD, BRL, EUR, BTC")

while True:
    print("\nDigite 'sair' a qualquer momento para encerrar.")
    
    
    moeda_origem = input("Digite a moeda de origem: ").strip().upper()
    if moeda_origem == "SAIR":
        break

  
    moeda_destino = input("Digite a moeda de destino: ").strip().upper()
    if moeda_destino == "SAIR":
        break

    # URL API
    URL = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"

    # Fazendo a requisição
    requisicao = requests.get(URL)

    if requisicao.status_code == 200:
        try:
            # Extraindo a cotação
            cotacao = requisicao.json().get(f"{moeda_origem}{moeda_destino}", {}).get("bid")
            if cotacao:
                print(f"\nA cotação de {moeda_origem} para {moeda_destino} é: {cotacao}")
            else:
                print("\nNão foi possível encontrar a cotação para as moedas informadas.")
        except Exception as e:
            print("Ocorreu um erro ao processar a resposta da API:", e)
    else:
        print(f"\nNão foi possível obter a cotação. Código de status: {requisicao.status_code}")

print("\nPrograma encerrado.")
