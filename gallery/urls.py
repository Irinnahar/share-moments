from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('uploadform/', views.GalleryCreate.as_view(), name = 'upload_form')
]