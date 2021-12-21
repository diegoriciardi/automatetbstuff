import os

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

stuff = {'gold coin': 42, 'rope': 1}

#dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'nikita', 'dagger' ]

def displayInventory(inventory):
    #os.system('clear')
    item_total = 0
    total = 0
    print("Inventory: ")
    for k, v in inventory.items():
        total = total + v
        item_total = item_total + v
        print(v, k)
    print(f"Total number of items: {total}")

displayInventory(stuff)

print(dragon_loot)

def add_to_inventory(inventory, added_items):
    for i in added_items:
        inventory.setdefault(i, 0)
        inventory[i] = inventory[i] + 1
    displayInventory(inventory)

add_to_inventory(stuff, dragon_loot)
