from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -------------------------
# ESTRUCTURA DE DATOS
# -------------------------
class Paciente(BaseModel):
    edad: int
    frecuencia_cardiaca: float
    presion: float
    nota_clinica: str

# -------------------------
# ENDPOINT
# -------------------------
@app.post("/predict")
def predict(data: Paciente):

    # Aquí irá el modelo real
    probabilidad = 0.82  # simulación

    return {
        "probabilidad": probabilidad,
        "riesgo": "ALTO" if probabilidad > 0.5 else "BAJO"
    }