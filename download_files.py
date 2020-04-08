import wget
import tqdm
import time
import os
import glob


def clear_jsons():
    to_delete = glob.glob('./jsons/*.json')
    for f in to_delete:
        try:
            os.remove(f)
        except:
            None


def clear_csvs():
    to_delete = glob.glob('./data/*.csv')
    for f in to_delete:
        try:
            os.remove(f)
        except:
            None


def download_jsons(path):
    wget.download(path, './jsons')


def download_csvs(path):
    wget.download(path, './data')


def update_all_data():

    pbar = tqdm.tqdm([

        clear_jsons(),
        clear_csvs(),
        download_jsons('https://eddb.io/archive/v6/systems_populated.json'),
        download_jsons('https://eddb.io/archive/v6/stations.json'),
        download_jsons('https://eddb.io/archive/v6/commodities.json'),
        download_csvs('https://eddb.io/archive/v6/listings.csv')

    ])

    for dwn in pbar:
        pbar.set_description("Downloading universe files... %s")
        time.sleep(0.25)


# update_all_data()
