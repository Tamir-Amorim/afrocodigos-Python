
from passagens import PassagensAereaManager, Passagem
from apresentacao import mostra_menu, menu_compra_passagem


while True:
    passagens_areareas_manager = PassagensAereaManager()
    
    mostra_menu()
    
    escolha_do_usuario = int(input("Digite aqui -->"))
    
    if escolha_do_usuario == 1:
        
       origem, destino, preço = menu_compra_passagem()
       
       passagem = Passagem(origem, destino, preço)
       
       passagens_areareas_manager.adicionar_passagem(passagem)
        
    elif escolha_do_usuario == 2:
        
        print("Você escolheu listar as passagens\n")
        print(passagens_areareas_manager.passagens_compradas)
        
    elif escolha_do_usuario == 3:
        print("Volte sempre! ")
        break
    
    else:  print("*" *25), print("Digite um número válido"), print("*" *25)
            
    
    
