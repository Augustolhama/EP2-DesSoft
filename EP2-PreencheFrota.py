#Função que define a posição dos navios
def define_posicoes(linha, coluna, orientacao, tamanho):
  lista=[]
  i=0

  if tamanho==1:
      return [[linha, coluna]]
  
  if orientacao == 'vertical':
    while i < tamanho:
        lista.append([linha+i, coluna])
        i += 1
      
  
  if orientacao == 'horizontal':
    while i < tamanho:
      lista.append([linha, coluna+i])
      i += 1

  return lista 

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
  x=[]
  x.append(define_posicoes(linha,coluna,orientacao,tamanho))
  
  if nome_navio not in frota:
    frota[nome_navio]= x
  else:
    tudo=frota[nome_navio]+x
    frota[nome_navio] = tudo

  return frota