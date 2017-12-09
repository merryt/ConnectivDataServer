from django.db import models


# Create your models here.

class NetworkNode(models.Model):
    node_name = models.CharField(max_length=200)
    mac_address = models.CharField(max_length=17)
    location_of_pi = models.CharField(max_length=200)
    def __str__(self):
        return self.node_name

class NetworkData(models.Model):
    node_name = models.ForeignKey(NetworkNode, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=39)
    external_ip = models.CharField(max_length=39)
    timestamp = models.DateTimeField("transmission started")
    ping = models.CharField(max_length=10)
    ping_destination = models.CharField(max_length=200)
    def __str__(self):
        return self.timestamp
    
    