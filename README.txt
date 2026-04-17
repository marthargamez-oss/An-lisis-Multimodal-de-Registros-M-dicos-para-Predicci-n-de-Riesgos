Sistema Multimodal para la Predicción de Riesgo en Registros Médicos

1. Descripción general

Este proyecto presenta el diseño e implementación de un sistema basado en Inteligencia Artificial para la predicción de riesgo a partir de información clínica. La solución integra datos estructurados y texto clínico mediante un enfoque multimodal, con el objetivo de evaluar el impacto de distintas estrategias de modelado sobre el desempeño predictivo.

El sistema se desarrolla bajo un enfoque de experimentación controlada y se implementa siguiendo principios de arquitectura desacoplada, permitiendo la separación entre la capa de modelo y la capa de servicio.

2. Objetivo

Desarrollar y evaluar un sistema de predicción que integre múltiples fuentes de datos clínicos, comparando diferentes enfoques de modelado:

* Modelo basado en datos estructurados (baseline)
* Modelo basado en texto clínico
* Modelo multimodal con fusión tardía (late fusion)
* Modelo multimodal con fusión temprana (early fusion)

3. Arquitectura del sistema

El sistema se implementa bajo una arquitectura cliente-servidor distribuida:

Frontend: Interfaz web desarrollada en Streamlit
Backend: API REST implementada con FastAPI
Modelo: Desarrollo experimental en entorno independiente

Flujo de funcionamiento:

  1. El usuario introduce datos clínicos en la interfaz web
  2. El frontend envía una solicitud HTTP al endpoint `/predict`
  3. El backend procesa la información y genera una predicción
  4. El resultado se devuelve al frontend para su visualización

Esta arquitectura permite desacoplar el desarrollo del modelo y la interfaz, facilitando la escalabilidad y mantenimiento del sistema.

4. Estructura del repositorio

proyecto

├── app.py                # Frontend (Streamlit)
├── api.py                # Backend (FastAPI)
├── model_training.ipynb  # Desarrollo y evaluación de modelos
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación

5. Implementación

 5.1 Frontend

El frontend fue desarrollado utilizando Streamlit, permitiendo:

* Captura de variables clínicas estructuradas
* Ingreso de texto clínico
* Visualización de resultados del modelo
* Representación gráfica del riesgo

5.2 Backend

El backend consiste en una API REST que expone el endpoint:

POST /predict

Este endpoint recibe los datos del paciente y devuelve:

json
{
  "probabilidad": float,
  "riesgo": "ALTO" | "BAJO"
}
```

5.3 Integración del modelo

El sistema implementa un mecanismo de simulación controlada dentro del backend. Esta decisión responde a la necesidad de:

* Garantizar disponibilidad del sistema
* Permitir validación end-to-end
* Desacoplar el desarrollo del modelo del despliegue

El modelo real se encuentra desarrollado y evaluado en el notebook:

model_training.ipynb

6. Modelado y experimentación

El desarrollo del modelo se realizó de manera independiente en el notebook `model_training.ipynb`, donde se incluyen:

* Preparación de datos
* Generación de variables textuales simuladas
* Entrenamiento de modelos
* Evaluación mediante métricas

Modelos evaluados:

* Baseline estructurado (Logistic Regression)
* Modelo de texto (TF-IDF + Logistic Regression)
* Late Fusion
* Early Fusion

Métricas utilizadas:

* AUC-ROC
* AUPRC
* Sensibilidad (Recall)
* Especificidad
* F1-score

7. Resultados

Los resultados experimentales muestran un desempeño elevado en el modelo baseline, lo cual sugiere la presencia de variables altamente discriminativas en el dataset utilizado.

La incorporación de información textual permite mantener o mejorar ligeramente el desempeño, validando la viabilidad del enfoque multimodal.

El modelo de fusión temprana presenta el mejor desempeño global, consistente con la literatura en sistemas multimodales.

8. Ejecución del proyecto

 8.1 Instalación de dependencias

bash
pip install -r requirements.txt

 8.2 Ejecución del backend

bash
uvicorn api:app --reload
 8.3 Ejecución del frontend

bash
streamlit run app.py
9. Consideraciones
* El sistema implementa una arquitectura desacoplada entre frontend, backend y modelo
* El modelo se desarrolla y valida de forma independiente
* La integración completa del modelo puede realizarse sustituyendo la lógica de simulación en el endpoint `/predict`

10. Conclusión

El proyecto demuestra la viabilidad de integrar múltiples fuentes de información en un sistema de predicción clínica, evidenciando que la incorporación de datos textuales puede complementar el desempeño de modelos basados únicamente en variables estructuradas.

Asimismo, se valida la implementación de una arquitectura distribuida que permite la evolución independiente de cada componente del sistema.

11. Trabajo futuro

* Integración completa del modelo en el backend
* Implementación de modelos más avanzados (transformers, deep learning)
* Evaluación en entornos reales de operación

