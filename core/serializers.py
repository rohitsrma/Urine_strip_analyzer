# analyzer/serializers.py
from rest_framework import serializers
from .models import UrineStrip

class UrineStripSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrineStrip
        fields = ['id', 'image', 'upload_datetime']
