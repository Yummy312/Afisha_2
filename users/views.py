from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserValidateSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from extra.utils import RandomCode
from .models import ConfirmUser
from .serializers import CodeSerializer


@api_view(['POST'])
def register_view(request):
    """Регистрация пользователя"""
    serializer = UserValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = User.objects.create_user(
        username=serializer.validated_data.get('username'),
        password=serializer.validated_data.get('password'),
        is_active=False
    )
    code = RandomCode().generate_code
    ConfirmUser.objects.create(
        code=code,
        user=user

    )

    return Response(data= f"User created, code for activate: {code} ",
                    status=status.HTTP_201_CREATED)


@api_view(['POST'])
def confirm_user_view(request):
    code = CodeSerializer(data=request.data)
    code.is_valid(raise_exception=True)
    data = ConfirmUser.objects.get(code=code.validated_data.get('code'))
    get_user = User.objects.get(username=data.user)
    get_user.is_active = True
    get_user.save()
    return Response(data='Проверка проведена успешно!')


@api_view(['POST'])
def authorization_view(request):
    """Авторизация пользователя"""
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(
        username=serializer.validated_data.get('username'),
        password=serializer.validated_data.get('password'))

    if user:  # if user found
        """Так как пользователь найден мы создаем для него ключ"""
        if user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key}, status=status.HTTP_200_OK)

    return Response(data='Подтвердите ваш аккаунт чтобы авторизоваться', status=status.HTTP_401_UNAUTHORIZED)