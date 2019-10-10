from Lecture2.flakontest.calcbp import calc
from flask import Flask, jsonify, request


app = Flask(__name__)
# app.register_blueprint(calc)
app.register_blueprint(calc)


@app.route('/api/person/<person_id>', methods=['GET'])
def person(person_id):
    print(request)
    response = jsonify({'Hello': person_id})
    return response


if __name__ == '__main__':
    app.run(debug=True)