import json
import csv
import requests


def hippogriff(port, host, **kwargs):
    response = requests.get(f'http://{host}:{port}')
    f = response.json()
    for el in kwargs:
        if el in f:
            f[el] = max(f[el], kwargs[el])
        else:
            f[el] = kwargs[el]

    return f



