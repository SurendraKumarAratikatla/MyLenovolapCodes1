from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Laptop
from .serializers import LaptopSerializer, RegistrationSerializer


#
# def laptop_view(request):
#     return HttpResponse('<h3>hello<h3>')

@api_view(['GET',])
def get_api_laptop_view(request):
    laptop_data = Laptop.objects.all()
    if request.method == 'GET':
        serializer = LaptopSerializer(laptop_data, many= True)
        return Response(serializer.data)

@api_view(['GET',])
def get_detail_api_laptop_view(request,pk):
    laptop_data = Laptop.objects.get(id = pk)
    serializer = LaptopSerializer(laptop_data, many= False)
    return Response(serializer.data)

@api_view(['PUT',])
def update_api_laptop_view(request, pk):
    laptop_data = Laptop.objects.get(id = pk)
    serializer = LaptopSerializer(instance=laptop_data, data = request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["Success"] = "Updated Successfully"
    return Response(data = data)

@api_view(['DELETE',])
def delete_api_laptop_view(request,pk):
    laptop_data = Laptop.objects.get(id = pk)
    if request.method == 'DELETE':
        operation = laptop_data.delete()
        data = {}
        if operation:
            data["Success"] = "Deleted Successfully"
        else:
            data["Failed"] = "Delete failed"
        return Response(data = data)

@api_view(['POST',])
def create_api_laptop_view(request):
    serializer = LaptopSerializer(data=request.data, many= True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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