import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE
AWS_ACCESS_KEY_ID = 'AKIAJ62QW2AMWR2A3RDA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'kyltti'
STATIC_URL = '//%s.s3-website-eu-west-1.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
