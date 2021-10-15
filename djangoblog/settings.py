TIME_ZONE = "Europe/Berlin"

LANGUAGE_CODE ="ru-ru"

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ALLOWED_HOSTS = ['127.0.0.1', 'pythonanywhere.com']

DATBASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
}

	

