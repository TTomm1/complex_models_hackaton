import sys
from flask import Flask
from flask import jsonify
from flask_restful import Api
from flask_restful import Resource, reqparse


app = Flask(__name__)
api = Api(app)



class Predict(Resource):

    def get(self):
        post_parser = reqparse.RequestParser()
        post_parser
        post_parser.add_argument(
            'user_age', type=int)
        post_parser.add_argument(
            'sample_uuid')

        args = post_parser.parse_args()
        if args.user_age<400:
            label=1.
        else:
            label=0.

        result = {
            'probability': 1.,
            'label': label,
            'sample_uuid': args.sample_uuid
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
