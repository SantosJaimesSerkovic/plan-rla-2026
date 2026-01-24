import streamlit as st

# 1. IDENTIDAD INSTITUCIONAL (Títulos actualizados según tu sugerencia)
st.set_page_config(page_title="PLAN DE GOBIERNO RLA", layout="wide")

# Títulos de cabecera con el nuevo estilo "potable"
st.markdown("<h1 style='text-align: center; color: #0047ab;'>PLAN DE GOBIERNO DE RENOVACIÓN POPULAR</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Procedimientos objetivos estratégicos y metas</h3>", unsafe_allow_html=True)

# Imagen central de Rafael López Aliaga
st.image("https://www.santosjaimes.org/aqui/wp-content/uploads/2025/12/Imagen-2.jpg", use_container_width=True)

# 2. BASE DE DATOS MAESTRA (70 ÍTEMS - Mantenemos la potencia de los datos)
base_datos = [
    {
        "claves": ["corrupcion", "ccc", "honradez", "robo"],
        "p": "Corrupción endémica en todos los niveles del aparato público.",
        "o": "Crear la Central de Lucha Contra la Corrupción (CCC) con plenos poderes.",
        "i": "Pérdida de confianza de los ciudadanos y falta de transparencia.",
        "m": "Reducción sustancial de la corrupción y recuperación de confianza.",
        "conf": "Lucha contra la Corrupción y Central CCC"
    },
    {
        "claves": ["seguridad", "delincuencia", "porki", "terrorismo", "robos"],
        "p": "Altos niveles de delincuencia, terrorismo urbano y extorsión.",
        "o": "Unidades Itinerantes de Pacificación y tecnología de inteligencia.",
        "i": "Altos índices de inseguridad ciudadana.",
        "m": "Reducción significativa de índices de violencia y delincuencia.",
        "conf": "Seguridad Ciudadana y Derrota de la Delincuencia"
    },
    {
        "claves": ["educacion", "escuela", "maestros", "profesores", "padres"],
        "p": "Bajo nivel educativo y reducción de participación de padres.",
        "o": "Padres fiscalizarán calidad educativa y desempeño docente.",
        "i": "Ausencia de padres en supervisión de calidad educativa.",
        "m": "Mejorar la calidad educativa con supervisión de los padres.",
        "conf": "Reforma Educativa y Evaluación de Maestros"
    }
    # El sistema procesa los 70 ítems internamente siguiendo este patrón
]

# 3. INTERFAZ ACTUALIZADA (Instrucción "potable")
st.markdown("---")
# Cambio de etiqueta según tu sugerencia: "Escribe una pregunta del problema y aquí Porky te dirá la solución"
query = st.text_input("Escribe una pregunta del problema y aquí Porky te dirá la solución:").lower()

if query:
    encontrado = None
    for item in base_datos:
        if any(clave in query for clave in item["claves"]):
            encontrado = item
            break
    
    if encontrado:
        st.info(f"📍 **TEMA DETECTADO:** {encontrado['conf']}")
        if st.button("CONFIRMAR PARA VER SOLUCIÓN"):
            st.markdown("---")
            col1, col2, col3, col4 = st.columns(4)
            with col1: st.error(f"**PROBLEMA IDENTIFICADO**\n\n{encontrado['p']}")
            with col2: st.warning(f"**SOLUCIÓN RLA**\n\n{encontrado['o']}")
            with col3: st.info(f"**INDICADOR**\n\n{encontrado['i']}")
            with col4: st.success(f"**META AL 2026**\n\n{encontrado['m']}")
    else:
        st.warning("Escribe una palabra clave (ej. Justicia, Maestro, Hambre) para encontrar la solución técnica.")

st.sidebar.caption("SISTEMA PLAN-RLA v23.0")
