def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for _ in range(10)]
    for tipo_navio, posicoes in frota.items():
        for posicao in posicoes:
            for coord in posicao:
                linha, coluna = coord[0], coord[1]
                tabuleiro[linha][coluna] = 1
                
    return tabuleiro