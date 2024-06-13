# Elabore um programa que receba a nota de um aluno e diga se o mesmo foi aprovado ou
# reprovado. O aluno é aprovado com nota maior ou igual a 6,0 (seis).

from FuncoesBasicas import printAbertura as Abertura

# Função de válidação da entrada da Nota
def validarEntrada(textoEntrada):
   while True:
       
        try: 
            num = int(input(textoEntrada))
            
            # if num == 999:
            #     Abertura('Entrada 999 detectada. Saindo...')
            #     exit()
            
            if 0 < num <= 10 :
                return num
            else:
                print('\33[1;31mNota digitada inválida, digite novamente\33[m')
                
        except ValueError:
            print('\33[1;31mNota digitada inválida, digite novamente\33[m')
        
# Inicio do programa
Abertura('CALCULAR MÉDIA ALUNOS')

alunos = {}

while True:
    
    nome = input('Digite o \33[1;32mNOME\033[m do aluno ou 999 para sair : ') 
    if nome == '999':
        print()
        break
        
    nota = validarEntrada('Digite a \33[1;34mNOTA\033[m do aluno ou 999 para sair : ')
    
    if nota == 999:
        # Abertura('Entrada 999 detectada. Saindo...')
        print()
        break
    
    alunos[nome] = nota

for nome_aluno, nota_aluno in alunos.items():
    if nota_aluno >= 6:
        print(f'{nome_aluno} foi \33[1;32mAPROVADO(A)\33[m com nota {nota_aluno}!')
    else:
        print(f'{nome_aluno}, \33[1;31mnão ficou dentro da média\33[m, precisa estudar mais.')

        
Abertura("Obrigado! Até breve!")
    