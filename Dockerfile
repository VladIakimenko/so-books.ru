FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV DJANGO_SETTINGS_MODULE=hermes.settings

RUN pip install python-dotenv && \
    python -c "from dotenv import load_dotenv; load_dotenv()"
    
ENV SECRET_KEY=$SECRET_KEY
ENV NAME=$NAME
ENV USER=$USER
ENV PASSWORD=$PASSWORD
ENV HOST=$HOST
ENV PORT=$PORT

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
