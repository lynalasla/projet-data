import requests
import pandas as pd

URL = "https://remotive.com/api/remote-jobs?category=data"

def get_jobs():
    response = requests.get(URL)

    print("Status:", response.status_code)

    data = response.json()

    jobs = []

    for job in data.get("jobs", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("candidate_required_location"),
            "source": "remotive"
        })

    return jobs


def save(jobs):
    df = pd.DataFrame(jobs)

    path = "data/raw/scrape_jobs.csv"
    df.to_csv(path, index=False)

    print("Saved:", len(df))
    print(path)


if __name__ == "__main__":
    jobs = get_jobs()
    save(jobs)