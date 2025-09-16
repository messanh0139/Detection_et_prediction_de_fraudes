# Pipeline CI/CD

## Intégration Continue (CI)

1.  **Déclencheur** : Push sur la branche `main` du dépôt Git.
2.  **Job 1 : Test et Linting**
    *   Exécute les tests unitaires et d'intégration.
    *   Analyse statique du code (linting) pour assurer la qualité du code.
3.  **Job 2 : Entraînement du modèle**
    *   Exécute le script `data_pipeline.py` pour entraîner le modèle de détection de fraude.
    *   Sauvegarde le modèle entraîné (`fraud_detection_model.pkl`) comme un artefact.

## Déploiement Continu (CD)

1.  **Déclencheur** : Succès de la phase d'intégration continue.
2.  **Job 1 : Déploiement du modèle**
    *   Déploie le modèle de détection de fraude sur une plateforme de machine learning (par exemple, SageMaker).
    *   Le modèle est exposé via une API pour les prédictions en temps réel.


