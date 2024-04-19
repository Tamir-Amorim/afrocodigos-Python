from operacoes import OperacoesMatematicas

instancia_operacoes = OperacoesMatematicas()

numero_1 = int(input("Informe um número -> "))
numero_2 = int(input("Informe outro número-> "))

soma = instancia_operacoes.soma(numero_1, numero_2)
subtracao = instancia_operacoes.subtracao(numero_1, numero_2)
multiplicacao = instancia_operacoes.multiplicacao(numero_1, numero_2)
divisao = instancia_operacoes.divisao(numero_1, numero_2)

print("*****************************")
print(f"A soma de {numero_1} e {numero_2} é {soma}" )
print(f"A subtração de {numero_1} e {numero_2} é {subtracao}" )
print(f"A multiplicação de {numero_1} e {numero_2} é {multiplicacao}" )
print(f"A divisão de {numero_1} e {numero_2} é {divisao}" )
print("*****************************")

#Com carinho, Tamir