#Sobreira Gustavo

#Passos:
#1- Entarda
#2- Escolher símbolo
#3- Tirar na sorte o primeiro jogador
#4- Adcionar jogada na matriz
#3.1- Jogador 2 joga
#4.1- Adicionar jogada na matriz
#5- Verifica se ultimo a jogar ganhou
#6- Caso jogadas for igual a 9 deu velha
#Extas - Música, som de cada jogada, comemoração do vencedor
from random import randint
def criar_tabuleiro():
    #Cria a matriz para o jogo
    for l in range(3):
        linha = []
        for c in range(3):
            linha.append('🟦')
        campo.append(linha)

def exibir_tabuleiro():
    criar_tabuleiro()
    #Enumera as colunas
    num = 0
    #Aqui sai a numeração de colunas
    print(' ' * 4, end=' ')
    for i in range(3):
        print(f'{num}', end='  ')
        num += 1
    print()
    #Aqui sai a numeração das linhas
    for l in range(3):
        print(f' {l}  ', end='')
        #Neste 'for c' é que é feito o visual do tabuleiro, aqui ele ganha forma
        for c in range(3):
            print(f'{campo[l][c]} ', end='')
        print()
        #O print a cima serve para que as linhas sejam puladas, recomendo que coloquem uma '#' nele e rodem o código

def selecionar_player():
    erro = 1
    while erro != 0:
        escolha = int(input('Antes de começarmos escolha seu símbolo\n'
                            '[ 1 ] - ❌\n'
                            '[ 2 ] - 🅾️\n'
                            'Digite o número referente ao símbolo:  '))
        if escolha == 1 or escolha == 2:
            erro -= 1
    return escolha

def fazer_jogada():
    jogadas = 0
    player  = 0
    bot     = 0
    if jogadas == 0:
        joga = randint(1, 2)

        if joga == 1:
            #vez do player

    while jogadas != 9:

campo = []











