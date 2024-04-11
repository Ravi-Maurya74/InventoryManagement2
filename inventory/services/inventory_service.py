from inventory.repostories.inventory_repository import InventoryRepository

class InventoryService:
    def __init__(self) -> None:
        self.respository = InventoryRepository()

    def get_inventory_by_sku(self,inventory_sku):
        return self.respository.get_inventory_by_sku(inventory_sku=inventory_sku)
    
    def create_an_inventory(self,data):
        return self.respository.create_an_inventory(data=data)