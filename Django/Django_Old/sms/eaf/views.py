from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import ChemicalElement, Commodity
from .serializers import EAFListSerializer


class ListEaf(APIView):
    def put(self,request):
        serializer = EAFListSerializer(data=request.data)
        stocks = ChemicalElement.objects.all()
        print(stocks)
        fields = ('id','name')
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Updated successfully'
            return Response(data= data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        stocks = ChemicalElement.objects.all()

        serializer = EAFListSerializer(stocks, many=True)
        return Response(serializer.data)

    # def get(self, request):
    #     stocks = ChemicalElement.objects.all()
    #
    #     serializer = EAFListSerializer(stocks, many=True)
    #     return Response(serializer.data)

    def post(self, pk):
        stocks = ChemicalElement.objects.all()
        serializer = EAFListSerializer(instance=stocks, many=False)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

