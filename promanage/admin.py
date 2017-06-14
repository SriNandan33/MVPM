from django.contrib import admin
from . import models

admin.site.register(models.Property)
admin.site.register(models.Notification)
admin.site.register(models.MaintenanceRequest)
