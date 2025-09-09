from rest_framework.response import Response
from watchlist.models import Watchlist
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

# from rest_framework.decorators import api_view
from watchlist.api.serializers import WatchlistSerializer,StreamplatformSerializer,ReviewSerializer
from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework import viewsets

from watchlist.models import Watchlist,Streamplatform,Review

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def query_set(self):
        return Review.objects.all()


    def perform_create(self,serializer):
        pk = self.kwargs.get('pk')
        movie = Watchlist.objects.get(pk=pk)
        watchlist = Watchlist.objects.get(pk=pk)

        review_user = self.request.user
        review_queyset = Review.objects.filter(watchlist= watchlist , review_user=review_user)

        if review_queyset.exists():
            raise ValidationError("Already given a review ")

        serializer.save(Watchlist=Watchlist,review_user = review_user)




class ReviewList(generics.ListCreateAPIView):
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        p = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    


# class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset  = Review.objects.all()
#     serializer_class = ReviewSerializer


#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class StreamplatformVS(viewsets.ModelViewSet):   
    queryset = Streamplatform.objects.all()
    serializer_class = StreamplatformSerializer

    # def list(self, request):
    #     queryset = Streamplatform.objects.all()
    #     serializer = StreamplatformSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Streamplatform.objects.all()
    #     watchlist = get_object_or_404(queryset, pk=pk)
    #     serializer = StreamplatformSerializer(watchlist)
    #     return Response(serializer.data)

    # def create(self,request):
    #     serializer = StreamplatformSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else :
    #         return Response(serializer.saved)
        


class StreamplatformAV(APIView):
    def get(self,request):
        platform = Streamplatform.objects.all()
        serializer = StreamplatformSerializer(platform,many = True)
        return Response(serializer.data)

    def post(self,request):
        platform = Streamplatform.objects.all()
        serializer = StreamplatformSerializer(platform, many = True)
        serializer = StreamplatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.saved)
        

        


class WatchListAV(APIView):
    def get(self,request):
        movies = Watchlist.objects.all()
        serializer= WatchlistSerializer(movies, many =True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
        


class WatchDetailAV(APIView):
    def get(self,request,pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchlistSerializer(movie)
        return Response(serializer.data)

    def put(self, request,pk):
        movie = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,pk):
        movie = Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response ( status=status.HTTP_404_NOT_FOUND)








# @api_view(['GET','PUT','DELETE'])
# def movie_list(request):

#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer= MovieSerializer(movies, many =True)
#         return Response(serializer.data)
    
#     if request.method =='POST':
        # serializer = MovieSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else :
        #     return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method == 'GET':
#         movie = Movie.objects.get(pk=pk)
#         serializer= MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else :
#             return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)



#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response ( status=status.HTTP_404_NOT_FOUND)