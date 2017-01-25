import sys
from flask import Flask
from flask import jsonify
from flask_restful import Api
from flask_restful import Resource


app = Flask(__name__)
api = Api(app)


class Predict(Resource):

    def get(self):
        result = {
            'probability': 1.,
            'label': 0.,
        }
        return jsonify(**result)


api.add_resource(Predict, '/api/v1/predict')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        host = sys.argv[1]
        port = int(sys.argv[2])
    else:
        host = None
        port = None

    app.run(host=host, port=port, debug=False)
