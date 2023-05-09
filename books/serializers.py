from rest_framework import serializers

from books.models import Books, Photos, Boxes


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Books
        fields = ["author", "name", "made_in", "year", "box"]


class BooksListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk')
    box_name = serializers.CharField(source='box.name')

    class Meta:
        model = Books
        fields = ["id", "author", "name", "made_in", "year", "box_name"]


class PhotosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photos
        fields = ["book", "photo"]


class BoxesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boxes
        fields = ["name", "description"]
        
