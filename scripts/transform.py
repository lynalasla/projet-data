import pandas as pd

# 1. Load raw
api = pd.read_csv("data/raw/api_jobs.csv")
scrape = pd.read_csv("data/raw/scrape_jobs.csv")

# 2. Merge
df = pd.concat([api, scrape], ignore_index=True)

# 3. Cleaning
df["title"] = df["title"].astype(str)
df["title_lower"] = df["title"].str.lower()

df.drop_duplicates(inplace=True)

# 4. Feature engineering (IMPORTANT projet)
df["title_length"] = df["title"].str.len()

def get_level(title):
    title = title.lower()
    if "senior" in title:
        return "senior"
    elif "junior" in title:
        return "junior"
    return "mid"

df["level"] = df["title"].apply(get_level)

# 5. Save processed locally
df.to_csv("data/processed/jobs_clean.csv", index=False)

print("ETL DONE")