from fastapi import FastAPI
from pydantic import BaseModel
import random

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

    # Simulación de estructura para modelo (ajustar cuando lo integren)
    df = {
        "edad": data.edad,
        "frecuencia_cardiaca": data.frecuencia_cardiaca,
        "presion": data.presion
    }

    # TODO: Reemplazar por modelo entrenado final
    # Este bloque garantiza que el sistema siga funcionando aunque el modelo no esté disponible
    try:
        # Ejemplo futuro:
        # probabilidad = modelo.predict_proba(df)[0][1]

        # Simulación temporal dependiente de datos (más realista que un valor fijo)
        probabilidad = round(
            min(0.9, max(0.1, (data.edad / 100) + random.uniform(-0.1, 0.1))),
            2
        )

    except Exception as e:
        print(f"Error en modelo: {e}")

        # Fallback alternativo (en caso de error inesperado)
        probabilidad = round(random.uniform(0.3, 0.9), 2)

    return {
        "probabilidad": probabilidad,
        "riesgo": "ALTO" if probabilidad > 0.5 else "BAJO"
    }

# -------------------------
# RUN LOCAL (opcional)
# -------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
