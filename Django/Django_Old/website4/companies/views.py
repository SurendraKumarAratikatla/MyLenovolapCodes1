from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Stock
from .serializers import StockSerializer

# lists all stocks or create a new one
# Stocks/

class StockList(APIView):

    def get(self,request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        serializer = StockSerializer(data=request.data)
        stocks = Stock.objects.all()
        print(stocks)
        fields = ('ticker','open','close','volume')
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Updated successfully'
            return Response(data= data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST',])
# def post(request):
#     stocks = Stock.objects.get(pk = 1)
#     blog_post = BlogPost(author= stocks)
#
#     if request.method == "POST":
#         serializer = BlogPost(blog_post, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)