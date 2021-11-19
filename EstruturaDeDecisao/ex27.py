# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
# e escreva o valor a ser pago pelo cliente.

morango = float(
    input("Digite a quantidade de morangos em Kg que deseja comprar: "))
maca = float(input("Digite a quantidade de maçãs em Kg que deseja comprar: "))

if morango <= 5:
    precoMorango = morango * 2.5
else:
    precoMorango = morango * 2.2

if maca <= 5:
    precoMaca = maca * 1.8
else:
    precoMaca = maca * 1.5

totalPeso = morango + maca
totalPreco = precoMorango + precoMaca

if totalPeso > 8 or totalPreco > 25:
    precoFinal = ((precoMorango + precoMaca) / 100) * 90
else:
    precoFinal = precoMorango + precoMaca

print("Você comprou", morango, "kgs em morango; \nVocê comprou", maca,
      "kgs em maçã; \nO preço final dos produtos foi de R$", round(precoFinal, 2))
