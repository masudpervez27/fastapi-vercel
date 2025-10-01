from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"msgs": "Welcome to my api."}

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}