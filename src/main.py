from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from utils import APIException
from werkzeug.utils import secure_filename
from helpers import *
from PIL import Image
from io import BytesIO  

app = Flask(__name__)
app.config.from_object("config")

CORS(app)

# app.config.from_object("flask_s3_upload.config")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def hello_world():
    return "<div style='text-align: center; background-color: orange'><h1>Backend running...</h1><br/><h3>Welcome back samir</h3><img src='https://media.gettyimages.com/photos/woman-sitting-by-washing-machine-picture-id117852649?s=2048x2048' width='80%' /></div>"



@app.route("/upload", methods=['POST','PUT'])
def upload_file():

    # body = request.get_json()

    # file = body["the_file"]
    file = request.files['the_file']

    # return str(file.filename)
	
    if file is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)

    if file.filename == "":
        return jsonify({
                'received': 'nope its empty',
                'msg': 'Please select a file'
            })

    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        output   	  = upload_file_to_s3(file, app.config["S3_BUCKET"])
        return jsonify({
                'received': 'uploaded successfuly',
                'msg': str(output)
            })

    else:
        return jsonify({
                'received': 'upload failed',
                'msg': 'not upoladed, something is wrong!'
            })

@app.route("/multi", methods=['PUT'])
def multi_upload_files():

    files = request.files.getlist('files[]')

    # myList = []

    # for i in files:
    #     myList.append(i.filename)
    
    # return jsonify({
    #     "seemylist": myList
    # })



    if files is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)

    jobDone = []

    for file in files:

        if file.filename == "":
            return jsonify({
                    'received': 'nope its empty',
                    'msg': 'Please select a file'
                })

        if file and allowed_file(file.filename):
            file.filename = secure_filename(file.filename)
            
            output = upload_file_to_s3(file, app.config["S3_BUCKET"])

            jobDone.append(str(output))
            
            # return jsonify({
            #         'received': 'uploaded successfuly',
            #         'msg': output
            #     })
        else:
            return jsonify({
                    'received': 'upload failed',
                    'msg': 'not upoladed, something is wrong!'
                })

    return jsonify({
            'received': 'uploaded successfuly',
            'msg': jobDone
        })

@app.route("/resize", methods=['PUT'])
def resize_uploaded_img():

    file = request.files['fileToResize']
	
    if file is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)

    # image = Image.open(file)

    # image.thumbnail((500, 1000))
    # image.save("newFile.jpg")
    # ///
    # image = Image.open(file.filename)
    # image_io = BytesIO()
    # image.thumbnail((500, 1000))
    # image.save(image_io, 'jpeg')
    # ////
    # image = Image.fromarray(file, mode=None)
    # image.thumbnail((500, 1000))
    # ///
    # image = Image.open(file)
    # img_io = BytesIO()
    # image.save(img_io, 'JPEG', quality=70)
    # img_io.seek(0)
    # return send_file(img_io, mimetype='image/jpeg')
    # image = Image.open(file.stream.read())
    # image_bytes = BytesIO(file.stream.read())
    myImage = file.read()
    print("from the stream: ",myImage)
    img = Image.open(BytesIO(myImage))
    print("the byte: ",img)
    img.thumbnail((500, 1000))
    print("after resizing: ", img)
    img.seek(0)
    print("after seek: ", img)

    return str(img)

    # output = upload_file_to_s3(img, app.config["S3_BUCKET"])
    # return jsonify({
    #         'received': 'uploaded successfuly',
    #         'msg': str(output)
    #     })

    # return jsonify({
    #     "myImageFormat": image.format,
    #     "myImageSize": image.size,
    #     "myImage": image.filename
    # })
    
    # response = s3.Object('my-bucket', asset.s3_key()).put(Body=image_bytes)
    # upload to S3

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)