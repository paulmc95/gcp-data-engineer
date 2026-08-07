import argparse
from google.cloud import storage

def main():
    parser = argparse.ArgumentParser(description="Create a GCP bucket.")
    parser.add_argument("bucket_name", type=str, help="Name of the bucket to create.")
    parser.add_argument("--project", type=str, default=None, help="GCP project ID to use (optional).")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without creating the bucket.")
    args = parser.parse_args()

    bucket_name = args.bucket_name
    project = args.project

    print(f"Bucket name received: {bucket_name}")
    if project:
        print(f"Using project: {project}")

    """Creates a new bucket in Google Cloud Storage."""
    # Initialize a client (pass project if provided so Client() can be constructed)
    storage_client = storage.Client(project=project)

    # Create a bucket object for the requested bucket name.
    # This does not create the bucket in GCP yet; it just prepares the bucket resource.
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "STANDARD"  # Set the storage class for the bucket object.

    if args.dry_run:
        print(f"Dry run: would create bucket '{bucket_name}' in project '{project or '<detected>'}' in us-central1 with class {bucket.storage_class}.")
        return

    # Send the request to GCP to actually create the bucket in the specified location.
    new_bucket = storage_client.create_bucket(bucket, location="us-central1")
    print(f"Bucket {new_bucket.name} created in {new_bucket.location} with class {new_bucket.storage_class}.")

if __name__ == "__main__":
    # Example usage
    main()