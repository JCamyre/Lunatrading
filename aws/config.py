import os 
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage




AWS_USERNAME = os.environ.get('AWS_USERNAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_ACL = None
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True



DEFAULT_FILE_STORAGE = 'aws.utils.MediaRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'lunatrading-static' # os.environ.get('BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN')



S3DIRECT_REGION = 'us-west-1'

S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

# maybe have to do /static/media
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME

MEDIA_ROOT = MEDIA_URL

STATICFILES_LOCATION = 'static'
STATIC_URL = '//%s/%s/' % (AWS_S3_CUSTOM_DOMAIN,
STATICFILES_LOCATION)

class StaticStorage(S3Boto3Storage):
    location = STATICFILES_LOCATION

    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = AWS_S3_CUSTOM_DOMAIN
        super(StaticStorage, self).__init__(*args, **kwargs)

# STATIC_URL = S3_URL + 'static/'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


AWS_HEADERS = {
'Cache-Control': 'max-age=86400',
}

