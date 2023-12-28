# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Organizer

class OrganizerAdmin(UserAdmin):
    list_display = ['username', 'full_name', 'email', 'is_approved']
    list_filter = ['is_approved']
    search_fields = ['username', 'full_name', 'email']
    actions = ['approve_organizers']

    def approve_organizers(self, request, queryset):
        queryset.update(is_approved=True)
    approve_organizers.short_description = "Approve selected organizers"

admin.site.register(Organizer, OrganizerAdmin)
