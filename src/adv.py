from room import Room
from player import Player
from item import Item

# Declare the items

item = {
    'key': Item("Key", "An old weathered silver key "),

    'lamp': Item("Lamp", "Casts a flickering glow around you")

}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",  "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item['key'],]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'], '')

while player.name == '':
    player.name = str(input("What is your name traveller?\n"))

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print(player)
direction = str(input("Which direction do you choose..?\n[n] North, [e] East, [s] South, [w] West, [i] Inventory, [q] Quit\n"))

while not direction == 'q':
    if direction == 'n':
        if hasattr(player.location, 'n_to'):
            player.location = player.location.n_to
            print(player)
            if player.location.list != []:
                print(f"You see something on the ground in the dim light, it's a {player.location.list[0].name}")
                action, item = input(f"What do you do?\n[take {player.location.list[0].name}], [leave it]\n").split(' ')
                if action == 'take' and item == player.location.list[0].name:
                    player.add_item(player.location.list[0])
                    player.location.list.pop(0)
        else:
            print("The path seems to end here, time to look for another way..")

    if direction == 'e':
        if hasattr(player.location, 'e_to'):
            player.location = player.location.e_to
            print(player)
            if player.location.list != []:
                print(f"You see something on the ground in the dim light, it's a {player.location.list[0].name}")
                action, item = input(f"What do you do?\n[take {player.location.list[0].name}], [leave it]\n").split(' ')
                if action == 'take' and item == player.location.list[0].name:
                    player.add_item(player.location.list[0])
                    player.location.list.pop(0)
        else:
            print("To the east the dropoff is steep and makes you dizzy, you step back from the ledge..")

    if direction == 's':
        if hasattr(player.location, 's_to'):
            player.location = player.location.s_to
            print(player)
            if player.location.list != []:
                print(f"You see something on the ground in the dim light, it's a {player.location.list[0].name}")
                action, item = input(f"What do you do?\n[take {player.location.list[0].name}], [leave it]\n").split(' ')
                if action == 'take' and item == player.location.list[0].name:
                    player.add_item(player.location.list[0])
                    player.location.list.pop(0)

        else:
            print("The way is barred, perhaps another direction?")

    if direction == 'w':
        if hasattr(player.location, 'w_to'):
            player.location = player.location.w_to
            print(player)
            if player.location.list != []:
                print(f"You see something on the ground in the dim light, it's a {player.location.list[0].name}")
                action, item = input(f"What do you do?\n[take {player.location.list[0].name}], [leave it]\n").split(' ')
                if action == 'take' and item == player.location.list[0].name:
                    player.add_item(player.location.list[0])
                    player.location.list.pop(0)
        else:
            print("There's a feeling you get as you look to the west, and your spirit calls for leaving..")


    if len(player.list) > 0 and (direction == 'i' or direction == 'inventory'):
        print(f"Inventory:\n{player.list}")
        action, item = input(f"[drop <Item>], [do nothing]\n").split(' ')
        if action == 'drop' and [i for i in player.list if i.name == item]:
            item = next(i for i in player.list if i.name == item)
            player.location.add_item(item)
            player.drop_item(item)
    elif direction == 'i' or direction == 'inventory':
        print(f"Nothing in inventory!")

    

    
    direction = str(input("Which direction do you choose..?\n[n] North, [e] East, [s] South, [w] West, [i] Inventory, [q] Quit\n"))

