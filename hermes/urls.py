from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from books.views import BooksViewSet, PhotosViewSet, BoxesViewSet

router = routers.DefaultRouter()
router.register('books', BooksViewSet, basename="books")
router.register('photos', PhotosViewSet, basename="photos")
router.register('boxes', BoxesViewSet, basename="boxes")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

