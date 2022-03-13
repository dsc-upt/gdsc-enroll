from rest_framework import status
from rest_framework.decorators import api_view
from backend.Serializers.ticket_serializer import TicketSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def new_ticket(request):
    if request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        return Response()
    return Response(status=status.HTTP_400_BAD_REQUEST)
