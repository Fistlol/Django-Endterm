from datetime import datetime
from rest_framework import serializers
from main.models import Product, Category, Sale, Appeal, Sub_category
from django.contrib.auth.models import User


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.FloatField()
    description = serializers.CharField()
    image = serializers.CharField(read_only=True)
    rating = serializers.FloatField(read_only=True)
    sub_category_id = serializers.IntegerField(read_only=True)

    def create(self, data):
        product = Product.objects.create(name=data.get('name'))
        return product

    def update(self, instance, data):
        instance.name = data.get('name')
        instance.price = data.get('price')
        instance.description = data.get('description')
        instance.save()
        return instance

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price is lower than zero')
        return value


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Invalid name')
        return value


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('id', 'name', 'description', 'date', 'image')

    def validate_date(self, value):
        if value < datetime.today():
            raise serializers.ValidationError('Date cannot be in the past!')
        return value

    def validate_name(self, value):
        if 'buy' in value:
            raise serializers.ValidationError('Name cannot contain buy word')
        return value


class AppealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appeal
        fields = ('id', 'title', 'file', 'is_active')


class SubCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    image = serializers.CharField()
    category_id = serializers.IntegerField()

    def create(self, data):
        sub_category = Sub_category.objects.create(name=data.get(['name']))
        return sub_category

    def update(self, instance, data):
        instance.name = data.get['name']
        instance.save()
        return instance

    def validate_name(self, value):
        if value.isupper():
            raise serializers.ValidationError('Name cannot be in capital letters')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'is_active', 'is_superuser')
