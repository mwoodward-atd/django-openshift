from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('database_name'),
        'USER': os.getenv('username'),
        'PASSWORD': os.getenv('password'),
        'HOST': os.getenv('database_service_name'),
        'PORT': 5432,
    }
}
