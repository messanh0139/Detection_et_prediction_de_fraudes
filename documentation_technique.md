# Documentation Technique

## 1. Vue d'ensemble

Ce document décrit l'architecture technique et les composants du projet de détection de fraude par carte de crédit. L'objectif est de construire une infrastructure de données robuste et évolutive pour traiter les transactions par carte de crédit en temps réel et identifier les transactions frauduleuses.

## 2. Architecture des données

L'architecture des données est basée sur une approche de cloud hybride, en tirant parti des services d'un fournisseur de cloud majeur pour le stockage, le traitement et l'apprentissage automatique. Les principaux composants sont :

*   **Data Lake (S3)** : Un compartiment Amazon S3 est utilisé comme data lake pour stocker les données brutes des transactions (fichiers CSV) et les données traitées.
*   **Data Warehouse (Snowflake)** : Snowflake est utilisé comme entrepôt de données pour stocker les données structurées et permettre des analyses complexes.
*   **Plateforme de Machine Learning (SageMaker)** : Amazon SageMaker est utilisé pour entraîner, déployer et surveiller les modèles d'apprentissage automatique pour la détection de la fraude.
*   **Orchestration (Airflow)** : Apache Airflow est utilisé pour orchestrer les pipelines de données, y compris l'ingestion, la transformation et le chargement (ETL) des données.

## 3. Schéma de données

Le schéma de données est conçu pour stocker les informations relatives aux transactions par carte de crédit. La table principale est la table `transactions`, qui contient les colonnes suivantes :

| Colonne | Type | Description |
|---|---|---|
| `transaction_id` | `INTEGER` | Identifiant unique de la transaction (clé primaire) |
| `distance_from_home` | `FLOAT` | Distance entre le lieu de la transaction et le domicile du titulaire de la carte |
| `distance_from_last_transaction` | `FLOAT` | Distance entre le lieu de la transaction et le lieu de la transaction précédente |
| `ratio_to_median_purchase_price` | `FLOAT` | Ratio du montant de la transaction par rapport au prix d'achat médian |
| `repeat_retailer` | `BOOLEAN` | Indique si le titulaire de la carte a déjà effectué un achat chez ce commerçant |
| `used_chip` | `BOOLEAN` | Indique si la transaction a été effectuée avec la puce de la carte |
| `used_pin_number` | `BOOLEAN` | Indique si le code PIN a été utilisé pour la transaction |
| `online_order` | `BOOLEAN` | Indique si la transaction a été effectuée en ligne |
| `fraud` | `BOOLEAN` | Indique si la transaction est frauduleuse |

## 4. Pipelines de traitement des données

Le pipeline de traitement des données est responsable de l'ingestion, de la transformation et du chargement des données des transactions par carte de crédit. Le pipeline est mis en œuvre à l'aide d'un script Python (`data_pipeline.py`) et orchestré par Airflow. Les principales étapes du pipeline sont :

1.  **Chargement des données** : Les données brutes des transactions sont chargées à partir du fichier CSV.
2.  **Préparation des données** : Les données sont nettoyées, transformées et préparées pour l'entraînement du modèle.
3.  **Entraînement du modèle** : Un modèle de classification par forêt aléatoire est entraîné sur les données préparées.
4.  **Évaluation du modèle** : Le modèle entraîné est évalué sur un ensemble de données de test pour mesurer ses performances.
5.  **Sauvegarde du modèle** : Le modèle entraîné est sauvegardé dans un fichier (`fraud_detection_model.pkl`) pour un déploiement ultérieur.

## 5. Pipeline CI/CD

Un pipeline d'intégration et de déploiement continus (CI/CD) est mis en place pour automatiser le processus de construction, de test et de déploiement de l'infrastructure de données. Le pipeline est défini dans un fichier `cicd_pipeline.md` et mis en œuvre à l'aide d'un outil CI/CD tel que Jenkins ou GitLab CI. Les principales étapes du pipeline sont :

*   **Intégration continue (CI)** : Déclenchée par un push sur la branche `main` du dépôt Git, cette étape exécute les tests, le linting et l'entraînement du modèle.
*   **Déploiement continu (CD)** : Déclenchée par le succès de la phase CI, cette étape déploie le modèle entraîné sur SageMaker.

## 6. Système de supervision

Un système de supervision est mis en place pour surveiller la santé et les performances de l'infrastructure de données. Le système utilise une combinaison d'outils, notamment CloudWatch, Prometheus et Grafana, pour surveiller les composants clés tels que le data lake, l'entrepôt de données, la plateforme d'apprentissage automatique et l'orchestrateur de pipeline. Des tableaux de bord et des alertes personnalisés sont configurés pour fournir une visibilité en temps réel sur l'état de l'infrastructure.


