from fastapi import FastAPI
import os
import datetime

app = FastAPI(title="Lab 4 - Docker Compose", version="1.0.0")

@app.get("/")
def root():
    return {
        "lab": 4,
        "title": "Docker Compose Lab",
        "version": "1.0.0",
        "status": "success",
        "timestamp": datetime.datetime.now().isoformat(),
        "containers": ["web", "redis"],
        "message": "Мультиконтейнерное приложение работает через Docker Compose!",
        "features": [
            "Multi-container setup",
            "Docker Compose orchestration",
            "Volume persistence",
            "CI/CD automation"
        ]
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "lab4-docker-compose",
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.get("/info")
def info():
    return {
        "environment": os.environ.get("ENV", "development"),
        "hostname": os.environ.get("HOSTNAME", "unknown"),
        "deployed_at": "2025-12-10"
    }
