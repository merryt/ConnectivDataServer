from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import NetworkNode, NetworkData

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class NetworkNodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NetworkNode
        fields = ('node_name', 'mac_address', 'location_of_pi')

class NetworkDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NetworkData
        fields = ('node_name', 'ip_address', 'external_ip', 'external_ip', 'timestamp', 'ping', 'ping_destination')

