
from flask import Flask, render_template, request
import boto3
import os
app = Flask(__name__)
from werkzeug.utils import secure_filename
from secret import access_key,secret_access_key 
s3 = boto3.client('s3',
                    aws_access_key_id=access_key,
                    aws_secret_access_key= secret_access_key,
                    )

BUCKET_NAME='assignmentdevops2'

@app.route('/')  
def home():
    return render_template("file_upload_to_s3.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key= filename
                )
                msg = "Upload Done ! "

    return render_template("file_upload_to_s3.html",msg =msg)




if __name__ == "__main__":
    
    app.run(debug=True)


