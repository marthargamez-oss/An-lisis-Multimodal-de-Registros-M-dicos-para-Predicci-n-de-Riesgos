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
    # TODO: Reemplazar fallback por modelo entrenado final
    # Este bloque asegura que el sistema siga funcionando si el modelo no está disponible
try:
    probabilidad = modelo.predict_proba(df)[0][1]
except Exception as e:
    print(f"Error en modelo: {e}")
    probabilidad = 0.82  # fallback temporal
    
    return {
        "probabilidad": probabilidad,
        "riesgo": "ALTO" if probabilidad > 0.5 else "BAJO"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
