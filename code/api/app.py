import sys
from flask import Flask
from flask import jsonify
from flask_restful import Api
from flask_restful import Resource, reqparse
from sklearn.externals import joblib

import machine_learning as ml


app = Flask(__name__)
api = Api(app)



class Predict(Resource):

    def get(self):
        post_parser = reqparse.RequestParser()

        post_parser.add_argument(
            'body_length', type=float)
        post_parser.add_argument(
            'channels', type = float)
        post_parser.add_argument(
            'fb_published', type=float)
        post_parser.add_argument(
            'name_length', type=float)
        post_parser.add_argument(
            'num_order', type=float)
        post_parser.add_argument(
            'num_payouts', type=float)
        post_parser.add_argument(
            'org_facebook', type=float)
        post_parser.add_argument(
            'org_twitter', type=float)
        post_parser.add_argument(
            'user_age', type=float)
        post_parser.add_argument(
            'user_type', type=float)

        args = post_parser.parse_args()


        output = ml.get_random_forest_predict(model, args)

        if output:
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
    model = joblib.load('filename.pkl')
    if len(sys.argv) > 1:
        host = sys.argv[1]
        port = int(sys.argv[2])
    else:
        host = None
        port = None

    app.run(host=host, port=port, debug=False)
