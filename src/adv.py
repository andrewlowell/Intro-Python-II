from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

  print (f"Current room: {player.currentRoom.name}")
  print (f"Current room: {player.currentRoom.description}")
  move = input("Please indicate which direction you'd like to move, either n, e, s, or w, q to quit: ")

  if move == "q":
    gameOver = True

  elif move == "n":
    if not hasattr(player.currentRoom, "n_to"):
      print("No room to the North")
    else:
      player.currentRoom = player.currentRoom.n_to

  elif move == "e":
    if not hasattr(player.currentRoom, "e_to"):
      print("No room to the East")
    else:
      player.currentRoom = player.currentRoom.e_to

  elif move == "s":
    if not hasattr(player.currentRoom, "s_to"):
      print("No room to the South")
    else:
      player.currentRoom = player.currentRoom.s_to

  elif move == "w":
    if not hasattr(player.currentRoom, "w_to"):
      print("No room to the West")
    else:
      player.currentRoom = player.currentRoom.w_to

  else:
    print("Malformed input")