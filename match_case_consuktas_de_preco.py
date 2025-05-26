# exibe os codigos disponiveis
print("codigos de produtos:")
print("1 - cafe")
print("2 - cha")
print("3 - suco")
print("4 - refrigerante")
print("5 - agua")
print("0 - sair")

#solicita o codigo do ao usuario 
codigo = int(input("digite o codigo do produto: "))

#usa match-case para mostrar o preço com base no codigo 
match codigo:
    case 1:
        print("produto: cafe - preço: r$ 4,50")
    case 2:
        print("produto: cha - preço: r$ 3,00")   
    case 3:
         print("produto: suco - preço: r$ 5,00") 
    case 4:     
        print("produto: refrigerante - preço r$ 6,00")
    case 5:
        print("produto: agua - preço r$ 2,00") 
    case 0:
        print("saindo do programa...") 
        exit() #encerra o progrma se o codigo for 0
    case _:
        print("codigo invalido. por favor,tente novamente.")           