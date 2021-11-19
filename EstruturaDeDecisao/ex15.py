# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

print("Digite o valor do lado A do triângulo")
ladoA = float(input())

print("Digite o valor do lado B do triângulo")
ladoB = float(input())

print("Digite o valor do lado C do triângulo")
ladoC = float(input())

if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    if ladoA == ladoB and ladoA == ladoC:
        print("É um Triângulo Equilátero")
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print("É um Triângulo Isósceles")
    elif ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
        print("É um Triângulo Escaleno")
else:
    print("Não é possível formar um triângulo")