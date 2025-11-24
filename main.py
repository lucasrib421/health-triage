# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from service import TriageService

app = FastAPI(title="HealthTriage API")
triage_service = TriageService()

class SymptomRequest(BaseModel):
    description: str

@app.post("/triagem")
def realizar_triagem(request: SymptomRequest):
    return triage_service.classify_symptom(request.description)

# Para rodar: uvicorn main:app --reload