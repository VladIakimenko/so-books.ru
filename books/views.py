from rest_framework import viewsets
from books.models import Books, Photos, Boxes
from books.serializers import BooksSerializer, PhotosSerializer, BoxesSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = PhotosSerializer
    
    
class BoxesViewSet(viewsets.ModelViewSet):
    queryset = Boxes.objects.all()
    serializer_class = BoxesSerializer

