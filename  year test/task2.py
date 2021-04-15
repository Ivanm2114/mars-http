import json
import csv

with open('magic_help.json') as f:
    data = json.load(f)
print(data)
with open('hide_and_seek.csv', 'w', newline='') as f:
    writer = csv.DictWriter(
        f, fieldnames=list(data[0].keys()),
        delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for d in sorted(data, key=lambda x:x['creature'], reverse=True):
        if d['hide'] > 10:
            writer.writerow(d)
