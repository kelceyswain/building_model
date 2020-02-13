from rest_framework import generics
from rest_framework import filters

from payload.models import Image, Text, Video, Sound, Building
from .serializers import ImageSerializer, TextSerializer, VideoSerializer, SoundSerializer, BuildingSerializer


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

# Lists 

#TODO Cut down the amount of information displayed in the lists

class ListImage(generics.ListAPIView):
    filter_backends = [DynamicSearchFilter]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ListText(generics.ListAPIView):
    filter_backends = [DynamicSearchFilter]
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    
class ListVideo(generics.ListAPIView):
    filter_backends = [DynamicSearchFilter]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class ListSound(generics.ListAPIView):
    filter_backends = [DynamicSearchFilter]
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer

class ListBuilding(generics.ListAPIView):
    filter_backends = [DynamicSearchFilter]
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

# Details

class DetailImage(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class DetailText(generics.RetrieveAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    
class DetailVideo(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class DetailSound(generics.RetrieveAPIView):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer

class DetailBuilding(generics.RetrieveAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer    
