FROM python:3.10

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv

RUN pipenv install
    
COPY . /app/

EXPOSE 8000

CMD if [ "$DEBUG" = "False" ]; then \
        pipenv run python manage.py migrate && \
        pipenv run python manage.py loaddata books/fixtures/data.json && \
        pipenv run python manage.py collectstatic --noinput && \
        pipenv run gunicorn hermes.wsgi:application --bind 0.0.0.0:8000 --workers 3 --log-level=info --access-logfile=/var/log/access.log --error-logfile=/var/log/error.log && \
        rm /app/fixtures/data.json; \
    else \
        pipenv run python manage.py migrate && \
        pipenv run python manage.py loaddata books/fixtures/data.json && \
        pipenv run python manage.py collectstatic --noinput && \
        pipenv run python manage.py runserver 0.0.0.0:8000 && \
        rm /app/fixtures/data.json; \
    fi
    
