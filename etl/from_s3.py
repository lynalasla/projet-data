import boto3

s3 = boto3.client("s3")

BUCKET = "projet-data-lyna-lasla"

s3.download_file(
    BUCKET,
    "processed/jobs_clean.csv",
    "data/processed/jobs_clean.csv"
)

print("Downloaded from S3")