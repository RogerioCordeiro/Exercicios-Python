# Escreva um programa para que sejam informados 10 (dez) números inteiros. O programa	
# deve informar o menor e o maior valor informado.
import re

print("#"*25)
print("Digite 999 para sair!")
num_max = 0
num_min = 0
list_num = []
validar = True

def validar_numeros(entrada):
    return bool(re.match('[0-9]+$', entrada))

for i in range(10):
    
    while validar:
        num = input("Digite um número inteiro: ")
        if validar_numeros(num):
            validar = False
        else:
            print("Entrada inválida digite novamente!")

    if (int(num) == 999):
        print('Entrada 999 detectada. Saindo... ')
        exit()
    
    list_num.append(int(num))
    validar = True

num_max = max(list_num)
num_min = min(list_num)
num_sum = sum(list_num)

print('Os numeros digitados foram: ', list_num)
print('O maior número digitado foi: ', num_max)
print('O menor número digitado foi: ', num_min)
print('A soma de todos os números digitados é: ', num_sum)