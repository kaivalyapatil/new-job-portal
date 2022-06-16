from flask import Flask, jsonify, make_response, request
from apis import job_api
app=Flask(__name__)

@app.before_request
def before():                                                                                   
    print(f"Request is received in {request.method}-{request.url}")

# @app.route('/test',methods=['GET'])
# def test():
#     return jsonify({'message':'welcome to job portal'})

@app.errorhandler(500)
def handle_500_error(_error):
    return make_response(jsonify({"error":"server error"}),500)

app.register_blueprint(job_api.get_blueprint())



# start the application 

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)