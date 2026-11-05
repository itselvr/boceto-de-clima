import streamlit as st
import requests

st.set_page_config(page_title="Clima en Chihuahua", page_icon="🌤️")
st.title("Clima Actual Chihuahua")

LATITUD = 28.6353
LONGITUD = -106.0889

@st.cache_data(ttl=600)  
def obtener_clima(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,rain,wind_speed_10m"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["current"]
    return None

datos_clima = obtener_clima(LATITUD, LONGITUD)

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

    st.sidebar.header("👕 RECOMENDACIÓN DE OUTFIT")
    
    if clasificacion == "Calor húmedo":
        outfit = "Ropa muy ligera y de tela transpirable (lino o algodón fino). Evita ropa ajustada."
        accesorios = "🕶️ Lentes de sol, protector solar y gorra o sombrero."
    elif clasificacion == "Calor seco":
        outfit = "Ropa fresca, manga corta o sin mangas, colores claros."
        accesorios = "🕶️ Lentes de sol, sombrero y abundante agua/bloqueador."
    elif clasificacion == "Templado lluvioso":
        outfit = "Impermeable o chaqueta resistente al agua, pantalones ligeros y calzado cerrado antiderrapante."
        accesorios = "☂️ Paraguas imprescindible y calzado impermeable."
    elif clasificacion == "Templado":
        outfit = "Camiseta cómoda con una chamarra ligera o suéter delgado fácil de quitar."
        accesorios = "👟 Calzado cómodo de diario."
    else:  # Frío
        outfit = "Vestimenta en capas: chamarra/abrigo grueso, suéter cálido y pantalones térmicos o gruesos."
        accesorios = "🧣 Bufanda, gorro y guantes si sales temprano o de noche."

    if llueve > 0 and clasificacion != "Templado lluvioso":
        accesorios += "\n\n🌧️ *Lleva un paraguas o impermeable por la lluvia registrada.*"

    st.sidebar.subheader(f"Para hoy ({clasificacion}):")
    st.sidebar.info(f"**Vestimenta:**\n{outfit}")
    st.sidebar.warning(f"**Accesorios sugeridos:**\n{accesorios}")

    st.subheader(f"Estado: {clasificacion}")

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
