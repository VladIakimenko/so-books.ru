# Generated by Django 4.1.1 on 2023-03-22 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_boxes_remove_books_management_books_box'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='box',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.boxes', verbose_name='Коробка'),
        ),
    ]