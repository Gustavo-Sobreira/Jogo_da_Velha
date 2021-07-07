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
            linha.append('🟪')
        campo.append(linha)

def exibir_tabuleiro():
    criar_tabuleiro()
    #Enumera as colunas
    num = 0
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
                            '[ 1 ] - 🔳\n'
                            '[ 2 ] - 🔘\n'
                            'Digite o número referente ao símbolo:  '))
        if escolha == 1 or escolha == 2:
            erro -= 1
    return escolha

def fazer_jogada(rodada):
    #Já que se player escolhe 'X' obrigatoriamente bot escolhe 'O' temos:
    if escolha == 1:
        simbolo_player = '🔳'
        simbolo_bot = '🔘'
    else:
        simbolo_player = '🔘'
        simbolo_bot = '🔳'

    #Para que o jogo nunca comece com o mesmo player, coloco um randint para deixar aleatório
    ordem_jogada = 0
    if rodada == 0:
        ordem_jogada = randint(1, 2)
        rodada += 1
    while rodada != 10:

        #Assim caso o número que seja sorteado seja 2 o player joga
        if ordem_jogada % 2 == 0:
            erro = 1
            ordem_jogada -= 1

            #Evitando de usar 'Break' já que é uma função exclusiva Python busco essa solução com a função 'erro'
            #Só haverá mudanças em erro caso o jogador acerte a jogada
            while erro != 0:
                linha = int(input('Selecione uma coordenada utilizando apenas os números\n'
                                      'Linha:  '))
                coluna = int(input('Coluna: '))
                if linha in (0, 1, 2) and coluna in (0, 1, 2):
                    if campo[linha][coluna] == '🟪':
                        campo[linha][coluna] = simbolo_player
                        erro -= 1
                        exibir_tabuleiro()
                        rodada += 1
                else:
                    print(' =- =- =- =- =- Busque casas vazias -= -= -= -= -= ')
        else:
            erro = 1
            ordem_jogada += 1
            while erro != 0:
                linha = randint(0, 2)
                coluna = randint(0, 2)
                if campo[linha][coluna] == '🟪':
                    campo[linha][coluna] = simbolo_bot
                    erro -= 1
                    exibir_tabuleiro()
                    rodada += 1

def ganhar():
    print('')


campo = []
exibir_tabuleiro()
escolha = selecionar_player()
fazer_jogada(0)
