from django.shortcuts import render
from .models import Gallery
from django.views import generic
from django.views.generic.edit import CreateView,DeleteView,UpdateView


# Create your views here.
class IndexView(generic.ListView):
    
    template_name = 'gallery/index.html'
    context_object_name = 'images'
    queryset = Gallery.objects.all()


class GalleryCreate(CreateView):
    model = Gallery
    fields = ['image_name', 'image_type', 'image_logo']
    
