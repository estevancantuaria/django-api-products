from rest_framework import viewsets
from products.api import serializers
from products import models

class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Products.objects.all()