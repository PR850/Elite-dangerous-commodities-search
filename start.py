import download_files
import data_prep
import search_station_name
import tqdm
import time

print("Welcome to Elite Dangerous Commodities Search")
choice = input(
    "Do you want to update all data? \n It will take a few minutes (yes/no): ")

if choice == 'yes':

    pbar = tqdm.tqdm([
        download_files.update_all_data(),
        data_prep.convert_necessary_data_from_json_to_csv()
    ])

    for dwn in pbar:
        pbar.set_description("Preparing Data... %s")
        time.sleep(0.25)

commodity = input("Choose commodity (f.e Meta-Alloys or Explosives): ")

search_station_name.find_system_name(
    search_station_name.find_stations_ids(commodity))

print("This is test version, all stations wanted commodieties appeard in 'systems_sought_without_length.csv' ")
