import zipfile

files_to_zip = ['lambda_function.py', 'download_file.py','ghalib.zip']
output_zip = 'ghactivity_downloader.zip'

with zipfile.ZipFile(output_zip, 'w') as zipf:
    for file in files_to_zip:
        zipf.write(file)

print(f"{output_zip} created successfully.")
