import os 

AWS_USERNAME = os.environ.get('AWS_USERNAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_ACL = None
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKET_NAME')

S3DIRECT_REGION = 'us-west-1'

S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME

MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME

MEDIA_ROOT = MEDIA_URL

STATIC_URL = S3_URL + 'static/'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

AWS_HEADERS = {
'Cache-Control': 'max-age=86400',
}

