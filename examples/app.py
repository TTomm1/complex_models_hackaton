import numpy as np
import sys
from flask import Flask
from flask import jsonify
from flask_restful import Api
from flask_restful import Resource, reqparse


app = Flask(__name__)
api = Api(app)

post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'user_age')

args = post_parser.parse_args()

print args.head(3)


class Predict(Resource):

    def get(self, args):
        r = np.random.rand()
        result = {
            'probability': r,
            'label': float(r > 0.5),
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
