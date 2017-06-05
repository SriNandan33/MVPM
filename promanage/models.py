from django.db import models

from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
    return "%s/thumbnail/%s" % (instance.user, filename)

class Property(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    proname = models.CharField('Name',max_length=50)
    PROPERTY_TYPE_CHOICES = (
        ('H','HOUSE'),
        ('L','LAND'),
        ('A','APARTMENT'),
    )
    PLAN_CHOICES=(
        ('S','SILVER'),
        ('G', 'GOLD'),
        ('D', 'DIAMOND'),
    )
    SERVICE_TYPE_CHOICES =(
        ('RE','RENTAL'),
        ('SA', 'SALE'),
        ('MA', 'MAINTENANCE'),
        ('CO', 'CONSTRUCTION'),
    )
    property_type = models.CharField(
        max_length=1,
        choices=PROPERTY_TYPE_CHOICES,
        default='H'
    )
    service_type = models.CharField(
        max_length=2,
        choices=SERVICE_TYPE_CHOICES,
        default='MA'
    )
    plan = models.CharField(
        max_length=1,
        choices=PLAN_CHOICES,
        default='S'
    )
    city = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to=upload_location, null=True)
    def __str__(self):
            return self.user.username