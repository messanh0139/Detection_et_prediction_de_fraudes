import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Charger les données
df = pd.read_csv('/home/jes/Bureau/detection_de_fraude/card_transdata.csv')

# Séparer les features et la cible
X = df.drop('fraud', axis=1)
y = df['fraud']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Entraîner un modèle de classification
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Évaluer le modèle
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))

# Sauvegarder le modèle
joblib.dump(model, '/home/jes/Bureau/detection_de_fraude/fraud_detection_model.pkl')


