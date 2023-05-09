import os
import shutil

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.core.files.storage import default_storage

from books.models import Boxes, Books, Photos

class EndpointsTestCase(APITestCase):
    boxes_url = reverse('boxes-list')
    books_url = reverse('books-list')
    photos_url = reverse('photos-list')
    test_photo_path = os.path.join('books', 'tests', 'test_image.jpg')
    media_path = os.path.join(settings.MEDIA_ROOT, 'tests_media')
    os.makedirs(media_path, exist_ok=True)
    settings.MEDIA_ROOT = media_path
    

    def setUp(self):
        self.box_data = {'name': 'Test Box'}
        box = Boxes.objects.create(**self.box_data)
        
        self.book_data = {
            'author': 'Test Author',
            'name': 'Test Book',
            'made_in': 'Test Publisher',
            'year': 2023,
            'box': box
        }
        book = Books.objects.create(**self.book_data)
        self.book_data['box'] = reverse('boxes-detail', args=[box.id])
        
        test_photo = SimpleUploadedFile(name='test_image.jpg', content=open(self.test_photo_path, 'rb').read(), content_type='image/jpeg')
        self.photo_data = {
            'book': reverse('books-detail', args=[book.id]),
            'photo': test_photo
        }
        

    def test_box(self):
        count = Boxes.objects.count()
        response = self.client.post(self.boxes_url, self.box_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
       
        response = self.client.get(self.boxes_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], count + 1)
        self.assertEqual(response.data['results'][0]['name'], 'Test Box')

    def test_book(self):
        count = Books.objects.count()
        response = self.client.post(self.books_url, self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(self.books_url)     
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], count + 1)
        self.assertEqual(response.data['results'][0]['name'], 'Test Book')
        self.assertEqual(response.data['results'][0]['box_name'], 'Test Box')
        
    def test_photo(self):
        count = Photos.objects.count()
        response = self.client.post(self.photos_url, self.photo_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        response = self.client.get(self.photos_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], count + 1)
        
        filepath = str(response.data['results'][0]['photo']).rpartition('media/')[-1]
        with default_storage.open(filepath, 'rb') as f:
            test_image = f.read()
        with open(self.test_photo_path, 'rb') as f:
            target_image = f.read()
        self.assertEqual(test_image, target_image)
        
        self.assertIn(self.photo_data['book'], response.data['results'][0]['book'])
        
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.media_path)
        
        
        
        
