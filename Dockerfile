# Utiliser une image de base plus légère pour réduire la taille finale
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier des dépendances en premier pour profiter du cache de Docker
COPY requirements.txt .

# Mettre à jour pip et installer les dépendances
RUN pip install --upgrade pip --root-user-action=ignore
RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt


# Copier le reste du code de l'application
COPY . . 

# Exposer le port sur lequel Streamlit va tourner
EXPOSE 8080

# Commande pour lancer l'application en spécifiant le port
CMD ["streamlit", "run", "detection_fraude.py", "--server.port=8080", "--server.address=0.0.0.0"]
