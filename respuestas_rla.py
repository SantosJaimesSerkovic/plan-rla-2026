import streamlit as st import urllib.parse

# 1. IDENTIDAD INSTITUCIONAL
st.set_page_config(page_title="PLAN-RLA", layout="wide") st.title("SISTEMA PLAN-RLA") st.markdown("### Hoja de Ruta Técnica 2026-2031")

# 2. MATRIZ ESTRATÉGICA
plan = { "Seguridad": { "p": "Altos niveles de delincuencia y extorsión.", "s": "Unidades de Pacificación e Inteligencia Artificial.", "m": "Reducción del 50% en la victimización en 2 años." }, "Hambre": { "p": "Desnutrición y pobreza extrema en zonas vulnerables.", "s": "Potenciar Ollas Comunes como centros de producción.", "m": "Hambre Cero y erradicación de la anemia infantil." }, "Corrupción": { "p": "Mafias enquistadas que roban el dinero público.", "s": "Creación de la Central de Lucha Contra la Corrupción CCC.", "m": "Ahorro de 20 mil millones de soles anuales." } }

# 3. INTERFAZ Y LÓGICA
tema = st.selectbox("Seleccione un eje estratégico:", ["Seleccione...", "Seguridad", "Hambre", "Corrupción"])

if tema != "Seleccione...": res = plan[tema] col1, col2, col3 = st.columns(3)

st.sidebar.caption("SISTEMA PLAN-RLA v7.1")
