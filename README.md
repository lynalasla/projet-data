<div align="center">

# 🚀 Projet Data Cloud — Pipeline ETL AWS

**Collecte · Transformation · Stockage · Visualisation**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20RDS-FF9900?style=flat-square&logo=amazon-aws&logoColor=white)](https://aws.amazon.com)
[![Docker](https://img.shields.io/badge/Docker-Conteneurisé-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-RDS-336791?style=flat-square&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Plotly](https://img.shields.io/badge/Dashboard-Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)](https://plotly.com)

*Mastère Data & Intelligence Artificielle — École Multimédia, Paris*
*Auteure : **Lyna Lasla***

---

</div>

## 📋 Table des matières

- [Description](#-description)
- [Architecture](#-architecture)
- [Stack technique](#-stack-technique)
- [Structure du projet](#-structure-du-projet)
- [Installation](#-installation)
- [Pipeline ETL](#-pipeline-etl)
- [Dashboard interactif](#-dashboard-interactif)
- [Analyses réalisées](#-analyses-réalisées)
- [Sécurité](#-sécurité)
- [Perspectives d'amélioration](#-perspectives-damélioration)

---

## 📖 Description

Ce projet conçoit une **infrastructure Data Cloud complète** autour du marché de l'emploi Data. Il combine collecte automatisée via API et scraping web, transformation et nettoyage des données en Python, stockage sur **AWS S3** (Data Lake) et **PostgreSQL RDS** (Data Warehouse), puis visualisation dans un dashboard interactif Plotly.

> 🎯 **Objectif** : reproduire un pipeline ETL moderne conforme aux standards du Data Engineering et du Cloud Computing.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     SOURCES DE DONNÉES                       │
│        API Offres d'emploi  +  Web Scraping                  │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                  PIPELINE ETL (Python)                        │
│   Collecte (api.py / scrape.py) → Transform → Load           │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│               CONTENEURISATION (Docker)                       │
│         Dockerfile + docker-compose.yml                      │
└──────────┬──────────────────────────┬───────────────────────┘
           │                          │
           ▼                          ▼
┌──────────────────┐      ┌──────────────────────────┐
│   AWS S3         │      │   AWS RDS PostgreSQL      │
│   (Data Lake)    │      │   (Data Warehouse)        │
│  Données brutes  │      │  Données structurées      │
└──────────────────┘      └────────────┬─────────────┘
                                       │
                                       ▼
                          ┌────────────────────────┐
                          │  Dashboard Plotly/HTML  │
                          │  KPIs · Filtres · Graphs│
                          └────────────────────────┘
```

---

## 🛠️ Stack technique

| Technologie             | Rôle                                      | Catégorie       |
|-------------------------|-------------------------------------------|-----------------|
| **Python 3.11**         | Développement du pipeline ETL             | Core            |
| **Pandas**              | Nettoyage et transformation des données   | Data Processing |
| **Docker**              | Conteneurisation de l'application         | Infrastructure  |
| **AWS S3**              | Stockage Data Lake (données brutes)       | Cloud Storage   |
| **AWS RDS PostgreSQL**  | Base de données analytique (Data WH)      | Cloud Database  |
| **Plotly**              | Visualisations interactives               | Dataviz         |
| **HTML / CSS / JS**     | Interface du dashboard                    | Frontend        |
| **DBeaver**             | Administration et gestion PostgreSQL      | Tooling         |
| **GitHub**              | Versioning et collaboration               | DevOps          |

---

## 📁 Structure du projet

```
projet-data/
│
├── 📂 aws/                         # Configuration infrastructure AWS
│   ├── iam_policy.json             # Politiques IAM (permissions)
│   ├── rds_schema.sql              # Schéma de la base PostgreSQL
│   └── s3_config.md                # Configuration du bucket S3
│
├── 📂 dashboard/                   # Application de visualisation
│   ├── app.py                      # Serveur Flask/Dash
│   ├── dashboard.html              # Interface principale
│   ├── logo-dark.svg               # Logo (thème sombre)
│   └── logo-light.svg              # Logo (thème clair)
│
├── 📂 data/                        # Données du projet
│   ├── processed/
│   │   └── jobs_clean.csv          # Données nettoyées et transformées
│   └── raw/
│       ├── api_jobs.csv            # Données brutes issues de l'API
│       └── scrape_jobs.csv         # Données brutes issues du scraping
│
├── 📂 etl/                         # Modules ETL (chargement)
│   ├── check_rds.py                # Vérification connexion RDS
│   ├── from_s3.py                  # Lecture depuis S3
│   ├── load_to_rds.py              # Chargement vers PostgreSQL RDS
│   ├── test_rds.py                 # Tests de la base RDS
│   └── to_s3.py                    # Upload vers S3
│
├── 📂 notebooks/
│   └── analysis.ipynb              # Analyses exploratoires (EDA)
│
├── 📂 scripts/                     # Scripts principaux ETL
│   ├── api.py                      # Collecte via API
│   ├── main.py                     # Point d'entrée du pipeline
│   ├── scrape.py                   # Web scraping
│   └── transform.py                # Nettoyage et transformation
│
├── Dockerfile                      # Image Docker du projet
├── docker-compose.yml              # Orchestration des conteneurs
├── requirements.txt                # Dépendances Python
├── .env                            # Variables d'environnement (non versionné)
└── README.md                       # Documentation du projet
```

---

## ⚙️ Installation

### Prérequis

- Python 3.11+
- Docker & Docker Compose
- Compte AWS avec accès S3 et RDS configuré
- Fichier `.env` à créer à partir du modèle ci-dessous

### Variables d'environnement (`.env`)

```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=eu-west-1
S3_BUCKET_NAME=your-bucket-name
RDS_HOST=your-rds-endpoint.rds.amazonaws.com
RDS_PORT=5432
RDS_DB=projet_data
RDS_USER=your_user
RDS_PASSWORD=your_password
```

### 1. Cloner le dépôt

```bash
git clone https://github.com/lynalasla/projet-data.git
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

> Le pipeline collecte, transforme et charge automatiquement les données vers **AWS S3** et **PostgreSQL RDS**.

---

## 🔄 Pipeline ETL

Le pipeline est orchestré par `scripts/main.py` et se déroule en 3 phases :

### 1. Extract — Collecte des données

| Source | Script | Méthode |
|--------|--------|---------|
| API offres d'emploi | `api.py` | Requêtes HTTP / JSON |
| Sites web | `scrape.py` | BeautifulSoup / Selenium |

### 2. Transform — Nettoyage & enrichissement

Géré par `scripts/transform.py` :
- Suppression des doublons et valeurs nulles
- Normalisation des intitulés de poste et des localisations
- Extraction des compétences depuis les descriptions (NLP basique)
- Uniformisation des formats de dates

### 3. Load — Chargement vers le Cloud

| Destination | Script | Format |
|-------------|--------|--------|
| AWS S3 (Data Lake) | `etl/to_s3.py` | CSV brut |
| PostgreSQL RDS | `etl/load_to_rds.py` | Tables relationnelles |

---

## 📊 Dashboard interactif

Le dashboard, construit avec **Plotly** et **HTML/CSS/JS**, offre :

| Fonctionnalité | Description |
|----------------|-------------|
| 📈 KPIs dynamiques | Nombre d'offres, entreprises, localisations uniques |
| 🔍 Filtres interactifs | Par localisation, niveau de poste, compétence |
| 📉 Graphiques dynamiques | Barres, camemberts, heatmaps |
| 🏢 Top entreprises | Classement des recruteurs actifs |
| 🗺️ Carte des offres | Distribution géographique |
| 🧠 Analyse des compétences | Nuage de mots et fréquences |

---

## 🔍 Analyses réalisées

Les analyses sont documentées dans `notebooks/analysis.ipynb` :

- **Entreprises qui recrutent le plus** — classement des sociétés les plus actives
- **Localisations des offres** — répartition géographique (Paris, Lyon, remote…)
- **Niveaux de postes** — junior / confirmé / senior / lead
- **Compétences recherchées** — Python, SQL, Power BI, Spark, etc.
- **Sources de données** — comparaison API vs scraping (volume, qualité)

---

## 🔒 Sécurité

| Mesure | Détail |
|--------|--------|
| **IAM AWS** | Rôles et politiques à moindre privilège (`aws/iam_policy.json`) |
| **Security Groups** | Accès PostgreSQL restreint aux IPs autorisées |
| **Variables d'environnement** | Credentials hors du code via `.env` (non versionné) |
| **Isolation Docker** | Réseau interne entre les conteneurs |
| **.gitignore** | Exclusion des fichiers sensibles (`.env`, credentials) |

---

## 🔭 Perspectives d'amélioration

- [ ] **Apache Airflow** — Orchestration et planification des pipelines
- [ ] **CI/CD GitHub Actions** — Tests et déploiement automatisés
- [ ] **Dashboard temps réel** — Streaming avec Kafka ou AWS Kinesis
- [ ] **Machine Learning** — Recommandation d'offres, prédiction de salaires
- [ ] **Monitoring cloud** — CloudWatch, alertes et dashboards AWS

---

## 👤 Auteure

**Lyna Lasla**
Mastère Data & Intelligence Artificielle
École Multimédia — Paris
---

<div align="center">

*Projet réalisé dans le cadre du Mastère Directeur de Projet en Intelligence Artificielle — École Multimédia, Paris*

</div>
