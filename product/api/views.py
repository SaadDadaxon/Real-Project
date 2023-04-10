import permission as permission
from django.shortcuts import render
from rest_framework import generics, permissions
from product.models import Category, Product, SubImage, Description, Characteristic
from .serializer import CategorySerializer, ProductPOSTSerializer, ProductGETSerializer, SubImageGETSerializer, SubImagePOSTSerializer, \
    DescriptionGETSerializer, DescriptionPOSTSerializer, CharacteristicPOSTSerializer, CharacteristicGETSerializer


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductGETSerializer
        return ProductPOSTSerializer


class ProductRUD(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductGETSerializer
        return ProductPOSTSerializer


class SubImageListCreate(generics.ListCreateAPIView):
    queryset = SubImage.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SubImageGETSerializer
        return SubImagePOSTSerializer


class DescriptionListCreate(generics.ListCreateAPIView):
    queryset = Description.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DescriptionGETSerializer
        return DescriptionPOSTSerializer


class DescriptionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Description.objects.all()
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DescriptionGETSerializer
        return DescriptionPOSTSerializer


class CharacteristicListCreate(generics.ListCreateAPIView):
    queryset = Characteristic.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CharacteristicGETSerializer
        return CharacteristicPOSTSerializer


class CharacteristicRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Characteristic.objects.all()
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CharacteristicGETSerializer
        return CharacteristicPOSTSerializer



