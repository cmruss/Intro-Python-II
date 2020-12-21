# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, name):
        self.location = location
        self.name = name
        self.list = []
    def add_item(self, item):
        self.list.append(item)
        print(f"{item.name} added to inventory!")
    def drop_item(self, item):
        self.list.remove(item)
    def __str__(self):
        return f"{self.name} {self.location}"
