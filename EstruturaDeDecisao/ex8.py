# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

print("Qual o preço do suco")
suco = float(input())

print("Qual o preço do maçã")
maca = float(input())

print("Qual o preço do chocolate")
chocolate = float(input())

produto = min(suco, maca, chocolate)

if produto == suco and produto == maca and produto == chocolate:
    print("Os três produtos possuem o mesmo preço")
    
elif produto == suco and produto == maca:
    print("Suco e Maçã são os produtos mais baratos")
    
elif produto == suco and produto == chocolate:
    print("Suco e Chocolate são os produtos mais baratos")
    
elif produto == maca and produto == chocolate:
    print("Maçã e Chocolate são os produtos mais baratos")
    
elif produto == suco:
    print("O suco é produto mais barato")
    
elif produto == maca:
    print("A maçã é produto mais barato")
    
elif produto == chocolate:
    print("O chocolate é produto mais barato")
