from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView

from backend.Serializers.ticket_serializer import TicketSerializer


class NewTicket(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = TicketSerializer
