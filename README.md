# E-PMU - Modélisation IA pour Courses de Chevaux

## Description du Projet

E-PMU est un projet Python dédié à la création de modèles d'intelligence artificielle pour prédire les résultats des courses de chevaux. Le projet utilise les données historiques des courses pour entraîner des modèles de machine learning capables de faire des prédictions sur des courses futures.

## Fonctionnalités

- Collecte de données de courses via des scripts Python
- Traitement et transformation des données brutes
- Ingénierie de caractéristiques pour l'analyse
- Entraînement de modèles de prédiction
- Évaluation des performances des modèles
- Suivi des expériences et des résultats

## Architecture du Projet

python/
│
├── data/
│   ├── raw/                     # Données brutes importées
│   └── processed/               # Données transformées prêtes pour les modèles
│
├── src/
│   ├── domain/                  # Définition du domaine métier
│   │   ├── __init__.py
│   │   └── entities/            # Entités du domaine
│   │       ├── __init__.py
│   │       ├── horse.py         # Entité cheval
│   │       ├── race.py          # Entité course
│   │       └── result.py        # Entité résultat
│   │
│   ├── data_access/             # Accès et manipulation des données
│   │   ├── __init__.py
│   │   ├── csv_handlers/        # Handlers pour les fichiers CSV
│   │   │   ├── __init__.py
│   │   │   ├── reader.py        # Lecture des CSV
│   │   │   └── writer.py        # Écriture des CSV
│   │   │
│   │   ├── repositories/        # Repositories basés sur CSV
│   │   │   ├── __init__.py
│   │   │   ├── horse_repo.py
│   │   │   └── race_repo.py
│   │   │
│   │   └── mappers/             # Mappers entre entités et CSV
│   │       ├── __init__.py
│   │       └── csv_mappers.py
│   │
│   ├── data_collection/         # Scripts de collecte de données
│   │   ├── __init__.py
│   │   ├── scrapers/            # Web scrapers si nécessaire
│   │   │   └── __init__.py
│   │   └── importers/           # Import depuis différentes sources
│   │       ├── __init__.py
│   │       ├── fetch_races.py
│   │       └── fetch_results.py
│   │
│   ├── data_processing/         # Traitement des données
│   │   ├── __init__.py
│   │   ├── preprocessing.py     # Nettoyage et prétraitement
│   │   └── feature_engineering.py # Création de features
│   │
│   ├── models/                  # Modèles d'IA
│   │   ├── __init__.py
│   │   ├── training.py          # Entraînement des modèles
│   │   ├── evaluation.py        # Évaluation des performances
│   │   └── prediction.py        # Génération de prédictions
│   │
│   └── utils/                   # Utilitaires
│       ├── __init__.py
│       ├── config.py            # Gestion de la configuration
│       ├── logger.py            # Configuration des logs
│       └── helpers.py           # Fonctions utilitaires diverses
│
├── scripts/                     # Scripts d'exécution
│   └── scraping /
|       └── scraper.py           #Script de récupération des données
│
├── notebooks/                   # Notebooks pour l'exploration
│
├── tests/                       # Tests unitaires et d'intégration
│
├── configs/                     # Fichiers de configuration
│   └── data_paths.yaml          # Chemins vers les fichiers CSV
│
├── .env                         # Variables d'environnement
├── requirements.txt             # Dépendances du projet
├── setup.py                     # Pour installer le package
├── run.py                       # Point d'entrée principal
└── README.md                    # Documentation du projet


## Organisation des Modules

### Domain
Cette couche contient les entités métier qui représentent le modèle du domaine. Elle définit les concepts fondamentaux comme les chevaux, les courses et les résultats.

### Data Access
Cette couche gère l'accès aux données stockées en CSV. Elle comprend les handlers pour lire et écrire dans des fichiers CSV, des repositories pour encapsuler la logique d'accès aux données, et des mappers pour transformer entre les formats CSV et les entités du domaine.

### Data Collection
Ce module est responsable de la collecte des données brutes. Il peut contenir des scrapers web ou des importateurs pour différentes sources de données.

### Data Processing 
Ce module traite les données brutes et les transforme en données utilisables pour l'entraînement des modèles. Il comprend le prétraitement et l'ingénierie de caractéristiques.

### Models
Cette couche contient tous les modèles IA, leurs logiques d'entraînement, d'évaluation et de prédiction. Elle s'intègre avec MLflow pour le suivi des expériences.

### Utils
Contient des utilitaires communs comme la gestion de la configuration, les logs et des fonctions helpers.

## Dépendances

Le projet utilise les bibliothèques Python suivantes:
- pandas : Manipulation et analyse de données
- numpy : Calculs numériques
- scikit-learn : Algorithmes de machine learning
- seaborn & matplotlib : Visualisation de données
- mlflow : Suivi des expériences et gestion des modèles

## Démarrage

1. Clonez ce dépôt
2. Installez les dépendances : `pip install -r requirements.txt`
3. Créez les dossiers de base : `mkdir -p data/raw data/processed`
4. Lancez les scripts de collecte de données
5. Prétraitez les données et entraînez vos modèles

## Flux de Travail Typique

1. Collecte de données : `python scripts/import_data.py`
2. Prétraitement : `python scripts/process_data.py`
3. Entraînement des modèles : `python scripts/train_models.py`
4. Analyse des résultats via les notebooks Jupyter

## Bonnes Pratiques

- Maintenir une séparation claire entre les différentes couches
- Documenter le code et les modèles
- Utiliser MLflow pour suivre toutes les expériences
- Écrire des tests pour les fonctionnalités critiques
- Versionner les données importantes