import streamlit as st

# Configuración de la página
st.set_page_config(page_title="SISTEMA NIE-IA V7.2", layout="wide")

st.title("🏛️ SISTEMA DE INTELIGENCIA ELECTORAL (NIE-IA)")
st.subheader("Versión 7.2 - Control Estratégico")

st.info("Bienvenido, Ingeniero. El sistema está listo para procesar la base de datos de propuestas.")

# Sidebar para navegación
with st.sidebar:
    st.header("Panel de Control")
    opcion = st.radio("Seleccione Módulo:", ["Resumen Ejecutivo", "Análisis de Propuestas", "Bitácora V7.2"])

if opcion == "Resumen Ejecutivo":
    st.write("### Estado Actual del Plan de Gobierno")
    st.write("- Integración con Google Sheets: Pendiente")
    st.write("- Procesamiento de IA: Activo")

elif opcion == "Bitácora V7.2":
    st.write("### Registro de Avances")
    st.success("✅ Repositorio creado en GitHub")
    st.warning("⏳ Pendiente: Carga de base de datos de Renovación Popular")
