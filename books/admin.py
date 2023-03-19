from django.contrib import admin
from books.models import Books, Photos


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display_links = ('name',)
    list_display = ('name', 'author',)
    fields = ('author', 'name', 'made_in', 'year', 'management',)
    ordering = ('name',)


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('book',)
    fields = ('book', 'photo',)
    ordering = ('book',)

    def get_queryset(self, request):
        return Photos.objects.select_related("book").all()
