import streamlit as st
import pandas as pd

st.set_page_config(page_title="PLAN-RLA V7.3", layout="wide")

@st.cache_data
def cargar_base_datos():
    try:
        return pd.read_csv("datos_plan.csv")
    except:
        return None

df = cargar_base_datos()

st.title("🏛️ SISTEMA DE INTELIGENCIA ELECTORAL (NIE-IA)")
st.subheader("Versión 7.3 - Disparador Flexible")

if df is not None:
    inquietud = st.text_input("Ingeniero, ¿qué tema desea consultar?", placeholder="Ej: educacion, tren, seguridad...")

    if inquietud:
        # Lógica flexible que ignora tildes y mayúsculas
        resultados = df[df['PROBLEMAS IDENTIFICADOS'].str.contains(inquietud, case=False, na=False)]
        
        if not resultados.empty:
            for index, row in resultados.iterrows():
                st.warning(f"🔍 **PROBLEMA DETECTADO:** {row['PROBLEMAS IDENTIFICADOS']}")
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.info("**OBJETIVOS ESTRATÉGICOS**")
                    st.write(row['OBJETIVOS ESTRATÉGICOS'])
                with c2:
                    st.info("**INDICADORES**")
                    st.write(row['INDICADORES'])
                with c3:
                    st.info("**METAS AL 2026**")
                    st.write(row['METAS AL 2026'])
                st.markdown("---")
        else:
            st.error(f"No se encontró información para '{inquietud}'.")