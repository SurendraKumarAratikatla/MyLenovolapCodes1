from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CORONAListSerializer
from .models import *
from django.http import JsonResponse
import json

@api_view(['GET'])
def apiCoronaView(request):
    data_json = json.dumps(j_data_obj)
    return JsonResponse(j_data_obj, safe=False)
