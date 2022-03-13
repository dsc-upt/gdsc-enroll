from rest_framework.decorators import api_view
from rest_framework.response import Response


# this view only provides an URL to for frontend
@api_view(['GET'])
def dashboard(request):
    return Response()
