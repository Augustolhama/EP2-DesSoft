def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna]==0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'

    return tabuleiro