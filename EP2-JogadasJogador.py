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

#função que preenche o dicionário
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
  x=[]
  x.append(define_posicoes(linha,coluna,orientacao,tamanho))
  
  if nome_navio not in frota:
    frota[nome_navio]= x
  else:
    tudo=frota[nome_navio]+x
    frota[nome_navio] = tudo

  return frota

#registra as jogadas
def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna]==0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'

    return tabuleiro

#Cria tabuleiro
def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for _ in range(10)]
    for tipo_navio, posicoes in frota.items():
        for posicao in posicoes:
            for coord in posicao:
                linha, coluna = coord[0], coord[1]
                tabuleiro[linha][coluna] = 1
                
    return tabuleiro

#Embarcações afundadas
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

#Posição é valida ou não
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

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto


posicionando=True
contador=0
frota = {}

while posicionando:
    orientacao=''
    if contador >= 6:
        nome_navio='submarino'
        tamanho=1
    elif contador >= 3:
        nome_navio='contratorpedeiro'
        tamanho=2
    elif contador >= 1:
        nome_navio='navio-tanque'
        tamanho=3
    elif contador == 0:
        nome_navio='porta-aviões'
        tamanho=4
    
    print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(nome_navio,tamanho))
    linha=int(input('Linha:'))
    coluna=int(input('Coluna:'))
    if tamanho >1:
        num=input('[1] Vertical [2] Horizontal >')
        if int(num) == 1:
            orientacao = 'vertical'
        elif int(num) == 2:
            orientacao = 'horizontal'
    else:
        orientacao=''

    if posicao_valida(frota,linha,coluna,orientacao,tamanho):
        preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho)
        contador+=1
        if contador ==10:
            posicionando=False       
    else:
        print('Esta posição não está válida!')

frota_oponente = {'porta-aviões': [[[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]]}

tabuleiro_op=posiciona_frota(frota_oponente)
tabuleiro=posiciona_frota(frota)
jogando=True
jogadas_anteriores=[]

while jogando:
    jogada=[]
    linha=-1
    coluna=-1
    print(monta_tabuleiros(tabuleiro,tabuleiro_op))
    
    while linha <0 or linha >9: 
        linha=int(input('Qual linha deseja atcar?'))

        if linha <0 or linha >9: 
            print('Linha inválida!')
    
    while coluna <0 or coluna >9: 
        coluna=int(input('Qual coluna deseja atcar?'))
        
        if coluna <0 or coluna >9: 
            print('coluna inválida!')

    
    jogada.append([linha,coluna])

    if jogada in jogadas_anteriores:
        print('A posição linha LINHA e coluna COLUNA já foi informada anteriormente')
    else:
        jogadas_anteriores.append(jogada)
        tabuleiro_op=faz_jogada(tabuleiro_op,linha,coluna)
        if afundados(frota_oponente,tabuleiro_op) == 10:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            jogando=False