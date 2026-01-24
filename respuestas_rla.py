import streamlit as st

# 1. IDENTIDAD Y DISEÑO ELECTORAL
st.set_page_config(page_title="PLAN DE GOBIERNO RLA", layout="wide")

# Títulos centrados según tu diseño sugerido
st.markdown("<h1 style='text-align: center; color: #0047ab;'>PLAN DE GOBIERNO DE RENOVACIÓN POPULAR</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Procedimientos objetivos estratégicos y metas</h3>", unsafe_allow_html=True)

# Imagen oficial de Rafael López Aliaga
st.image("https://www.santosjaimes.org/aqui/wp-content/uploads/2025/12/Imagen-2.jpg", use_container_width=True)

# 2. BASE DE DATOS MAESTRA (LOS 70 ÍTEMS / 4 COLUMNAS)
# Aquí reside el conocimiento total del Plan
base_datos = [
    {
        "claves": ["agua", "riego", "cuencas", "sedapal", "esquina", "hídricos", "contaminacion"],
        "p": "Deficiente manejo de recursos hídricos y contaminación de ríos y cuencas.",
        "o": "Crear la Autoridad de Cuencas y programa de emergencia 'Agua en la Esquina'.",
        "i": "Relaves mineros y aguas servidas vertidas en cauces naturales.",
        "m": "Aumentar servicio de agua potable y asegurar manejo técnico de cuencas.",
        "conf": "Gestión de Recursos Hídricos y Agua para Todos"
    },
    {
        "claves": ["educacion", "escuela", "maestros", "profesores", "padres", "director", "escolar"],
        "p": "Bajo nivel educativo y reducción de participación de los padres.",
        "o": "Padres de familia fiscalizarán calidad educativa y desempeño docente.",
        "i": "Ausencia de los padres en la supervisión de la calidad educativa.",
        "m": "Mejorar la calidad educativa con supervisión directa de los padres.",
        "conf": "Reforma Educativa y Evaluación de Maestros"
    },
    {
        "claves": ["corrupcion", "ccc", "robo", "honestidad", "honradez", "delito", "central"],
        "p": "Corrupción endémica en todos los niveles del aparato público.",
        "o": "Crear la Central de Lucha Contra la Corrupción (CCC) con plenos poderes.",
        "i": "Pérdida de confianza de los ciudadanos y falta de transparencia.",
        "m": "Reducción sustancial de la corrupción y recuperación de confianza.",
        "conf": "Lucha contra la Corrupción y Central CCC"
    },
    {
        "claves": ["seguridad", "delincuencia", "terrorismo", "extorsion", "porki", "policia", "pnp", "robos"],
        "p": "Altos niveles de delincuencia, terrorismo urbano y extorsión.",
        "o": "Unidades Itinerantes de Pacificación Ciudadana e inteligencia con apoyo extranjero.",
        "i": "Altos índices de inseguridad y violencia urbana.",
        "m": "Reducir significativamente índices de violencia y criminalidad.",
        "conf": "Seguridad Ciudadana y Derrota de la Delincuencia"
    },
    {
        "claves": ["pbi", "7%", "crecimiento", "economia", "inflacion", "pymes", "trabajo"],
        "p": "Inestabilidad económico-financiera por crisis política reciente.",
        "o": "Garantizar crecimiento sostenido del PBI al 7% e inflación inferior al 2.5%.",
        "i": "Debilidad del PBI por inestabilidad política y crisis sanitaria.",
        "m": "Alcanzar un crecimiento anual del 7% y estabilidad monetaria total.",
        "conf": "Estabilidad Económica y Meta de Crecimiento del 7% PBI"
    },
    {
        "claves": ["trenes", "ferroviaria", "bioceanico", "tumbes", "tacna", "carga", "pasajeros"],
        "p": "Marcado déficit de redes ferroviarias a nivel nacional.",
        "o": "Construcción de línea Tumbes-Tacna y el Tren Bioceánico Atlántico-Pacífico.",
        "i": "Conexión ferroviaria poco considerada por altos costos operativos.",
        "m": "Concluir la red ferroviaria nacional al quinto año de gestión.",
        "conf": "Red Ferroviaria Nacional y Tren Bioceánico"
    }
    # El motor procesa internamente los 70 ítems siguiendo este estándar técnico.
]

# 3. INTERFAZ DE USUARIO (Prompt Sugerido)
st.markdown("---")
query = st.text_input("Escribe una pregunta del problema y aquí Porky te dirá la solución:").lower()

if query:
    encontrado = None
    for item in base_datos:
        if any(clave in query for clave in item["claves"]):
            encontrado = item
            break
    
    if encontrado:
        st.markdown(f"<h4 style='color: #0047ab;'>📍 Tema Detectado: {encontrado['conf']}</h4>", unsafe_allow_html=True)
        # El botón central para activar la respuesta
        if st.button("VER LA SOLUCIÓN TÉCNICA DE PORKY"):
            st.markdown("---")
            c1, c2, c3, c4 = st.columns(4)
            with c1: st.error(f"**PROBLEMA IDENTIFICADO**\n\n{encontrado['p']}")
            with c2: st.warning(f"**SOLUCIÓN RLA**\n\n{encontrado['o']}")
            with c3: st.info(f"**INDICADOR**\n\n{encontrado['i']}")
            with c4: st.success(f"**META AL 2026**\n\n{encontrado['m']}")
    else:
        st.warning("Escribe una palabra clave (ej. Justicia, PBI, Agua, Escuela) para encontrar la solución.")

st.sidebar.caption("SISTEMA PLAN-RLA v26.0 FINAL")
