from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductViewSet(generics.ListCreateAPIView,
                    generics.RetrieveUpdateDestroyAPIView
                    ):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class CategoryViewSet(generics.ListCreateAPIView,
                     generics.RetrieveUpdateDestroyAPIView): 
    serializer_class = ProductSerializer
    queryset = Product.objects.all()