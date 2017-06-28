from django.contrib import admin
from . import models

class PropertyAdmin(admin.ModelAdmin):
    list_display = ["proname","user","property_type","plan","service_type"]
    list_filter = ["service_type","plan","property_type"]
    search_fields = ["user__username","proname"]
    class Meta:
        model = models.Property

admin.site.register(models.Property,PropertyAdmin)

class RentalAdmin(admin.ModelAdmin):
    list_display = ["user","property","rent_amount","is_available"]
    list_filter = ['is_available']
    search_fields = ["user_username",]
    class Meta:
        model= models.RentalProperty

admin.site.register(models.RentalProperty,RentalAdmin)
class RentalApplicationAdmin(admin.ModelAdmin):
    list_display = ['rent_property','name','email','phone','is_responded']
    list_filter = ['is_responded']
    class Meta:
        model = models.RentalApplication
admin.site.register(models.RentalApplication,RentalApplicationAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ["to_user","title","is_read"]
    list_filter = ["is_read"]
    search_fields = ['to_user__username']
    class Meta:
        model = models.Notification
admin.site.register(models.Notification,NotificationAdmin)

class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ["user","issue_title","is_serviced"]
    list_filter = ["is_serviced","date"]
    search_fields = ["user__username",]
    class Meta:
       model = models.MaintenanceRequest
admin.site.register(models.MaintenanceRequest,MaintenanceRequestAdmin)
