from rest_framework import serializers

from books.models import Books, Photos, Boxes


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    box_name = serializers.SerializerMethodField()
    id = serializers.IntegerField(source='pk', read_only=True)
    box = serializers.PrimaryKeyRelatedField(queryset=Boxes.objects.all(), write_only=True)
    
    class Meta:
        model = Books
        fields = ["id", "author", "name", "made_in", "year", "box", "box_name"]
        
    def get_box_name(self, obj):
        return obj.box.name if obj.box else None


class PhotosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photos
        fields = ["book", "photo"]


class BoxesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boxes
        fields = ["name", "description"]
        
