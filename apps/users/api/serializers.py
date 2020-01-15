from rest_framework import serializers

from ..models import User


class MiniprogramLoginSerializer(serializers.Serializer):

    code = serializers.CharField()
    avatar_url = serializers.CharField()
    name = serializers.CharField()
    encryptedData = serializers.CharField()
    iv = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'avatar', 'name']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'avatar', 'name']


