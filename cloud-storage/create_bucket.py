import argparse
from google.cloud import storage

def main():
    parser = argparse.ArgumentParser(description="Create a GCP bucket.")
    parser.add_argument("bucket_name", type=str, help="Name of the bucket to create.")
    args= parser.parse_args()

    bucket_name= args.bucket_name
    print(f"Bucket name received: {bucket_name}")
    
    """Creates a new bucket in Google Cloud Storage."""
    # Initialize a client
    storage_client = storage.Client()

    # Create a bucket object for the requested bucket name.
    # This does not create the bucket in GCP yet; it just prepares the bucket resource.
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "STANDARD"  # Set the storage class for the bucket object.

    # Send the request to GCP to actually create the bucket in the specified location.
    new_bucket = storage_client.create_bucket(bucket, location="us-central1")
    print(f"Bucket {new_bucket.name} created in {new_bucket.location} with class {new_bucket.storage_class}.")

if __name__ == "__main__":
    # Example usage
    main()