# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

valor01 = int(input("Digite um número inteiro :"))
valor02 = int(input("Digite um outro número inteiro :"))
valor03 = int(input("Digite um número real :"))

produto = (valor01 * 2) * (valor02 / 2)
soma = (valor01 * 3)  + valor03
elevado = valor03 ** 3

print("O produto do dobro do primeiro com metade do segundo é" , produto)
print("A soma do triplo do primeiro com o terceiro é" , soma)
print("o terceiro elevado ao cubo" , elevado)