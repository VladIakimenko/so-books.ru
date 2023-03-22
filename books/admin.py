from django.contrib import admin
from books.models import Books, Photos, Boxes


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ('name', 'author', 'box')
    fields = ('author', 'name', 'made_in', 'year', 'box')
    ordering = ('name',)
    
    def get_queryset(self, request):
        return Books.objects.select_related("box").all()    


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('book',)
    fields = ('book', 'photo',)
    ordering = ('book',)

    def get_queryset(self, request):
        return Photos.objects.select_related("book").all()
        
          
@admin.register(Boxes)
class BoxesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name', 'description',)
    ordering = ('name',)
