from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from inventory.models import Inventory
from inventory.repostories.inventory_repository import InventoryRepository
from inventory.serializers import InventorySerializer
from rest_framework.views import APIView

# Create your views here.

inventory_repository = InventoryRepository()

class InventoryListCreateView(APIView):
    def get(self,request):
        paginator = PageNumberPagination()
        paginator.page_size = 10 
        
        inventories = inventory_repository.get_all_inventories() 
        result_page = paginator.paginate_queryset(inventories, request)
        serializer = InventorySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)   

    def post(self,request):
        data = request.data
        try:
            inventory = inventory_repository.create_an_inventory(data=data)
            serialied_data = InventorySerializer(inventory).data
            return Response(serialied_data,status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': str(e)},status=status.HTTP_400_BAD_REQUEST)
        
class InventoryRetrieveUpdateDestroyView(APIView):
    def get(self,request,sku):
        if not sku:
            return Response({'message': 'SKU parameter is required'},status=status.HTTP_400_BAD_REQUEST)
        try:
            inventory = inventory_repository.get_inventory_by_sku(sku)
            serialized_data = InventorySerializer(inventory).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        except Inventory.DoesNotExist:
            return Response({'message': 'Inventory not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
        
    