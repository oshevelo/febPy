from rest_framework import serializers
from .models import Image



class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['id', 'product', 'name', 'descrption', 'size', 'time_posted']


class ImageListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    editor = serializers.ReadOnlyField(source='editor.username')

    class Meta:
        model = Image
        fields = ['owner', 'editor', 'id', 'product', 'name', 'descrption', 'size', 'time_posted', 'upload']

