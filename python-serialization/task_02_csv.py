import csv
import json

def convert_csv_to_json(csv_file):
    with open(csv_file, newline="") as f:
        read = csv.DictReader(csv_file)
        data = list(read)

    try:
        with open("data.json", "w") as json_file:
            json.dump(data, json_file)
        return True
    except Exception as ex:
        print(f"file not found: {ex}")
        return False