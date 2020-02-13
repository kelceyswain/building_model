from rest_framework import serializers
from payload.models import Image, Text, Video, Sound, Building

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'title', 'public', 'date_added', 'body', 'building')

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('id', 'title', 'public', 'date_added', 'body', 'building')

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'public', 'date_added', 'body', 'building')

class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ('id', 'title', 'public', 'date_added', 'body', 'building')

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('id', 'name', 'description')
