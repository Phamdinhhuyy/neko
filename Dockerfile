FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_ENV=production
EXPOSE 80
CMD ["python", "run.py"]

# comment: This Dockerfile sets up a Python Flask application in a slim image, installs dependencies, and runs the app.
