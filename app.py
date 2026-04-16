import requests
import streamlit as st
import matplotlib.pyplot as plt

# -------------------------
# CONFIGURACIÓN
# -------------------------
st.set_page_config(page_title="Sistema de Predicción Médica", layout="wide")

# -------------------------
# ESTILO
# -------------------------
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #0066cc;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.title("Sistema de Predicción de Reingreso Hospitalario")
st.markdown("### Modelo Multimodal basado en datos clínicos y texto")

st.divider()

# -------------------------
# LAYOUT
# -------------------------
col1, col2 = st.columns([1,1])

# -------------------------
# INPUTS
# -------------------------
with col1:
    st.subheader("Datos del paciente")

    edad = st.number_input("Edad", min_value=0, max_value=120)
    frecuencia_cardiaca = st.number_input("Frecuencia cardiaca")
    presion = st.number_input("Presión arterial")

    st.subheader("Información clínica")
    nota_clinica = st.text_area("Notas clínicas", height=200)

# -------------------------
# RESULTADOS
# -------------------------
with col2:
    st.subheader("Resultados del modelo")

    if st.button("Predecir riesgo"):

        data = {
            "edad": edad,
            "frecuencia_cardiaca": frecuencia_cardiaca,
            "presion": presion,
            "nota_clinica": nota_clinica
        }

        import requests

        try:
            response = requests.post(
                "https://an-lisis-multimodal-de-registros-m-dicos.onrender.com/predict",
                json=data
            )

            result = response.json()
            probabilidad = result["probabilidad"]

        except:
            st.error("No se pudo conectar con la API")
            probabilidad = 0.5

        st.success("Predicción generada")

        st.metric(
            "Riesgo de reingreso",
            "ALTO" if probabilidad > 0.5 else "BAJO"
        )
        st.metric(
            "Probabilidad",
            f"{probabilidad*100:.1f}%"
        )
        st.divider()

        # GRÁFICA DE PASTEL
        st.subheader("Distribución de riesgo")

        sizes = [probabilidad, 1 - probabilidad]
        labels = ["Alto riesgo", "Bajo riesgo"]
        colors = ["#FF4B4B", "#00C49A"]

        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(2.2, 2.2))

        ax.pie(
            sizes,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            startangle=90,
            textprops={'fontsize': 8}
        )

        ax.axis('equal')

        st.pyplot(fig)

        # INTERPRETACIÓN
        st.subheader("Interpretación")

        if probabilidad > 0.7:
            st.error("Riesgo alto: se recomienda atención prioritaria")
        elif probabilidad > 0.4:
            st.warning("Riesgo moderado: monitoreo recomendado")
        else:
            st.success("Riesgo bajo")
# -------------------------
# FOOTER
# -------------------------
st.divider()
st.caption("Prototipo académico - Inteligencia Artificial en Salud")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
