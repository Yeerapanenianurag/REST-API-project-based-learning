
from django.urls import path, include
# from watchlist.api.views import movie_list,movie_details
from watchlist.api.views import WatchListAV, WatchDetailAV,StreamplatformAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name = 'movie-list'),
    path('<int:pk>',  WatchDetailAV.as_view(), name = 'movie-detail'),

    path('stream', StreamplatformAV.as_view(),name = 'stream')
]   

