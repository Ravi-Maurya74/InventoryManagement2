from django.test import TestCase
from inventory.models import Inventory
from inventory.repostories.inventory_repository import InventoryRepository
from inventory.services.inventory_service import InventoryService
from unittest.mock import MagicMock


class TestInventoryService(TestCase):
    def setUp(self) -> None:
        self.mock_repository = MagicMock(spec=InventoryRepository)
        self.service = InventoryService(repository=self.mock_repository)
        self.mock_inventory = Inventory.objects.create(
            primary_location='Location A',
            vin='1234',
            make='Tata',
            model='Punch',
            year=2022,
            cost=15000.00,
            selling_price=20000.00
        )
        self.mock_repository.get_inventory_by_sku.return_value = self.mock_inventory

    def testGetInventoryBySku(self):
        inventory = self.service.get_inventory_by_sku(self.mock_inventory.sku)

        self.assertEqual(inventory, self.mock_inventory)
        self.mock_repository.get_inventory_by_sku.assert_called_once_with(inventory_sku=self.mock_inventory.sku)

    def testCreateAnInventory(self):
        data = {
            'primary_status': 'CREATED',
            'primary_location': 'Warehouse B',
            'vin': '98765432109876543',
            'make': 'Honda',
            'model': 'Accord',
            'year': 2023,
            'cost': 17000.00,
            'selling_price': 22000.00
        }
        self.mock_repository.create_an_inventory.return_value = self.mock_inventory

        inventory = self.service.create_an_inventory(data)

        self.assertEqual(inventory, self.mock_inventory)
        self.mock_repository.create_an_inventory.assert_called_once_with(data=data)
