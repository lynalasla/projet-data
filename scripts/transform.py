import pandas as pd

# Je charge les deux sources de données brutes séparément
api = pd.read_csv("data/raw/api_jobs.csv")
scrape = pd.read_csv("data/raw/scrape_jobs.csv")

# Je fusionne les deux sources en un seul DataFrame
df = pd.concat([api, scrape], ignore_index=True)

# Je normalise les titres pour pouvoir les comparer facilement
df["title"] = df["title"].astype(str)
df["title_lower"] = df["title"].str.lower()

# Je supprime les doublons pour éviter de biaiser l'analyse
df.drop_duplicates(inplace=True)

# Je calcule la longueur des titres pour analyser leur complexité
df["title_length"] = df["title"].str.len()

# Je détecte le niveau d'expérience directement depuis le titre du poste
def get_level(title):
    title = title.lower()
    if "senior" in title:
        return "senior"
    elif "junior" in title:
        return "junior"
    return "mid"  # Par défaut je considère le poste comme mid-level

df["level"] = df["title"].apply(get_level)

# Je sauvegarde le fichier nettoyé et enrichi pour le dashboard
df.to_csv("data/processed/jobs_clean.csv", index=False)

print("ETL DONE")