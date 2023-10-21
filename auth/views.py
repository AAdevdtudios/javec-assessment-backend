from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import views
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status

# Create your views here.
from .serializers import UserSerializer, TokenPairSerializer


class SignupView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(TokenObtainPairView):
    serializer_class = UserSerializer


class LogoutView(views.APIView):
    def post(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)
