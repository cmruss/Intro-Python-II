# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, list=None):
        self.name = name
        self.description = description
        self.list = [] if list is None else list
    def add_item(self, item):
        self.list.append(item)
        print(f"{item.name} dropped on the floor.")
    def __str__(self):
        return f"walks to the {self.name}.\n{self.description}"