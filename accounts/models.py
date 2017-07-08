from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


def upload_location(instance, filename):
    return "%s/avatar/%s" % (instance.user, filename)
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=upload_location,null=True,blank=True)
    description = models.CharField(max_length=100,default="")
    email = models.EmailField()
    phone = models.BigIntegerField(default=0)
    country = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    city = models.CharField(max_length=100,null=True)
    zipcode=models.IntegerField(default=0)
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.user.username


def create_profile(sender , **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)