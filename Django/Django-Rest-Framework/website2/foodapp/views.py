from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Laptop
from .serializers import LaptopSerializer


@api_view(['GET',])
def get_api_laptop_view(request):
    laptop_data = Laptop.objects.all()
    if request.method == 'GET':
        serializer = LaptopSerializer(laptop_data, many= True)
        return Response(serializer.data)

@api_view(['POST',])
def post_api_laptop_view(request):
    laptop_data = Laptop.objects.all()
    serializer = LaptopSerializer(instance=laptop_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("data inserted successfully")
