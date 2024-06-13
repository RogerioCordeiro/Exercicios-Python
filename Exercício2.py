# Um município deseja saber a porcentagem de votos de três candidatos, além da porcentagem de votos brancos e nulos. 
# Monte um programa que receba como entrada o número de votos de cada um dos três candidatos e tambem os votos nulos e brancos. 
# Ao final, o programa deve apresentar o total de votos e a porcentagem, em relação a todos
# os eleitores que votaram, de votos de cada candidato, votos nulos e votos em branco.

print("-" * 50)
print("CALCULADORA DE VOTOS!".center(50))
print("-" * 50)

def validar_voto(text_input):
    while True:
        frase = str('Digite o total de votos do ' + text_input)
        try:
            entrada = input(frase)
            return int(entrada)
            break
        except ValueError:
            print('Entrada inválida, digite um número inteiro.')

candidato1 = validar_voto('CANDIDATO 1: ')
candidato2 = validar_voto('CANDIDATO 2: ')
candidato3 = validar_voto('CANDIDATO 3: ')
brancos = validar_voto('BRANCOS: ')
nulos = validar_voto('NULOS: ')

total_votos = sum([candidato1, candidato2, candidato3, brancos, nulos])

print("-" * 50)
print("O TOTAL de votos desta eleição foi de ", total_votos)
print('O total de votos do CANDIDATO 1 foi de ', candidato1, ' = ', candidato1/total_votos*100, '%')
print("Obrigado por usar a calculadora de fotos!")
print("CALCULADORA DE VOTOS!".center(50))
print("-" * 50)