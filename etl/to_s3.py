import boto3

# Je me connecte à S3 via boto3 (les credentials sont gérés par AWS CLI)
s3 = boto3.client("s3")

# Nom de mon bucket S3
BUCKET = "projet-data-lyna-lasla"

# J'uploade le fichier CSV nettoyé depuis le dossier local vers S3
s3.upload_file(
    "data/processed/jobs_clean.csv",  # Fichier source en local
    BUCKET,                            # Bucket de destination
    "processed/jobs_clean.csv"         # Chemin de destination dans le bucket
)

print("Uploaded processed data")