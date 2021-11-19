# Faça um Programa que leia três números e mostre o maior e o menor deles.
print("Digite três númeos, um de cada vez")

nmr1 = int(input())
nmr2 = int(input())
nmr3 = int(input())

maior = str(max(nmr1, nmr2, nmr3))
menor = str(min(nmr1, nmr2, nmr3))

print(maior , "foi o maior número digitado")
print(menor , "foi o menor número digitado")