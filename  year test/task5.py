import csv

from flask import Flask, request, render_template
from flask import url_for
import argparse
import sys

import json
from random import choice

# parser = argparse.ArgumentParser()
# parser.add_argument('--server', type=str)
# parser.add_argument('--port', type=str)
# parser.add_argument('--file', type=str)
# args = parser.parse_args()
#
app = Flask(__name__)


@app.route('/')
def f():
    d = {}
    with open('crabs.csv', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
        for el in reader:
            if el['color'] in d:
                d[el['color']].append([el['size'], el['shell thickness']])
            else:
                d[el['color']] = [[el['size'], el['shell thickness']]]
            d[el['color']].sort(key=lambda x: x[0])
            print(d)
    return d


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
