from ..Models.ticket_model import Ticket
from rest_framework import serializers


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ('id', 'status')
