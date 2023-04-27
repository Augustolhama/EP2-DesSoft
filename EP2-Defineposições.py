#Função que define a posição dos navios
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