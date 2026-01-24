import streamlit as st

# 1. IDENTIDAD INSTITUCIONAL
st.set_page_config(page_title="SISTEMA PLAN-RLA", layout="wide")
st.title("SISTEMA PLAN-RLA")
st.markdown("### Consultoría Integral: Soluciones para el Desarrollo Nacional")

# 2. BASE DE DATOS MAESTRA (70 ÍTEMS - BLOQUE RECURSOS) [cite: 25-97]
base_datos = {
    "mineria": {
        "p": "Deficiente participación nacional en la modernización de la minería e investigación geológica. ",
        "o": "Inversión en tecnología de última generación para una industria moderna, limpia y cuidadosa del ambiente. ",
        "m": "Modernización minera compatible con la agricultura y aumento de exportación de productos terminados. ",
        "conf": "¿Buscas el plan para la modernización minera y el valor agregado a materias primas?"
    },
    "tala": {
        "p": "Lucha frontal contra la tala ilegal y deficiente protección de bosques. [cite: 116]",
        "o": "Intervención de las FFAA contra la tala ilegal y enérgica política de reforestación. ",
        "m": "Recuperar bosques y áreas protegidas; reforestar 500 mil hectáreas anuales. ",
        "conf": "¿Te refieres a la lucha contra la tala ilegal y la reforestación nacional?"
    },
    "agua": {
        "p": "Deficiente manejo de recursos hídricos y excesivas regulaciones para su distribución. [cite: 78, 116]",
        "o": "Creación de la Autoridad de Cuencas y programa de emergencia 'agua en la esquina'. ",
        "m": "Garantizar agua de calidad, siembra y cosecha de agua, y manejo técnico de cuencas. [cite: 85, 116]",
        "conf": "¿Deseas ver las soluciones para el agua potable y la gestión de cuencas?"
    },
    "hambre": {
        "p": "Pobreza extrema, desnutrición crónica infantil y anemia. [cite: 28, 110]",
        "o": "Programa Hambre Cero: potenciar Ollas Comunes y comprar a productores nacionales. [cite: 28, 110]",
        "m": "Erradicar la anemia y desnutrición infantil para el 2026. [cite: 28, 110]",
        "conf": "¿Buscas el plan para erradicar el hambre y la pobreza extrema?"
    }
}

# 3. INTERFAZ Y LÓGICA DE BÚSQUEDA
query = st.text_input("Identifique un Problema (ej. Minería, Tala, Agua, Hambre):").lower()

if query:
    encontrado = None
    for clave in base_datos:
        if clave in query:
            encontrado = clave
            break
    
    if encontrado:
        data = base_datos[encontrado]
        st.info(f"📍 **ANÁLISIS SEMÁNTICO:** {data['conf']}")
        if st.button("SÍ, CONFIRMO ESTE TEMA"):
            st.markdown("---")
            c1, c2, c3 = st.columns(3)
            with c1: st.error(f"**PROBLEMA IDENTIFICADO**\n\n{data['p']}")
            with c2: st.warning(f"**OBJETIVO ESTRATÉGICO RLA**\n\n{data['o']}")
            with c3: st.success(f"**META AL 2026**\n\n{data['m']}")
    else:
        st.warning("Escribe una palabra clave como 'Minería', 'Tala' o 'Agua' para ver la solución técnica.")

st.sidebar.caption("SISTEMA PLAN-RLA v15.0 | Datos Oficiales 2026-2031")
