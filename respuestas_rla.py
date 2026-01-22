import streamlit as st import urllib.parse

1. IDENTIDAD INSTITUCIONAL: PLAN-RLA
st.set_page_config(page_title="PLAN-RLA: Consultor 2026", page_icon="🔵") st.markdown("<h1 style='text-align: center; color: #003366;'>SISTEMA PLAN-RLA</h1>", unsafe_allow_html=True) st.markdown("<p style='text-align: center;'><b>Ideario Humanista y Cristiano</b></p>", unsafe_allow_html=True)

2. MATRIZ ESTRATÉGICA (Extraída del Plan de Gobierno 2026-2031)
plan_maestro = { "corrupcion": { "problema": "Corrupción endémica en todos los niveles del aparato público.", "objetivo": "Crear la Central de Lucha Contra la Corrupción (CCC) con plenos poderes.", "meta": "Reducción sustancial de la corrupción y recuperación de la confianza.", "icono": "⚖️" }, "seguridad": { "problema": "Altos niveles de delincuencia, terrorismo urbano y extorsión.", "objetivo": "Unidades Itinerantes de Pacificación Ciudadana y tecnología de punta.", "meta": "Reducir significativamente los índices de violencia y delincuencia.", "icono": "🛡️" }, "hambre": { "problema": "Pobreza extrema y desnutrición crónica infantil.", "objetivo": "Potenciar Ollas Comunes y convertirlas en centros de emprendimiento.", "meta": "Erradicar la anemia y desnutrición infantil comprando productos nacionales.", "icono": "🍲" }, "rendicion": { "problema": "Falta de transparencia en el cumplimiento de las metas del plan.", "objetivo": "Informe anual presidencial cada 28 de julio ante la representación nacional.", "meta": "Crecimiento anual del PBI al 7% e inflación inferior al 2.5%.", "icono": "📊" } }

3. INTERFAZ DE USUARIO
st.subheader("⚠️ ¿Cuál es el problema que más te preocupa hoy?") opcion = st.selectbox("Selecciona para ver la solución del PLAN-RLA:", ["Seleccione...", "Corrupción", "Seguridad", "Hambre", "Rendición"])

if 'votos' not in st.session_state: st.session_state.votos = {"corrupcion": 150, "seguridad": 280, "hambre": 310, "rendicion": 95}

if opcion != "Seleccione...": clave = opcion.lower().replace("ó", "o") data = plan_maestro[clave] st.markdown(f"### {data['icono']} Respuesta Integral PLAN-RLA") st.error(f"❌ EL PROBLEMA IDENTIFICADO: {data['problema']}") st.warning(f"💡 EL OBJETIVO ESTRATÉGICO RLA: {data['objetivo']}") st.success(f"✅ LA META AL 2026: {data['meta']}") st.markdown("---") if st.button(f"👍 SÍ, EL PLAN-RLA DEBE PRIORIZAR ESTO"): st.session_state.votos[clave] += 1 st.balloons() st.success(f"Voto registrado. Tu opinión ayuda a priorizar las soluciones.") mensaje = f"Mira la solución del PLAN-RLA para {opcion}: https://www.google.com/search?q=https://plan-rla-2026.streamlit.app/" st.markdown(f"")

st.sidebar.image("", width=100) st.sidebar.caption("SISTEMA PLAN-RLA v5.0")
