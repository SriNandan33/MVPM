from django.db import models

from django.db import models
from django.contrib.auth.models import User

def upload_location(instance, filename):
    return "%s/thumbnail/%s" % (instance.user, filename)

class Property(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    proname = models.CharField('Name',max_length=50)
    PROPERTY_TYPE_CHOICES = (
        ('HOUSE','HOUSE'),
        ('LAND','LAND'),
        ('APARTMENT','APARTMENT'),
    )
    PLAN_CHOICES=(
        ('SILVER','SILVER'),
        ('GOLD', 'GOLD'),
        ('DIAMOND', 'DIAMOND'),
    )
    SERVICE_TYPE_CHOICES =(
        ('RENTAL','RENTAL'),
        ('SALE', 'SALE'),
        ('MAINTENANCE', 'MAINTENANCE'),
        ('CONSTRUCTION', 'CONSTRUCTION'),
    )
    property_type = models.CharField(
        max_length=10,
        choices=PROPERTY_TYPE_CHOICES,
        default='HOUSE'
    )
    service_type = models.CharField(
        max_length=20,
        choices=SERVICE_TYPE_CHOICES,
        default='MAINTENANCE'
    )
    plan = models.CharField(
        max_length=20,
        choices=PLAN_CHOICES,
        default='SILVER'
    )
    city = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to=upload_location, null=True)
    def __str__(self):
            return self.user.username