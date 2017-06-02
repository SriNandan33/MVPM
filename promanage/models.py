from django.db import models

from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField

class Property(models.Model):
    user = models.ForeignKey(User)
    proname = models.CharField('Name',max_length=50)

    TYPE_CHOICES = (
        ('H','HOUSE'),
        ('L','LAND'),
        ('A','APARTMENT'),
    )
    PLAN_CHOICES=(
        ('S','SILVER'),
        ('G', 'GOLD'),
        ('D', 'DIAMOND'),
    )
    type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default='H'
    )
    city = models.CharField(max_length=50,blank=True)
    location = PlainLocationField(based_fields=['city'],zoom=7)
    plan = models.CharField(
        max_length=1,
        choices=PLAN_CHOICES,
        default='S'
    )
    def __str__(self):
            return self.user.username