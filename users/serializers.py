from rest_framework import serializers
from .models import User


class SignUpSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'phone_number', 'tokens']
        read_only_fields = ['id',]


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']
