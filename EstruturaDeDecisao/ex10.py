# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("Em que turno você estuda? Digite M-matutino, V-Vespertino ou N- Noturno")
turno = input()

if turno == 'm' or turno == 'M':
    print('Bom dia!')
elif turno == 'v' or turno == 'V':
    print('Boa tarde!')
elif turno == 'n' or turno == 'N':
    print('Boa noite!')
else:
    print('Valor inválido!')