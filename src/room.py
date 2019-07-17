# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, items = [], n_to = None, e_to = None, s_to = None, w_to = None):
    self.name = name
    self.description = description
    self.items = items
    self.n_to = n_to
    self.e_to = e_to
    self.s_to = s_to
    self.w_to = w_to

  def get_item(self, item):
    self.items.append(item)

  # *** Returns the item dropped if it existed, None if it didn't
  def drop_item(self, inputName):
    item = None
    for n, i in enumerate(self.items):
      if i.name == inputName:
        item = i
        self.items.pop(n)
    return item