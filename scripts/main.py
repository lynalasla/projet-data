import os

print("START PIPELINE")

os.system("python scripts/transform.py")
os.system("python etl/to_s3.py")

print("PIPELINE DONE")