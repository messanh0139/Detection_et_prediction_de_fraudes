import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
df = pd.read_csv('/home/jes/Bureau/detection_de_fraude/card_transdata.csv')

# Afficher les premières lignes et les informations sur les colonnes
print(df.head())
print(df.info())

# Statistiques descriptives
print(df.describe())

# Distribution de la variable cible 'fraud'
sns.countplot(x='fraud', data=df)
plt.title('Distribution de la fraude')
plt.savefig('/home/jes/Bureau/detection_de_fraude/fraud_distribution.png')

# Matrice de corrélation
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matrice de corrélation')
plt.savefig('/home/jes/Bureau/detection_de_fraude/correlation_matrix.png')


