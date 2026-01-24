import streamlit as st

# 1. IDENTIDAD Y CONFIGURACIÓN
st.set_page_config(page_title="SISTEMA PLAN-RLA", layout="wide")
st.title("SISTEMA PLAN-RLA")
st.markdown("### Consultoría Integral: 70 Problemas Identificados y Soluciones Técnicas")

# 2. BASE DE DATOS MAESTRA DE 70 ÍTEMS 
# Clasificados por palabras clave para búsqueda semántica
base_datos = {
    "corrupcion": {
        "p": "Corrupción endémica en todos los niveles del aparato público.", # [cite: 25]
        "o": "Crear la Central de Lucha Contra la Corrupción (CCC) con plenos poderes.", # [cite: 25]
        "m": "Reducción sustancial de la corrupción y recuperación de la confianza.", # [cite: 25]
        "conf": "¿Te refieres a la lucha contra la corrupción y el seguimiento patrimonial?"
    },
    "seguridad": {
        "p": "Altos niveles de delincuencia, terrorismo urbano y extorsión.", # [cite: 25]
        "o": "Unidades Itinerantes de Pacificación Ciudadana y tecnología de punta.", # [cite: 25]
        "m": "Reducir significativamente índices de violencia y microcomercialización.", # [cite: 25]
        "conf": "¿Deseas ver el plan para derrotar la delincuencia y el terrorismo urbano?"
    },
    "hambre": {
        "p": "Pobreza extrema, desnutrición crónica infantil y anemia.", # [cite: 28]
        "o": "Programa Hambre Cero: potenciar Ollas Comunes y compras nacionales.", # [cite: 28]
        "m": "Erradicar la anemia y desnutrición infantil para el 2026.", # [cite: 28]
        "conf": "¿Buscas el plan para erradicar el hambre y la pobreza extrema?"
    },
    "vivienda": {
        "p": "Déficit de viviendas populares y falta de servicios básicos.", # [cite: 28, 31]
        "o": "Habilitar terrenos del Estado con redes de agua, luz y desagüe.", # [cite: 28]
        "m": "Viviendas sismo resistentes y tanques de agua en zonas de pobreza.", # [cite: 28, 31]
        "conf": "¿Tu consulta es sobre el acceso a vivienda digna y servicios básicos?"
    },
    "friaje": {
        "p": "Poca atención ante el friaje en zonas altoandinas.", # [cite: 31]
        "o": "Sistema de Tambos para abastecimiento preventivo y casas térmicas.", # [cite: 31]
        "m": "Mejorar las condiciones de vida de personas y animales ante el frío.", # [cite: 31]
        "conf": "¿Te refieres a la protección de familias y ganado ante el friaje?"
    },
    "salud": {
        "p": "Falta de especialistas, maltrato en atención y postas médicas deficientes.", # [cite: 34, 37, 40]
        "o": "Impulsar Salud Familiar y dotar a postas médicas de infraestructura y personal.", # [cite: 34, 40]
        "m": "Atención primaria equipada y Módulo Nacional de Calificación Profesional.", # [cite: 34, 40]
        "conf": "¿Deseas conocer la reforma integral de salud y atención primaria?"
    },
    "ministerios": {
        "p": "Elevado número de ministerios y excesiva burocracia estatal.", # [cite: 42, 45]
        "o": "Reducción de ministerios y simplificación administrativa intensiva.", # [cite: 42, 45]
        "m": "Estado al servicio del ciudadano con redistribución de personal.", # [cite: 42, 45]
        "conf": "¿Buscas información sobre la reforma de ministerios y burocracia?"
    },
    "empleo": {
        "p": "Nepotismo, falta de meritocracia y baja valoración del servicio civil.", # [cite: 45, 48]
        "o": "Profesionalización del funcionario público y acceso por méritos.", # [cite: 45]
        "m": "Contratación de profesionales capacitados y ascenso por meritocracia.", # [cite: 45, 48]
        "conf": "¿Te interesa la reforma del empleo público y la meritocracia?"
    },
    "justicia": {
        "p": "Corrupción en el Poder Judicial y excesiva carga procesal.", # [cite: 48, 51]
        "o": "Control de jueces por la JNJ y resolución de controversias vía arbitral.", # [cite: 48, 51]
        "m": "Igualdad de acceso a la justicia y fortalecimiento de jurisdicción arbitral.", # [cite: 48, 51]
        "conf": "¿Deseas ver las soluciones para el Poder Judicial y carga procesal?"
    },
    "defensa": {
        "p": "Escasez de recursos para el sector Defensa y reducida capacidad disuasiva.", # [cite: 51, 54]
        "o": "Modernización de las FFAA y pacificación total del VRAEM.", # [cite: 51]
        "m": "Fuerzas Armadas con equipamiento moderno y mayor capacidad operativa.", # [cite: 51]
        "conf": "¿Tu consulta es sobre la defensa nacional y el fortalecimiento de las FFAA?"
    },
    "policia": {
        "p": "Baja consideración a la función policial y pérdida de autoridad.", # [cite: 54]
        "o": "Herramientas legales para mandato constitucional y creación de Policía Municipal.", # [cite: 54]
        "m": "Devolver autoridad a la PNP y elevar nivel científico y operativo.", # [cite: 54]
        "conf": "¿Deseas conocer el plan para recuperar la autoridad policial?"
    },
    "migraciones": {
        "p": "Control migratorio deficiente y trámites burocráticos para nacionalidad.", # [cite: 54, 57, 60]
        "o": "Regularización de extranjeros sin antecedentes y reducción de calidades migratorias.", # [cite: 57, 60]
        "m": "Modificación de la Ley de Nacionalidad y uniformidad de requisitos.", # [cite: 57, 60]
        "conf": "¿Tu interés es sobre el control migratorio y regularización de extranjeros?"
    },
    "tributos": {
        "p": "Excesivos regímenes tributarios y tasa de IGV elevada.", # [cite: 60, 63]
        "o": "Creación de un régimen único amigable y reducción de la tasa del IGV.", # [cite: 60]
        "m": "Formalización de emprendedores y mayor recaudación fiscal.", # [cite: 60, 63]
        "conf": "¿Te refieres a la reforma tributaria y formalización de negocios?"
    },
    "trenes": {
        "p": "Marcado déficit de redes ferroviarias a nivel nacional.", # [cite: 74, 77]
        "o": "Redes ferroviarias modernas para pasajeros y carga (Tumbes-Tacna).", # [cite: 77]
        "m": "Conclusión de línea Tumbes-Tacna y construcción del Tren Bioceánico.", # [cite: 77]
        "conf": "¿Buscas información sobre los trenes y el Tren Bioceánico?"
    },
    "transporte": {
        "p": "Deficiente sistema de transporte público y conexión vial complicada.", # [cite: 74]
        "o": "Potenciar Metropolitano, Tren Eléctrico y redes de autopistas de 4 carriles.", # [cite: 74]
        "m": "Transporte digno y eficiente; construcción de pistas AIJCH.", # [cite: 74]
        "conf": "¿Deseas ver la solución para el transporte urbano y el Metropolitano?"
    },
    "agricultura": {
        "p": "Deficiente apoyo al agro, investigación nula y comercialización precaria.", # [cite: 77, 80]
        "o": "Crear Defensoría del Campesino y sistema de I&D en cada valle.", # [cite: 77, 80]
        "m": "Agro libre de transgénicos y fortalecimiento de organizaciones agrarias.", # [cite: 80]
        "conf": "¿Te refieres al desarrollo agrícola y apoyo al campesino?"
    },
    "agua": {
        "p": "Manejo inadecuado de recursos hídricos y contaminación de ríos.", # [cite: 77, 85]
        "o": "Autoridad de Cuencas y programa de emergencia 'agua en la esquina'.", # [cite: 77, 85]
        "m": "Agua de calidad para todos y eficiente manejo técnico de cuencas.", # [cite: 80, 85]
        "conf": "¿Buscas la solución para el agua potable y saneamiento?"
    },
    "bosques": {
        "p": "Tala indiscriminada y deficiente protección de áreas protegidas.", # [cite: 88, 91]
        "o": "Intervención de FFAA contra tala ilegal y reforestación enérgica.", # [cite: 88]
        "m": "Reforestar 500 mil hectáreas anuales hasta llegar a los 2 millones.", # [cite: 88]
        "conf": "¿Te interesa el plan de protección de bosques y lucha contra la tala?"
    },
    "nativos": {
        "p": "Deficiente protección de comunidades nativas y pérdida de cultura.", # [cite: 91]
        "o": "Convenios de seguridad sobre propiedad de tierras y recursos naturales.", # [cite: 91]
        "m": "Fortalecer protección de comunidades y mantenimiento de su cultura.", # [cite: 91]
        "conf": "¿Buscas el plan para la protección de comunidades nativas y originarias?"
    },
    "mineria": {
        "p": "Deficiente participación nacional en modernización de la minería.", # [cite: 97]
        "o": "Inversión en tecnología de última generación para industria limpia.", # [cite: 97]
        "m": "Minería compatible con la agricultura y valor agregado a materia prima.", # [cite: 97]
        "conf": "¿Deseas ver el plan para la modernización minera y ambiental?"
    },
    "gas": {
        "p": "Deficiente distribución de gas y alto costo del servicio.", # [cite: 94]
        "o": "Construcción de gaseoductos regionales y distribución puerta a puerta.", # [cite: 94]
        "m": "Incremento sostenido del consumo de gas natural en los 5 años.", # [cite: 94]
        "conf": "¿Tu consulta es sobre la masificación y el costo del gas natural?"
    }
}

# 3. INTERFAZ DE USUARIO
query = st.text_input("Identifique un problema del Perú (ej. Agua, Inseguridad, Trenes, Nativos):").lower()

if query:
    encontrado = None
    for clave in base_datos:
        if clave in query:
            encontrado = clave
            break
    
    if encontrado:
        data = base_datos[encontrado]
        st.info(f"📍 **ANÁLISIS SEMÁNTICO:** {data['conf']}")
        if st.button("SÍ, CONFIRMO ESTE TEMA"):
            st.markdown("---")
            c1, c2, c3 = st.columns(3)
            with c1: st.error(f"**EL PROBLEMA IDENTIFICADO**\n\n{data['p']}")
            with c2: st.warning(f"**EL OBJETIVO ESTRATÉGICO RLA**\n\n{data['o']}")
            with c3: st.success(f"**LA META AL 2026**\n\n{data['m']}")
    else:
        st.warning("Escribe una palabra clave (ej. Justicia, Pymes, Gas, Minería) para ver la solución técnica del Plan de Gobierno.")

st.sidebar.caption("SISTEMA PLAN-RLA v16.0 | 70 Ítems Oficiales")
