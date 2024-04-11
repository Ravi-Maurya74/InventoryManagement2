from django.test import TestCase
from inventory.models import Inventory
from inventory.repostories.inventory_repository import InventoryRepository

class TestInventoryRepository(TestCase):
    def setUp(self) -> None:
        self.repository = InventoryRepository()

    def testCreateInventory(self):
        data = {
            "primary_location": "TestLocation",
            "vin": "VIN",
            "year": 2022,
            "cost": 150000.05,
            "selling_price": 100000.00,
        }
        created_inventory = self.repository.create_an_inventory(data=data)
        retrieved_inventory = Inventory.objects.get(pk=created_inventory.sku)
        self.assertEqual(created_inventory,retrieved_inventory)

    def testGetInventory(self):
        data = {
            "primary_location": "TestLocation",
            "vin": "VIN",
            "year": 2022,
            "cost": 150000.05,
            "selling_price": 100000.00,
        }
        created_inventory = self.repository.create_an_inventory(data=data)
        retrieved_inventory = self.repository.get_inventory_by_sku(inventory_sku=created_inventory.sku)
        self.assertEqual(created_inventory,retrieved_inventory)