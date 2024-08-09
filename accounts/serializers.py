from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


# Admin only create user
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'is_customer', 'is_consultant', 'is_admin', 'is_customer_service']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_customer': {'required': False},
            'is_consultant': {'required': False},
            'is_admin': {'required': False},
            'is_customer_service': {'required': False},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_customer=validated_data['is_customer'],
            is_consultant=validated_data['is_consultant'],
            is_admin=validated_data['is_admin'],
            is_customer_service=validated_data['is_customer_service']
        )
        return user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'is_customer', 'is_consultant', 'is_admin', 'is_customer_service']



class PasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=255)
    new_password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError('Passwords do not match')
        return data