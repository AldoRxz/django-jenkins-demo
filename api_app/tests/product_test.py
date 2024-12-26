from django.test import TestCase, Client
from django.urls import reverse
from ..models import Product
import json


class ProductAPITestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.product = Product.objects.create(
            name="Test Product",
            description="Test description",
            price=10.00
        )

        self.product_detail_url = f'/products/{self.product.id}/'
        self.product_list_url = '/products/'

    def test_get_product_list(self):
        response = self.client.get(self.product_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], "Test Product")

    def test_post_product_list(self):
        data = {
            "name": "New Product",
            "description": "New product description",
            "price": 50.00
        }
        response = self.client.post(
            self.product_list_url,
            data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.last().name, "New Product")

    def test_get_product_detail(self):
        response = self.client.get(self.product_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], "Test Product")

    def test_put_product_detail(self):
        # Prueba el método PUT para actualizar un producto
        data = {
            "name": "Updated Product",
            "description": "Updated description",
            "price": 150.00
        }
        response = self.client.put(
            self.product_detail_url,
            data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Product.objects.get(id=self.product.id).name, "Updated Product")

    def test_delete_product_detail(self):
        # Prueba el método DELETE para eliminar un producto
        response = self.client.delete(self.product_detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.count(), 0)
