import json
import csv

with open('trouble.json') as f:
    data = json.load(f)
with open('advices.csv', 'w', newline='') as f:
    writer = csv.DictWriter(
        f, fieldnames=list(data[0].keys()),
        delimiter=',')
    writer.writeheader()
    for d in sorted(data, key=lambda x: x['name']):
        if d['self'] != d['advice']:
            writer.writerow(d)
