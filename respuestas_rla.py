import streamlit as st

# 1. IDENTIDAD INSTITUCIONAL
st.set_page_config(page_title="SISTEMA PLAN-RLA", layout="wide")
st.title("SISTEMA PLAN-RLA")
st.markdown("### Consultoría Integral: 70 Soluciones Técnicas 2026-2031")

# 2. BASE DE DATOS MAESTRA: LOS 70 PROBLEMAS IDENTIFICADOS 
# Verificados uno por uno contra el Plan de Gobierno
base_datos = {
    # DIMENSIÓN SOCIAL (20 ítems)
    "corrupcion": {"p": "Corrupción endémica en todos los niveles del aparato público.", "o": "Central de lucha Contra la Corrupción (CCC) con plenos poderes.", "m": "Reducción sustancial de la corrupción y recuperación de confianza.", "c": "¿Te refieres a las medidas contra la Corrupción?"},
    "delincuencia": {"p": "Altos niveles de delincuencia y terrorismo urbano.", "o": "Unidades Itinerantes de Pacificación Ciudadana e inteligencia.", "m": "Reducción significativa de índices de violencia y extorsión.", "c": "¿Buscas el plan contra la Delincuencia y el Terrorismo Urbano?"},
    "pandillaje": {"p": "Proliferación del pandillaje y microcomercialización de drogas.", "o": "Agentes encubiertos e inteligencia integrada con serenazgo.", "m": "Reducir la proliferación de drogas y violencia urbana.", "c": "¿Tu consulta es sobre el control del Pandillaje y Drogas?"},
    "pobreza": {"p": "Pobreza extrema como lastre para el desarrollo.", "o": "Convertir a los más pobres en emprendedores y fortalecer programas sociales.", "m": "Disminuir significativamente los índices de pobreza extrema.", "c": "¿Te refieres a la lucha contra la Pobreza Extrema?"},
    "esparcimiento": {"p": "Escasez de áreas de esparcimiento familiar.", "o": "Extender a todo el país la experiencia de los Clubes Zonales.", "m": "Aumentar los lugares de esparcimiento de calidad en todo el Perú.", "c": "¿Deseas ver el plan para crear áreas de Esparcimiento Familiar?"},
    "hambre": {"p": "Desnutrición crónica infantil y anemia.", "o": "Alimentación desde el vientre materno y compras a productores nacionales.", "m": "Erradicar la anemia y la desnutrición infantil.", "c": "¿Tu interés es sobre el Hambre y la Anemia infantil?"},
    "vivienda": {"p": "Déficit de viviendas populares y sismo resistentes.", "o": "Habilitar terrenos del Estado con acceso a redes de agua y luz.", "m": "Mejorar las viviendas sociales durante los 5 años de gestión.", "c": "¿Buscas la solución para el acceso a Vivienda Popular?"},
    "comunidades": {"p": "Déficit de salud y educación en comunidades campesinas y nativas.", "o": "Incorporar dirigentes agrarios en directorios de gobierno.", "m": "Efectivo desarrollo de las comunidades campesinas y nativas.", "c": "¿Te refieres al desarrollo de Comunidades Campesinas?"},
    "friaje": {"p": "Poca atención ante el friaje en zonas altoandinas.", "o": "Sistema de Tambos para abastecimiento y casas térmicas.", "m": "Reducir impactos negativos y proteger personas y animales.", "c": "¿Buscas protección para las zonas afectadas por el Friaje?"},
    "pescado": {"p": "Déficit de pescado para la mesa popular.", "o": "Crear cadenas de frío del mar a la olla.", "m": "Incrementar el consumo de pescado masivo (anchoveta, jurel).", "c": "¿Tu consulta es sobre el acceso a Pescado barato?"},
    "medicamentos": {"p": "Falta de acceso a medicamentos y cobros excesivos.", "o": "Farmacias obligadas a tener genéricos básicos de calidad.", "m": "Garantizar que no falten medicamentos básicos en boticas.", "c": "¿Te refieres al costo y acceso a Medicamentos?"},
    "postas": {"p": "Postas Médicas deficientes en infraestructura y personal.", "o": "Dotar a postas de materiales, medicinas y profesionales.", "m": "Equipamiento adecuado y personal capacitado en Postas.", "c": "¿Deseas ver el fortalecimiento de las Postas Médicas?"},
    "deporte": {"p": "Déficit de deporte y altos índices de obesidad.", "o": "Crear Centros de Alto Rendimiento Deportivo (CAR) en colegios.", "m": "Impulsar actividad deportiva en todos los niveles escolares.", "c": "¿Tu interés es sobre el Deporte y salud física?"},
    "educacion": {"p": "Reducción de participación de padres en gestión educativa.", "o": "Padres fiscalizarán calidad educativa y desempeño docente.", "m": "Mejorar la educación con supervisión directa de los padres.", "c": "¿Buscas la reforma de Educación y rol de los padres?"},
    "escuela": {"p": "Bajo cumplimiento de estándares en instituciones educativas.", "o": "El Director será responsable de la gestión educativa total.", "m": "Calidad educativa superior supervisada por la comunidad.", "c": "¿Te refieres a la gestión de Escuelas y calidad escolar?"},
    "maestros": {"p": "Necesidad de mejorar desempeño y evaluación docente.", "o": "Padres de familia evaluarán el desempeño de los profesores.", "m": "Docencia de alta calidad basada en resultados y supervisión.", "c": "¿Tu consulta es sobre los Maestros y la evaluación docente?"},
    "igualdad": {"p": "Desigualdad de oportunidades entre hombres y mujeres.", "o": "Generar oportunidades basadas en la meritocracia sin distinción.", "m": "Igualdad real en directorios y cargos por mérito propio.", "c": "¿Deseas ver el plan de Igualdad de Oportunidades?"},
    "mujer": {"p": "Falta de capacitación y créditos para la mujer emprendedora.", "o": "Programas de capacitación técnica y sistema de crédito para mujeres.", "m": "Brindar herramientas para el desarrollo de la mujer emprendedora.", "c": "¿Buscas apoyo para la Mujer Emprendedora?"},
    "primaria": {"p": "Precariedad en atención primaria de salud.", "o": "Elevar cobertura para reducir sobredemanda hospitalaria.", "m": "Fortalecer Centros de Atención Primaria con equipamiento.", "c": "¿Te refieres a la Atención Primaria de Salud?"},
    "regional": {"p": "Inadecuado manejo de la gestión de salud regional.", "o": "Impulsar educación sanitaria y estilos de vida saludables.", "m": "Innovación científica y tecnológica en salud regional.", "c": "¿Tu interés es sobre la Gestión de Salud Regional?"},

    # DIMENSIÓN INSTITUCIONAL (20 ítems)
    "familia": {"p": "Invisibilidad de la especialidad Salud Familiar.", "o": "Impulsar Médicos de Familia como eje central de prevención.", "m": "Plan Nacional de Promoción de Salud con acento familiar.", "c": "¿Buscas información sobre la Salud Familiar?"},
    "trato": {"p": "Maltrato en atención por personal de salud.", "o": "Crear centros de desarrollo personal y trato humanizado.", "m": "Módulo Nacional de Calificación Profesional continuo.", "c": "¿Te refieres al Trato Humanizado en hospitales?"},
    "trabajo": {"p": "Ausencia de protocolos de seguridad en el trabajo.", "o": "Favorecer la Salud Ocupacional como derecho ciudadano.", "m": "Crear la Oficina Nacional de Salud Ocupacional.", "c": "¿Tu consulta es sobre Seguridad en el Trabajo?"},
    "ministerios": {"p": "Deficiente organización y elevado número de ministerios.", "o": "Reducción de ministerios y simplificación administrativa.", "m": "Estado moderno, reducido y al servicio del ciudadano.", "c": "¿Deseas ver la Reforma de Ministerios?"},
    "gestion": {"p": "Deficiente gestión de gobiernos regionales y municipales.", "o": "Equipos gerenciales especializados y presupuesto por resultados.", "m": "Capacitar y fomentar proyectos de inversión regional.", "c": "¿Buscas mejorar la Gestión Regional y Municipal?"},
    "servicios": {"p": "Servicio civil con baja valoración y meritocracia.", "o": "Ingreso por méritos y pruebas de conocimiento constantes.", "m": "Revalorar la función pública mediante la meritocracia.", "c": "¿Te refieres a la Reforma del Servicio Civil?"},
    "nepotismo": {"p": "Excesiva contratación de amistades en el aparato estatal.", "o": "Acceso, permanencia y progresión por resultados evaluados.", "m": "Eliminar el nepotismo y contratar profesionales capaces.", "c": "¿Deseas ver el plan contra el Nepotismo?"},
    "transparencia": {"p": "Falta de transparencia y manipulación de información.", "o": "Asegurar acceso masivo a información vía Internet (Gobierno Digital).", "m": "Integrar la transparencia del Estado con los ciudadanos.", "c": "¿Tu consulta es sobre Transparencia y Gobierno Digital?"},
    "jueces": {"p": "Falta de incentivos para la carrera judicial de jóvenes.", "o": "Formación especializada en la Academia de la Magistratura.", "m": "Promover el ingreso de jueces jóvenes a la carrera judicial.", "c": "¿Buscas la renovación de Jueces y Fiscales?"},
    "justicia": {"p": "Corrupción en el Poder Judicial y Ministerio Público.", "o": "Órganos de control dependerán de la Junta Nacional de Justicia.", "m": "Garantizar igualdad de acceso a la justicia para todos.", "c": "¿Te refieres a la Lucha contra la Corrupción Judicial?"},
    "carga": {"p": "Excesiva carga procesal y lentitud judicial.", "o": "Ley para que controversias civiles se resuelvan vía arbitral.", "m": "Fortalecer la jurisdicción arbitral para procesos rápidos.", "c": "¿Buscas reducir la Carga Procesal y juicios lentos?"},
    "defensa": {"p": "Escasez de recursos para el Sector Defensa.", "o": "Modernización de las FFAA y capacidad disuasiva nacional.", "m": "Fuerzas Armadas con equipamiento moderno y operativo.", "c": "¿Deseas ver el plan para fortalecer la Defensa?"},
    "vraem": {"p": "Necesidad de pacificar zonas de conflicto interno.", "o": "Terminar de pacificar el VRAEM y presencia en el Putumayo.", "m": "Pacificación total y soberanía en fronteras.", "c": "¿Tu consulta es sobre la pacificación del VRAEM?"},
    "policia": {"p": "Baja consideración y pérdida de autoridad policial.", "o": "Devolver autoridad a la PNP y crear Policía Municipal.", "m": "Autoridad restituida y policía con nivel científico elevado.", "c": "¿Buscas recuperar la Autoridad Policial?"},
    "migraciones": {"p": "Superintendencia de Migraciones con control deficiente.", "o": "Migraciones pasará al Ministerio de Relaciones Exteriores.", "m": "Control migratorio estricto de ciudadanos extranjeros.", "c": "¿Te refieres al Control de Migraciones?"},
    "soberania": {"p": "Debilidad del sistema multilateral y soberanía.", "o": "Incrementar relaciones en Asia Pacífico, UE y América.", "m": "Resguardar prioritariamente nuestra absoluta soberanía.", "c": "¿Deseas ver el plan de Relaciones Exteriores?"},
    "pex": {"p": "Peruanos en el exterior sin norma que los ampare.", "o": "Aprobar un Plan PEX que beneficie a los 3.5 millones de peruanos.", "m": "Reconocimiento de los derechos de los peruanos en el exterior.", "c": "¿Buscas apoyo para Peruanos en el Exterior?"},
    "nacionalidad": {"p": "Falta de restricciones en obtención de nacionalidad.", "o": "Nacionalidad tras 5 años de residencia pacífica y productiva.", "m": "Modificación de la Ley de Nacionalidad para extranjeros.", "c": "¿Tu consulta es sobre la obtención de Nacionalidad?"},
    "tributos": {"p": "Existencia de tres regímenes tributarios complejos.", "o": "Eliminar regímenes para crear uno solo amigable y simple.", "m": "Formalización de emprendedores y negocios.", "c": "¿Te refieres a la Reforma Tributaria?"},
    "igv": {"p": "Tasa impositiva del IGV elevada.", "o": "Reducir la tasa del IGV para fomentar la formalización.", "m": "Reducción de informalidad y mayor recaudación fiscal.", "c": "¿Buscas información sobre la reducción del IGV?"},

    # DIMENSIÓN ECONÓMICA (18 ítems)
    "exoneraciones": {"p": "Amplias exoneraciones que reducen base tributaria.", "o": "Reducir exoneraciones para ampliar la recaudación fiscal.", "m": "Compatibilidad tributaria con estándares de la OCDE.", "c": "¿Deseas ver el plan sobre Exoneraciones Tributarias?"},
    "sunat": {"p": "Abuso hacia el contribuyente y arbitrariedades.", "o": "Promulgar la Ley del Contribuyente para evitar abusos.", "m": "Seguridad jurídica para el ciudadano que paga impuestos.", "c": "¿Tu consulta es sobre los abusos de la Administración Tributaria?"},
    "pbi": {"p": "Inestabilidad económico-financiera y baja del PBI.", "o": "Garantizar crecimiento sostenido y tipo de cambio estable.", "m": "Incremento anual del 7% del PBI al quinto año.", "c": "¿Te refieres al Crecimiento Económico y PBI?"},
    "industria": {"p": "Reducida industrialización y valor agregado.", "o": "Dotar al aparato productivo de alto contenido tecnológico.", "m": "Aparato productivo industrializado y 2 millones de empleos.", "c": "¿Buscas el plan de Industrialización nacional?"},
    "empleo": {"p": "Inexistente trabajo digno en zonas de pobreza rural.", "o": "Retribución por horas en zonas rurales para obras comunales.", "m": "Trabajo digno e igualitario en las propias comunidades.", "c": "¿Deseas ver el plan de Generación de Empleo?"},
    "pymes": {"p": "Falta de incentivos y asociatividad para PYMES.", "o": "Crear el Instituto de Promoción y Desarrollo de las PYMEs.", "m": "PYMES con visión internacional y clusters productivos.", "c": "¿Te refieres al apoyo a las PYMES?"},
    "financiamiento": {"p": "Reducido financiamiento para emprendedores.", "o": "Apoyar la creación del Banco Pyme con capital privado.", "m": "Acceso real a capital inicial para las PYMES.", "c": "¿Buscas Financiamiento para emprendedores?"},
    "mercados": {"p": "Falta de apoyo a los mercados populares y abastos.", "o": "Modernización de mercados de abasto y mayoristas.", "m": "Mercados modernos, dignos y eficientes para el pueblo.", "c": "¿Deseas ver el plan de Mercados Populares?"},
    "zonas": {"p": "Reducidas Zonas Libres de Impuestos en fronteras.", "o": "Impulsar Parques Logísticos y Zonas Libres en Selva y Sur.", "m": "Zonas de comercio para contrarrestar el contrabando.", "c": "¿Tu consulta es sobre Zonas Francas y Logísticas?"},
    "nativos": {"p": "Reducida promoción de productos autóctonos.", "o": "Desarrollo industrial para consumo interno de maca, cuy, trucha.", "m": "Aumento de calidad y exportación de productos nativos.", "c": "¿Buscas apoyo para Productos Autóctonos?"},
    "artesania": {"p": "Reducida promoción de la producción artesanal.", "o": "Incorporar comunidades rurales al trabajo artesanal familiar.", "m": "Incentivo para seguir impulsando el trabajo artesanal.", "c": "¿Te refieres al apoyo a la Artesanía familiar?"},
    "transporte": {"p": "Deficiente sistema de transporte público y desorden.", "o": "Potenciar Metropolitano, Tren Eléctrico y líneas de Metro.", "m": "Transporte digno, eficiente y orden vial en ciudades.", "c": "¿Buscas la solución al Transporte Público?"},
    "carreteras": {"p": "Deficiente infraestructura vial y de penetración.", "o": "Rehabilitación de Red Vial con batallones de ingeniería FFAA.", "m": "Autopistas de 4 carriles para conectar todos los pueblos.", "c": "¿Deseas ver el plan de Carreteras y Autopistas?"},
    "puertos": {"p": "Deficiente infraestructura portuaria y aeroportuaria.", "o": "Modernización de aeropuertos y ampliación de muelles Callao.", "m": "Perú como eje del transporte de carga en Sudamérica.", "c": "¿Tu consulta es sobre Puertos y Aeropuertos?"},
    "trenes": {"p": "Marcado déficit de redes ferroviarias nacional.", "o": "Construcción de línea Tumbes-Tacna y Tren Bioceánico.", "m": "Conexión ferroviaria moderna para pasajeros y carga.", "c": "¿Buscas información sobre Trenes y el Bioceánico?"},
    "internet": {"p": "Deficiente conectividad de internet en todo el país.", "o": "Proveedores deben dar banda ancha a precios asequibles.", "m": "Conectividad digital total a nivel nacional.", "c": "¿Te refieres al acceso a Internet y banda ancha?"},
    "agro": {"p": "Deficiente apoyo a la actividad agropecuaria.", "o": "Implementar la Ley de la Defensoría del Campesino.", "m": "Trabajo digno y reconocido para trabajadores agrarios.", "c": "¿Buscas el plan para el Sector Agropecuario?"},
    "riego": {"p": "Excesivas regulaciones para distribución hídrica.", "o": "Impulsar la Autoridad de Cuencas para manejo integrado.", "m": "Distribución eficiente del agua para agricultura y vida.", "c": "¿Deseas ver el plan de Riego y Agua?"},

    # DIMENSIÓN TERRITORIAL - AMBIENTAL (12 ítems)
    "investigacion": {"p": "Deficiente investigación y desarrollo agrícola.", "o": "Sistema de I&D en cada valle con soporte universitario.", "m": "Perú como potencia mundial en biodiversidad y orgánicos.", "c": "¿Tu consulta es sobre Investigación Agrícola?"},
    "comercializacion": {"p": "Deficiente comercialización de productos agrarios.", "o": "Gestionar clusters y cadenas productivas regionales.", "m": "Fortalecimiento de las organizaciones agrarias locales.", "c": "¿Buscas mejorar la Comercialización Agraria?"},
    "gases": {"p": "Deficiente control de emisiones de efecto invernadero.", "o": "Control estricto de contaminantes según Convenio de Kyoto.", "m": "Reducción significativa de la emisión de gases tóxicos.", "c": "¿Te refieres al Control de Emisiones y Medio Ambiente?"},
    "hídricos": {"p": "Manejo inadecuado de recursos hídricos y contaminación.", "o": "Tratamiento obligatorio de aguas residuales y relaves mineros.", "m": "Administración eficiente para contar con agua de calidad.", "c": "¿Deseas ver el plan de Recursos Hídricos?"},
    "bosques": {"p": "Deficiente protección de bosques y tala ilegal.", "o": "Reforestación enérgica (2 millones Ha) con apoyo de reservistas.", "m": "Recuperación masiva de áreas verdes y protección de hábitat.", "c": "¿Buscas detener la Tala Ilegal y Reforestar?"},
    "marinos": {"p": "Deficiente protección de recursos marinos y acidificación.", "o": "Pesca sostenible mitigando impacto de residuos industriales.", "m": "Implementación de PYMES de acuicultura transversal.", "c": "¿Tu interés es sobre la Protección del Mar?"},
    "renovables": {"p": "Deficiente gestión de recursos renovables y no renovables.", "o": "Uso sostenible mediante gestión efectiva de diversidad biológica.", "m": "Adecuada gestión de explotación minera, pesquera y forestal.", "c": "¿Te refieres a la Gestión de Recursos Naturales?"},
    "originarios": {"p": "Deficiente protección de comunidades nativas.", "o": "Garantizar seguridad sobre propiedad de tierras y recursos.", "m": "Mantenimiento de la cultura pluricultural y multilingüe.", "c": "¿Buscas protección para las Comunidades Nativas?"},
    "amazonía": {"p": "Reducida inversión en la Amazonía peruana.", "o": "Capacitación para producción de café, cacao y camu-camu.", "m": "Recursos y financiamiento para comunidades amazónicas.", "c": "¿Deseas ver el plan para la Amazonía?"},
    "limpia": {"p": "Deficiente generación de energía limpia y renovable.", "o": "Priorizar energía Hidráulica, Eólica y Solar con inversión.", "m": "Promover fuentes de energías limpias desde la tecnología.", "c": "¿Buscas información sobre Energía Limpia?"},
    "gas": {"p": "Deficiente distribución de gas natural y alto costo.", "o": "Gaseoductos regionales para distribución casa por casa.", "m": "Consumo masivo de gas natural a precios justos.", "c": "¿Buscas la Masificación del Gas Natural?"},
    "mineria": {"p": "Deficiente modernización de la minería nacional.", "o": "Tecnología limpia y procesos con mayor valor agregado.", "m": "Minería moderna, limpia y compatible con la agricultura.", "c": "¿Te refieres a la Modernización de la Minería?"}
}

# 3. INTERFAZ Y MOTOR DE BÚSQUEDA
query = st.text_input("Identifique un problema o escriba una palabra clave (ej. Escuela, Pymes, Gas, Minería):").lower()

if query:
    encontrado = None
    for clave in base_datos:
        if clave in query:
            encontrado = clave
            break
    
    if encontrado:
        data = base_datos[encontrado]
        st.info(f"📍 **TEMA DETECTADO:** {data['c']}")
        if st.button("SÍ, CONFIRMO ESTE TEMA"):
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.error(f"**EL PROBLEMA IDENTIFICADO**\n\n{data['p']}")
            with col2:
                st.warning(f"**LA SOLUCIÓN RLA**\n\n{data['o']}")
            with col3:
                st.success(f"**LA META AL 2026**\n\n{data['m']}")
    else:
        st.warning("Escribe una palabra clave (ej. Justicia, Maestro, Hambre, PEX) para encontrar la solución técnica.")

st.sidebar.caption("SISTEMA PLAN-RLA v18.0 | 70 Ítems Oficiales")
