from rest_framework import serializers

from books.models import Books, Photos, Boxes


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ["author", "name", "box", "made_in", "year"]


class PhotosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photos
        fields = ["book", "photo"]


class BoxesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boxes
        fields = ["name", "description"]
        
