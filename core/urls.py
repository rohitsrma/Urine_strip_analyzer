from django.urls import path
from .views import IndexView, UrineStripUploadView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('upload/', UrineStripUploadView.as_view(), name='upload_urine_strip'),
]