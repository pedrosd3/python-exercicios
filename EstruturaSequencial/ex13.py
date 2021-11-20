# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = input("Digite 'm' para sexo masculino e 'f' para o feminino :")

altura = float(input("Digite sua altura :"))

if sexo == 'm':
    formula = (72.7 * altura) - 58
    print("Seu peso ideal é" , formula , "Kgs")
elif sexo == 'f':
    formula = (62.1 * altura) - 44.7
    print("Seu peso ideal é" , formula , "Kgs")
else:
    print("Valor Inválido")