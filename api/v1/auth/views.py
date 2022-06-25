import requests
import json
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User
from user.models import Profile
from api.v1.auth.serializers import ProfileSerializer
from api.v1.auth.serializers import UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.name
        
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def create(request):
    data = request.data
    name = request.data["name"]
    email = request.data["email"]
    mobile = request.data["mobile"]
    password = request.data["password"]

    user_serializer = UserSerializer(data=data)
    profile_serializer = ProfileSerializer(data=data)

    if profile_serializer.is_valid():
        if user_serializer.is_valid():

            if not User.objects.filter(username=name).exists():
                user = User.objects.create_user(
                    username = name,
                    email = email,
                    password = password
                )

                profile = Profile.objects.create(
                    user_id = user.id,
                    name = name,
                    mobile = mobile
                )

                headers={
                    "content-Type" : "application/json" 
                }
                data={
                    "username" : name,
                    "email" : email,
                    "password" : password
                }

                # for login automatically after signup
                protocol = "http://"
                if request.is_secure():
                    protocol = "https://"
                host = request.get_host()

                url = protocol + host +"/api/v1/auth/token/"
                response = requests.post(url, headers=headers, data=json.dumps(data))
                response_data = {
                    "status_code" : 6000,
                    "data" : response.json(),
                    "message" : "Account Created"
                }       
            else:
                response_data = {
                    "status_code" : 6001,
                    "error" : "This account already exist."
                }    
        else:           
            response_data = {
                "status_code" : 6001,
                "error" : user_serializer.errors
            } 
    else:
        response_data = {
            "status_code" : 6001,
            "error" : profile_serializer.errors
        } 
    
    return Response(response_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_profile(request,pk):
    if Profile.objects.filter(user=pk).exists():         
        instance = Profile.objects.get(user=pk)
        context = {"request" : request}
        serializer = ProfileSerializer(instance,context = context)
        response_data = {
            'status_code' : 6000,
            'data' : serializer.data
        }
    else:
        response_data = {
            'status_code' : 6001,
            'message' : 'Profile not exist'
        }
    return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_profile(request,pk):
    try: 
        user = pk
        name = request.data["name"]
        address = request.data["address"]
        pincode = request.data["pincode"]
        mobile = request.data["mobile"]   
    except:
        response_data = {
            'status_code' : 6001,
            'message' : "There was something wrong while updating your profile."
        }
        return Response(response_data)

    if not(User.objects.filter(id = user)).exists():
        response_data = {
            'status_code' : 6001,
            'message' : 'No such user found!'
        }        
    else:       
        profile = Profile.objects.filter(user = user)
        if profile.exists():
            is_mobile = Profile.objects.filter(~Q(user=user),Q(mobile=mobile)).exists()
            if not is_mobile:
                profile.update(user=user,name = name,address = address,pincode=pincode,mobile=mobile)
                response_data = {
                    'status_code' : 6000,
                    'message' : "Profile Updated"
                }
            else:
                response_data = {
                'status_code' : 6001,
                'error' : 'Mobile number already exist.'
                }  
        else:
            Profile.objects.create(
                user_id = user,
                name = name,
                address = address,
                pincode = pincode,
                mobile = mobile
            )
            response_data = {
                'status_code' : 6000,
                'message' : "Profile Created"
            }
    
    return Response(response_data)

    