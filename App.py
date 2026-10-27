import streamlit as st

st.title("Clima en Chihuahua")

st.sidebar.header("Parámetros de Medición")

temp_input = st.sidebar.number_input("Temperatura (°C)", value=31, step=1)
hum_input = st.sidebar.number_input("Humedad (%)", value=68, min_value=0, max_value=100, step=1)
viento_input = st.sidebar.number_input("Velocidad del viento (km/h)", value=10, step=1)
llueve_input = st.sidebar.number_input("Lluvia (mm)", value=0, min_value=0, step=1)

medicion = [temp_input, hum_input, llueve_input, viento_input]

# 2. Extraer valores desde la lista
temperatura, humedad, llueve, viento = medicion

# 3. Clasificación de condiciones
if temperatura >= 30 and humedad >= 70:
    clasificacion = "Calor húmedo"
elif temperatura >= 30 and humedad < 70:
    clasificacion = "Calor seco"
elif 15 <= temperatura < 30 and llueve > 0:
    clasificacion = "Templado lluvioso"
elif 15 <= temperatura < 30 and llueve == 0:
    clasificacion = "Templado"
else:
    clasificacion = "Frío"

# Mostramos las métricas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Temperatura", value=f"{temperatura} °C", icon="🌡️")

with col2:
    st.metric(label="Humedad", value=f"{humedad}%", icon="💧")

with col3:
    st.metric(label="Viento", value=f"{viento} km/h", icon="💨")

with col4:
    st.metric(label="Lluvia", value=f"{llueve} mm", icon="🌧️")

alerta = temperatura >= 35 and humedad >= 70
alerta2 = llueve <= 10 and humedad >= 70
if alerta:
    st.error("⚠️ **ALERTA POR CALOR ACTIVADA:** Existe riesgo por altas temperaturas y humedad.")
elif alerta:
    st.success("✅ **Alerta por calor:** No activa.")
elif alerta2:
    st.error("⚠️ **ALERTA POR LLUVIA ACTIVADA:** Existe riesgo por inundaciones.")
elif alerta2:
    st.success("✅ **Alerta por lluvia:** No activa.")
