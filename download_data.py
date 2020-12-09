from google.cloud import storage

BUCKET_NAME = "fil-simulation-data"
JSON_PATH = 'config/storage.json'
FILES_TO_DOWNLOAD = ['data/aggregated.parquet', 'data/granular.nc']

storage_client = storage.Client.from_service_account_json(JSON_PATH)
bucket = storage_client.bucket(BUCKET_NAME)

blobs = [path for path in bucket.list_blobs()
         if any(s in path.name for s in FILES_TO_DOWNLOAD)
         and path.name[:4] != 'data']

last_datetime = (sorted(blobs,
                        key=lambda x: x.name,
                        reverse=True)[0]
                 .name
                 .split("/")[0])

blobs_to_download = [blob for blob in blobs
                     if last_datetime in blob.name]

for blob in blobs_to_download:
    path = "/".join(blob.name.split("/")[1:])
    print(f"Downloading {blob.name} into {path}")
    blob.download_to_filename(path)
print("All files downloaded")
