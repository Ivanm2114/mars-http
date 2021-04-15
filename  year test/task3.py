import json
import csv
import requests


def horklump(address, port, **kwargs):
    response = requests.get(f'http://{address}:{port}')
    f = response.json()
    if kwargs['place'] in f:
        data = {}
        for key in kwargs.keys():
            if key != 'place':
                data[key] = kwargs[key]
        f[kwargs['place']].append(data)
    else:
        data = {}
        for key in kwargs.keys():
            if key != 'place':
                data[key] = kwargs[key]
        f[kwargs['place']] = [data]
    return f


print(horklump('127.0.0.1', 5000, place='France', weight=13, count=3))
print(horklump('127.0.0.1', 8080, place='England', color='blue', magic='high'))
