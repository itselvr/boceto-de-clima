import streamlit as st
import pandas as pd
import numpy as np

st.title("Ejemplo de st.metric")

# 1. Métrica básica
st.metric(
    label="Ventas Totales",
    value="$12,450",
    delta="$1,200",
    help="Ventas netas acumuladas en el último mes"
)

st.divider()

# 2. Métrica con borde e icono
st.metric(
    label="Usuarios Activos",
    value="1,842",
    delta="-5%",
    delta_color="normal",  # Verde si sube, rojo si baja
    icon="👥",
    border=True,
    help="Usuarios activos en los últimos 7 días"
)

st.divider()

# 3. Métrica con indicador inverso (p. ej. tiempo de respuesta: bajar es bueno)
st.metric(
    label="Tiempo de Respuesta",
    value="240 ms",
    delta="-45 ms",
    delta_color="inverse",  # Invierte los colores: el delta negativo se muestra en verde
    border=True
)

st.divider()

# 4. Métrica avanzada con gráfico de tendencia integrado (mini-sparkline)
datos_tendencia = pd.DataFrame({
    "tendencia": np.random.randn(15).cumsum() + 50
})

st.metric(
    label="Rendimiento del Servidor",
    value="98.5%",
    delta="+1.2%",
    border=True,
    chart_data=datos_tendencia,
    chart_type="line",
    help="Porcentaje de uptime en las últimas 24 horas"
)
