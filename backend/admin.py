from django.contrib import admin

from backend.Models.ticket_model import Ticket, Team

admin.site.register(Ticket)
admin.site.register(Team)
