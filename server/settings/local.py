from .base import *
from .base import env

env.read_env(str(ROOT_DIR.path(".env")))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o(+wd&x@mzhkgohsw$b36#!d&*gaei39=a@ch^uq9@-25faoz%'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD':env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': 10,
        'OPTIONS': {
            'init_command': 'SET CHARACTER SET utf8mb4',
            'charset': 'utf8mb4',
        }
    }

}
# CACHE

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # Mimicing memcache behavior.
            # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
            "IGNORE_EXCEPTIONS": True,
        },
    }
}
