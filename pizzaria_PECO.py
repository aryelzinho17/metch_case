#exibe o menu de pizzas
print("menu de pizzaria")
print("1 - margherita")
print("2 - calabresa")
print("3 - frango com catupiry")
print("4 - quatro queijos")
print("5 - portuguesa")
print("0 - sair")

#solicita o codigo do sabor 
codigo_pizza = int(input("digite o codigo da pizza desejada"))

#usa match_case para mostrar o sabor e preço
match codigo_pizza:
    case 1:
        print("pizza: margherita - preço: r$ 35,00")
    case 2:
        print("pizza: calabresa - preço: r$ 38,00")
    case 3:
        print("pizza: frango com catupiry - preço: 42,00")  
    case 4:
        print("pizza:quatro queijos - preço r$ 40,00")  
    case 5:
        print("pizza: portuguesa - preço r$ 39,00 ")
    case 0:
        print("saindo do programa...")
        #encerra o programa se o codigo for 0
    case _:
        print("codigo invalido. por favor, selecione um codigo do menu")          



