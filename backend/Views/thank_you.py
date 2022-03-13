from rest_framework import status
from rest_framework.decorators import api_view
from backend.Serializers.ticket_serializer import TicketSerializer
from rest_framework.response import Response
import json


@api_view(['GET'])
def thank_you(request):
    return Response(json.dumps({'name': request.user.username}))
