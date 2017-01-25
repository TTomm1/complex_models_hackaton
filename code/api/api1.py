"""
Simple api to serve predictions.
"""
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import json

app = Flask(__name__)
api = Api(app)

# A training process has stored predictions into a
# json file
with open('simple.json') as f:
    PREDICTIONS = json.load(f)

def abort_if_prediction_doesnt_exist(user_id):
    if user_id not in PREDICTIONS:
        abort(404, message="User {} doesn't exist".format(user_id))

class SimpleModel(Resource):
    """
    The resource we want to expose
    """
    def get(self, user_id, user_age):
        abort_if_prediction_doesnt_exist(user_id)
        return PREDICTIONS[user_id, user_age]


api.add_resource(SimpleModel, '/predict/<user_id>')

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5000, debug=True)