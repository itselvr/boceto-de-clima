import streamlit as st

st.title("Clima en Chihuahua (Tiempo Real)")

st.sidebar.header("Parámetros de Medición")

temp_input = st.sidebar.number_input("Temperatura (°C)", value=31, step=1)
hum_input = st.sidebar.number_input("Humedad (%)", value=68, min_value=0, max_value=100, step=1)
viento_input = st.sidebar.number_input("Velocidad del viento (km/h)", value=10, step=1)
llueve_input = st.sidebar.checkbox("¿Está lloviendo?", value=False)

if temperatura >= 30:
    if humedad >= 70:
        clasificacion = "Calor húmedo"
    else:
        clasificacion = "Calor seco"
elif 15 <= temperatura < 30:
    if llueve:
        clasificacion = "Templado lluvioso"
    else:
        clasificacion = "Templado"
else:
    clasificacion = "Frío"

# Agregar la condición de viento a la clasificación final
if viento >= 20:
    clasificacion += " con viento fuerte"

# 4. Despliegue en Streamlit
st.subheader(f"Estado del tiempo: {clasificacion}")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Temperatura", value=f"{temperatura} °C", icon="🌡️")

with col2:
    st.metric(label="Humedad", value=f"{humedad}%", icon="💧")

with col3:
    st.metric(label="Lluvia", value="Sí" if llueve else "No", icon="🌧️")

with col4:
    st.metric(label="Viento", value=f"{viento} km/h", icon="💨")
