import requests

def downloadfile(file):
    res = requests.get(f'https://data.gharchive.org/{file}')
    return res

# res = downloadfile('2021-01-29-0.json.gz')

# print(res.status_code)