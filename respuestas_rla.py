import streamlit as st
import urllib.parse

# 1. IDENTIDAD Y CONFIGURACIÓN
st.set_page_config(page_title="PLAN-RLA: Consultor 2026", layout="wide")
st.title("SISTEMA PLAN-RLA")
st.markdown("### Hoja de Ruta Técnica y Soluciones Reales")

# 2. BASE DE DATOS MAESTRA (Extraída del Plan de Gobierno)
base_datos = {
    "friaje": {
        "problema_doc": "Poca atención ante el friaje en zonas altoandinas.", [cite: 31]
        "objetivo": "Crear el Sistema de Tambos para abastecimiento preventivo y casas térmicas.", [cite: 31]
        "meta": "Reducir impactos negativos del friaje y mejorar condiciones de vida de personas y animales.", [cite: 31]
        "confirmacion": "¿Tu consulta es sobre la protección ante el friaje en zonas altoandinas?"
    },
    "salud": {
        "problema_doc": "Invisibilidad de la especialidad Salud Familiar y falta de infraestructura.", [cite: 37, 40]
        "objetivo": "Impulsar la especialidad en Salud Familiar y fortalecer Centros de Atención Primaria.", [cite: 37, 40]
        "meta": "Módulo Nacional de Calificación Profesional y atención primaria con equipamiento completo.", [cite: 37, 40]
        "confirmacion": "¿Deseas conocer la reforma del sistema de salud y la medicina familiar?"
    },
    "vivienda": {
        "problema_doc": "Déficit de viviendas populares y falta de servicios básicos.", [cite: 28, 31]
        "objetivo": "Habilitar terrenos del Estado con acceso a redes de agua, desagüe y electricidad.", [cite: 28]
        "meta": "Viviendas sociales sismo resistentes y tanques de agua en zonas de pobreza extrema.", [cite: 28, 31]
        "confirmacion": "¿Te refieres al acceso a vivienda digna y servicios básicos?"
    },
    "mineria": {
        "problema_doc": "Deficiente participación nacional en la modernización de la minería.", [cite: 97]
        "objetivo": "Inversión en tecnología de última generación para una industria moderna y limpia.", [cite: 97]
        "meta": "Modernización minera compatible con el medio ambiente y la agricultura.", [cite: 97]
        "confirmacion": "¿Deseas ver el plan de modernización minera y protección ambiental?"
    },
    "gas": {
        "problema_doc": "Deficiente distribución de gas y alto costo del servicio.", [cite: 94]
        "objetivo": "Construcción de gaseoductos regionales para distribución domiciliaria (puerta a puerta).", [cite: 94]
        "meta": "Incremento sostenido del consumo de gas natural durante los 5 años de gestión.", [cite: 94]
        "confirmacion": "¿Tu interés es sobre la masificación y el costo del gas natural?"
    }
}

# 3. MOTOR DE BÚSQUEDA Y LÓGICA DE RESPUESTA
user_query = st.text_input("Escribe tu problema o necesidad aquí (ej. Friaje, Salud, Gas):").lower()

if user_query:
    encontrado = None
    for clave in base_datos:
        if clave in user_query:
            encontrado = clave
            break
    
    if encontrado:
        st.info(f"📍 **Identificado:** {base_datos[encontrado]['confirmacion']}")
        if st.button("SÍ, MOSTRAR SOLUCIÓN RLA"):
            data = base_datos[encontrado]
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.error(f"**PROBLEMA IDENTIFICADO**\n\n{data['problema_doc']}")
            with col2:
                st.warning(f"**OBJETIVO ESTRATÉGICO**\n\n{data['objetivo']}")
            with col3:
                st.success(f"**META AL 2026**\n\n{data['meta']}")
    else:
        st.warning("Escribe una palabra clave como 'Gas', 'Friaje', 'Vivienda' o 'Salud' para encontrar la solución técnica.")

st.sidebar.caption("PLAN-RLA v8.1 | Datos Oficiales 2026-2031")
