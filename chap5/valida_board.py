import ast

def separador(caractere):
    quantidade = 10
    print(caractere * quantidade)

def logador(mensagem):
    separador('+')
    print(mensagem)
    separador('+')

def valida_reis(pecas):
    quantidade_branco = list(pecas.values()).count('wking')
    quantidade_preto = list(pecas.values()).count('bking')
    if quantidade_branco != 1 or quantidade_preto != 1:
        logador('quantidade de reis incorreta')
        return False
    return True

def valida_quantidade_total_pecas(pecas):
    total = 32
    if len(pecas) > total:
        logador('quantidade de pecas maior que 32 (limite)')
        return False
    return True

def valida_quantidade_pecas_cores_peoes_e_nomes(pecas):
    nomes_pecas = [ 'pawn', 'knight', 'bishop', 'rook', 'queen', 'king' ]
    nomes_casas = [ 'a', 'b', 'c', 'd', 'e' ,'f', 'g' ,'h' ]
    contador_branco = 0
    contador_preto = 0
    limite_peoes = 8
    for peca in list(pecas.values()):
        if not peca.startswith('w') and not peca.startswith('b'):
            logador('peca que nao comeca com a cor branca ou preta')
            return False
        if peca.startswith('w'):
            contador_branco = contador_branco + 1
        if peca.startswith('b'):
            contador_preto = contador_preto + 1
        if peca[1:] not in nomes_pecas:
            logador('peca  que nao faz parte da lista de pecas')
            return False
    if contador_branco > 16 or contador_preto > 16:
        logador('quantide de pecas brancas ou pretas maior que 16 (maximo)')
        return False
    if list(pecas.values()).count('wpawn') > limite_peoes or list(pecas.values()).count('bpawn') > limite_peoes:
            logador('quantidade de peoes brancos ou pretos maior que 8 (maximo)')
            return False
    for casa in list(pecas.keys()):
        if casa[1] not in nomes_casas:
            logador('casa invalida informada')
            return False
    return True

def validacao():
    if not valida_reis(entrada) or not valida_quantidade_total_pecas(entrada) or not valida_quantidade_pecas_cores_peoes_e_nomes(entrada):
        return False
    return True

entrada = ast.literal_eval(input("informe por favor o tabuleiro de pecas como dicionario: "))
if validacao() == True:
    print("sucesso")
else:
    print("falha....")