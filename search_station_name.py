import pandas
import json


def find_stations_ids(item_name):

    listings = pandas.read_csv('./data/listings.csv')
    with open('./jsons/commodities.json', 'r') as f:
        commodities = json.load(f)

    item_id = ''
    for c in commodities:
        if (c.get('name') == item_name):
            item_id = c.get('id')

    stations = listings.loc[(listings['commodity_id']
                             == item_id) & (listings['supply'] > 0)]

    return stations[['station_id']]


def find_system_name(station_id):
    stations = pandas.read_csv('./data/stations.csv')
    systems = pandas.read_csv('./data/systems_populated.csv')

    station_id.rename(columns={'station_id': 'id'}, inplace=True)
    station_id.reset_index(drop=True)
    stations = pandas.merge(stations, station_id, on=['id'], how='inner')
    stations = stations.drop(columns='id')

    stations.rename(columns={'system_id': 'id',
                             'name': 'station_name'}, inplace=True)
    systems.rename(columns={'name': 'system_name'}, inplace=True)

    systems = pandas.merge(systems, stations, on=['id'], how='inner')
    systems = systems.drop(columns='id')

    systems.to_csv('./data/systems_sought_without_length.csv', index=False)


#station_ids = find_stations_ids('Explosives')
# find_system_name(station_ids)
