# Faça um Programa que leia três números e mostre o maior deles.
from typing import Match

print("Digite três númeos, um de cada vez")

nmr1 = float(input())
nmr2 = float(input())
nmr3 = float(input())

maior = max(nmr1, nmr2, nmr3)

print(maior)
