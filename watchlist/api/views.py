from rest_framework.response import Response
from watchlist.models import Movie
from rest_framework import status
from rest_framework.decorators import api_view
from watchlist.api.serializers import MovieSerializer 

@api_view(['GET','PUT','DELETE'])
def movie_list(request):

    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer= MovieSerializer(movies, many =True)
        return Response(serializer.data)
    
    if request.method =='POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def movie_details(request,pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=pk)
        serializer= MovieSerializer(movie)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)



    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response ( status=status.HTTP_404_NOT_FOUND)