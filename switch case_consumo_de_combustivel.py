#switch case
#solicita os dados do usuário
distancia_percorrida=float(input("digite a distancia percorrida em km:"))
combustivel_gasto=float(input("digite a quantidade de combustivel gasto em litros:"))

#calcula o consumo medio
consumo_medio=distancia_percorrida/combustivel_gasto

#classifica o consumo usando match-case
match consumo_medio: #match consumo_: abre o bloco de "casos".
    case valor if valor< 8:
        print("consumo menor que 8 km/1-desempenho ruim")
    case valor if valor< 12:
        print("consumo entre 8 e 12 km/1-desempenho medio")
    case _:
        print("consumo maior ou igual a 12 km/1-otimo desempenho")    