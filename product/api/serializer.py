from product.models import Product, Category, Characteristic, Description, SubImage
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title']


class SubImagePOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubImage
        fields = ['id', 'product', 'image']


class SubImageGETSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubImage
        fields = ['id', 'image']


class DescriptionGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ['id', 'text']


class DescriptionPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ['id', 'product', 'text']


class CharacteristicPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = Characteristic
        fields = ['id', 'product', 'tip_model', 'test_conditions', 'maximum_power', 'voltage', 'voltage_maximum']


class CharacteristicGETSerializer(serializers.ModelSerializer):

    class Meta:
        model = Characteristic
        fields = ['id', 'tip_model', 'test_conditions', 'maximum_power', 'voltage', 'voltage_maximum']


class ProductGETSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    sub_image = SubImageGETSerializer(read_only=True, many=True)
    description = DescriptionGETSerializer(read_only=True)
    characteristic = CharacteristicGETSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'image', 'price', 'sub_image', 'description', 'characteristic']


class ProductPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'image', 'price']
