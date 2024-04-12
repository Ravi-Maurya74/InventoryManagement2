from django.urls import path
from inventory import views
import uuid

urlpatterns = [
    path("<uuid:sku>/",views.InventoryRetrieveUpdateDestroyView.as_view(),name='get-inventory-by-sku'),
    path("",views.InventoryListCreateView.as_view(),name='get-all-inventories'),
]