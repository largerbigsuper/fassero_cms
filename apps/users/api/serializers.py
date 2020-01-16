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
        fields = ['id', 'avatar', 'name', 'desc', 'phone', 'position', 'address']


class UserProfileSerializer(serializers.ModelSerializer):
    
    avatar_url = serializers.CharField(write_only=True, allow_blank=True, required=False)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'avatar', 'name', 'avatar_url', 'desc', 'phone', 'position', 'address']
        read_only_fields = ['avatar', 'username']


