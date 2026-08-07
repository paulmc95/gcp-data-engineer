from google.cloud import storage

def create_bucket(bucket_name, location="US-CENTRAL", storage_class="STANDARD"):
    """Creates a new bucket in Google Cloud Storage."""
    # Initialize a client
    storage_client = storage.Client()

    # Create a bucket object for the requested bucket name.
    # This does not create the bucket in GCP yet; it just prepares the bucket resource.
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = storage_class  # Set the storage class for the bucket object.

    # Send the request to GCP to actually create the bucket in the specified location.
    new_bucket = storage_client.create_bucket(bucket, location=location)
    print(f"Bucket {new_bucket.name} created in {new_bucket.location} with class {new_bucket.storage_class}.")