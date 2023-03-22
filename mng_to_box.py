#!/usr/bin/env python
import os
import subprocess

import django
from django.db import connection

from logger import email_log

TABLE = 'books_books'
DATA = 'books/fixtures/Books&Boxes.json'


@email_log
def migrate():
    subprocess.run(["python", "manage.py", "migrate"])

@email_log
def delete_records(table):
    Books.objects.all().delete()

@email_log
def load_data(data):
    subprocess.run(["python", "manage.py", "loaddata", f"{data}"])

@email_log
def check_table(table):
    return Books.objects.all()


def repopulate():
    migrate()
    delete_records(TABLE)
    load_data(DATA)
    check_table(TABLE)
    
    
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hermes.settings')
    django.setup()
    from books.models import Books
    
    repopulate()
