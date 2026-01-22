import streamlit as st

# 1. IDENTIDAD Y CONFIGURACION (PWA Ready)
st.set_page_config(page_title="Consultor NIE-IA RLA", page_icon="🔵")
st.markdown("<h1 style='text-align: center; color: #003366;'>SISTEMA NIE-IA: CONSULTOR 2026</h1>", unsafe_allow_html=True)

# 2. DICCIONARIO DE INTELIGENCIA (Mapeo de Temas)
mapeo_estrategico = {
    "salud": {"titulo": "Salud y Bienestar", "item": "2000", "icono": "🏥"},
    "seguridad": {"titulo": "Seguridad Ciudadana", "item": "0500", "icono": "🛡️"},
    "carretera": {"titulo": "Infraestructura y Transportes", "item": "2500", "icono": "🛣️"},
    "via": {"titulo": "Infraestructura y Transportes", "item": "2500", "icono": "🛣️"},
    "agua": {"titulo": "Infraestructura Humana (Agua/Desague)", "item": "1000", "icono": "💧"},
    "hambre": {"titulo": "Lucha contra la Pobreza (Hambre Cero)", "item": "1500", "icono": "🍲"}
}

# 3. MÓDULO 1: EL PREGUNTADOR (ANALISTA)
st.subheader("1. Tu Necesidad")
entrada_usuario = st.text_input("¿Que necesita su localidad o distrito?").lower()

if entrada_usuario:
    # Identificación del tema
    tema_clave = next((k for k in mapeo_estrategico if k in entrada_usuario), None)
    
    if tema_clave:
        info = mapeo_estrategico[tema_clave]
        
        # CONFIRMACION Y ADAPTACION
        st.markdown(f"### {info['icono']} He detectado que consulta sobre: **{info['titulo']}**")
        st.write(f"Esta necesidad corresponde al **Item {info['item']}** del Plan de Gobierno de RLA.")
        
        if st.button("CONFIRMAR Y VER PROPUESTA TECNICA"):
            # 4. MÓDULO 2: EL RESPONDEDOR (TRIPLE FUENTE)
            st.markdown("---")
            st.subheader(f"Respuesta de Triple Fuente: {info['titulo']}")
            
            # Bloques de respuesta adaptados
            col1, col2, col3 = st.columns(3)
            with col1:
                st.info(f"**PLAN DE GOBIERNO**\n\nSustento tecnico bajo el Item {info['item']}. Prioridad Nacional.")
            with col2:
                st.success(f"**CUERPO TECNICO**\n\nNuestros candidatos regionales tienen el mapa de ejecucion para {info['titulo']}.")
            with col3:
                st.warning(f"**VISION DE RLA**\n\n'Cero corrupcion y obras rapidas'. Gestion directa y eficiente.")
                
            st.markdown("---")
            st.caption("Mas detalles en: santosjaimes.org")
    else:
        st.warning("🔍 Tema en analisis. Intente con: Salud, Seguridad, Carreteras, Agua o Hambre.")

# Pie de pagina fijo
st.sidebar.image("https://www.santosjaimes.org/wp-content/uploads/2024/logo_rla.png", width=100)
st.sidebar.write("Sistema NIE-IA 2026")
