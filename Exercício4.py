# Um caixa precisa de um programa que o auxilie no fornecimento de valores com o mínimo
# de cédulas/moedas possíveis. Monte um programa que seja fornecido o valor (inteiro) a
# ser fornecido e tenha como saída o total de cédulas utilizadas, nos valores de 100, 50, 20,
# 10, 5, 2 e 1.

from FuncoesBasicas import printAbertura as Abertura
import time

# Função que valida a entrada do usuário e converte em inteiro.
def EnumInterio(entrada):
    while True:
        print('\033[1;33mPara sair digite "SAIR"\033[m')
        valor = input(entrada)
        
        try:
            if (valor.lower() == 'sair'):
                print("\033[1;30;41mSolicitação de sainda dectada, saindo...\033[m")
                time.sleep(2)
                Abertura("obrigado, até mais!")
                exit()
                
            valor = int(valor)
            
            if (valor <= 0):
                print("\033[1;31mEntrada inválida\033[m, favor digite um número inteiro \033[1;32mpositivo!\033[m \n")
                time.sleep(2)
            else:
                return valor
        
        except ValueError:
            print("\033[1;31mEntrada inválida\033[m, favor digite um número inteiro: \n")
            time.sleep(2)

# Inicio do programa
Abertura("contador de notas")

cedulas = [100, 50, 20, 10, 5, 2, 1]

while True:
    num = EnumInterio("Digite um valor inteiro para calcular a quantidade de notas: ")
   
    for cedula in cedulas:
        quantidade = int(num / cedula)
        
        if (quantidade > 0 ):
            print(f'{quantidade} cedúla(s) de R$ {cedula}!')
        
        num %= cedula
    
    print()
    
