# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, currentRoom, items = []):
    self.name = name
    self.currentRoom = currentRoom
    self.items = items

  def get_item(self, inputName):
    item = self.currentRoom.drop_item(inputName)
    if item:
      self.items.append(item)
      print(f"You picked up a {item.name}.\n")

  def drop_item(self, inputName):
    item = None
    for n, i in enumerate(self.items):
      if i.name == inputName:
        item = i
        self.items.pop(n)
        print(f"You dropped the {item.name}.\n")
        self.currentRoom.get_item(item)
    if not item:
      print("Can't drop an item you don't have :(")