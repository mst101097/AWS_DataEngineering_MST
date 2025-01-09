Let us develop the download functionality using requests and validate locally. We will understand how to integrate 3rd party libraries as part of the next topic using requests as an example.

Develop the base functionality to download the zip file using requests library. I have created a new program called download.py for this.

import requests
 
def download_file(file):
  res = requests.get(f'https://data.gharchive.org/{file}')
  return res
Refactor the code as part of lambda_function.py to invoke the new function and also to capture the response.

import json
from download import download_file
 
def lambda_handler(event, context):
  download_res = download_file('2021-01-29-0.json.gz')
  return {
    'statusCode': download_res.status_code,
    'body': json.dumps('Download status code')
  }