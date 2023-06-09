from django.db import models


def directory_path(instance, filename):
    return f'books/{instance.book.id}/{filename}'


class Boxes(models.Model):
    name = models.CharField(verbose_name="Название коробки", max_length=64)
    description = models.CharField(verbose_name="Описание содержимого коробки", blank=True, max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Коробку"
        verbose_name_plural = "Коробки"


class Books(models.Model):
    author = models.CharField(verbose_name="Автор", max_length=128)
    name = models.CharField(verbose_name="Название книги", max_length=128)
    made_in = models.CharField(verbose_name="Издательство", max_length=64)
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    box = models.ForeignKey(Boxes, on_delete=models.SET_NULL, null=True, verbose_name="Коробка")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"


class Photos(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="Книга")
    photo = models.ImageField(verbose_name="Картинка книги", upload_to=directory_path)

    def __str__(self):
        return self.book.name

    class Meta:
        ordering = ["book"]
        verbose_name = "Фотографию книги"
        verbose_name_plural = "Фотографии книг"
