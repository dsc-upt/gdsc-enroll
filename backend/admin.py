from django.contrib import admin
from django.utils.html import format_html
from backend.Models.ticket_model import Ticket, Team

admin.site.register(Team)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("full_name", "status", "facebook_profile")

    def full_name(self, obj):
        return obj.first_name + " " + obj.last_name

    full_name.short_description = "Full Name"

    def facebook_profile(self, obj):
        return format_html(f'<a href="{obj.facebook}"'
                           f'class="button">Profile</a>')

    facebook_profile.short_description = "Facebook Profile"
