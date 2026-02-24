import json
import csv

contents = open("people.csv").readlines()
print(json.dumps(list(csv.reader(contents))))