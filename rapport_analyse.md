# Rapport d'analyse des données de transactions de cartes

## Introduction

Ce rapport présente une analyse exploratoire des données de transactions de cartes fournies dans le fichier `card_transdata.csv`. L'objectif est de comprendre la structure des données, d'identifier les tendances et les anomalies, et de préparer le terrain pour la conception d'une architecture data de détection de fraude.

## Analyse exploratoire des données (EDA)

Le jeu de données contient 1 000 000 de transactions, chacune décrite par 8 caractéristiques. Les données sont complètes, sans aucune valeur manquante.

### Distribution de la fraude

La variable cible, `fraud`, est fortement déséquilibrée. Environ 8,7% des transactions sont frauduleuses, ce qui est une considération importante pour la modélisation.

![Distribution de la fraude](/home/ubuntu/fraud_distribution.png)

### Matrice de corrélation

La matrice de corrélation met en évidence les relations entre les différentes variables. On observe notamment que :

- `ratio_to_median_purchase_price` a la plus forte corrélation positive avec la fraude (0.46).
- `distance_from_home` et `online_order` ont également une corrélation positive avec la fraude (0.19).
- `used_pin_number` a une corrélation négative avec la fraude (-0.10).

![Matrice de corrélation](/home/ubuntu/correlation_matrix.png)

## Conclusion

L'analyse exploratoire a permis de mettre en évidence les caractéristiques les plus importantes pour la détection de fraude. Ces informations seront cruciales pour la conception de l'architecture data et des pipelines de traitement. La prochaine étape consistera à concevoir l'architecture data et le schéma de données.


