from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user","email","phone"]
    search_fields = ["user__username"]
    class Meta:
        model = UserProfile

admin.site.register(UserProfile,UserProfileAdmin)
