from rest_framework import serializers
 
from user.models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','name','address','pincode','mobile')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ('email','password')
        
