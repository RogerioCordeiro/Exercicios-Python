# Um município deseja saber a porcentagem de votos de três candidatos, além da porcentagem de votos brancos e nulos.
# Monte um programa que receba como entrada o número de votos de cada um dos três candidatos e tambem os votos nulos e brancos.
# Ao final, o programa deve apresentar o total de votos e a porcentagem, em relação a todos
# os eleitores que votaram, de votos de cada candidato, votos nulos e votos em branco.

print("-" * 50)
print("CALCULADORA DE VOTOS!".center(50))
print("-" * 50)

def validar_voto(text_input):
    # Função que valida se um voto foi digitado corretamente verificando se 
    # a entrada foi um numero inteiro positivo.
    while True:
        frase = str('Digite o total de votos do ' + text_input + ' = ')
        try:
            entrada = int(input(frase))
            if entrada > 0:
                return entrada
                # break
            else:
                print('A quantidade de votos precisa ser positiva.')

        except ValueError:
            print('Entrada inválida, digite um número inteiro.')

def str_resultado(nome_candidato, votos, votos_totais):
    # Função que cria e imprime a frase na tela com os valores dos votos individuais e 
    # o percentual referente ao total de votos daquele periodo
    perc_votos = round(votos/votos_totais*100, 2)
    return print(f'O TOTAL de votos para {nome_candidato} foi de {votos} representa {perc_votos}% dos votos totais!\n')

candidatos = ['CANDIDATO 1', 'CANDIDATO 2', 'CANDIDATO 3', 'BRANCOS', 'NULOS']
votos = [validar_voto(candidato) for candidato in candidatos]
total_votos = sum(votos)

# candidato1 = validar_voto('CANDIDATO 1: ')
# candidato2 = validar_voto('CANDIDATO 2: ')
# candidato3 = validar_voto('CANDIDATO 3: ')
# brancos = validar_voto('BRANCOS: ')
# nulos = validar_voto('NULOS: ')

# total_votos = sum([candidato1, candidato2, candidato3, brancos, nulos])

print("-" * 50)
print("O TOTAL de votos desta eleição foi de", total_votos, '\n')

# laço que percore todos os candidatos e envia os dados para a função str_resultado para mostrar na tela
# os valores dos votos de cada um deles.
for candidato, voto in zip(candidatos, votos):
    str_resultado(candidato, voto, total_votos)
    
# str_resultado('CANDIDATO 1', candidato1, total_votos)
# str_resultado('CANDIDATO 2', candidato2, total_votos)
# str_resultado('CANDIDATO 3', candidato3, total_votos)
# str_resultado('BRANCOS', brancos, total_votos)
# str_resultado('NULOS', nulos, total_votos)

print("-" * 50)
print("Obrigado por usar a calculadora de votos!".center(50))
print("-" * 50)