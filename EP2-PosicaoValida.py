
def define_posicoes(linha,coluna,orientacao,tamanho):
    lista=[]
    i=0

    if tamanho==1:
        return [[linha,coluna]]
    
    if orientacao == 'vertical':
        while i<tamanho:
            lista.append([linha+i,coluna])
            
            i=i+1
        
    
    if orientacao == 'horizontal':
        while i<tamanho:
            lista.append([linha,coluna+i])
            
            i=i+1

    return lista   


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if orientacao == 'vertical' and 10 - linha< tamanho:
        return False
    if orientacao == 'horizontal' and 10 - coluna < tamanho:
        return False

    for posicao in novas_posicoes:
        linha = posicao[0]
        coluna = posicao[1]

        for tipo, novas_posicoes in frota.items():
            for posicao in novas_posicoes:
                for linha_frota ,coluna_frota in posicao:
                    if linha == linha_frota and coluna == coluna_frota:
                        return False

    return True


