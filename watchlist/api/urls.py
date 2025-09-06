
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist.api.views import movie_list,movie_details
from watchlist.api.views import (ReviewList,ReviewDetail,WatchListAV,
                                WatchDetailAV,
                                StreamplatformAV,ReviewCreate,StreamplatformVS)

router = DefaultRouter()
router.register('stream',StreamplatformVS,basename = 'streamplatform')



urlpatterns = [
    path('list/', WatchListAV.as_view(), name = 'movie-list'),
    path('<int:pk>',  WatchDetailAV.as_view(), name = 'movie-detail'),
    path('',include(router.urls)),


    #path('stream', StreamplatformAV.as_view(),name = 'stream'),
    #path('review',ReviewList.as_view(),name = 'Review-list'),
    #path('review/<int:pk>',ReviewDetail.as_view(),name = 'Review-Detail'),



    path('stream/<int:pk>/review',ReviewList.as_view(),name = 'Review-List'),
    path('stream/review/<int:pk>',ReviewDetail.as_view(),name = 'Review-Detail'),
    path('stream/<int:pk>/review-create',ReviewCreate.as_view(),name = 'Review-Create'),

  



]   

