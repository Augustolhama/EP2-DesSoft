def afundados(frota, tabuleiro):
    afundados = 0
    for navio in frota.values():
        for posicoes in navio:
            afundou_navio = True
            for posicao in posicoes:
                linha, coluna = posicao
                if tabuleiro[linha][coluna] != 'X':
                    afundou_navio = False
                    break
            if afundou_navio:
                afundados += 1
    return afundados
