# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combustivel = input("Digite 'G' para abastecer com gasolina, e 'A' para abastecer com Álcool: ")

if combustivel == 'G':
    quant = float(input("Digite a quantidade de gasolina que deseja colocar: "))
    valor = quant * 2.5
    
    if quant <= 20:
        valorComDesconto = (quant / 100) * 96
        print("O valor à ser pago com descontos é de" , valorComDesconto)
    else:
        valorComDesconto = (quant / 100) * 94
        print("O valor à ser pago com descontos é de" , valorComDesconto)
elif combustivel == 'A':
    quant = float(input("Digite a quantidade de gasolina que deseja colocar: "))
    valor = quant * 1.9
    
    if quant <= 20:
        valorComDesconto = (quant / 100) * 97
        print("O valor à ser pago com descontos é de" , valorComDesconto)
    else:
        valorComDesconto = (quant / 100) * 95
        print("O valor à ser pago com descontos é de" , valorComDesconto)
else:
    print("O valor digitado não corresponde ao esperado.")