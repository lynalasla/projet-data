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

Ce projet conçoit une **infrastructure Data Cloud complète** autour du marché de l'emploi Data. Il combine collecte automatisée via API, transformation et nettoyage des données en Python, stockage sur **AWS S3** (Data Lake) et **PostgreSQL RDS** (Data Warehouse), puis visualisation dans un dashboard interactif Plotly.

> 🎯 **Objectif** : reproduire un pipeline ETL moderne conforme aux standards du Data Engineering et du Cloud Computing.

---

## 🏗️ Architecture
┌─────────────────────────────────────────────────────────────┐
│                     SOURCES DE DONNÉES                       │
│           API Adzuna  +  API Remotive (remote jobs)          │
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
│    Lance automatiquement : transform.py → to_s3.py           │
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
projet-data/
│
├── 📂 aws/                         # Configuration infrastructure AWS
│   ├── iam_policy.json             # Politiques IAM (permissions)
│   ├── rds_schema.sql              # Schéma prévu pour les prochaines améliorations
│   └── s3_config.md                # Configuration du bucket S3
│
├── 📂 dashboard/                   # Application de visualisation
│   ├── app.py                      # Génération du dashboard HTML
│   ├── dashboard.html              # Interface principale
│   ├── logo-dark.svg               # Logo (thème sombre)
│   └── logo-light.svg              # Logo (thème clair)
│
├── 📂 data/                        # Données du projet
│   ├── processed/
│   │   └── jobs_clean.csv          # Données nettoyées et transformées
│   └── raw/
│       ├── api_jobs.csv            # Données brutes issues de l'API Adzuna
│       └── scrape_jobs.csv         # Données brutes issues de l'API Remotive
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
│   ├── api.py                      # Collecte via API Adzuna
│   ├── main.py                     # Point d'entrée du pipeline
│   ├── scrape.py                   # Collecte via API Remotive
│   └── transform.py                # Nettoyage et transformation
│
├── Dockerfile                      # Image Docker du projet
├── docker-compose.yml              # Orchestration des conteneurs
├── requirements.txt                # Dépendances Python
├── .env                            # Variables d'environnement (non versionné)
└── README.md                       # Documentation du projet

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
AWS_DEFAULT_REGION=eu-north-1
S3_BUCKET_NAME=your-bucket-name
RDS_HOST=your-rds-endpoint.rds.amazonaws.com
RDS_PORT=5432
RDS_DB=jobsdb
RDS_USER=your_user
RDS_PASSWORD=your_password
ADZUNA_APP_ID=your_app_id
ADZUNA_APP_KEY=your_app_key
```

### 1. Cloner le dépôt

```bash
git clone https://github.com/lynalasla/projet-data.git
cd projet-data
```

### 2. Étape préalable — Collecte des données

Avant de lancer Docker, exécuter la collecte manuellement :

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux / Mac

pip install -r requirements.txt

python scripts/api.py
python scripts/scrape.py
```

### 3. Lancer le pipeline avec Docker

```bash
docker compose up --build
```

> Docker lance automatiquement `transform.py` puis `to_s3.py` pour transformer et envoyer les données vers **AWS S3**.

### 4. Lancer le dashboard

```bash
python dashboard/app.py
start dashboard/dashboard.html
```

---

## 🔄 Pipeline ETL

Le pipeline se déroule en 3 phases :

### 1. Extract — Collecte des données

| Source | Script | Méthode |
|--------|--------|---------|
| API Adzuna | `scripts/api.py` | Requêtes HTTP / JSON |
| API Remotive | `scripts/scrape.py` | Requêtes HTTP / JSON |

### 2. Transform — Nettoyage & enrichissement

Géré par `scripts/transform.py` :
- Fusion des deux sources de données
- Suppression des doublons
- Normalisation des intitulés de poste
- Détection du niveau d'expérience (junior / mid / senior)
- Calcul de la longueur des titres de poste

### 3. Load — Chargement vers le Cloud

| Destination | Script | Format |
|-------------|--------|--------|
| AWS S3 (Data Lake) | `etl/to_s3.py` | CSV |
| PostgreSQL RDS | `etl/load_to_rds.py` | Tables relationnelles |

---

## 📊 Dashboard interactif

Le dashboard, construit avec **Plotly** et **HTML/CSS/JS**, offre :

| Fonctionnalité | Description |
|----------------|-------------|
| 📈 KPIs dynamiques | Nombre d'offres, entreprises, localisations, sources |
| 🔍 Filtres interactifs | Par localisation et par entreprise |
| 📊 Graphiques dynamiques | Barres, camemberts, histogrammes |
| 🏢 Top entreprises | Classement des recruteurs les plus actifs |
| 🌍 Top localisations | Répartition géographique des offres |
| 🧠 Analyse des compétences | Détection de Python, SQL, AWS, AI dans les titres |
| 🌙 Thème dark / light | Bascule dynamique sans rechargement |

---

## 🔍 Analyses réalisées

- **Entreprises qui recrutent le plus** — classement des sociétés les plus actives
- **Localisations des offres** — répartition géographique (Paris, remote…)
- **Niveaux de postes** — junior / mid / senior détectés depuis les titres
- **Compétences recherchées** — Python, SQL, AWS, AI
- **Sources de données** — comparaison Adzuna vs Remotive (volume, couverture)
- **Complexité des titres** — distribution de la longueur des intitulés de poste

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
