from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EAFListSerializer, EAFListSerializerCommodity
from .models import ChemicalElement, Commodity

@api_view(['GET'])
def apiOverview(request):
    return Response("API VIEW")

# for ChemicalElement view

@api_view(['GET'])
def taskList(request):
    tasks = ChemicalElement.objects.all()
    serializer = EAFListSerializer(tasks, many= True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request,pk):
    tasks = ChemicalElement.objects.get(id = pk)
    serializer = EAFListSerializer(tasks, many= False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = EAFListSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    tasks = ChemicalElement.objects.get(id=pk)
    serializer = EAFListSerializer(instance=tasks,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request,pk):
    tasks = ChemicalElement.objects.get(id=pk)
    tasks.delete()
    return Response("Item successfully deleted")





# for Commodity view

@api_view(['GET'])
def taskListComm(request):
    tasks = Commodity.objects.all()
    serializer = EAFListSerializerCommodity(tasks, many= True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetailComm(request,pk):
    tasks = Commodity.objects.get(id = pk)
    serializer = EAFListSerializerCommodity(tasks, many= False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreateComm(request):
    serializer = EAFListSerializerCommodity(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdateComm(request,pk):
    tasks = Commodity.objects.get(id=pk)
    serializer = EAFListSerializerCommodity(instance=tasks,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDeleteComm(request,pk):
    tasks = Commodity.objects.get(id=pk)
    tasks.delete()
    return Response("Item successfully deleted")