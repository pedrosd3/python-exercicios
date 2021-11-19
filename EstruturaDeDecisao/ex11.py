# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

print('Digite o salário atual do colaborador :')
salario_atual = float(input())
if salario_atual <= 280:
    aumento = 20
    valor_reajuste = (salario_atual * 0.2)
    salario_reajustado = valor_reajuste + salario_atual
    print('O salário inicial era de :',salario_atual ,
          '\n O percentual de aumento foi de:', aumento, '%', 
          '\n O valor do aumento foi de :',valor_reajuste, 
          '\n O novo salário será de :',salario_reajustado)
elif salario_atual > 280 and salario_atual <= 700:
    aumento = 15
    valor_reajuste = (salario_atual * 0.15)
    salario_reajustado = valor_reajuste + salario_atual
    print('O salário inicial era de :',salario_atual ,
          '\n O percentual de aumento foi de:', aumento, '%', 
          '\n O valor do aumento foi de :',valor_reajuste, 
          '\n O novo salário será de :',salario_reajustado)
elif salario_atual > 700 and salario_atual <= 1500:
    aumento = 10
    valor_reajuste = (salario_atual * 0.1)
    salario_reajustado = valor_reajuste + salario_atual
    print('O salário inicial era de :',salario_atual ,
          '\n O percentual de aumento foi de:', aumento, '%',
          '\n O valor do aumento foi de :',valor_reajuste, 
          '\n O novo salário será de :',salario_reajustado)
elif salario_atual > 1500:
    aumento = 5
    valor_reajuste = (salario_atual * 0.05)
    salario_reajustado = valor_reajuste + salario_atual
    print('O salário inicial era de :',salario_atual ,
          '\n O percentual de aumento foi de:', aumento, '%',
          '\n O valor do aumento foi de :',valor_reajuste, 
          '\n O novo salário será de :',salario_reajustado)