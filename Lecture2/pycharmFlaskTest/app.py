from flask import Flask, jsonify, request

from Lecture2.pycharmFlaskTest.teamsblueprint import teams

app = Flask(__name__)
app.register_blueprint(teams)


@app.route('/')
def hello_world():
    return 'Hello World!'


# methods ti da la lista di metodi che accetta quell'endpoint
# => try to use PUSH methods => will fail:
#                                               curl -v -X PUSH  http://127.0.0.1:5000/api
@app.route('/api', methods=['POST', 'DELETE', 'GET'])
def my_microservice():
    print(request)
    response = jsonify({'Hello': 'Word'})
    return response


@app.route('/api/person/<person_id>', methods=['GET'])
def person(person_id):
    print(request)
    response = jsonify({'Hello': person_id})
    return response


if __name__ == '__main__':
    app.run(debug=True)
