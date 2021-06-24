from flask import Flask, json
from flask_restful import Resource, Api
from flask.ext.jsonpify import jsonify
import random

app = Flask(__name__)
#api = Api(app)


BusinessFeedsTable = ({"id": 1, "headline": "Company One headline"},
        {"id": 2, "headline": "Company Two headline"},
        {"id": 3, "headline": "Company Three headline"},
        {"id": 4, "headline": "Company Four headline"},
        {"id": 5, "headline": "Company Five headline"},
        {"id": 6, "headline": "Company Six headline"},
        {"id": 7, "headline": "Company Seven headline"},
        {"id": 8, "headline": "Company Eight headline"},
        {"id": 9, "headline": "Company Nine headline"},
        {"id": 10, "headline": "Company Ten headline"})

def random_business_feed():
    rand_int = random.randint(0,len(BusinessFeedsTable) - 1)
    #print(type(BusinessFeedsTable[rand_int]))
    return BusinessFeedsTable[rand_int]


class BusinessFeed(Resurce):
    def get(self):
        return random_business_feed()

api.add_resource(BusinessFeed, '/business_feed') # Route_1 http://localhost:1234/business_feed

#if __name__ == '__main__':
#     app.run(port='1234')
