from inventory.repostories.inventory_repository import InventoryRepository

class InventoryService:
    def __init__(self,repository:InventoryRepository) -> None:
        self.respository = repository

    def get_inventory_by_sku(self,inventory_sku):
        return self.respository.get_inventory_by_sku(inventory_sku=inventory_sku)
    
    def create_an_inventory(self,data):
        return self.respository.create_an_inventory(data=data)
    
    def get_all_inventories(self):
        return self.respository.get_all_inventories()
    
    def update_inventory(self,inventory_sku,updated_data):
        return self.respository.update_inventory(inventory_sku=inventory_sku,updated_data=updated_data)