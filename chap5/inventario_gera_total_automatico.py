allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Catharina': {'sausage sandwiches': 5, 'apples': 12},
             'Carol': {'cups': 3, 'apple pies': 1}}



def totalBrought(guests, item):
    resposta = {
            'numBrought': 0,
            'total': 0
            }
    for k, v in guests.items():
        resposta['numBrought'] = resposta['numBrought'] + v.get(item, 0)
        for x, y in v.items():
            resposta['total'] = resposta['total'] + y
    return resposta

def print_total(guests):
    lista_itens = {}
    separador = "--------------------------------"
    for k, v in guests.items():
        for it in list(v.keys()):
            lista_itens.setdefault(it, it)
    lista_itens = list(lista_itens.keys())
    print(f"\nNumber of things being brought: ")
    for produto in lista_itens:
        print(f"{produto} =  ".capitalize() + str(totalBrought(allGuests, produto)['numBrought']))
    print(separador)
    print(f"TOTAL =  " + str(totalBrought(allGuests, produto)['total']))

print_total(allGuests)
print()
