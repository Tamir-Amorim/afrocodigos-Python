
entrada = int(input("Informe um número\n"))
fatorial = 0


for i in range(entrada,0,-1):
    fatorial += i    

print("##########################")
print(f"O fatorial de {entrada} é {fatorial}")
print("##########################")