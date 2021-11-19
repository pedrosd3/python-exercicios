# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print('Para formar uma data válida, digite primeiro dia, depois mês e posteriormente ano')
dia = int(input())
mes = int(input())
ano = int(input())

if dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and ano > 0:
    print('Data válida :', dia , '/' , mes , '/' , ano)
else:
    print('Data inválida')