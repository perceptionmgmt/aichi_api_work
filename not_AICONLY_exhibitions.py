import requests
import json
import glob

# this file loops through exhibition JSON data
# if type does not equal "AIC Only" it writes out data to "not_AICONLY_exhibitions.json"

# api_endpoint = "https://api.artic.edu/api/v1/exhibitions"
# r = requests.get(api_endpoint)

#path to json files:
# artic-api-data/json/*.json

traveling_exhib_count = 0
for filename in glob.glob("exhibitions/*.json"):
    # print(filename)
    with open(filename, "r") as jsonfiles:
        data = json.load(jsonfiles)

        if data["type"] != "AIC Only":
            print(data)

            with open("not_AICONLY_exhibitions.json", "a") as out:
                json.dump(data, out, indent=2)

        # if data["type"] == "AIC & Other Venues":
        # if data["type"] == "Mini Exhibition":
        # if data["type"] == "Permanent Collection Special Project":
        # if data["type"] == "AIC Only":
        # if data["type"] == "Rotation":
        # if data["type"] != "AIC Only":
            # traveling_exhib_count+=1
            # print(data)
            # print(traveling_exhib)
