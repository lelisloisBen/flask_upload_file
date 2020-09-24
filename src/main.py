from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from utils import APIException
from werkzeug.utils import secure_filename
from helpers import *

app = Flask(__name__)
app.config.from_object("config")
app.config['CORS_HEADERS'] = 'Content-Type'

myOrigin = "https://samir-upload-to-s3.herokuapp.com/"

cors = CORS(app, resources={r"/upload/*": {"origins": myOrigin }}) 

# CORS(app)

# app.config.from_object("flask_s3_upload.config")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def hello_world():
    return "<div style='text-align: center; background-color: orange'><h1>Backend running...</h1><br/><h3>Welcome back samir</h3><img src='https://media.gettyimages.com/photos/woman-sitting-by-washing-machine-picture-id117852649?s=2048x2048' width='80%' /></div>"



@app.route("/upload", methods=["POST"])
@cross_origin(origin=myOrigin,headers=['Content-Type','Authorization'])
def upload_file():

    body = request.get_json()

    file = body["the_file"]
	
    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)

    if file.name == "":
        return jsonify({
                'received': 'nope its empty',
                'msg': 'Please select a file'
            })

    if file and allowed_file(file.name):
        file.name = secure_filename(file.name)
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


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)