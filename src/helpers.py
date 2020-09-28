import boto3, botocore
from config import S3_KEY, S3_SECRET, S3_BUCKET

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

s3 = boto3.client(
   "s3",
   aws_access_key_id=S3_KEY,
   aws_secret_access_key=S3_SECRET
)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file_to_s3(file, bucket_name, folder_name, file_name, myType, acl="public-read"):

    """
    Docs = http://boto3.readthedocs.io/en/latest/guide/s3.html
    Docs S3 = https://stackabuse.com/file-management-with-aws-s3-python-and-flask/
    Docs resize img = https://auth0.com/blog/image-processing-in-python-with-pillow/#:~:text=To%20resize%20an%20image%2C%20you,Image%20with%20the%20new%20dimensions.
    """
    # directory_name = folder_name
    # s3.put_object(Bucket=bucket_name, Key=(directory_name+'/'))
    file_path = folder_name+"/"+file_name

    try:

        s3.upload_fileobj(
            file,
            bucket_name,
            file_path,
            ExtraArgs={
                "ACL": acl,
                "ContentType": myType
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e

    return "{}{}".format('http://{}.s3.amazonaws.com/'.format(S3_BUCKET), file_path)