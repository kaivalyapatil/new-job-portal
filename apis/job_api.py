from flask import Blueprint,jsonify,make_response, request

from models.candidates import Candidate
from aws.aws_s3 import upload_file
from aws.aws_ses import send_email
from werkzeug.utils import secure_filename
import io


api=Blueprint("job_api",__name__)

arr=[]

def get_blueprint():
    return api

@api.route('/register',methods=['POST'])
def register_candidate():
    # data=request.json
    data=request.form.to_dict()
    file = request.files['file']
    
    candidate=Candidate(
        id=data['id'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        birth_date=data['birth_date'],
        email=data['email'],
        mobile=data['mobile'],
        address=data['address'],
        filename=secure_filename(file.filename)
    )
    arr.append(candidate)
              
    binary_file = io.BytesIO(file.read())    
    upload_file(binary_file,"job-kp",secure_filename(file.filename))

    # send mail
    sub="job protal"
    msg=f"""
        <html>
            <head><title>Job Portal</title></head>
            <body>
                <h3>Hi {candidate.first_name} {candidate.last_name},</h3>
                <p>Your registration is successful. You will get the notifications in the registered emails later.</p>
                <h4>Job Portal Team</h4>
                <h5>Better job opportinities</h5>
            </body>
        </html>
    """

    from_addr=candidate.email
    to_addr="kaivalyapatil0@gmail.com"
    send_email(sub,msg,from_addr,to_addr)
 
    return make_response(jsonify({'message':'welcome to job portal'}),201)


@api.route('/list',methods=["GET"])
def get_candidate():
    return jsonify( [c.serialize() for c in arr] )