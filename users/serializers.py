from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import ConfirmUser


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserValidateSerializer(UserLoginSerializer):
    def validate_username(self, username):
        """ Проверяем существует ли пользователь"""
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')


class CodeSerializer(serializers.Serializer):
    code = serializers.CharField(min_length=6, max_length=6)

    def validate_code(self, code):
        try:
            ConfirmUser.objects.get(code=code)
        except ConfirmUser.DoesNotExist:
            raise ValidationError('Код не действителен')
        return code