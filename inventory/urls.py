from django.urls import path
from inventory import views
import uuid

urlpatterns = [
    # path("",views.create_inventory,name='create-inventory'),
    path("<uuid:sku>/",views.get_inventory_by_sku,name='get-inventory-by-sku'),
    path("",views.get_all_inventories,name='get-all-inventories'),
]