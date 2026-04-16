# Sistema de Predicción de Reingreso Hospitalario

## Descripción
Sistema basado en inteligencia artificial para la predicción de riesgo de reingreso hospitalario utilizando datos clínicos estructurados y texto médico.

## Arquitectura
- Frontend: Streamlit
- Backend: FastAPI
- Modelo: Machine Learning (pendiente integración)

## Ejecución local

### 1. Instalar dependencias
pip install -r requirements.txt

### 2. Ejecutar API
uvicorn api:app --reload

### 3. Ejecutar frontend
streamlit run app.py

## Uso
Ingresar datos del paciente en la interfaz web y presionar "Predecir riesgo".

## Nota
El modelo debe ser integrado en el endpoint `/predict` dentro de `api.py`.

## Estado del proyecto
MVP funcional con integración pendiente del modelo.