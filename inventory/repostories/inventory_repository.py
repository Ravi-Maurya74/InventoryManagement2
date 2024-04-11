from inventory.models import Inventory

class InventoryRepository:
    def get_inventory_by_uuid(self,inventory_uuid):
        return Inventory.objects.get(uuid=inventory_uuid)
    
    def create_an_inventory(self,data):
        return Inventory.objects.create(**data)