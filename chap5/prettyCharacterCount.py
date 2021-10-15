import pprint

separador = '=============================================='
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
#message = 'It was a bright cold day in April, and the clocks were striking thirteeeeeeeeeeeeeeeeeeeeeeeen.'
#message = 'ana'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
maximumValue = -999
keyname = 0
for k, v in count.items():
    print(str(k) + ' => ' + str(v))
    if v > maximumValue:
        maximumValue = v
        keyname = k


print(f"key: '{keyname}' with value:{maximumValue}")

for letter in sorted(list(count.keys())):
    print(f"{letter} => {count[letter]}")

print(separador)

pprint.pprint(count)

print(separador)

pprint.pprint(count)

print(separador)

print(pprint.pformat(count))
