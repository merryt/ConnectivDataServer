import uuid

from django.db import models
from django.utils.translation import ugettext_lazy

# Create your models here.
class UUIDIdMixin(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class NetworkNode(UUIDIdMixin):
    node_name = models.CharField(max_length=200)
    mac_address = models.CharField(max_length=17)
    location_of_pi = models.CharField(max_length=200)
    def __str__(self):
        return self.node_name

class NetworkData(UUIDIdMixin):
    node_name = models.ForeignKey(
        NetworkNode, 
        editable=False, 
        verbose_name=ugettext_lazy('networknode'), 
        related_name='networkdatas',
        on_delete = models.CASCADE)
    ip_address = models.CharField(max_length=39)
    external_ip = models.CharField(max_length=39)
    timestamp = models.DateTimeField("transmission started")
    ping = models.CharField(max_length=10)
    ping_destination = models.CharField(max_length=200)

    
    