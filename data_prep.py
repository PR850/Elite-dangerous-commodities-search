import pandas
import math
import json
from pandas.io.json import json_normalize


def convert_necessary_data_from_json_to_csv():

    with open('./jsons/stations.json') as f:
        data = json.load(f)

    prepared = json_normalize(data)
    prepared = prepared[['id', 'system_id', 'name']]
    prepared.to_csv('./data/stations.csv', index=False)

    with open('./jsons/systems_populated.json') as f:
        data = json.load(f)

    prepared = json_normalize(data)
    prepared = prepared[['id', 'name']]
    prepared.to_csv('./data/systems_populated.csv',  index=False)

    prepared = json_normalize(data)
    prepared = prepared[['name', 'x', 'y', 'z']]
    prepared.to_csv('./data/systems_populated_coords.csv',  index=False)
