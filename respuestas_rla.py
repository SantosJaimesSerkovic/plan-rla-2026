import streamlit as st

# 1. IDENTIDAD
st.set_page_config(page_title="SISTEMA PLAN-RLA", layout="wide")
st.title("SISTEMA PLAN-RLA")
st.markdown("### Consultoría Integral de Soluciones 2026-2031")

# 2. BASE DE DATOS MAESTRA (EXTRAÍDA TOTALMENTE DEL PDF)
base_datos = {
    "seguridad": {
        "p": "Altos niveles de delincuencia, terrorismo urbano y extorsión.",
        "o": "Unidades Itinerantes de Pacificación Ciudadana y tecnología de punta.",
        "m": "Reducción significativa de índices de violencia y microcomercialización.",
        "conf": "¿Deseas conocer el plan contra la delincuencia y el terrorismo urbano?"
    },
    "corrupcion": {
        "p": "Corrupción endémica en todos los niveles del aparato público.",
        "o": "Crear la Central de Lucha Contra la Corrupción (CCC) con plenos poderes.",
        "m": "Reducción sustancial de la impunidad y recuperación del ahorro público.",
        "conf": "¿Te refieres a la lucha contra la corrupción estatal?"
    },
    "hambre": {
        "p": "Pobreza extrema, desnutrición crónica infantil y anemia.",
        "o": "Programa Hambre Cero: potenciar Ollas Comunes y compras estatales.",
        "m": "Erradicar la anemia y desnutrición infantil para el 2026.",
        "conf": "¿Tu interés es sobre el combate al hambre y la anemia?"
    },
    "agua": {
        "p": "Déficit de servicios básicos y falta de agua en zonas de pobreza.",
        "o": "Tanques de agua y programa 'Agua en la esquina'.",
        "m": "Garantizar agua potable de calidad y saneamiento para todos.",
        "conf": "¿Buscas la solución para el acceso al agua potable?"
    },
    "bosques": {
        "p": "Deficiente protección de bosques y tala ilegal.",
        "o": "Fortalecer OEFA y SERFOR, e intervenir con las FFAA contra la tala ilegal.",
        "m": "Recuperación de áreas protegidas y reducción de la actividad ilegal.",
        "conf": "¿Te interesa la protección de nuestros bosques y medio ambiente?"
    },
    "empleo": {
        "p": "Elevada informalidad laboral y baja productividad.",
        "o": "Reforma laboral para la formalización y apoyo a emprendedores.",
        "m": "Incremento de empleos dignos y reducción de la brecha de informalidad.",
        "conf": "¿Deseas ver el plan de formalización y creación de empleo?"
    },
    "friaje": {
        "p": "Poca atención ante el friaje en zonas altoandinas.",
        "o": "Sistema de Tambos y construcción de casas térmicas.",
        "m": "Protección efectiva de la vida humana y el ganado ante el frío.",
        "conf": "¿Tu consulta es sobre la protección ante el friaje?"
    },
    "educacion": {
        "p": "Bajo nivel educativo y falta de infraestructura tecnológica.",
        "o": "Modernización de mallas curriculares y acceso universal a internet.",
        "m": "Mejora en los rankings internacionales de educación y conectividad total.",
        "conf": "¿Te refieres a la reforma educativa y tecnológica?"
    }
}

# 3. MOTOR DE BÚSQUEDA
query = st.text_input("Identifique un Problema (ej. Agua, Bosques, Hambre, Seguridad):").lower()

if query:
    encontrado = None
    for clave in base_datos:
        if clave in query:
            encontrado = clave
            break
    
    if encontrado:
        data = base_datos[encontrado]
        st.info(f"📍 **Tema Detectado:** {data['conf']}")
        if st.button("CONFIRMAR Y VER SOLUCIÓN"):
            st.markdown("---")
            c1, c2, c3 = st.columns(3)
            with c1: st.error(f"**PROBLEMA IDENTIFICADO**\n\n{data['p']}")
            with c2: st.warning(f"**OBJETIVO ESTRATÉGICO**\n\n{data['o']}")
            with c3: st.success(f"**META AL 2026**\n\n{data['m']}")
    else:
        st.warning("Palabra clave no encontrada. Intente con términos del Plan de Gobierno.")

st.sidebar.caption("SISTEMA PLAN-RLA v9.0")
