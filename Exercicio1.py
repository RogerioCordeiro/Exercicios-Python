# Escreva	um	programa	para	que	sejam	informados	10	(dez)	números	inteiros.	O	programa	
# deve	informar	o	menor	e	o	maior	valor	informado.
import re
import sys

print("#"*25)
print("Digite 999 para sair!")
max = 0
min = 0
list = []
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
        print('entrei aqui')
        break
    
    list.append(int(num))
    validar = True

print('Os numeros digitados foram: ', list)