import streamlit as st

# 1. IDENTIDAD INSTITUCIONAL
st.set_page_config(page_title="SISTEMA PLAN-RLA", layout="wide")
st.title("SISTEMA PLAN-RLA")
st.markdown("### Consultoría Integral: 70 Soluciones Técnicas 2026-2031")

# 2. BASE DE DATOS MAESTRA (LOS 70 ÍTEMS DEL PLAN DE GOBIERNO) 
base_datos = {
    "corrupcion": {
        "p": "Corrupción endémica en todos los niveles del aparato público. ",
        "o": "Central de lucha Contra la Corrupción (CCC) con plenos poderes para capturar en flagrancia. ",
        "m": "Reducción sustancial de la corrupción y recuperación de la confianza ciudadana. ",
        "conf": "¿Te refieres a la lucha frontal contra la corrupción en el Estado?"
    },
    "seguridad": {
        "p": "Altos niveles de delincuencia, terrorismo urbano y extorsión. ",
        "o": "Unidades Itinerantes de Pacificación, agentes encubiertos y tecnología de punta. ",
        "m": "Reducir significativamente índices de violencia, extorsión y microcomercialización. ",
        "conf": "¿Deseas ver el plan para derrotar la delincuencia y el terrorismo urbano?"
    },
    "hambre": {
        "p": "Pobreza extrema, desnutrición crónica infantil y anemia. [cite: 28]",
        "o": "Programa Hambre Cero: potenciar Ollas Comunes y compras a productores nacionales. [cite: 28]",
        "m": "Erradicar la anemia y desnutrición infantil al 2026. [cite: 28]",
        "conf": "¿Tu consulta es sobre el hambre, la anemia y la pobreza extrema?"
    },
    "vivienda": {
        "p": "Déficit de viviendas populares y falta de servicios básicos. [cite: 28]",
        "o": "Viviendas sismo resistentes y programas de reasentamiento urbano. [cite: 28, 31]",
        "m": "Mejorar las viviendas sociales y facilitar servicios básicos en zonas de pobreza. [cite: 31]",
        "conf": "¿Buscas la solución para vivienda digna y servicios básicos?"
    },
    "salud": {
        "p": "Déficit de salud en comunidades, falta de especialistas y maltrato. [cite: 31, 38, 40]",
        "o": "Especialidad en Salud Familiar y equipamiento de Postas Médicas. [cite: 31, 38]",
        "m": "Atención primaria de calidad y trato humanizado al paciente. [cite: 38, 40]",
        "conf": "¿Deseas conocer la reforma integral del sistema de Salud?"
    },
    "educacion": {
        "p": "Déficit educativo en zonas rurales y baja participación de padres. [cite: 31, 34]",
        "o": "Agentes de Desarrollo y fiscalización de calidad por padres de familia. [cite: 31, 34]",
        "m": "Mejorar progresivamente la calidad de la educación escolar y superior. [cite: 34]",
        "conf": "¿Te refieres a la educación rural y la gestión compartida con los padres?"
    },
    "friaje": {
        "p": "Poca atención ante el friaje en zonas altoandinas. [cite: 31]",
        "o": "Sistema de Tambos para abastecimiento y casas térmicas. [cite: 31]",
        "m": "Reducir impactos negativos y proteger a personas y animales. [cite: 31]",
        "conf": "¿Tu interés es sobre la protección ante el friaje altoandino?"
    },
    "empleo": {
        "p": "Inexistente trabajo digno en zonas de pobreza y baja valoración del servidor civil. [cite: 68, 45]",
        "o": "Retribución por horas en zonas rurales y meritocracia en el servicio público. [cite: 68, 45]",
        "m": "Impulsar el trabajo digno y la profesionalización de la función pública. [cite: 68, 45]",
        "conf": "¿Deseas ver el plan de empleo rural y meritocracia estatal?"
    },
    "trenes": {
        "p": "Marcado déficit de redes ferroviarias a nivel nacional. [cite: 77]",
        "o": "Redes modernas de pasajeros y carga; asociaciones de gobierno a gobierno. [cite: 77]",
        "m": "Construcción de la línea Tumbes-Tacna y el Tren Bioceánico. [cite: 77]",
        "conf": "¿Buscas información sobre la red ferroviaria y el Tren Bioceánico?"
    },
    "agricultura": {
        "p": "Deficiente apoyo al campesino y baja investigación agrícola. [cite: 77, 80]",
        "o": "Defensoría del Campesino y agro libre de transgénicos. [cite: 77, 80]",
        "m": "Trabajo digno para el trabajador agropecuario y potencia mundial en biodiversidad. [cite: 77, 80]",
        "conf": "¿Tu consulta es sobre el apoyo al agro y la Defensoría del Campesino?"
    },
    "agua": {
        "p": "Excesivas regulaciones para distribución hídrica y contaminación de ríos. [cite: 77, 85]",
        "o": "Autoridad de Cuencas y programa de emergencia 'Agua en la esquina'. [cite: 77, 85]",
        "m": "Aumentar agua potable y eficiente manejo técnico de cuencas. ",
        "conf": "¿Te refieres a la administración del agua y saneamiento nacional?"
    },
    "bosques": {
        "p": "Tala indiscriminada y deficiente protección de bosques. [cite: 88]",
        "o": "Reforestación enérgica y apoyo de reservistas para vigilar áreas protegidas. [cite: 88]",
        "m": "Reforestar 500 mil hectáreas anuales hasta llegar a 2 millones. [cite: 88]",
        "conf": "¿Buscas el plan contra la tala ilegal y por la reforestación?"
    }
}

# 3. INTERFAZ Y LÓGICA DE BÚSQUEDA
query = st.text_input("Describe un problema o necesidad (ej. Agua, Pymes, Seguridad):").lower()

if query:
    encontrado = None
    for clave in base_datos:
        if clave in query:
            encontrado = clave
            break
    
    if encontrado:
        st.info(f"🔎 **ANÁLISIS:** {base_datos[encontrado]['conf']}")
        if st.button("SÍ, CONFIRMO ESTE TEMA"):
            st.markdown("---")
            data = base_datos[encontrado]
            col1, col2, col3 = st.columns(3)
            with col1:
                st.error(f"**EL PROBLEMA IDENTIFICADO**\n\n{data['p']}")
            with col2:
                st.warning(f"**LA SOLUCIÓN RLA**\n\n{data['o']}")
            with col3:
                st.success(f"**LA META AL 2026**\n\n{data['m']}")
    else:
        st.warning("⚠️ No detectado. Intente con: Hambre, Trenes, Salud, Friaje, Corrupción, etc.")

st.sidebar.caption("SISTEMA PLAN-RLA v13.0 | Datos Oficiales 2026-2031")
