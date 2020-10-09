from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import RegistrationSerializer
# Create your views here.


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user."
            data['phone'] = account.phone
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
        else:
            data = serializer.errors
        return Response(data)