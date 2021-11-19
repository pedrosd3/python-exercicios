# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

print("Digite um número qualquer, que seja menor que 1000.")
valor = int(input())

if valor >= 1 and valor <= 999:
    if valor >= 100 and valor <= 999:
        centena = str(valor)
        dezena = str(valor)
        unidade = str(valor)
        
        print("O número", valor, "possui")
        if centena[0] == '1':
            print(centena[0] , "centena")
        else:
            print(centena[0], "centenas")
                
        if dezena[1] == '1':
            print(dezena[1] , "dezena")
        else:
            print(dezena[1], "dezenas")
                
        if unidade[2] == '1':
            print(unidade[2] , "unidade")
        else:
            print(unidade[2], "unidades")
    elif valor >= 10 and valor <= 99:
        dezena = str(valor)
        unidade = str(valor)
        
        print("O número", valor, "possui")
        if dezena[0] == '1':
            print(dezena[0] , "dezena")
        else:
            print(dezena[0], "dezenas")
                
        if unidade[1] == '1':
            print(unidade[1] , "unidade")
        else:
            print(unidade[1], "unidades")
    else:
        unidade = str(valor)
        
        print("O número", valor, "possui")
        if unidade[0] == '1':
            print(unidade[0] , "unidade")
        else:
            print(unidade[0], "unidades")
else:
    print("O valor digitado não pôde ser lido, digite um valor entre 1 e 999")
    

    
