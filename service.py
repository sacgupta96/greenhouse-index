from flask import Flask ,jsonify
from flask_restful import Api, Resource, reqparse
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)

class GasData(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('country', required=True)
        args = parser.parse_args()

        data = pd.read_csv('output.csv')

        df = data.loc[data['country'] == args['country']]
        df1 = df.dropna(axis=1)
        del df1['country']

        resultjson = {}
        gaslist = list(df1.columns.values)[1:]
        for gas in gaslist:
            node = {}
            for index,row in df1.iterrows():
                node[int(row['year'])] = row[gas]
            resultjson[gas] = node
        return resultjson
    
class Country(Resource):

    def get(self):
        data = pd.read_csv('output.csv')
        return { 'countryList': sorted(list(set(data['country'].tolist())))}

# Add URL endpoints
api.add_resource(GasData, '/gasData')
api.add_resource(Country, '/countries')

if __name__ == '__main__':
    app.run(debug=True)