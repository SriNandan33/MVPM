from django.contrib import admin
from . import models

admin.site.register(models.Property)
admin.site.register(models.Notification)

class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ["user","issue_title","is_serviced"]
    list_filter = ["is_serviced","date"]
    search_fields = ["user__username",]
    class Meta:
       model = models.MaintenanceRequest
admin.site.register(models.MaintenanceRequest,MaintenanceRequestAdmin)
