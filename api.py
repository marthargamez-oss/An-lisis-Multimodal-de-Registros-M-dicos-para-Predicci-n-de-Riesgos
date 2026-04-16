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
    probabilidad = 0.33  # simulación

    return {
        "probabilidad": probabilidad,
        "riesgo": "ALTO" if probabilidad > 0.5 else "BAJO"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
