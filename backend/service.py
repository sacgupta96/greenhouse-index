from flask import Flask ,jsonify
from flask_restful import Api, Resource, reqparse
import pandas as pd
import json
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

api = Api(app)

# Global Variables
COUNTRY = 'country'
OUTPUTCSV = 'output.csv'
YEAR = 'year'

"""
This class process the dataset of gases
"""

class GasData(Resource):
    """
    This method process dataset of gases for a particular country
    Param : country(string)
    Response : json of dictionary of year to value map
    """
    def post(self):
        # Get the argument from the request
        parser = reqparse.RequestParser()
        parser.add_argument(COUNTRY, required=True)
        args = parser.parse_args()

        data = pd.read_csv(OUTPUTCSV)

        # Get the data for a selected country , remove the null column and country column
        df = data.loc[data[COUNTRY] == args[COUNTRY]]
        df1 = df.dropna(axis=1)
        del df1[COUNTRY]

        # manipulate the data format
        resultjson = {}
        gaslist = list(df1.columns.values)[1:]
        for gas in gaslist:
            node = {}
            for index,row in df1.iterrows():
                node[int(row[YEAR])] = row[gas]
            resultjson[gas] = node
        return resultjson


"""
This class process list of country
"""
class Country(Resource):
    """
    This method process list of country
    Response : json of list of country
    """
    def get(self):
        data = pd.read_csv(OUTPUTCSV)
        return { 'countryList': sorted(list(set(data[COUNTRY].tolist())))}

# Add URL endpoints
api.add_resource(GasData, '/gasData')
api.add_resource(Country, '/countries')

if __name__ == '__main__':
    app.run()