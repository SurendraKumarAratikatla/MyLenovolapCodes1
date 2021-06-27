from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CORONAListSerializer
from .models import CoronaModel
from django.http import JsonResponse


@api_view(['GET'])
def apiCoronaView(request):
    tasks = CoronaModel.objects.all()
    serializer = CORONAListSerializer(tasks, many= True)
    return JsonResponse(serializer.data)