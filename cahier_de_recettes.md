# Cahier de recettes et de tests

## 1. Tests unitaires

| Test | Description | Résultat attendu |
|---|---|---|
| `test_data_loading` | Vérifie que les données sont correctement chargées à partir du fichier CSV. | Le DataFrame n'est pas vide. |
| `test_data_preprocessing` | Vérifie que les données sont correctement prétraitées. | Aucune valeur manquante dans le DataFrame. |
| `test_model_training` | Vérifie que le modèle est correctement entraîné. | Le modèle est un objet de type `RandomForestClassifier`. |

## 2. Tests d'intégration

| Test | Description | Résultat attendu |
|---|---|---|
| `test_data_pipeline` | Vérifie que le pipeline de traitement des données s'exécute de bout en bout sans erreur. | Le modèle est sauvegardé dans un fichier. |
| `test_api_prediction` | Vérifie que l'API de prédiction retourne une prédiction valide. | La prédiction est 0 ou 1. |

## 3. Tests de performance

| Test | Description | Résultat attendu |
|---|---|---|
| `test_prediction_latency` | Mesure la latence de l'API de prédiction. | La latence est inférieure à 100 ms. |
| `test_training_time` | Mesure le temps d'entraînement du modèle. | Le temps d'entraînement est inférieur à 10 minutes. |


