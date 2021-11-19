# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

carne = input(
    "Digite o tipo de carne que você deseja: 'file', 'alcatra' ou 'picanha' :")

if carne == 'file':
    qtd = float(input("Digite a quantidade de File Duplo em Kgs que você deseja :"))
    if qtd <= 5:
        preco = qtd * 4.9
    else:
        preco = qtd * 5.8
elif carne == 'alcatra':
    qtd = float(input("Digite a quantidade de Alacatra em Kgs que você deseja :"))
    if qtd <= 5:
        preco = qtd * 5.9
    else:
        preco = qtd * 6.8
elif carne == 'picanha':
    qtd = float(input("Digite a quantidade de Picanha em Kgs que você deseja :"))
    if qtd <= 5:
        preco = qtd * 6.9
    else:
        preco = qtd * 7.8
else:
    print("Tipo de carne não encontrado.")

pagamento = input("""
Qual método de pagamento será utilizado:
'guanabara' para Cartão Guanabara,
'credito' para Cartão de Crédito,
'debito' para Cartão de Débito,
'dinheiro' para Dinheiro
Aqui -> """)

if pagamento == 'guanabara':
    precoFinal = (preco / 100) * 95
    
elif pagamento == 'credito' or  pagamento == 'debito' or pagamento == 'dinheiro':
    precoFinal = preco
    
else:
    print("Método de pagamento inválido.")
    
print("Você comprou" , qtd , "Kgs de" , carne , 
      "\nE pagando com" , pagamento , "o valor final será de R$" , precoFinal)
