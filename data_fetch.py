import requests
import json

# 25544 is ISS
URL = 'https://network.satnogs.org/api/observations/?id=&status=&ground_station=&start=&end=&satellite__norad_cat_id=&transmitter_uuid=ZJxCeQmih9zDfYNVrB4wRN&transmitter_mode=&transmitter_type=&waterfall_status=&vetted_status=&vetted_user=&observer=&start__lt=&observation_id='
result = requests.get(URL)
pertinent_data = {}
for i in range(len(result.json())):
    if result.json()[i]["vetted_datetime"] is not None:
        pertinent_data[i] = {}
        pertinent_data[i]["norad_cat_id"] = result.json()[i]["norad_cat_id"]
        pertinent_data[i]["vetted_datetime"] = result.json()[i]["vetted_datetime"]
print(json.dumps(pertinent_data, indent=4))