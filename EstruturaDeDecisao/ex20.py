# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input("Digite o valor da primeira nota :"))
nota2 = float(input("Digite o valor da segunda nota :"))
nota3 = float(input("Digite o valor da terceira nota :"))

media = float((nota1 + nota2 + nota3) / 3)

if media >= 0 and media <= 10:
    if media == 10:
        print("Aprovado com distinção, sua média final foi" , media)
    elif media >= 7:
        print("Aprovado, sua média final foi" , media)
    else:
        print("Reprovado, sua média final foi" , media)
else:
    print("Os valores inseridos não correspondem com os esperados, por favor, digite valores entre 0 e 10")