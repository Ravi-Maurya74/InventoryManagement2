from inventory.models import Inventory

class InventoryRepository:
    def get_inventory_by_sku(self,inventory_sku):
        return Inventory.objects.get(sku=inventory_sku)
    
    def create_an_inventory(self,data):
        return Inventory.objects.create(**data)