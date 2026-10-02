import json
import os

#Define load_inventory()
def load_inventory(filename):
    if os.path.exists(filename):
        try:
            with open(filename,"r") as file:
                records = json.load(file)
        except json.JSONDecodeError:
            records = []
    else:
        with open(filename,"w") as file:
            records = []
    return records