Let us understand how we can deploy the locally developed Lambda Function to AWS Lambda Web Console.

You need to build the zip file with the source code.

zip -r ghactivity-downloader.zip lambda_function.py

Use AWS Lambda Web Console to upload the Zip file.

You can review the source code in Python scripts and test the function by creating a test event.