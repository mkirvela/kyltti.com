import dj_database_url
DEBUG = False
MEDIA_URL = 'http://kyltti.s3.amazonaws.com/'
STATIC_URL = '/static/'
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
