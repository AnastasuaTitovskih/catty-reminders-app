from fastapi import FastAPI

app = FastAPI(title="Lab 4 - Docker Compose")

@app.get("/")
def root():
    return {
        "lab": 4,
        "title": "Docker Compose Lab",
        "status": "success",
        "containers": ["web", "redis"],
        "message": "Мультиконтейнерное приложение работает!"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
