# Um caixa precisa de um programa que o auxilie no fornecimento de valores com o mínimo
# de cédulas/moedas possíveis. Monte um programa que seja fornecido o valor (inteiro) a
# ser fornecido e tenha como saída o total de cédulas utilizadas, nos valores de 100, 50, 20,
# 10, 5, 2 e 1.

from FuncoesBasicas import printAbertura as Abertura

# Função que valida a entrada do usuário e converte em inteiro.
def EnumInterio(entrada):
    while True:
        valor = input(entrada)
        
        try:
            valor = int(valor)
            
            if (valor == 999):
                print("\033[1;30;41mEntrada 999 detectada, saindo...\033[m")
                exit()
            
            if (valor <= 0):
                print("\033[1;31mEntrada inválida\033[m, favor digite um número inteiro \033[1;32mpositivo!\033[m ")
            else:
                return valor
        
        except ValueError:
            print("\033[1;31mEntrada inválida\033[m, favor digite um número inteiro: ")


# Inicio do programa
Abertura("contador de notas")
print('Para sair digite 999')

cedulas = [100, 50, 20, 10, 5, 2, 1]

num = EnumInterio("Digite um valor inteiro para calcular a quantidade de notas: ")

