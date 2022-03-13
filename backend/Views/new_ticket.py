from rest_framework import status
from rest_framework.decorators import api_view
from backend.Serializers.ticket_serializer import TicketSerializer
from rest_framework.response import Response


@api_view(['POST'])
def new_ticket(request):
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)