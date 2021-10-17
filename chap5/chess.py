import pprint

letras = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ]
pecas = [
    'rook',
    'knight',
    'bishop',
    'king',
    'queen',
    'bishop',
    'knight',
    'rook',
    'pawn',
    'pawn',
    'pawn',
    'pawn',
    'pawn',
    'pawn',
    'pawn',
    'pawn'    
]

chess = {}

cor = 'w'
contador = 0
for i in range(1, 9):
	for letra in letras:
		if i <= 2:
			chess[f"{i}{letra}"] = f"{cor}{pecas[contador]}"
			contador = contador + 1
			if contador > 15:
				contador = 15
				cor = "b"
		if i > 6:
			chess[f"{i}{letra}"] = f"{cor}{pecas[contador]}"
			contador = contador - 1
    
pprint.pprint(chess)