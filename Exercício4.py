# Um caixa precisa de um programa que o auxilie no fornecimento de valores com o mínimo
# de cédulas/moedas possíveis. Monte um programa que seja fornecido o valor (inteiro) a
# ser fornecido e tenha como saída o total de cédulas utilizadas, nos valores de 100, 50, 20,
# 10, 5, 2 e 1.

from FuncoesBasicas import printAbertura as Abertura

Abertura("contador de notas")

cedulas = [100, 50, 20, 10, 5, 2, 1]

num = input("Digite um valor inteiro para calcular a quantidade de notas: ")
