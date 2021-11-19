# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
print("Digite 'M' para masculino e 'F' para feminino")
sexo = input()
if sexo == 'M' or sexo == 'm':
    print("Masculino")
    
elif sexo == 'F' or sexo == 'f':
    print("Feminino")
    
else:
    print("Inválido")