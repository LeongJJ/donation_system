from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'full_name', 'email', 'contact_number', 'birthdate', 'gender', 'profile_image']
    actions = ['remove_custom_users']

    def remove_custom_users(self, request, queryset):
        queryset.delete()
    remove_custom_users.short_description = "Remove selected custom users"

admin.site.register(CustomUser, CustomUserAdmin)
