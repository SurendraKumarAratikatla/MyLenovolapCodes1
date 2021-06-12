from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import MoviesList
from .serializers import MoviesListSerializer


# class ListMoives(APIView):
# 	def put(self, request):
# 		serializer = MoviesListSerializer(data=request.data)
# 		movies_list = MoviesList.objects.all()
# 		print(movies_list)
# 		fields = ('movie_name','hero_name','heroin_name','music_director_name','director_name')
# 		data = {}
# 		if serializer.is_valid():
# 			serializer.save()
# 			data['success'] = 'Updated successfully'
# 			return Response(data=data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListMovies(APIView):
    def put(self,request):
        serializer = MoviesListSerializer(data=request.data)
        stocks = MoviesList.objects.all()
        print(stocks)
        fields = ('movie_name','hero_name','heroin_name','music_director_name','director_name')
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Updated successfully'
            return Response(data= data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)