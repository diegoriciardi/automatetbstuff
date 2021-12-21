allGuests = {'Alice': {'apples': 5, 'pretzels': 12},   
             'Bob': {'ham sandwiches': 3, 'apples': 2},
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

print(f"Number of things being brought: ")
print(' - Apples         = ' + str(totalBrought(allGuests, 'apples')['numBrought']))
print(' - Cups           = ' + str(totalBrought(allGuests, 'cups')['numBrought']))
print(' - Cake           = ' + str(totalBrought(allGuests, 'cakes')['numBrought']))
print(' - Ham Sandwiches = ' + str(totalBrought(allGuests, 'ham sandwiches')['numBrought']))
print(' - Apple Pies     = ' + str(totalBrought(allGuests, 'apple pies')['numBrought']))
print(' - Pretzels       = ' + str(totalBrought(allGuests, 'pretzels')['numBrought']))
print(' ----------------------')
print('   (TOTAL)        = ' + str(totalBrought(allGuests, 'apple pies')['total']))
