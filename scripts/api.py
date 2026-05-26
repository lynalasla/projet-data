import requests
import pandas as pd

APP_ID = "3d53ebcb"
APP_KEY = "2b301c31d5e45146519e79106892878e"

URL = "https://api.adzuna.com/v1/api/jobs/fr/search/1"

def get_jobs():
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": "data scientist",
        "where": "Paris",
        "results_per_page": 20,
        "content-type": "application/json"
    }

    response = requests.get(URL, params=params)

    print("Status:", response.status_code)

    if response.status_code != 200:
        print("Erreur API:", response.text)
        return []

    data = response.json()

    jobs = []

    for job in data.get("results", []):
        jobs.append({
            "title": job.get("title"),
            "company": job["company"]["display_name"] if job.get("company") else None,
            "location": job["location"]["display_name"] if job.get("location") else None,
            "salary_min": job.get("salary_min"),
            "salary_max": job.get("salary_max"),
            "source": "adzuna"
        })

    return jobs


def save(jobs):
    df = pd.DataFrame(jobs)

    path = "data/raw/api_jobs.csv"

    df.to_csv(path, index=False)

    print("Saved:", len(df))
    print("File:", path)


if __name__ == "__main__":
    jobs = get_jobs()
    save(jobs)