import argparse
import csv
import json

from flask import Flask

parser = argparse.ArgumentParser()
parser.add_argument('--server', type=str)
parser.add_argument('--port', type=str)
parser.add_argument('--filename', type=str)
args = parser.parse_args()
app = Flask(__name__)

d = {'doxy': [], 'fairy': []}
with open(a, encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=':')
    for el in reader:
        print(el['number of pair hands'])
        if int(el['presence of wool']) == 1 or int(el['number of pair hands']) > 1 or int(
                el['number of pair legs']) > 1:
            d['doxy'].append([el['color'], int(el['size'])])
        else:
            d['fairy'].append([el['color'], int(el['size'])])
for el in d:
    d[el].sort(key=lambda x: (x[0], x[1]))


@app.route('/fairy')
def f():
    return json.dumps(d)


app.run(port=args.port, host=args.server)
#
# app.run(port='8080', host='127.0.0.1')
