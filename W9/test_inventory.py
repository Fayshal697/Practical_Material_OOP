# test_inventory.py

import unittest
from item import Item, InventoryManager

class TestInventorySystem(unittest.TestCase):
    def setUp(self):
        self.item1 = Item("Pulpen", 100)
        self.item2 = Item("Buku", 50)
        self.inventory = InventoryManager()
        self.inventory.add_item(self.item1)
        self.inventory.add_item(self.item2)

    def test_restock_item(self):
        self.item1.restock(50)
        self.assertEqual(self.item1.quantity, 150)

    def test_consume_item_success(self):
        self.item2.consume(20)
        self.assertEqual(self.item2.quantity, 30)

    def test_consume_item_insufficient_stock(self):
        with self.assertRaises(ValueError) as context:
            self.item2.consume(100)
        self.assertEqual(str(context.exception), "Stok tidak cukup.")

    def test_get_item_names(self):
        names = self.inventory.get_item_names()
        self.assertIn("Pulpen", names)
        self.assertIn("Buku", names)

    def test_find_item_by_name(self):
        found = self.inventory.find_item_by_name("Pulpen")
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Pulpen")

        not_found = self.inventory.find_item_by_name("Penggaris")
        self.assertIsNone(not_found)


if __name__ == '__main__':
    unittest.main()
