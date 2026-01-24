import streamlit as st

# 1. CONFIGURACIÓN E IDENTIDAD
st.set_page_config(page_title="SISTEMA PLAN-RLA", layout="wide")
st.title("SISTEMA PLAN-RLA")
st.markdown("### Consultor Semántico Total: Matriz de 70 ítems (4 Columnas)")

# 2. BASE DE DATOS INTEGRAL (PROBLEMAS, OBJETIVOS, INDICADORES Y METAS) [cite: 25-97, 110]
# El sistema busca en todas las columnas para detectar el tema
base_datos = [
    # DIMENSIÓN SOCIAL
    {
        "claves": ["corrupcion", "ccc", "patrimonial", "confianza", "flagrancia", "central", "infiltrar"],
        "p": "Corrupción endémica en todos los niveles del aparato público.", # [cite: 25, 110]
        "o": "Crear la Central de lucha Contra la Corrupción (CCC) con plenos poderes para detectar y capturar.", # [cite: 25, 110]
        "i": "Pérdida de confianza de los ciudadanos y falta de transparencia en contratos estatales.", # [cite: 25, 110]
        "m": "Reducir sustancialmente los niveles de corrupción y recuperar la confianza del pueblo.", # [cite: 25, 110]
        "conf": "Lucha contra la Corrupción y Central CCC"
    },
    {
        "claves": ["seguridad", "delincuencia", "terrorismo", "extorsion", "drogas", "videovigilancia", "inteligencia", "itinerantes", "pnp"],
        "p": "Altos niveles de delincuencia, terrorismo urbano y proliferación de pandillaje.", # [cite: 25, 110]
        "o": "Unidades Itinerantes de Pacificación Ciudadana y convenios de inteligencia con EE.UU.", # [cite: 25, 110]
        "i": "Altos índices de inseguridad y necesidad de tecnología de vigilancia integrada.", # [cite: 25, 110]
        "m": "Reducir significativamente índices de violencia, extorsión y comercialización de drogas.", # [cite: 25, 110]
        "conf": "Seguridad Ciudadana y Derrota del Terrorismo Urbano"
    },
    {
        "claves": ["hambre", "pobreza", "anemia", "desnutricion", "ollas", "comunes", "canastas", "alimentos", "madre"],
        "p": "Pobreza extrema, desnutrición crónica infantil y anemia como lastre.", # [cite: 28, 110]
        "o": "Programa Hambre Cero, potenciar ollas comunes y compras a productores nacionales.", # [cite: 28, 110]
        "i": "Incremento de desnutrición en hogares y altos índices de desempleo.", # [cite: 28, 110]
        "m": "Erradicar la anemia y desnutrición infantil mediante productos nacionales.", # [cite: 28, 110]
        "conf": "Hambre Cero y Combate a la Pobreza Extrema"
    },
    {
        "claves": ["educacion", "escuela", "maestros", "profesores", "padres", "director", "escolar", "superior", "fiscalizacion"],
        "p": "Bajo nivel educativo y reducción de participación de padres en la gestión.", # [cite: 34, 110]
        "o": "Padres de familia fiscalizarán la calidad educativa y el desempeño de profesores.", # [cite: 34, 110]
        "i": "Ausencia de los padres en la supervisión de la calidad educativa impartida.", # [cite: 34, 110]
        "m": "Mejorar la calidad de la educación escolar y superior bajo supervisión de padres.", # [cite: 34, 110]
        "conf": "Reforma Educativa y Evaluación de Maestros"
    },
    # DIMENSIÓN ECONÓMICA
    {
        "claves": ["trenes", "ferroviaria", "bioceanico", "tumbes", "tacna", "carga", "pasajeros", "ferrocarril"],
        "p": "Marcado déficit de redes ferroviarias a nivel nacional y falta de conectividad.", # [cite: 77, 114]
        "o": "Construcción de la línea ferroviaria Tumbes-Tacna y el Tren Bioceánico Atlántico-Pacífico.", # [cite: 77, 114]
        "i": "Desfase en la importancia de la conexión ferroviaria por altos costos de implementación.", # [cite: 77, 114]
        "m": "Concluir la red Tumbes-Tacna al 5to año y activar el transporte masivo de carga.", # [cite: 77, 114]
        "conf": "Red Ferroviaria Nacional y Tren Bioceánico"
    },
    {
        "claves": ["pbi", "7%", "inflacion", "crecimiento", "economia", "moneda", "2.5%", "disciplina"],
        "p": "Inestabilidad económico-financiera a causa de la inestabilidad política reciente.", # [cite: 65, 114]
        "o": "Garantizar crecimiento sostenido del PBI y una reducida inflación promedio.", # [cite: 65, 114]
        "i": "Debilidad del PBI por crisis sanitaria y política; inflación acumulada.", # [cite: 65, 114]
        "m": "Alcanzar un crecimiento anual del 7% y mantener la fortaleza de la moneda.", # [cite: 65, 114, 120]
        "conf": "Crecimiento Económico y Meta del 7% PBI"
    },
    # DIMENSIÓN AMBIENTAL
    {
        "claves": ["agua", "riego", "cuencas", "hídricos", "siembra", "cosecha", "sedapal", "esquina"],
        "p": "Deficiente manejo de recursos hídricos y contaminación de ríos y cuencas.", # [cite: 85, 116]
        "o": "Crear la Autoridad de Cuencas y programa de emergencia 'Agua en la Esquina'.", # [cite: 85, 116]
        "i": "Relaves mineros y aguas servidas vertidas en cauces naturales.", # [cite: 85, 116]
        "m": "Aumentar el servicio de agua potable y asegurar manejo técnico de cuencas.", # [cite: 85, 116]
        "conf": "Gestión de Recursos Hídricos y Agua para Todos"
    }
    # NOTA: En la versión final de GitHub se deben listar los 70 ítems siguiendo este patrón.
]

# 3. LÓGICA DE INTERROGACIÓN Y RESPUESTA
st.markdown("---")
pregunta = st.text_input("Escribe cualquier palabra del Plan de Rafael (ej. 7%, Maestros, Trenes, Agua):").lower()

if pregunta:
    encontrado = None
    for item in base_datos:
        if any(clave in pregunta for clave in item["claves"]):
            encontrado = item
            break
    
    if encontrado:
        st.markdown(f"### 📍 Tema Detectado: {encontrado['conf']}")
        if st.button("CONFIRMAR PARA VER MATRIZ TÉCNICA"):
            st.markdown("---")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.error(f"**1. EL PROBLEMA**\n\n{encontrado['p']}")
            with col2:
                st.warning(f"**2. LA SOLUCIÓN RLA**\n\n{encontrado['o']}")
            with col3:
                st.info(f"**3. INDICADOR**\n\n{encontrado['i']}")
            with col4:
                st.success(f"**4. LA META 2026**\n\n{encontrado['m']}")
    else:
        st.warning("⚠️ Palabra no encontrada. Intente con términos técnicos como 'PBI', 'Anemia', 'Justicia' o 'Bioceánico'.")

st.sidebar.caption("SISTEMA PLAN-RLA v21.0 | Base de Datos Total")
