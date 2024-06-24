from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UrineStripSerializer
from .process import analyse_colors
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "base.html"

class UrineStripUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = UrineStripSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            image_path = file_serializer.data['image']
            colors = analyse_colors(image_path)
            return JsonResponse({"colors": colors}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)