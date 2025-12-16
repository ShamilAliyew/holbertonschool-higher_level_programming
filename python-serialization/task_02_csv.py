import csv
import json

def convert_csv_to_json(csv_file):
    data = []
    with open(csv_file, "r") as f:
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            data.append(row)

    try:
        with open("data.json", "w") as json_file:
            json.dump(data, json_file)
        return True
    except Exception as ex:
        print(f"file not found: {ex}")
        return False