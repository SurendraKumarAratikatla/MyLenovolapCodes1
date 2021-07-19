from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RegistrationSerializer


# user Registration
@api_view(['POST',])
def registration_api(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            register = serializer.save()
            data['Response'] = "Successfully registered a new user."
            data['email'] = register.email
            data['username'] = register.username
        else:
            data = serializer.errors
        return Response(data)