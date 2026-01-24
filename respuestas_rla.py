import streamlit as st
import urllib.parse

# 1. IDENTIDAD Y CONFIGURACIÓN
st.set_page_config(page_title="PLAN-RLA: Inteligencia Electoral", layout="wide")
st.title("SISTEMA PLAN-RLA")
st.markdown("### Consultor de Soluciones Técnicas 2026-2031")

# 2. BASE DE DATOS INTEGRADA (Extraída del Plan de Gobierno)
# Se vinculan palabras clave con los Problemas Identificados del PDF
base_datos = {
    "corrupcion": {
        "problema_doc": "Corrupción endémica en todos los niveles del aparato público.", # [cite: 25]
        "objetivo": "Crear la Central de Lucha Contra la Corrupción (CCC) con plenos poderes para capturar en flagrancia.", # [cite: 25]
        "meta": "Reducción sustancial de los niveles de corrupción y recuperación del principio de autoridad.", # [cite: 25]
        "confirmacion": "¿Te refieres a la lucha contra la corrupción y la impunidad en el Estado?"
    },
    "seguridad": {
        "problema_doc": "Altos niveles de delincuencia, terrorismo urbano y extorsión.", # [cite: 25]
        "objetivo": "Unidades Itinerantes de Pacificación Ciudadana y tecnología de punta con apoyo de inteligencia extranjera.", # [cite: 25]
        "meta": "Reducción significativa de los índices de violencia, delincuencia común y microcomercialización de drogas.", # [cite: 25]
        "confirmacion": "¿Deseas conocer el plan para combatir la delincuencia y el terrorismo urbano?"
    },
    "hambre": {
        "problema_doc": "Pobreza extrema, desnutrición crónica infantil y anemia.", # [cite: 28]
        "objetivo": "Programa Hambre Cero, potenciando Ollas Comunes y comprando a productores nacionales.", # [cite: 28, 110]
        "meta": "Erradicar la anemia y desnutrición infantil para el 2026.", # [cite: 28, 110]
        "confirmacion": "¿Tu consulta es sobre la erradicación del hambre y la pobreza extrema?"
    },
    "agua": {
        "problema_doc": "Déficit de servicios básicos y falta de agua en zonas de pobreza extrema.", # [cite: 31]
        "objetivo": "Implementar tanques de agua y el programa de emergencia 'Agua en la esquina'.", # 
        "meta": "Garantizar agua potable de calidad y servicios básicos en todo el país.", # [cite: 85, 86]
        "confirmacion": "¿Te interesa conocer la solución para el acceso al agua potable y saneamiento?"
    }
}

# 3. LÓGICA DEL PREGUNTADOR (Buscador semántico)
user_query = st.text_input("Describe el problema que te preocupa (ej. Inseguridad, Corrupción, Hambre):").lower()

if user_query:
    encontrado = None
    # Busca coincidencia de palabras clave en la consulta
    for clave in base_datos:
        if clave in user_query:
            encontrado = clave
            break
    
    if encontrado:
        st.info(f"📍 **Identificado:** {base_datos[encontrado]['confirmacion']}")
        if st.button("SÍ, ESTO ES LO QUE BUSCO"):
            data = base_datos[encontrado]
            st.markdown("---")
            st.subheader(f"✅ Propuesta Técnica del PLAN-RLA")
            
            # Despliegue de las 3 columnas solicitadas
            col1, col2, col3 = st.columns(3)
            with col1:
                st.error(f"**PROBLEMA IDENTIFICADO**\n\n{data['problema_doc']}")
            with col2:
                st.warning(f"**OBJETIVO ESTRATÉGICO**\n\n{data['objetivo']}")
            with col3:
                st.success(f"**META AL 2026**\n\n{data['meta']}")
    else:
        st.warning("No logré identificar el tema exacto. Por favor, intenta con palabras como 'Seguridad', 'Hambre', 'Agua' o 'Corrupción'.")

st.sidebar.caption("SISTEMA PLAN-RLA v8.0")
