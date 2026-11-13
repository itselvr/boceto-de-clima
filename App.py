import streamlit as st
import requests

st.set_page_config(page_title="Clima en Chihuahua", page_icon="🌤️")
st.title("Clima Actual Chihuahua")

LATITUD = 28.6353
LONGITUD = -106.0889
ESTILOS_CLIMA = {
    "Calor húmedo": {
        "fondo": "#ffe6cc", 
        "texto": "#1a1a1a", 
        "sidebar_fondo": "#ffd1a4"
    },
    "Calor seco": {
        "fondo": "#fff2cc", 
        "texto": "#1a1a1a", 
        "sidebar_fondo": "#ffe599"
    },
    "Templado lluvioso": {
        "fondo": "#2c3e50", 
        "texto": "#ffffff", 
        "sidebar_fondo": "#1a252f"
    },
    "Templado": {
        "fondo": "#e1eeec", 
        "texto": "#1a1a1a", 
        "sidebar_fondo": "#c2e0dc"
    },
    "Frío": {
        "fondo": "#1c2833", 
        "texto": "#ffffff", 
        "sidebar_fondo": "#111b24"
    },
}
IMAGENES_OUTFIT = {
    "Calor húmedo": "https://i.pinimg.com/736x/0d/01/02/0d0102d9671cc22e24529fb9b4d7395c.jpg",
    "Calor seco": "https://i.pinimg.com/736x/d8/24/f1/d824f19775acdc8d3884bae0535d4fba.jpg",
    "Templado lluvioso": "https://i.pinimg.com/1200x/97/df/11/97df1115e3f69a71d30a258ffe68822c.jpg",
    "Templado": "https://i.pinimg.com/1200x/44/8f/7c/448f7cecdffbc871c23e4cdc45369296.jpg",
    "Frío": "https://i.pinimg.com/1200x/24/4a/cb/244acb6a79e2b7f35f2d1f8ff01dd582.jpg",
}

@st.cache_data(ttl=600)  
def obtener_clima(lat, lon, version=2):
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
    uv = datos_clima.get("uv_index", 0.0)

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

    #clasificacion = "Templado lluvioso"
    estilo_actual = ESTILOS_CLIMA.get(
            clasificacion, 
            {"fondo": "#ffffff", "texto": "#000000", "sidebar_fondo": "#f0f2f6"}
        )
    st.markdown(
        f"""
        <style>
        /* 1. Fondo principal y color de texto */
        .stApp {{
            background-color: {estilo_actual["fondo"]};
            color: {estilo_actual["texto"]};
        }}
        .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6, .stApp p, .stApp span {{
            color: {estilo_actual["texto"]} !important;
        }}

        /* 2. Fondo de la barra lateral (Sidebar) */
        [data-testid="stSidebar"] {{
            background-color: {estilo_actual["sidebar_fondo"]} !important;
        }}
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] h4, [data-testid="stSidebar"] h5, [data-testid="stSidebar"] h6, 
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {{
            color: {estilo_actual["texto"]} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
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
    else:  
        outfit = "Vestimenta en capas: chamarra/abrigo grueso, suéter cálido y pantalones térmicos o gruesos."
        accesorios = "scarf Bufanda, gorro y guantes si sales temprano o de noche."

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
    with col5:
        st.metric(label="Rayos UV", value=f"{uv}")

    alerta_calor = temperatura >= 35 and humedad >= 70
    alerta_lluvia = llueve >= 10 and humedad >= 70

    if alerta_calor:
        st.error("⚠️ **ALERTA POR CALOR ACTIVADA:** Riesgo por altas temperaturas y humedad.")
    elif alerta_lluvia:
        st.error("⚠️ **ALERTA POR LLUVIA ACTIVADA:** Riesgo por inundaciones.")
    else:
        st.success("✅ **Alerta por clima:** No activa.")

    st.divider()
    st.subheader("📸 Outfit Recomendado")

    img_url = IMAGENES_OUTFIT.get(clasificacion)
    if img_url:
        st.image(img_url, caption=f"Estilo sugerido para {clasificacion}", width=350)    
else:
    st.error("No se pudieron obtener los datos meteorológicos en este momento.")
