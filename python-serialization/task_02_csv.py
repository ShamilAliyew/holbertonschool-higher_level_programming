import csv
import json
import os.path


def convert_csv_to_json(csv_file):
    if not os.path.exists(csv_file):
        raise FileNotFoundError("file not found")
    with open(csv_file, newline="") as f:
        read = csv.DictReader(f)
        data = list(read)

    try:
        with open("data.json", "w") as json_file:
            json.dump(data, json_file)
        return True
    except Exception as ex:
        print(f"file not found: {ex}")
        return False