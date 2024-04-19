
def mostra_menu():
    
    print("##" *10)
    print("Passágens Aéreas")
    print("##" *10)
    print("Digite 1 para comprar Passagens")
    print("Digite 2 para Listar Passagens")
    print("Digite 3 para Sair")
    
def menu_compra_passagem():
    origem = input("Informe a origem ->")
    destino = input("Informe o destino ->")
    preço = float(input("informe qual o valor ->"))
    
    return origem, destino, preço