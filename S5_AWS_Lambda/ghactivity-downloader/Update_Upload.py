import sys
sys.path.append('C:/Users/52329058/OneDrive - Conduent/Desktop/PythonNotes/DataEngineer/AWS_DataEngineering/AWS_DataEngineering_MST/S5_AWS_Lambda/ghactivity-downloader/ghalib')


import os
import boto3
import requests

# Set AWS environment variables (if not already configured)
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAQXUIX7IUQIMZKCWC'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'

# Initialize S3 client
s3_client = boto3.client('s3', region_name='us-east-1')

# File details
file = '2021-01-29-0.json.gz'
url = f'https://data.gharchive.org/{file}'

try:
    # Fetch the file from the URL
    res = requests.get(url, timeout=60)  # Add timeout for network reliability
    res.raise_for_status()  # Raise an HTTPError if the request fails

    # Upload the file to S3
    upload_res = s3_client.put_object(
        Bucket='mst-github',
        Key=file,
        Body=res.content
    )

    # Print the response from S3
    print("Upload successful:", upload_res)

except requests.exceptions.RequestException as e:
    print(f"Error while downloading the file from {url}: {e}")

except boto3.exceptions.Boto3Error as e:
    print(f"Error while uploading the file to S3: {e}")
