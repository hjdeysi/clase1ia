import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Agenda de Reunión", layout="centered")

st.title("📅 Agenda de Reunión")

# Datos codificados directamente
agenda = [
    {"Hora": "09:00", "Tema": "Introducción y bienvenida", "Responsable": "Juan Pérez", "Duración (min)": 15},
    {"Hora": "09:15", "Tema": "Revisión de objetivos", "Responsable": "Marta Gómez", "Duración (min)": 30},
    {"Hora": "09:45", "Tema": "Informe de progreso", "Responsable": "Luis Ramírez", "Duración (min)": 45},
    {"Hora": "10:30", "Tema": "Pausa para café", "Responsable": "", "Duración (min)": 15},
    {"Hora": "10:45", "Tema": "Discusión de próximos pasos", "Responsable": "Ana Torres", "Duración (min)": 30},
    {"Hora": "11:15", "Tema": "Conclusiones y cierre", "Responsable": "Juan Pérez", "Duración (min)": 15},
]

# Crear DataFrame
df = pd.DataFrame(agenda)

# Mostrar tabla
st.subheader("🗓️ Detalles de la Agenda")
st.dataframe(df, use_container_width=True)

# Visualización de distribución de tiempo
st.subheader("⏰ Duración por Tema")

fig = px.pie(
    df[df["Duración (min)"] > 0],
    names="Tema",
    values="Duración (min)",
    title="Distribución de tiempo por tema",
    hole=0.4
)

st.plotly_chart(fig, use_container_width=True)

st.caption("Creado con ❤️ usando Streamlit.")
