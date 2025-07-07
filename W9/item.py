# item.py

class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def restock(self, amount):
        self.quantity += amount

    def consume(self, amount):
        if amount > self.quantity:
            raise ValueError("Stok tidak cukup.")
        self.quantity -= amount


class InventoryManager:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_item_names(self):
        return [item.name for item in self.items]

    def find_item_by_name(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None
