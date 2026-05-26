import boto3

s3 = boto3.client("s3")

BUCKET = "projet-data-lyna-lasla"

s3.upload_file(
    "data/processed/jobs_clean.csv",
    BUCKET,
    "processed/jobs_clean.csv"
)

print("Uploaded processed data")