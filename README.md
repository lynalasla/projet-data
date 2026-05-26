# Projet Data Cloud – Pipeline ETL AWS

## Description

Ce projet consiste à concevoir une infrastructure Data Cloud complète permettant de collecter des offres d'emploi Data via API et scraping web, transformer et nettoyer les données avec Python, les stocker dans AWS S3 et PostgreSQL RDS, puis les visualiser dans un dashboard interactif.

L'objectif est de reproduire un pipeline ETL moderne proche des standards utilisés en Data Engineering et Cloud Computing.

---

## Architecture

API + Web Scraping
        ↓
Pipeline ETL Python
        ↓
Docker Container
        ↓
AWS S3 (Data Lake)
        ↓
AWS RDS PostgreSQL (Data Warehouse)
        ↓
Dashboard HTML / Plotly

## Stack technique

| Technologie             | Rôle                                    |
| ----------------------- | --------------------------------------- |
| Python                  | Développement du pipeline ETL           |
| Pandas                  | Nettoyage et transformation des données |
| Docker                  | Conteneurisation                        |
| AWS S3                  | Stockage Data Lake                      |
| AWS RDS PostgreSQL      | Base de données analytique              |
| Plotly                  | Visualisations interactives             |
| HTML / CSS / JavaScript | Dashboard                               |
| DBeaver                 | Gestion PostgreSQL                      |
| GitHub                  | Versioning du projet                    |

## Structure du projet

projet-data/
│
├── aws/
│   ├── iam_policy.json
│   ├── rds_schema.sql
│   └── s3_config.md
│
├── dashboard/
│   ├── app.py
│   ├── dashboard.html
│   ├── logo-dark.svg
│   └── logo-light.svg
│
├── data/
│   ├── processed/
│   │   └── jobs_clean.csv
│   │
│   └── raw/
│       ├── api_jobs.csv
│       └── scrape_jobs.csv
│
├── etl/
│   ├── check_rds.py
│   ├── from_s3.py
│   ├── load_to_rds.py
│   ├── test_rds.py
│   └── to_s3.py
│
├── notebooks/
│   └── analysis.ipynb
│
├── scripts/
│   ├── api.py
│   ├── main.py
│   ├── scrape.py
│   └── transform.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md

---

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/USERNAME/projet-data.git
cd projet-data
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer avec Docker

```bash
docker compose up --build
```

Le pipeline collecte, transforme et charge les données vers AWS S3 et PostgreSQL RDS.

---

## Dashboard interactif

Le dashboard permet :
- affichage des KPIs
- filtres interactifs
- graphiques dynamiques
- analyse des compétences
- visualisation des entreprises et localisations

---

## Analyses réalisées

- Entreprises qui recrutent le plus
- Localisations des offres
- Niveaux de postes
- Compétences recherchées
- Sources de données

---

## Sécurité

- IAM AWS pour les permissions
- Security Groups pour PostgreSQL
- Variables d'environnement pour protéger les credentials
- Isolation Docker

---

## Perspectives d'amélioration

- Orchestration avec Apache Airflow
- CI/CD automatisé
- Dashboard temps réel
- Intégration Machine Learning
- Monitoring cloud avancé

---

## Auteur

**Lyna Lasla**  
Mastère Data & Intelligence Artificielle  
École Multimédia – Paris