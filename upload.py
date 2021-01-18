import os
import uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

try:
    print("Azure Blob storage v" + __version__ + " - Python quickstart sample")
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    containter_name = 'geekjr'
    upload_file_path = './school.st'

    blob_client = blob_service_client.get_blob_client(
        container=containter_name, blob=upload_file_path)

    print("\nUploading to Azure Storage as blob:\n\t" + upload_file_path)

    # Upload the created file
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

except Exception as ex:
    print('Exception:')
    print(ex)
