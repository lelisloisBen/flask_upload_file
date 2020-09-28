import os

S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
S3_KEY = os.environ.get("S3_ACCESS_KEY")
S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
MYSQL_HOSTNAME = os.environ.get("HOST_MYSQL")
MYSQL_USERNAME = os.environ.get("USER_MYSQL")
MYSQL_PASS = os.environ.get("PASS_MYSQL")
MYSQL_DATABASE = os.environ.get("DATABASE_MYSQL")

SECRET_KEY = os.urandom(32)
DEBUG = True
PORT = 5000