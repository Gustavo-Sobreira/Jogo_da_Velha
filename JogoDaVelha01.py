#Sobreira Gustavo
#Falta u, placar e repetições
from random import randint

def criar_tabuleiro():
    #Cria a matriz para o jogo
    for l in range(3):
        linha = []
        for c in range(3):
            linha.append('🟫')
        campo.append(linha)

def enumerar_colunas():
    print('                   COLUNA')
    num = 0
    print('    ' * 4, end='  ')
    for i in range(3):
        print(f'{num}', end='  ')
        num += 1
    print()

def enumerar_linha():
    linha = 'INHA'
    print('          L')
    for l in range(3):
        print(f'          {linha[l]}  {l}  ', end=' ')

        # Neste 'for c' é que é feito o visual do tabuleiro, aqui ele ganha forma
        for c in range(3):
            print(f'{campo[l][c]} ', end='')
        print()
    print('          A')
    # O print a cima serve para que as linhas sejam puladas, recomendo que coloquem uma '#' nele e rodem o código

def exibir_tabuleiro():
    criar_tabuleiro()
    alinhar()
    enumerar_colunas()
    enumerar_linha()
    alinhar()

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

def verificar_ganhador():
    ganhador = 0
    for c in range(0, 3):
        if (campo[0][c] == '🔳' and campo[1][c] == '🔳' and campo[2][c] == '🔳') \
                or (campo[0][0] == '🔳' and campo[1][1] == '🔳' and campo[2][2] == '🔳')\
                or campo[0][2] == '🔳' and campo[1][1] == '🔳' and campo[2][0] == '🔳':
            ganhador += 1
        else:
            if (campo[0][c] == '🔘' and campo[1][c] == '🔘' and campo[2][c] == '🔘') \
                    or (campo[0][0] == '🔘' and campo[1][1] == '🔘' and campo[2][2] == '🔘') \
                    or campo[0][2] == '🔘' and campo[1][1] == '🔘' and campo[2][0] == '🔘':
                ganhador += 2
    return ganhador

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
        if verificar_ganhador() != 0:
            if verificar_ganhador() == 1:
                print('O jogador 🔳 VENCEU')
            else:
                print('O jogador 🔘 VENCEU')
            break

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
                    if campo[linha][coluna] == '🟫':
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
                if campo[linha][coluna] == '🟫':
                    campo[linha][coluna] = simbolo_bot
                    erro -= 1
                    exibir_tabuleiro()
                    rodada += 1
        if rodada == 10:
            print('Deu Velha')

def alinhar():
    print('\n')
    print('='*40)
    print('\n')

campo = []
exibir_tabuleiro()
escolha = selecionar_player()
verificar_ganhador()
fazer_jogada(0)
