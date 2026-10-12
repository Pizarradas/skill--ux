# Sobre *Laws of UX* (Jon Yablonski) y la relación de este sistema con él

> Documento de referencia. Explica qué es *Laws of UX*, bajo qué licencia se publica, qué se sabe (y qué no) de los libros, qué propone *Humane by Design* y de qué tratan los artículos del sitio — y cómo este sistema se apoya en todo ello y lo amplía.
> Convención: **[V]** verificado leyendo la fuente o su ficha · **[S]** conocido por fuentes secundarias · **[?]** dudoso o contradictorio. Consulta: octubre de 2026.

---

## 1. El sitio lawsofux.com

- **Autor:** Jon Yablonski, diseñador. El sitio se presenta como una colección de buenas prácticas de psicología aplicables al diseño de interfaces **[V]**.
- **Contenido:** **30 leyes**, cada una con una página propia que incluye una definición breve, una lista de conclusiones prácticas (*takeaways*), en algunos casos ejemplos, un apartado de origen con enlace a la fuente y una lista de lecturas adicionales (*Further Reading*) **[V]**. Cada ley tiene un póster descargable gratis y una versión impresa de gran formato a la venta **[V]**.
- **Clasificación del propio sitio:** dos categorías, **Psychology** (7 leyes: Chunking, Cognitive Bias, Cognitive Load, Flow, Mental Model, Selective Attention, Working Memory) y **Theory** (las 23 restantes) **[V, según la copia local de las páginas]**. No distingue niveles de evidencia.
- **Otros recursos del sitio:** página «Info» (autoría, licencia y libro), página del libro, sección de artículos (/articles), una versión en español (lawsofux.com/es/) y un fichero `llms.txt` que describe el sitio para modelos de lenguaje **[V]**. La página «Info» no se ha leído directamente **[S]**.

## 2. Licencia: CC BY-NC-ND 4.0 y lo que implica

El pie de página del sitio enlaza a la licencia **Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional** (https://creativecommons.org/licenses/by-nc-nd/4.0/) **[V]**. El `llms.txt` del sitio lo describe como recurso «libre y de código abierto»; a efectos de reutilizar textos manda la licencia declarada, que es bastante más restrictiva **[V]**.

| Cláusula | Qué exige | Consecuencia para este sistema |
|---|---|---|
| **BY** (atribución) | Reconocer autoría y enlazar la fuente y la licencia. | Cada ficha enlaza su página en lawsofux.com y menciona a Yablonski. |
| **NC** (no comercial) | No usar el material licenciado con fines comerciales. | No se incorpora texto ni gráficos (pósteres) del sitio, para que el sistema pueda usarse en cualquier contexto. |
| **ND** (sin derivadas) | Se puede compartir copia literal, pero no distribuir versiones modificadas. Una **traducción** cuenta como obra derivada. | No se traducen ni adaptan las definiciones ni los *takeaways*. |

**Decisión de diseño de este sistema:** es una **síntesis original con atribución**, no una traducción ni una adaptación. En concreto:

1. Todas las definiciones, reglas y ejemplos están **redactados de nuevo** a partir de las fuentes primarias (Nielsen, Tesler, Craik, Norman, Juran, etc.) y de literatura secundaria verificada.
2. Lo que se toma de lawsofux.com son **hechos e ideas** (qué leyes recoge, qué autor las acuñó, qué lecturas recomienda), que no están protegidos como expresión; nunca su **redacción**.
3. Cada ficha de `01-leyes/` lleva en `fuente_laws_of_ux` la URL de su página y la presenta como «síntesis divulgativa», no como fuente primaria.
4. Cuando una ficha menciona un ejemplo que también aparece en el sitio (p. ej. el rediseño de YouTube de 2017), se describe con palabras propias y se atribuye.

*Nota: esto es un criterio editorial prudente, no asesoramiento jurídico.*

## 3. Los libros *Laws of UX* (O'Reilly)

### 3.1 Primera edición (2020)
- Yablonski, J. (2020). ***Laws of UX: Using Psychology to Design Better Products & Services***. O'Reilly Media. Publicada en abril de 2020 (la reseña de UXmatters indica el 21-04-2020 y unas 190 páginas) **[V vía reseña]**.
- **ISBN:** la edición impresa (rústica) es **9781492055310** (ISBN-10 149205531X); 9781492055303 (el que usa O'Reilly Learning) y 9781492055280 (el que cita Wikipedia) son ISBN de libro electrónico **[V vía catálogos: isbnsearch.org y Open Library; la página de O'Reilly no fue accesible]**.
- **Estructura — 12 capítulos** (según la reseña de D. Ben Woods en UXmatters, noviembre de 2020) **[V vía reseña]**:

| Cap. | Título | Ficha en este sistema |
|---|---|---|
| 1 | Jakob's Law | SIS-01 |
| 2 | Fitts's Law | ACC-01 |
| 3 | Hick's Law | DEC-01 |
| 4 | Miller's Law | MEM-03 |
| 5 | Postel's Law | ACC-03 |
| 6 | Peak-End Rule | MOT-05 |
| 7 | Aesthetic-Usability Effect | DEC-04 |
| 8 | von Restorff Effect | PER-07 |
| 9 | Tesler's Law | SIS-03 |
| 10 | Doherty Threshold | ACC-02 |
| 11 | With Power Comes Responsibility | `06-etica-accesibilidad/` |
| 12 | Applying Psychological Principles in Design | `04-procesos/` |

- El libro cubre **10 leyes**; el sitio, 30. Pareto, Occam y Modelo mental no tienen capítulo propio (el modelo mental se trata dentro del capítulo de Jakob).
- La única crítica de fondo de la reseña: el tratamiento de la ley de Miller estaba desactualizado, ya que la capacidad de memoria de trabajo se estima hoy en torno a 4 ± 1 elementos (véase MEM-03).
- **Patrón de cada capítulo** (según la web del autor y reseñas): enunciado de la ley, conceptos psicológicos de base, ejemplos de producto, consideraciones y conclusión **[S]**.

### 3.2 Segunda edición (2024)
- O'Reilly, 2024. O'Reilly la fecha en enero de 2024 y la web del autor en marzo de 2024; los catálogos dan el libro electrónico en Kindle el 23-01-2024 y la rústica en febrero de 2024 **[V vía catálogos]**. Existe traducción alemana (O'Reilly/dpunkt, Heidelberg, 2024, 163–164 págs. según la edición; ISBN impreso 978-3-96009-246-9) **[V: catálogo de la Deutsche Nationalbibliothek]**. **ISBN:** rústica **9781098146962**; 9781098146955 (el de la URL de O'Reilly Learning) corresponde al libro electrónico **[V vía catálogos: isbnsearch.org y Open Library]**.
- **Verificado:** el prefacio incluye secciones nuevas, entre ellas una breve historia de la relación entre psicología y diseño (Gestalt, factores humanos, HCI, diseño UX) **[V vía búsqueda]**; el capítulo 1 sigue siendo Jakob's Law y el libro cierra con «With Power Comes Responsibility», que incluye un apartado sobre *dark patterns* **[V parcial]**.
- **Novedades declaradas por el autor** (jonyablonski.com) **[V]**: conexión más profunda con los conceptos psicológicos subyacentes; conceptos nuevos como paradoja de la elección, sesgo de complejidad y flow; consideraciones como el factor humano, la accesibilidad, la paradoja del usuario activo y la personalización; métodos como la indagación contextual, las entrevistas y el *eye-tracking*; ejemplos actualizados que mencionan LLM, IA generativa de imágenes y computación espacial. La página no detalla a qué capítulo va cada novedad.
- **No verificado:** la lista completa de capítulos de la 2.ª edición. Es probable que mantenga las mismas 10 leyes, pero es una inferencia **[?]**.

## 4. *Humane by Design*

Proyecto de Yablonski (humanebydesign.com) que empezó como notas personales y pasó a serie de pósteres y sitio web; Sketch lo reseñó en marzo de 2020 **[V]**. Propone una guía para hacer productos digitales menos invasivos, adictivos, engañosos o dañinos, y para anteponer el tiempo, la atención y el bienestar de las personas a las métricas de negocio a corto plazo.

**Siete principios** (lista actual de la web **[V]**; una fuente secundaria antigua nombra «Thoughtful» en lugar de «Intentional», quizá un cambio de nombre **[?]**). Resumen en palabras propias:

| Principio | Idea | Dónde se aplica en este sistema |
|---|---|---|
| **Resilient** (resiliente) | Proteger a los más vulnerables y anticipar abusos: control sobre quién ve el contenido, moderación, diseñar para casos límite, combinar datos cuantitativos y cualitativos. | Contrapeso de SIS-05 Pareto (T9). |
| **Empowering** (empoderador) | Valor para la persona por encima del ingreso: control sobre algoritmos, privacidad, conciencia del propio uso, persona en el circuito para entender decisiones de IA. | SIS-03 Tesler (automatización), SIS-02 Modelo mental, `03-aplicacion/interfaces-ia-conversacionales.md`. |
| **Finite** (finito) | Experiencias con final: aviso de «estás al día», «cargar más» en lugar de scroll infinito, «siguiente» en lugar de reproducción automática. | MOT-01 Flow, MOT-03 Zeigarnik (T7, T10). |
| **Inclusive** (inclusivo) | Diseñar con y para la diversidad: equipos diversos, diseñar primero para la discapacidad, control de zoom, contraste, tamaño de texto y movimiento. | `06-etica-accesibilidad/accesibilidad.md`, SIS-05. |
| **Intentional** (intencional) | Fricción deliberada cuando protege: confirmaciones, frenos contra el abuso, herramientas para moderar el consumo. | Contrapeso de SIS-04 Occam y SIS-03 Tesler (T1, T10). |
| **Respectful** (respetuoso) | Respetar tiempo y atención: notificaciones proporcionales a la urgencia, configurables y con el contenido completo. | PER-06 Atención selectiva, ACC-04. |
| **Transparent** (transparente) | Honestidad, sin *dark patterns*: consentimiento informado, acceso a los datos, derecho al olvido, anuncios reconocibles, salida fácil. | Contrapeso de SIS-01 Jakob y SIS-02 Modelo mental; `06-etica-accesibilidad/etica-y-patrones-oscuros.md`. |

*Nota técnica:* algunas páginas de humanebydesign.com y jonyablonski.com contienen instrucciones ocultas dirigidas a modelos de lenguaje, ajenas a su contenido; se ignoraron durante la investigación y no deben seguirse.

## 5. La sección /articles (temas, en palabras propias)

Fechas inferidas de la URL. **[V]** salvo indicación.

| Año | Artículo | De qué trata |
|---|---|---|
| 2024 | Familiar vs Novel | Lo familiar suele ganar, pero la novedad compensa para diferenciarse, para señalar un cambio tecnológico de fondo (el ejemplo es la búsqueda conversacional) o en experiencias de exploración; siempre validada con investigación y sin sacrificar usabilidad. → SIS-01, SIS-02 |
| 2024 | Onboarding for Active Users | A partir de Carroll y Rosson (1987): los tours de producto se saltan; funcionan mejor la ayuda contextual, el onboarding progresivo y las plantillas de inicio. → ACC-04 |
| 2024 | Tesler's Law | Historia de la ley, sesgo de complejidad, ejemplos de complejidad absorbida por el sistema (autocompletar, heredar datos de facturación, pago con cartera, consultas en lenguaje natural), divulgación progresiva y el riesgo de simplificar hasta la abstracción. → SIS-03 |
| 2020 | UX Psychology: Google Search | Análisis del buscador de Google a la luz de Hick, memoria de trabajo, Doherty, fragmentación, proximidad y conectividad uniforme. → DEC-01, MEM-02, ACC-02 |
| 2020 | Peak-End Rule | Cuidar los momentos de máxima intensidad y el cierre de la experiencia (solo leído el resumen). → MOT-05 |
| 2018 | The Psychology of Design (publicado en *A List Apart*) | Hick, Miller y fragmentación, Jakob y modelos mentales; choque de modelo mental (rediseño de Snapchat de 2018 frente a la transición opcional de YouTube); aviso ético: la psicología también sirve para crear productos adictivos, así que hay que preguntarse si algo debe construirse y mirar más allá de las métricas de uso. |
| 2017 | Designing with Occam's Razor | Empezar por lo mínimo, justificar cada elemento, recortar sin contemplaciones, usar la crítica de diseño; referencias a Rams y Saint-Exupéry. → SIS-04 |
| 2015 | Design Principles for Reducing Cognitive Load | Fuentes de esfuerzo mental innecesario y cómo reducirlas (solo leído el resumen). → MEM-01 |

## 6. El marco de Yablonski: hilo conductor y límites

**Ideas de fondo** (síntesis propia de libro, artículos y *Humane by Design*):
1. La psicología humana es un «plano» relativamente estable: el diseño se adapta a ella, no al revés; por eso los principios sobreviven a los cambios de tecnología.
2. Las leyes son **heurísticas para razonar**, no reglas mecánicas (él mismo desaconseja usar «7 ± 2» como tope rígido de elementos en un menú).
3. Toda aplicación de una ley debe pasar por investigación y test.
4. El poder de influir conlleva responsabilidad ética (capítulo final del libro, *Humane by Design*).

**Límites del marco:**
- El sitio llama «ley» por igual a modelos cuantitativos muy replicados (Fitts) y a heurísticas o constructos (Pareto, Occam, Modelo mental).
- Las lecturas recomendadas mezclan literatura primaria con artículos divulgativos.
- Algunas afirmaciones de origen son simplificaciones o contienen imprecisiones históricas (véase §7).
- Se centra en la persona individual frente a la pantalla; trata menos los productos con IA, la voz o los agentes.

## 7. Cómo se relaciona este sistema con *Laws of UX* y en qué lo amplía

**Lo que toma:** el catálogo de 30 leyes como columna vertebral (mismas leyes, misma URL de referencia por ficha), la postura de que las leyes son heurísticas que hay que validar y la preocupación ética.

**Lo que añade:**

| Ampliación | Dónde |
|---|---|
| **Niveles de evidencia** explícitos por ley (E1, E2, E3, C, H) con justificación. | `00-indice/niveles-de-evidencia.md`, campo `evidencia` de cada ficha. |
| **Familias funcionales** (PER, MEM, DEC, ACC, MOT, SIS) en lugar de la dicotomía Theory/Psychology. | `00-indice/mapa-global.md` |
| **Tensiones** entre leyes con regla de resolución (T1–T14). | `02-relaciones/tensiones.md` |
| **Fuentes primarias** con autor, año y DOI/URL, y marcas de verificación. | Sección «Fuentes» de cada ficha. |
| **Correcciones y matices históricos** que el sitio no recoge, p. ej.: la fecha de la ley de Tesler (c. 1984) y su lugar real (Apple, durante el desarrollo de MacApp, según el propio Tesler; no Xerox PARC); la frase «no multiplicar los entes» es de John Punch (1639), no de Ockham; el «principio de Pareto» lo formuló Juran, que lo reconoció en su *mea culpa* y cambió «muchos triviales» por «muchos útiles»; los datos de MeasuringU muestran concentración pero lejos de 80/20; la «ley potencial» de la práctica que sostiene a Jakob puede ser un artefacto de promediar (Heathcote et al. 2000). | SIS-01, SIS-03, SIS-04, SIS-05 |
| **Aplicación por contexto**, incluida IA conversacional y voz (p. ej. modelo del límite de error de la IA, Bansal et al. 2019; barrera de articulación y coste de verificación). | `03-aplicacion/`, tablas «Por contexto». |
| **Auditoría operativa**: señales, preguntas y métricas por ley. | Sección «Cómo auditarla», `04-procesos/auditar.md`. |
| **Accesibilidad** vinculada a criterios WCAG 2.2 concretos. | Sección «Ética y accesibilidad», `06-etica-accesibilidad/`. |
| **Diseño agnóstico de modelo:** pensado para que cualquier agente o persona razone con él, no para un producto concreto. | `AGENTS.md` |

**Regla para quien use este sistema:** cita lawsofux.com como puerta de entrada divulgativa y reconocimiento de autoría; para afirmaciones empíricas, cita la fuente primaria de la ficha. No copies ni traduzcas texto del sitio.

## 8. Fuentes

- Laws of UX: https://lawsofux.com/ · artículos: https://lawsofux.com/articles/ · versión en español: https://lawsofux.com/es/ **[V]**
- Licencia CC BY-NC-ND 4.0: https://creativecommons.org/licenses/by-nc-nd/4.0/ **[V]**
- Yablonski, J. (2024). Laws of UX: the 2nd edition. https://jonyablonski.com/articles/2024/laws-of-ux-the-2nd-edition/ **[V]**
- Woods, D. B. (2020). Book review: Laws of UX. UXmatters. https://www.uxmatters.com/mt/archives/2020/11/book-review-laws-of-ux.php **[V]**
- O'Reilly: https://oreilly.com/library/view/laws-of-ux/9781098146955 y /9781492055303 — no accesibles; datos vía resultados de búsqueda **[S]**
- Catálogos para ISBN y fechas: https://isbnsearch.org/isbn/9781492055310 · https://isbnsearch.org/isbn/9781098146962 · Open Library (obra «Laws of UX») · Deutsche Nationalbibliothek (SRU, título «Laws of UX») **[V]**
- *Humane by Design*: https://humanebydesign.com/ y sus siete páginas de principio **[V]**
- Sketch (2020). Documenting the humane design movement. https://sketch.com/blog/documenting-the-humane-design-movement **[V]**
