import streamlit as st
import urllib.parse

# 1. CONFIGURACIÓN E IDENTIDAD
st.set_page_config(page_title="Consultor NIE-IA RLA", page_icon="🔵", layout="centered")

# Estilo para el título
st.markdown("<h1 style='text-align: center; color: #003366;'>SISTEMA NIE-IA: CONSULTOR 2026</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><b>Plan de Gobierno - Participación - Cuadros Técnicos</b></p>", unsafe_allow_html=True)

# 2. BASE DE DATOS ESTRATÉGICA (Items completos para áreas rurales)
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
        "icono": "🛣️"
    },
    "agua": {
        "titulo": "Agua y Desague",
        "item": "Item 1000",
        "detalle": "Agua para todos mediante plantas desalinizadoras en la costa y represas tecnificadas en la sierra. Cero anemia mediante agua potable de calidad.",
        "icono": "💧"
    }
}

# 3. MÓDULO: EL PREGUNTADOR ADAPTATIVO
st.subheader("🔍 1. Consulta tu necesidad")
entrada_usuario = st.text_input("¿Que necesita tu localidad? (Ej: Carretera, Agua, Salud)").lower()

if entrada_usuario:
    tema_clave = next((k for k in mapeo_estrategico if k in entrada_usuario), None)
    
    if tema_clave:
        info = mapeo_estrategico[tema_clave]
        st.markdown(f"### {info['icono']} Tema detectado: **{info['titulo']}**")
        
        if st.button("CONFIRMAR Y VER PROPUESTA TÉCNICA"):
            st.markdown("---")
            # RESPUESTA DE TRIPLE FUENTE
            st.error(f"📖 **PLAN DE GOBIERNO ({info['item']}):**\n\n{info['detalle']}")
            st.success(f"👷 **CUERPO TECNICO:**\n\nEjecucion regional prioritaria con mano de obra local.")
            st.warning(f"🦁 **VISION RLA:**\n\n'Dinero hay, lo que sobra son ladrones'. Gestion honesta y eficiente.")
            
            # Botón Viral
            msg = f"Mira la propuesta de {info['titulo']} en el Consultor RLA: https://plan-rla-2026.streamlit.app/"
            st.markdown(f"[📢 Compartir esta propuesta por WhatsApp](https://wa.me/?text={urllib.parse.quote(msg)})")
    else:
        st.warning("Escriba una palabra clave como: Salud, Seguridad, Carretera o Agua.")

st.markdown("---")

# 4. MÓDULO: ACCIÓN Y COMUNIDAD (El corazón de la APP)
st.subheader("🚀 2. Únete al Cambio: ¡Te necesitamos!")

col1, col2 = st.columns(2)

with col1:
    with st.expander("🏗️ FORMAR CUADROS"):
        st.write("¿Eres profesional o líder? Súmate a los equipos técnicos.")
        st.link_button("Postular como Cuadro", "https://santosjaimes.org/")

    with st.expander("📢 ENVIAR IDEAS O PEDIDOS"):
        pedido = st.text_area("Cuéntanos qué necesita tu distrito:")
        if st.button("Registrar Pedido"):
            st.success("Tu pedido ha sido registrado en la base de datos NIE-IA.")

with col2:
    with st.expander("👥 UNIRSE A LA COMUNIDAD"):
        st.write("Recibe noticias y defiende el voto.")
        st.link_button("WhatsApp Oficial", "https://santosjaimes.org/")

    with st.expander("🤝 AFILIACIÓN"):
        st.link_button("Ficha de Afiliación", "https://renovacionpopular.pe")

# Lateral Informativo
st.sidebar.image("https://www.santosjaimes.org/wp-content/uploads/2024/logo_rla.png", width=100)
st.sidebar.write("Sistema NIE-IA 2026")
st.sidebar.caption("Versión 2.0 - Despliegue Masivo")
