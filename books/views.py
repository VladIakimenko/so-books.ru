from rest_framework import viewsets
from books.models import Books, Photos, Boxes
from books.serializers import BooksSerializer, BooksListSerializer, PhotosSerializer, BoxesSerializer
from django.shortcuts import render, reverse


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    def get_serializer_class(self):
        return (self.serializer_class, BooksListSerializer)[self.action == 'list']


class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    
    
class BoxesViewSet(viewsets.ModelViewSet):
    queryset = Boxes.objects.all()
    serializer_class = BoxesSerializer


def home_view(request):
    template_name = 'home.html'

    pages = {
        'Admin': reverse('admin:index'),
        'API': reverse('books-list'),
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)
