import json

import os
import io

from PIL import Image

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Products
# Create your tests here.


class ProductsViewTestCase(APITestCase):

    # Função definida para gerar uma imagem aleatória para ser usada no teste de inserção de product
    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file
    
    def setUp(self):
        image_file = self.generate_photo_file()
        self.product = Products.objects.create(id=542,name="Mouse",price=5.99)
        self.products_data = {
            "id":542,
            "name": "Mouse",
            "price": 5.99,
            "image_url": image_file
        }

        self.response = self.client.post("http://localhost:5000/products/",self.products_data)

    def test_insert_product(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_list_products(self):
        response = self.client.get("http://localhost:5000/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        id = str(self.product.id)
        response = self.client.delete("http://localhost:5000/products/"+id+"/")
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
   
    def test_edit_product(self):
        id = str(self.product.id)
        data = {
            "name": "SSD",
            "price": 7.99,
        }
        response = self.client.put("http://localhost:5000/products/"+id+"/",data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)