from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# creating the flask app
app = Flask(__name__)

# creating api object 
api = Api(app)
# restful class hello
# making class for particular resource 
class Hello(Resource):
    # the get, post methods correspond to get and post request 
    # they are automatically mapped by flask_restful
    # other methods include put, delete, etc

    # corresponds to GET request this function is called whenever there is a GET request for this resource 
    def get(self):
        return jsonify({"message":"Hello world"})

    def post(self):
        data = request.get_json()
        # print(data)
        return jsonify({"data":data})

# restful api of sqaure class
class Square(Resource):
    def get(self,num):
        return jsonify({"square":num**2})


# adding the defined resource along with their corresponding urls
api.add_resource(Hello,'/')
api.add_resource(Square,'/square/<int:num>')


if __name__ == '__main__':
    app.run(debug=True)