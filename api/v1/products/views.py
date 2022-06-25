from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
 
from api.v1.products.serializers import ProductSerializer,GallerySerializer,CategorySerializer,BannerSerializer,ReviewSerializer
from products.models import Product,Gallery,Category,Banner,Review
 
from django.contrib.auth.models import User

 
@api_view(["GET"])
@permission_classes([AllowAny])
def products(request):
    instances = Product.objects.filter(is_deleted = False)
    context = {"request" : request}
    serializer = ProductSerializer(instances,many =True,context=context)
    response_data = {
        'status_code' : 6000,
        'data' : serializer.data
    }
    return Response(response_data)

 
@api_view(["GET"])
@permission_classes([AllowAny])
def gallery(request):
    instances = Gallery.objects.all()
    context = {"request" : request}
    serializer = GallerySerializer(instances,many =True,context=context)
    response_data = {
        'status_code' : 6000,
        'data' : serializer.data
    }
    return Response(response_data)


@api_view(["GET"])
@permission_classes([AllowAny])
def categories(request):
    instances = Category.objects.all()
    context = {"request" : request}
    serializer = CategorySerializer(instances,many =True,context = context)
    response_data = {
        'status_code' : 6000,
        'data' : serializer.data
    }
    return Response(response_data)


@api_view(["GET"])
@permission_classes([AllowAny])
def banners(request):
    instances = Banner.objects.all()
    context = {"request" : request}
    serializer = BannerSerializer(instances,many =True,context = context)
    response_data = {
        'status_code' : 6000,
        'data' : serializer.data
    }
    return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_review_rate(request):
    data = request.data
    product_id = request.data["product_id"]
    comment = request.data["comment"]
    rate = request.data["rate"]
    user_id = request.user.id
    
    serializer = ReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        Review(user_id=user_id,product_id=product_id,rate=rate,comment=comment).save()

        response_data={
            "status" : 6000,
            "data" : serializer.data,
            "message" : "Review Created!!"
        }
    else:
        response_data={
            "status" : 6001,
            "error" : serializer.errors,
        }
    return Response(response_data)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_review_rate(request,pk):
    instances = Review.objects.filter(product_id=pk)
    context = {"request" : request}
    serializer = ReviewSerializer(instances,many =True,context = context)
    response_data = {
        'status_code' : 6000,
        'data' : serializer.data
    }
    return Response(response_data)