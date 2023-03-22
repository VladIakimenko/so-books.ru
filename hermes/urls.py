from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from books.views import BooksViewSet, PhotosViewSet, BoxesViewSet

router = routers.DefaultRouter()
router.register(r'books', BooksViewSet)
router.register(r'photos', PhotosViewSet)
router.register(r'boxes', BoxesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

