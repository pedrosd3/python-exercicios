# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

valor1 = float(input("Digite um número, inteiro ou decimal :"))
valor2 = float(input("Digite outro número, inteiro ou decimal :"))

operacao = input(
"""Qual operação deseja fazer? 
'soma' para soma 
'sub' para subtração 
'div' para divisão 
'mult' para multiplicação
AQUI: """)

if operacao == 'soma':
    result = valor1 + valor2
    print(result)
    
    if result >= 0:
        print("O valor é positivo")
    else:
        print("O valor é negativo")
    if result % 1 == 0:
        print("O valor é inteiro")
        if result % 2 == 0:
            print("O valor é par")
        else:
            print("O valor é ímpar")
    else:
        print("O valor é decimal")
        print("Valores decimais não são considerados pares ou ímpares")
        
elif operacao == 'sub':
    result = valor1 - valor2
    print(result)
    
    if result >= 0:
        print("O valor é positivo")
    else:
        print("O valor é negativo")
    if result % 1 == 0:
        print("O valor é inteiro")
        if result % 2 == 0:
            print("O valor é par")
        else:
            print("O valor é ímpar")
    else:
        print("O valor é decimal")
        print("Valores decimais não são considerados pares ou ímpares")
        
elif operacao == 'div':
    result = valor1 / valor2
    print(result)
    
    if result >= 0:
        print("O valor é positivo")
    else:
        print("O valor é negativo")
    if result % 1 == 0:
        print("O valor é inteiro")
        if result % 2 == 0:
            print("O valor é par")
        else:
            print("O valor é ímpar")
    else:
        print("O valor é decimal")
        print("Valores decimais não são considerados pares ou ímpares")
        
elif operacao == 'mult':
    result = valor1 * valor2
    print(result)
    
    if result >= 0:
        print("O valor é positivo")
    else:
        print("O valor é negativo")
    if result % 1 == 0:
        print("O valor é inteiro")
        if result % 2 == 0:
            print("O valor é par")
        else:
            print("O valor é ímpar")
    else:
        print("O valor é decimal")
        print("Valores decimais não são considerados pares ou ímpares")

else:
    print("o valor digitado está inválido")
    