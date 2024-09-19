from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Product
from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    """реализуйте получение всех товаров из БД
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""
    # Получаем все записи из БД
    products = Product.objects.all()
    # Сериализуем полученные данные
    serializer = ProductListSerializer(products, many=True)
    # Отдаем Response
    return Response(serializer.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        """реализуйте получение товара по id, если его нет, то выдайте 404
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductDetailsSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            raise Http404('Product not found')



# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass
