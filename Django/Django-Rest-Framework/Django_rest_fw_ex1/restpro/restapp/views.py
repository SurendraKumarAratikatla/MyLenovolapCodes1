from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import students
from .serializers import StudentSerializer


class ListEaf(APIView):
    def put(self,request):
        serializer = StudentSerializer(data=request.data)
        stocks = students.objects.all()
        print(stocks)
        fields = ('student_id', 'first_name', 'last_name', 'address', 'gender', 'age')
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Updated successfully'
            return Response(data= data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request):
    #     stocks = ChemicalElement.objects.all()
    #
    #     serializer = EAFListSerializer(stocks, many=True)
    #     return Response(serializer.data)
    #
    # # def get(self, request):
    # #     stocks = ChemicalElement.objects.all()
    # #
    # #     serializer = EAFListSerializer(stocks, many=True)
    # #     return Response(serializer.data)
    #
    # def post(self, pk):
    #     stocks = ChemicalElement.objects.get(id=pk)
    #     serializer = EAFListSerializer(stocks, many=False)
    #     data = {}
    #     data['success'] = 'Updated successfully'
    #     return Response(data=data)

