Here are the steps using which we can set up a project. We will use this project to download the GitHub Activity files in incremental fashion.

Create folder for the project - ghactivity-downloader

Create virtual environment for this project - ghad-venv

python3 -m venv ghad-venv
source ghad-venv/bin/activate
We will install boto3 in the default location within the virtual environment. We need not include it as part of the bundle that will be deployed as a lambda function.

pip install boto3
pip install requests
We will install requests as part of lambdalib folder. It will be included as part of the bundle that will be deployed as a lambda function.

mkdir ghalib
pip install requests -t ghalib
We can create lambda_function.py with the default code we got when we get started.

import json
 
def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda using gha downloader!')
    }
We will create an additional file lambda_validate.py and have this piece of code so that we can run locally.

from lambda_function import lambda_handler
 
res = lambda_handler(None, None)
print(res)
We can run lambda_validate to validate locally.

python lambda_validate.py