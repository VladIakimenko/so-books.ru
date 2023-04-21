from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from books.views import BooksViewSet, PhotosViewSet, BoxesViewSet
from books.views import home_view


router = routers.DefaultRouter()
router.register('books', BooksViewSet, basename="books")
router.register('photos', PhotosViewSet, basename="photos")
router.register('boxes', BoxesViewSet, basename="boxes")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home_view, name="home"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

