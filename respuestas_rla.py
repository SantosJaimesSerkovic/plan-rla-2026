import streamlit as st 
import urllib.parse

1. IDENTIDAD INSTITUCIONAL: PLAN-RLA
st.set_page_config(page_title="PLAN-RLA: Soluciones para el Perú", layout="wide") st.markdown("<h1 style='text-align: center; color: #003366;'>SISTEMA PLAN-RLA</h1>", unsafe_allow_html=True) st.markdown("<p style='text-align: center;'><b>Hoja de Ruta Técnica 2026-2031</b></p>", unsafe_allow_html=True)

2. MATRIZ ESTRATÉGICA (Problema - Solución - Meta)
plan = { "Seguridad Ciudadana": { "problema": "Altos niveles de delincuencia, terrorismo urbano y extorsión.", "objetivo": "Unidades Itinerantes de Pacificación y uso de IA para captura en flagrancia.", "meta": "Reducción del 50% de la victimización delictiva en 2 años.", "icono": "🛡️" }, "Lucha Contra el Hambre": { "problema": "Desnutrición y pobreza extrema en zonas vulnerables.", "objetivo": "Potenciar Ollas Comunes como productoras con compras estatales directas.", "meta": "Hambre Cero y erradicación de la anemia infantil.", "icono": "🍲" }, "Cero Corrupción": { "problema": "Mafias enquistadas que roban el dinero de los más pobres.", "objetivo": "Creación de la Central de Lucha Contra la Corrupción (CCC) autónoma.", "meta": "Ahorro de 20 mil millones de soles anuales recuperados.", "icono": "⚖️" } }

3. INTERFAZ DE USUARIO
tema = st.selectbox("¿Qué problema deseas que Rafael solucione?", ["Seleccione...", "Seguridad Ciudadana", "Lucha Contra el Hambre", "Cero Corrupción"])

if tema != "Seleccione...": data = plan[tema] st.markdown(f"## {data['icono']} {tema}") col1, col2, col3 = st.columns(3) with col1: st.error(f"EL PROBLEMA\n\n{data['problema']}") with col2: st.warning(f"LA SOLUCIÓN RLA\n\n{data['objetivo']}") with col3: st.success(f"LA META 2026\n\n{data['meta']}")

st.sidebar.image("", width=150) st.sidebar.caption("PLAN-RLA v5.1")

