from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from .models import Product
import json


# Create your views here.
@csrf_exempt
def product_list(request):
    """Lista todos los productos (GET) y crea un nuevo producto (POST)."""
    if request.method == 'GET':
        products = Product.objects.all().values()
        return JsonResponse(list(products), safe=False, status=200)

    elif request.method == 'POST':
        data = json.loads(request.body)
        new_product = Product.objects.create(
            name=data['name'],
            description=data.get('description', ''),
            price=data.get('price', 0)
        )
        return JsonResponse({
            'id': new_product.id,
            'name': new_product.name,
            'description': new_product.description,
            'price': str(new_product.price),
            'created_at': new_product.created_at
        }, status=201)

    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'GET':
        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': str(product.price),
            'created_at': product.created_at
        }, status=200)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.save()
        return JsonResponse({
            'message': 'Product updated successfully'
        }, status=200)

    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({
            'message': 'Product deleted successfully'
        }, status=204)

    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])