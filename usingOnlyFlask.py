from flask import Flask, jsonify, request

# creating a flask app
app = Flask(__name__)

# get or post method
@app.route('/', methods=['GET', 'POST'])
def home():
    # data='GoodBye'
    result={
        "message":"using POST method"
    }
    if(request.method=='GET'):
        # data = "Hello world"
        result={
            "message":"using GET method"
        }
    return jsonify(result)


# sqaure value
@app.route('/home/<int:num>',methods=['GET'])
def disp(num):
    result={
        'sqaure value':num**2
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)