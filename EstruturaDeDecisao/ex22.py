# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

valor = int(input("Digite qualquer valor inteiro :"))

if valor % 2 == 0:
    print(valor , "é um numero par.")
else:
    print(valor , "é um número ímpar")