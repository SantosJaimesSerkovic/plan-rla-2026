import streamlit as st

# 1. IDENTIDAD Y CONFIGURACION
st.set_page_config(page_title="Consultor RLA 2026", layout="centered")
st.title("SISTEMA NIE-IA: CONSULTOR 2026")

# 2. MOTOR DE TRIPLE FUENTE (PLAN + CANDIDATOS + RLA)
def buscar_respuestas(tema):
    datos = {
        "salud": ["Item 2000: Telemedicina y Medicina Natural", "Cuerpo Tecnico: Red de salud distrital", "Vision RLA: Atencion inmediata sin colas"],
        "seguridad": ["Item 0500: Escudo Digital e IA", "Cuerpo Tecnico: Patrullaje integrado", "Vision RLA: Cero tolerancia al crimen"]
    }
    return datos.get(tema, ["Propuesta en proceso", "Consulte con su candidato regional", "Vision RLA: Eficiencia total"])

# 3. INTERFAZ DE PREGUNTAS
st.subheader("1. Realiza tu Consulta")
pregunta = st.text_input("Ingresa el tema (Ej: Salud o Seguridad):").lower()

if pregunta:
    if st.button("GENERAR RESPUESTA"):
        clave = "salud" if "salud" in pregunta else "seguridad" if "seguridad" in pregunta else "otro"
        p, t, v = buscar_respuestas(clave)
        
        st.markdown("---")
        st.success(f"**Plan de Gobierno:** {p}")
        st.info(f"**Candidatos Regionales:** {t}")
        st.warning(f"**Vision RLA:** {v}")
