from django.urls import path

from .views import ListImage, ListText, ListVideo, ListSound, ListBuilding
from .views import DetailImage, DetailText, DetailVideo, DetailSound, DetailBuilding

urlpatterns = [
    path('images/', ListImage.as_view()),
    path('texts/', ListText.as_view()),
    path('videos/', ListVideo.as_view()),
    path('sounds/', ListSound.as_view()),
    path('buildings/', ListBuilding.as_view()),
    
    path('image/<int:pk>/', DetailImage.as_view()),
    path('text/<int:pk>/', DetailText.as_view()),
    path('video/<int:pk>/', DetailVideo.as_view()),
    path('sound/<int:pk>/', DetailSound.as_view()),
    path('building/<int:pk>/', DetailBuilding.as_view()),
    
]
