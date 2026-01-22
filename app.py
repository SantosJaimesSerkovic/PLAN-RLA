import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="PLAN-RLA V7.2", layout="wide")

# Función para cargar los datos del Plan de Gobierno
@st.cache_data
def cargar_base_datos():
    try:
        # Cargamos el archivo que usted ya subió
        return pd.read_csv("datos_plan.csv")
    except:
        return None

df = cargar_base_datos()

st.title("🏛️ SISTEMA DE INTELIGENCIA ELECTORAL (NIE-IA)")
st.subheader("Versión 7.2 - Análisis de Propuestas PLAN-RLA")

if df is not None:
    st.info("✅ Base de datos del Plan de Gobierno cargada correctamente.")
    
    # El "Iniciador" por inquietud del usuario
    inquietud = st.text_input("Ingeniero, ¿cuál es el problema o tema que desea consultar?", 
                             placeholder="Ej: Corrupción, Delincuencia, Pobreza...")

    if inquietud:
        # Buscamos la palabra en la columna 'PROBLEMAS IDENTIFICADOS'
        resultados = df[df['PROBLEMAS IDENTIFICADOS'].str.contains(inquietud, case=False, na=False)]
        
        if not resultados.empty:
            for index, row in resultados.iterrows():
                st.warning(f"🔍 **PROBLEMA DETECTADO:** {row['PROBLEMAS IDENTIFICADOS']}")
                
                # Despliegue de las 3 columnas restantes
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.success("**OBJETIVOS ESTRATÉGICOS**")
                    st.write(row['OBJETIVOS ESTRATÉGICOS'])
                with col2:
                    st.success("**INDICADORES**")
                    st.write(row['INDICADORES'])
                with col3:
                    st.success("**METAS AL 2026**")
                    st.write(row['METAS AL 2026'])
                st.markdown("---")
        else:
            st.error(f"No se encontró información para '{inquietud}'. Intente con palabras del Plan como 'Ministerios' o 'Económico'.")
else:
    st.error("❌ Error: No se encontró el archivo 'datos_plan.csv'. Por favor verifique que el nombre sea exacto en GitHub.")

# Bitácora de Control en el menú lateral
with st.sidebar:
    st.header("Panel de Control V7.2")
    if st.button("Ver Bitácora"):
        st.write("- Repositorio: PLAN-RLA")
        st.write("- Base de Datos: datos_plan.csv")
        st.write("- Estado: Sincronizando IA")