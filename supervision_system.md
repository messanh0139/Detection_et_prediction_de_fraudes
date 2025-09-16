# Système de Supervision

## Introduction

Un système de supervision est essentiel pour garantir la fiabilité, la performance et la sécurité de l'infrastructure data. Il permet de surveiller en temps réel les différents composants de l'architecture, de détecter les anomalies et de déclencher des alertes en cas de problème.

## Composants supervisés

Le système de supervision couvrira les composants suivants :

*   **Data Lake (S3)** : Surveillance de l'espace de stockage, des accès et des erreurs de lecture/écriture.
*   **Data Warehouse (Snowflake)** : Surveillance des performances des requêtes, de l'utilisation des ressources et des coûts.
*   **Machine Learning Platform (SageMaker)** : Surveillance de l'état des modèles, des performances de prédiction et de la dérive des modèles.
*   **Orchestration (Airflow)** : Surveillance de l'état des DAGs, des temps d'exécution et des erreurs.

## Outils de supervision

Nous utiliserons une combinaison d'outils pour la supervision :

*   **CloudWatch** : Pour la surveillance des services AWS (S3, SageMaker).
*   **Prometheus et Grafana** : Pour la surveillance des applications et des infrastructures.
*   **Alertmanager** : Pour la gestion des alertes.

## Tableaux de bord

Des tableaux de bord personnalisés seront créés dans Grafana pour visualiser les métriques clés de chaque composant. Ces tableaux de bord permettront de suivre en temps réel l'état de santé de l'infrastructure et d'identifier rapidement les problèmes.


