from room import Room
from player import Player
from item import Item

# Declare all the rooms

torch = Item("Torch", "This torch lights your way.")
dagger = Item("Dagger", "Sharp, pointy knife, useful for protection.")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Torch", "This torch lights your way."), Item("Dagger", "Sharp, pointy knife, useful for protection.")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

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

player = Player("JoeBob", room["outside"])

print("Welcome to Adventure Quest!")

gameOver = False

while not gameOver:

  print("\n")
  print (f"Current room: {player.currentRoom.name}")
  print (f"Current room: {player.currentRoom.description}")


  # *** Print out the items in the room

  itemStr = "The room contains the following items: "

  if len(player.currentRoom.items) > 0:
    for item in player.currentRoom.items:
      # *** On the last item in the array, output special formatting
      if item == player.currentRoom.items[-1]:
        itemStr = itemStr + item.name
      else:
        itemStr = itemStr + item.name + ", "

    print(itemStr)


  # *** Get and make the player's move

  inputStr = input("Please indicate which direction you'd like to move, either n, e, s, or w, q to quit: ")
  split = inputStr.split()
  if len(split) == 2

  if move == "q":
    gameOver = True

  elif move == "n":
    if player.currentRoom.n_to == None:
      print("No room to the North")
    else:
      player.currentRoom = player.currentRoom.n_to

  elif move == "e":
    if player.currentRoom.e_to == None:
      print("No room to the East")
    else:
      player.currentRoom = player.currentRoom.e_to

  elif move == "s":
    if player.currentRoom.s_to == None:
      print("No room to the South")
    else:
      player.currentRoom = player.currentRoom.s_to

  elif move == "w":
    if player.currentRoom.w_to == None:
      print("No room to the West")
    else:
      player.currentRoom = player.currentRoom.w_to

  else:
    print("Malformed input")