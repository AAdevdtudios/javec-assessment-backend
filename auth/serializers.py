from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        username = attrs.get("username")
        password = attrs.get("password")

        if not email or not password or not username:
            raise serializers.ValidationError(
                "Please provide username, email and password"
            )

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exist")

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username already exist")

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user

    class Meta:
        model = User
        fields = ("username", "email", "password")


class TokenPairSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
