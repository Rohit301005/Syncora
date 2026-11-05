from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'is_phone_verified', 'is_staff')
    search_fields = ('full_name', 'email', 'phone')
