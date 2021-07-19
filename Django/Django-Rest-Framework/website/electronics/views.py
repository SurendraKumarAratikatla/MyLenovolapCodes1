from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Laptop
from .serializers import LaptopSerializer


#
# def laptop_view(request):
#     return HttpResponse('<h3>hello<h3>')

@api_view(['GET',])
def api_laptop_view(request):
    laptop_data = Laptop.objects.all()
    if request.method == 'GET':
        serializer = LaptopSerializer(laptop_data)
        return Response(serializer.data)
