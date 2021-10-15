birthdays = {'Alice':'Apr 1', 'Bob':'Dec 12', 'Carol':'Mar 4'}
separador='======================'

def imprime():
    print(separador)
    for k, v in birthdays.items():
        print(str(k) + ' ' + str(v))
    print(separador)

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
        imprime()

