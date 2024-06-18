from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework import response, status
from . import serializers, models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from .utils import Util
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class SingUp(GenericAPIView):

    serializer_class = serializers.SignUpSerializers

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.data

        # получение токенов
        user_email = models.User.objects.get(email=user['email'])
        tokens = RefreshToken.for_user(user_email).access_token
        # отправка почты для верификации пользователя
        current_site = get_current_site(request).domain
        relative_link = reverse('users:email-verify')
        absurl = 'http://' + current_site+relative_link+"?=token="+ str(tokens)
        email_body = 'Привет ' + user['username'] + ('Используй ссылку ниже что бы подтвердить '
                                                     'свой адресс электронной почты \n' +
                                                     absurl)
        data = {"email_body": email_body, 'to_email': user['email'],
                'email_subject': 'Подтвердите вашу почту'}
        Util.send_email(data=data)

        return response.Response({'user_data': user, 'access_token': str(tokens)}, status=status.HTTP_201_CREATED)


class VerifyEmail(GenericAPIView):
    serializer_class = serializers.EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING
    )
    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, options={'verify_signature': False})
            print(payload)
            user = models.User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return response.Response({'email': 'Успешно активирована'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return response.Response({'error': 'Истек срок действия'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return response.Response({"error": 'Неверный токен'}, status=status.HTTP_400_BAD_REQUEST)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', context={"request": request, 'form': form})


def login(request):
    if request.method == "POST":
        
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
    else:
        form = UserLoginForm()
        return render(request,'users/login.html', context={'request': request, 'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
