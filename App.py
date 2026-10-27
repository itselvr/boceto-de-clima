import streamlit as st

st.title("Clima en Chihuahua (Tiempo Real)")

st.sidebar.header("Parámetros de Medición")

temp_input = st.sidebar.number_input("Temperatura (°C)", value=31, step=1)
hum_input = st.sidebar.number_input("Humedad (%)", value=68, min_value=0, max_value=100, step=1)
llueve_input = st.sidebar.checkbox("¿Está lloviendo?", value=False)
# Guardar en la lista solicitada
medicion = [temp_input, hum_input, llueve_input]

# 2. Extraer valores desde la lista
temperatura, humedad, llueve, viento = medicion

# 3. Clasificación de condiciones
if temperatura >= 30 and humedad >= 70:
    clasificacion = "Calor húmedo"
elif temperatura >= 30 and humedad < 70:
    clasificacion = "Calor seco"
elif 15 <= temperatura < 30 and llueve:
    clasificacion = "Templado lluvioso"
elif 15 <= temperatura < 30 and not llueve:
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
