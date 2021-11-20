# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

salarioHora = float(input("Digite quanto você ganha por hora :"))
horasTrabalhadas = float((input("Digite quantas horas você trabalhou no mês :")))

salarioBruto = salarioHora * horasTrabalhadas

ir = (salarioBruto / 100) * 11
inss = (salarioBruto / 100) * 8
sindicato = (salarioBruto / 100) * 5

salarioLiquido = salarioBruto - (ir + inss + sindicato)

print("O salário líquido será de" , salarioLiquido)