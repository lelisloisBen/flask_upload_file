import os

S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
S3_KEY = os.environ.get("S3_ACCESS_KEY")
S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

MYSQL_HOST = os.environ.get("HOST_MYSQL")
MYSQL_USER = os.environ.get("USER_MYSQL")
MYSQL_PASSWORD = os.environ.get("PASS_MYSQL")
MYSQL_DB = os.environ.get("DATABASE_MYSQL")
MYSQL_CURSORCLASS = "DictCursor"

SECRET_KEY = os.urandom(32)
DEBUG = True
PORT = 5000