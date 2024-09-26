# Dockerfile
FROM python:3.9-slim

# Arbeitsverzeichnis erstellen und setzen
WORKDIR /app

# Kopiere requirements.txt in das Arbeitsverzeichnis
COPY requirements.txt .

# Installiere die Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Rest der Anwendung in das Arbeitsverzeichnis
COPY . .

# Setze die Umgebungsvariable für Streamlit
ENV STREAMLIT_PORT=8501

# Exponiere den Port, auf dem Streamlit läuft
EXPOSE 8501

# Befehl zum Starten der Streamlit-Anwendung
CMD ["/run.sh"]