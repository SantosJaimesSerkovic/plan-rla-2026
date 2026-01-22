import streamlit as st

# 1. IDENTIDAD
st.set_page_config(page_title="Consultor NIE-IA RLA", page_icon="🔵")
st.markdown("<h1 style='text-align: center; color: #003366;'>SISTEMA NIE-IA: CONSULTOR 2026</h1>", unsafe_allow_html=True)

# 2. BASE DE DATOS INTEGRADA (Contenido completo para áreas rurales)
mapeo_estrategico = {
    "salud": {
        "titulo": "Salud y Bienestar",
        "item": "Item 2000",
        "detalle": "Implementacion de Telemedicina con IA y Red de Postas Medicas 24/7. Uso de medicina natural y preventiva para reducir colas en hospitales nacionales.",
        "icono": "🏥"
    },
    "seguridad": {
        "titulo": "Seguridad Ciudadana",
        "item": "Item 0500",
        "detalle": "Plan Escudo Digital: Camaras con reconocimiento facial, drones de vigilancia y fortalecimiento de las Rondas Campesinas con tecnologia y comunicacion directa.",
        "icono": "🛡️"
    },
    "carretera": {
        "titulo": "Infraestructura y Transportes",
        "item": "Item 2500",
        "detalle": "Construccion de Caminos de Herradura y Carreteras Asfaltadas para conectar el agro con el mercado. Tren de la Costa y eliminacion de peajes corruptos.",
        "icono": " soloist🛣️"
    },
    "agua": {
        "titulo": "Agua y Desague",
        "item": "Item 1000",
        "detalle": "Agua para todos mediante plantas desalinizadoras en la costa y represas tecnificadas en la sierra. Cero anemia mediante agua potable de calidad.",
        "icono": "💧"
    }
}

# 3. PREGUNTADOR
st.subheader("1. Tu Consulta")
entrada = st.text_input("¿Que necesita su localidad? (Ej: Carretera, Agua, Salud)").lower()

if entrada:
    tema_clave = next((k for k in mapeo_estrategico if k in entrada), None)
    
    if tema_clave:
        info = mapeo_estrategico[tema_clave]
        st.markdown(f"### {info['icono']} Tema: **{info['titulo']}**")
        
        if st.button("VER PROPUESTA COMPLETA"):
            st.markdown("---")
            # RESPUESTA EXPANDIDA PARA MOVIL
            st.error(f"📖 **PLAN DE GOBIERNO ({info['item']}):**\n\n{info['detalle']}")
            
            st.success(f"👷 **CUERPO TECNICO:**\n\nNuestros candidatos ejecutaran este plan priorizando la mano de obra local y materiales de la region.")
            
            st.warning(f"🦁 **VISION RLA:**\n\n'Dinero hay, lo que sobra son ladrones'. Con gestion honesta, este proyecto se hara realidad sin adendas corruptas.")
            
            st.markdown("---")
            st.caption("Fuente oficial: Plan de Gobierno Renovacion Popular 2026")
    else:
        st.warning("Escriba una palabra clave como: Salud, Seguridad, Carretera o Agua.")
