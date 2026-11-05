import streamlit as st
import requests

st.set_page_config(page_title="Clima en Vivo", page_icon="🌤️")
st.title("Clima en Vivo")

CIUDADES = {
    "Chihuahua, MX": {"lat": 28.6353, "lon": -106.0889},
    "Ciudad Juárez, MX": {"lat": 31.7394, "lon": -106.4869},
    "Ciudad de México, MX": {"lat": 19.4326, "lon": -99.1332},
    "Monterrey, MX": {"lat": 25.6866, "lon": -100.3161},
}

st.sidebar.header("Ubicación y Configuración")
ciudad_seleccionada = st.sidebar.selectbox("Selecciona una ciudad", list(CIUDADES.keys()))

@st.cache_data(ttl=600)  
def obtener_clima(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,rain,wind_speed_10m"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["current"]
    return None

coords = CIUDADES[ciudad_seleccionada]
datos_clima = obtener_clima(coords["lat"], coords["lon"])

if st.sidebar.button("🔄 Actualizar Datos"):
    st.cache_data.clear()
    st.rerun()

if datos_clima:
    temperatura = datos_clima["temperature_2m"]
    humedad = datos_clima["relative_humidity_2m"]
    llueve = datos_clima["rain"]
    viento = datos_clima["wind_speed_10m"]

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

    st.subheader(f"Estado en {ciudad_seleccionada}: {clasificacion}")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Temperatura", value=f"{temperatura} °C")
    with col2:
        st.metric(label="Humedad", value=f"{humedad}%")
    with col3:
        st.metric(label="Viento", value=f"{viento} km/h")
    with col4:
        st.metric(label="Lluvia", value=f"{llueve} mm")

    alerta_calor = temperatura >= 35 and humedad >= 70
    alerta_lluvia = llueve >= 10 and humedad >= 70

    if alerta_calor:
        st.error("⚠️ **ALERTA POR CALOR ACTIVADA:** Riesgo por altas temperaturas y humedad.")
    elif alerta_lluvia:
        st.error("⚠️ **ALERTA POR LLUVIA ACTIVADA:** Riesgo por inundaciones.")
    else:
        st.success("✅ **Alerta por clima:** No activa.")
else:
    st.error("No se pudieron obtener los datos meteorológicos en este momento.")
