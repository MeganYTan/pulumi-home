import pulumi
from pulumi_gcp import storage

# Get current stack
stack = pulumi.get_stack()

# Use Pulumi config or custom logic for region
config = pulumi.Config("gcp")
region = "us-central1"

# Create a regional bucket
bucket = storage.Bucket(f"{stack}-bucket",
    location=region,
    force_destroy=True
)

pulumi.export("bucket_name", bucket.name)
