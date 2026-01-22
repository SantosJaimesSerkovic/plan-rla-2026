import streamlit as st

st.set_page_config(page_title="Consultor RLA 2026", layout="centered")
st.title("SISTEMA NIE-IA: CONSULTOR 2026")

# 1. DICCIONARIO DE ADAPTACION (El Cerebro del Preguntador)
mapeo_temas = {
    "salud": {"titulo": "Salud y Bienestar", "codigo": "2000"},
    "seguridad": {"titulo": "Seguridad Ciudadana", "codigo": "0500"},
    "carretera": {"titulo": "Infraestructura y Transportes", "codigo": "2500"},
    "via": {"titulo": "Infraestructura y Transportes", "codigo": "2500"},
    "agua": {"titulo": "Infraestructura Humana (Agua/Desague)", "codigo": "1000"},
    "hambre": {"titulo": "Lucha contra la Pobreza", "codigo": "1500"}
}

# 2. INTERFAZ DEL PREGUNTADOR
st.subheader("1. Realiza tu Consulta")
entrada = st.text_input("¿Que necesidad tiene su localidad?").lower()

if entrada:
    # Lógica de Adaptación
    tema_detectado = next((key for key in mapeo_temas if key in entrada), None)
    
    if tema_detectado:
        config = mapeo_temas[tema_detectado]
        # CONFIRMACION AL USUARIO
        st.write(f"🔍 **Tema Identificado:** {config['titulo']} (Item {config['codigo']})")
        st.write(f"⚙️ **Adaptando pregunta para el Respondedor...**")
        
        if st.button(f"CONFIRMAR Y BUSCAR PROPUESTA"):
            # 3. EL RESPONDEDOR (Activado tras confirmación)
            st.markdown("---")
            st.subheader(f"Respuesta Oficial: {config['titulo']}")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.info("**Plan de Gobierno**\n\nMejora integral segun Item " + config['codigo'])
            with col2:
                st.success("**Cuerpo Tecnico**\n\nEjecucion regional prioritaria.")
            with col3:
                st.warning("**Vision RLA**\n\nCero corrupcion en la obra publica.")
    else:
        st.warning("Tema en analisis. Por favor, intente con: Salud, Seguridad, Carreteras o Agua.")
