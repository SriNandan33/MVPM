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
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
    def __str__(self):
            return self.proname
class RentalProperty(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    rent_amount = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    thumbnail_1 = models.ImageField(upload_to=upload_location,null=True)
    thumbnail_2 = models.ImageField(upload_to=upload_location, null=True)
    thumbnail_3 = models.ImageField(upload_to=upload_location, null=True)
    thumbnail_4 = models.ImageField(upload_to=upload_location, null=True)
    class Meta:
        verbose_name = 'RentalProperty'
        verbose_name_plural = 'RentalProperties'

    def __str__(self):
        return self.property.proname

class RentalApplication(models.Model):
    rent_property = models.ForeignKey(RentalProperty,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField(default=0)
    is_responded = models.BooleanField(default=False)

    def __str__(self):
        return self.rent_property.property.proname

class MaintenanceRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    issue_title = models.CharField(max_length=50,null=True)
    describe_issue = models.TextField('Describe Issue',null=True)
    date = models.DateTimeField(auto_now_add=True)
    is_serviced = models.BooleanField(default=False)

    def __str__(self):
        return self.property.proname
def notification_file_location(instance,filename):
    return "%s/%d/%s" % (instance.to_user,instance.id,filename)
class Notification(models.Model):
    to_user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField('content')
    file = models.FileField(upload_to=notification_file_location,null=True,blank=True)
    image = models.ImageField(upload_to=notification_file_location,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta :
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ('-date',)

    def __str__(self):
        return self.to_user.username