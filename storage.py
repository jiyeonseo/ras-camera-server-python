import uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

AZURE_STORAGE_NAME = ""
AZURE_STORAGE_CONNECTION_STRING = ""
CONTAINER_NAME = ""

def upload(upload_file_path, local_file_name):
    
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    
    # container_client = blob_service_client.create_container(CONTAINER_NAME) # Create the container if needed

    tmp_file_name =  str(uuid.uuid4()) + ".jpg"
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=tmp_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

    return f'https://{AZURE_STORAGE_NAME}.blob.core.windows.net/{CONTAINER_NAME}/{tmp_file_name}'