# display inventory

player_inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inventory):
    print("Inventory:")
    total = 0
    for item, number in inventory.items():
        print(str(number) + ' ' + item)
        total += number
    print('Total number of items: {}'.format(str(total)))

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item not in inventory:
            inventory.setdefault(item, 1)
        else:
            inventory[item] += 1

    return inventory

new_player_inventory = add_to_inventory(player_inventory, dragon_loot)

display_inventory(new_player_inventory)