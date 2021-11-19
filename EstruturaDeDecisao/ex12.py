# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
# dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

valorHora = float(input("Digite o quanto recebe por hora :"))
horaTrabalhada = float(input("Digite quantas horas você trabalhou no mês :"))

salarioBruto = valorHora * horaTrabalhada

if salarioBruto <= 900:
    inss = (salarioBruto / 100) * 10
    fgts = (salarioBruto / 100) * 11
    ir = 0
elif salarioBruto > 900 and salarioBruto <= 1500:
    inss = (salarioBruto / 100) * 10
    fgts = (salarioBruto / 100) * 11
    ir = (salarioBruto / 100) * 5
elif salarioBruto > 1500 and salarioBruto <= 2500:
    inss = (salarioBruto / 100) * 10
    fgts = (salarioBruto / 100) * 11
    ir = (salarioBruto / 100) * 10
else:
    inss = (salarioBruto / 100) * 10
    fgts = (salarioBruto / 100) * 11
    ir = (salarioBruto / 100) * 20
    
descontos = ir + inss
salarioLiquido = salarioBruto - descontos
    
print("Salário Bruto: R$" , salarioBruto , 
      "\nImposto de Renda: R$" , ir , 
      "\nINSS: R$" , inss , 
      "\nFGTS: R$" , fgts , 
      "\nTotal de descontos: R$" , descontos , 
      "\nSalário Liquido : R$" , salarioLiquido)