from django.shortcuts import render
from .models import NetworkNode, NetworkData

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer, GroupSerializer, NetworkNodeSerializer, NetworkDataSerializer
# NetworkDataPOSTSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    """
    API returns and the nodes that have submitted network data 
    """
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    
class NetworkDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view all nodes that have submitted network date
    """
    queryset = NetworkData.objects.all()
    serializer_class = NetworkDataSerializer
