from django.shortcuts import render
from rest_framework import generics, views, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer


class RegisterView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = "yusuf123"
        serializer.save(password=password)
        return Response(data=serializer.data)


class BlacklistRefreshView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response("Success")
