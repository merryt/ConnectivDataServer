from django.shortcuts import render


# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer, GroupSerializer, NetworkNodeSerializer, NetworkDataSerializer
from .models import NetworkNode, NetworkData
from django.shortcuts import get_object_or_404


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
    

    def get_networknode(self, request, networknode_pk=None):
        networknode = get_object_or_404(NetworkNode.objects.all(), pk=networknode_pk)    
        print("asd")
        return networknode

    def create(self, request, *arg, **kwargs):
        self.get_networknode(request, networknode_pk=kwargs['node_name'])
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(
            network_node_pk = self.kwargs['networknode_pk']
        )
    # def get_queryset(self):
    #     print(self)
    #     return NetworkData.objects.filter(networknode = self.kwargs['networknode_pk'])

    def list(self, request, *arg, **kwargs):
        self.get_networknode(request, networknode_pk=kwargs['networknode_pk'])

        return super().list(request, *args, **kwargs)

    