from inventory.models import Inventory

class InventoryRepository:
    def get_inventory_by_sku(self,inventory_sku):
        return Inventory.objects.get(sku=inventory_sku)
    
    def create_an_inventory(self,data):
        return Inventory.objects.create(**data)
    
    def get_all_inventories(self):
        return Inventory.objects.all()
    
    def update_inventory(self,inventory_sku,updated_data):
        try:
            inventory = Inventory.objects.get(sku=inventory_sku)
        except Inventory.DoesNotExist:
            return None
        
        for key,value in updated_data.items():
            setattr(inventory,key,value)

        inventory.save()
        return inventory
    
    def delete_inventory(self,inventory_sku):
        try:
            inventory = Inventory.objects.get(sku=inventory_sku)
            inventory.delete()
            return True
        except Inventory.DoesNotExist:
            return False
