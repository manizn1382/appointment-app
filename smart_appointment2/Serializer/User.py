from rest_framework.serializers import ModelSerializer
from smart_appointment2.Model.Profile import User
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
