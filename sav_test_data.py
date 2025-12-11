import pandas as pd
from sklearn.model_selection import train_test_split

# Charger les données
df = pd.read_csv('/home/jes/Bureau/detection_de_fraude/card_transdata.csv')

# Séparer les features et la cible
X = df.drop('fraud', axis=1)
y = df['fraud']

# Diviser les données en ensembles d'entraînement et de test
# On utilise le même test_size et random_state que pour l'entraînement pour cohérence
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Créer un DataFrame combinant X_test et y_test
test_data = X_test.copy()
test_data['fraud'] = y_test

# Sauvegarder les données de test dans un fichier CSV
test_data.to_csv('/home/jes/Bureau/detection_de_fraude/test_data.csv', index=False)