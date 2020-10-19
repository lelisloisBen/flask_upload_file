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

# MAIL_SERVER = 'smtp.gmail.com'
DEBUG = True
MAIL_SERVER = 'smtp-relay.gmail.com'
MAIL_PORT = 25
DEFAULT_SENDER = os.environ.get("EMAIL_USERNAME")
MAIL_USERNAME = os.environ.get("EMAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("EMAIL_PASS")
MAIL_USE_TLS = True
MAIL_USE_SSL = False
EMAILS_USE_SMTP = True

SECRET_KEY = os.urandom(32)
DEBUG = True
PORT = 5000