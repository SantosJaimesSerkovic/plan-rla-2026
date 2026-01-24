import streamlit as st

# 1. IDENTIDAD INSTITUCIONAL
st.set_page_config(page_title="SISTEMA PLAN-RLA", layout="wide")
st.title("SISTEMA PLAN-RLA")
st.markdown("### Consultoría de Soluciones Reales 2026-2031")

# 2. BASE DE DATOS SEMÁNTICA (Muestra estratégica de los 70 ítems)
base_datos = {
    "corrupcion": {
        "identificado": "Corrupción endémica en todos los niveles del aparato público.",
        "objetivo": "Crear la Central de Lucha Contra la Corrupción (CCC) con plenos poderes.",
        "meta": "Reducción sustancial de la impunidad y recuperación del principio de autoridad.",
        "pregunta": "Entiendo que te preocupa la falta de honestidad en el Estado. ¿Te refieres a las medidas contra la Corrupción?"
    },
    "seguridad": {
        "identificado": "Altos niveles de delincuencia, terrorismo urbano y extorsión.",
        "objetivo": "Unidades Itinerantes de Pacificación Ciudadana y tecnología de inteligencia.",
        "meta": "Reducción significativa de los índices de violencia y delincuencia común.",
        "pregunta": "La inseguridad es crítica. ¿Deseas conocer la estrategia para derrotar la Delincuencia y el Terrorismo Urbano?"
    },
    "hambre": {
        "identificado": "Pobreza extrema, desnutrición crónica infantil y anemia.",
        "objetivo": "Programa Hambre Cero: potenciar Ollas Comunes y compras a productores nacionales.",
        "meta": "Erradicar la anemia y desnutrición infantil para el 2026.",
        "pregunta": "La alimentación es prioridad. ¿Buscas el plan para erradicar el Hambre y la Pobreza Extrema?"
    },
    "trenes": {
        "identificado": "Marcado déficit de redes ferroviarias a nivel nacional.",
        "objetivo": "Recuperar la conectividad con redes modernas de pasajeros y carga.",
        "meta": "Construcción de la línea Tumbes-Tacna y el Tren Bioceánico.",
        "pregunta": "¿Tu consulta es sobre el desarrollo de Trenes y la conectividad ferroviaria nacional?"
    }
}

# 3. INTERFAZ DE USUARIO
query = st.text_input("Describe tu preocupación o escribe una palabra clave:").lower()

if query:
    encontrado = None
    for clave in base_datos:
        if clave in query:
            encontrado = clave
            break
    
    if encontrado:
        data = base_datos[encontrado]
        st.markdown("---")
        st.info(f"🔎 **ANÁLISIS:** {data['pregunta']}")
        
        if st.button("SÍ, CONFIRMO QUE ESTE ES EL TEMA"):
            st.subheader("✅ Propuesta Técnica del PLAN-RLA")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.error(f"**PROBLEMA IDENTIFICADO**\n\n{data['identificado']}")
            with col2:
                st.warning(f"**OBJETIVO ESTRATÉGICO**\n\n{data['objetivo']}")
            with col3:
                st.success(f"**META AL 2026**\n\n{data['meta']}")
    else:
        st.warning("⚠️ No logré detectar el tema exacto. Intenta con: 'Hambre', 'Seguridad', 'Trenes' o 'Corrupción'.")

st.sidebar.caption("SISTEMA PLAN-RLA v11.5")
