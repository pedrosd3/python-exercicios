# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

pergunta01 = input("Telefonou para a vítima? :")
pergunta02 = input("Esteve no local do crime? :")
pergunta03 = input("Mora perto da vítima? :")
pergunta04 = input("Devia para a vítima? :")
pergunta05 = input("Já trabalhou com a vítima? :")

if pergunta01 == 'sim':
    resposta01 = 1
else:
    resposta01 = 0
    
if pergunta02 == 'sim':
    resposta02 = 1
else:
    resposta02 = 0
    
if pergunta03 == 'sim':
    resposta03 = 1
else:
    resposta03 = 0
    
if pergunta04 == 'sim':
    resposta04 = 1
else:
    resposta04 = 0
    
if pergunta05 == 'sim':
    resposta05 = 1
else:
    resposta05 = 0
    
total = resposta01 + resposta02 + resposta03 + resposta04 + resposta05

if total == 5:
    print("Assassino")
elif total == 4 or total == 3:
    print("Cúmplice")
elif total == 2:
    print("Suspeito")
else:
    print("Inocente")