from rest_framework.serializers import ModelSerializer
 
from products.models import Product,Gallery,Category,Banner,Review
from rest_framework import serializers
 
 
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = ["id","product","image"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = ('id','image')


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','user_id','product_id','rate','comment','created_at')