# 5) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever
# o valor correspondente em graus Celsius.

from FuncoesBasicas import printAbertura as abertura
from time import sleep

# Valida a entrada 
def validarInput(mensagem):
    while True:
        try:
            numero = input(mensagem)
            if (numero.upper() == "SAIR"):
                print("\033[0;37;41mDetectado solicitação de saída. Saindo...\033[m")
                sleep(2)
                exit()
            valor = float(numero)
            return valor
        except ValueError:
            print(f'\033[1;31m{numero} não é um valor valido!\033[1;36m\nDigite um valor ponto flutuante. Exemplo: 1.78\033[m')
            sleep(1)

# Calculo de conversão da temperatura
def converteTemperatura(escolha):
    if (escolha == 1):
        try:
            temperatura = validarInput("\033[1;32mDigite a temperatura em Fahrenheit:\033[m ")
            celsius = 5/9 * (temperatura - 32)
            print(f'{temperatura}ºF corresponde a {celsius:.1f}ºC')
            sleep(2)
        except ValueError:
            print("Erro ao realizar a conversão dos valores!")
    elif (escolha == 2):
        temperatura = validarInput('\033[1;34mDigite a temperatura em Celsius:\033[m')
        fahrenheit = 9/5 * temperatura + 32
        print(f'{temperatura}ºC corresponde a {fahrenheit:.1f}ºF') 
        sleep(2)



# Função menu
def printMenu():
    print("*"*50)
    print("\033[0;33mEscolha uma opção abaixo:\033[m".center(50))
    print(" 1 - \033[1;32mFahrenheit para Celsius\033[m".center(50))
    print(" 2 - \033[1;34mCelsius para Fahrenheit\033[m".center(50))
    print(" SAIR - \033[1;31mPara sair do programa.\033[m".center(50))
    print("*"*50)
    
# Inicio do progrma
while True:
    abertura("Conversor de tipos de temperaturas")
    printMenu()
    escolha = validarInput("Digite aqui sua escolha: ")
    converteTemperatura(escolha)
