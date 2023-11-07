from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenBlacklistSerializer
from users.models import CustomUser

class User_signup(serializers.ModelSerializer):
    
