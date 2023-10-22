from django.shortcuts import render
from django.views.generic import CreateView

from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    CreateAPIView,
    DestroyAPIView
)

from .models import Products
from .serializers import ProductsSerializer


# Create your views here.
class ProductCreateView(CreateView):
    model = Products
    fields = '__all__'
    template_name = 'food/new.html'
    success_url = '/'



# API for search foods
class APIFoodsListView(ListAPIView):
    serializer_class = ProductsSerializer
    def get_queryset(self):
        txt = self.kwargs['txt']
        queryset = Products.objects.filter(product_name__icontains=txt)
        return queryset


class APIFoodsUpdateView(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class APIFoodsCreateAPIView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class APIFoodsDeleteAPIView(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer