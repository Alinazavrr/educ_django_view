from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.serializers import HomeSerializer
from homes.models import Home


# Create your views here.


class HomesApi(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    # http_method_names = ['get']
