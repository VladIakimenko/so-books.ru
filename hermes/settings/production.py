DEBUG = False
ALLOWED_HOSTS = ['80.78.246.159', "213.189.201.49", "home-sobolev.ru", "hermes.home-sobolev.ru"]
CSRF_TRUSTED_ORIGINS = ['https://home-sobolev.ru', 'http://home-sobolev.ru',
                        'https://hermes.home-sobolev.ru', 'http://hermes.home-sobolev.ru',
                        'http://80.78.246.159', "http://213.189.201.49"]

CORS_ALLOWED_ORIGINS = [
    'https://home-sobolev.ru', 'http://home-sobolev.ru',
    'https://hermes.home-sobolev.ru', 'http://hermes.home-sobolev.ru',
    'http://80.78.246.159', "http://213.189.201.49",
    'http://localhost:8000', "http://localhost:8080"
]
