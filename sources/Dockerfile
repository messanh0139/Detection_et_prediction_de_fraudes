FROM python:3.12-slim

WORKDIR /app

# Copier requirements.txt depuis la racine
COPY requirements.txt .

RUN pip install --upgrade pip --root-user-action=ignore
RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt

# Copier le code source
COPY sources/ /app/

# Copier les datasets
COPY data/ /app/data/

# Copier le modèle
COPY fraud_detection_model.pkl /app/

EXPOSE 8080

CMD ["streamlit", "run", "detection_fraude.py", "--server.port=8080", "--server.address=0.0.0.0"]
