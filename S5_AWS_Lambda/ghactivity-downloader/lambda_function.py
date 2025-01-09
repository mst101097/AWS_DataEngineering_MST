import json
from download_file import downloadfile

def lambda_handler(event, context):
    # TODO implement
    res = downloadfile('2021-01-29-0.json.gz')
    return {
        'statusCode': res.status_code,
        'body': json.dumps('Downloaded successfully!')
    }