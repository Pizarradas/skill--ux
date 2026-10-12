---
id: PER-03
nombre: Ley de región común
nombre_en: Law of Common Region
alias: [principio del contenedor, agrupación por región delimitada]
familia: PER
evidencia: E2
etiquetas: [gestalt, agrupacion, contenedores, tarjetas, layout]
refuerza: [PER-01, MEM-04, PER-05, MEM-01]
tensiona: [PER-01, PER-02, DEC-04, SIS-04, PER-06]
tensiones: [T5]
fuente_laws_of_ux: https://lawsofux.com/law-of-common-region/
---

# PER-03 · Ley de región común (*Law of Common Region*)

> Los elementos situados dentro de un mismo área con un límite definido (un borde, un fondo propio, una tarjeta) se perciben como un grupo, y se interpreta que comparten función o característica, aunque sean de tipos distintos.

**Idea clave para quien diseña:** un contenedor es la señal de agrupación más fuerte y la más cara visualmente; úsalo cuando el espacio en blanco no basta, y nunca sin una unidad lógica detrás.

## Resumen operativo
- **Qué dice:** lo que está dentro de un mismo límite (borde, fondo, tarjeta) se percibe como grupo, aunque sea heterogéneo.
- **Evidencia:** E2 — Palmer (1992) muestra que puede imponerse a proximidad y semejanza; se olvida que es un principio moderno (no de Wertheimer) y que su fuerza relativa depende del contexto.
- **Haz:** 1) un contenedor por unidad lógica 2) controles dentro de la región sobre la que actúan 3) anidamiento máximo de 2–3 niveles.
- **Evita:** cajas "por si acaso" donde bastaría el espacio en blanco, y grupos que dependen sólo del color de fondo.
- **Sospecha de esta ley cuando…:** se asocian precio o valoración al ítem equivocado; el scroll se corta tras una franja de color.
- **Mide con:** tarea de asociación atributo–ítem; profundidad de scroll antes y después de franjas a ancho completo.
- **Vecinas:** PER-01 Proximidad (refuerza) · MEM-04 Fragmentación (refuerza) · SIS-04 Navaja de Occam (tensiona) · Pasos↔coste de interacción (tensiona, T5)

## Origen

- **Palmer, S. E. (1992).** "Common region: A new principle of perceptual grouping." *Cognitive Psychology*, 24(3), 436–447. doi:10.1016/0010-0285(92)90014-S (paginación y DOI verificados en Crossref y PubMed; leído el resumen).
- Palmer muestra que la región común puede **imponerse** a la proximidad y a la semejanza, que depende de las relaciones de profundidad percibidas, que la domina la región de fondo más pequeña, que admite anidamiento jerárquico y que no se reduce a otros factores conocidos (proximidad, cierre).
- **No es un principio de Wertheimer (1923).** Es una incorporación posterior, del entorno de Palmer y Rock, aunque la divulgación la presente junto a los principios clásicos. La revisión de Wagemans et al. (2012) la cuenta entre los "nuevos principios de agrupación", junto al destino común generalizado, la sincronía y la conectividad (de elementos y uniforme).

## Mecanismo

Un contorno cerrado se interpreta como la superficie u objeto que contiene a los elementos, y pertenecer al mismo objeto es un indicio muy fuerte de relación. El límite crea además una jerarquía de **figura y fondo anidada**: la región es figura respecto a la página y fondo respecto a su contenido.

Por eso funciona con elementos heterogéneos (imagen, texto, botón) que no comparten semejanza ni están necesariamente más cerca entre sí que de sus vecinos: el contenedor impone la pertenencia desde fuera.

## Evidencia y límites

- **Nivel: E2.** Evidencia de laboratorio clara (Palmer 1992 y trabajos posteriores de su grupo). En UX, NN/g (Harley 2020) la describe como una señal fuerte, capaz de imponerse a otros principios, pero no hay experimentos controlados con cifras en las fuentes revisadas.
- **Condiciones de validez y matices:**
  - Es especialmente útil cuando hay que contener elementos heterogéneos o cuando no se puede ajustar el espacio en blanco (NN/g, con ejemplos como un diálogo de impresión de escritorio o un sitio de recetas que mejoró al pasar de rejilla a tarjetas).
  - Su "fuerza" relativa depende del contexto; no hay un ranking universal entre principios.
- **Riesgos documentados:**
  - **Ruido visual:** bordes añadidos "por si acaso"; a menudo basta el espacio (NN/g).
  - **Falso suelo:** una franja de fondo a ancho completo puede hacer creer que la página ha terminado y cortar el scroll (NN/g).
  - **Anidamiento excesivo** (tarjeta dentro de tarjeta dentro de panel): la jerarquía se vuelve ilegible [H].
- **Malentendidos frecuentes:**
  1. *"Más cajas = más orden."* Cada contenedor añade un nivel de jerarquía y peso visual; sin función de agrupación, confunde.
  2. *"Si se ve agrupado, está agrupado."* Para tecnologías de apoyo, la región sólo existe si existe en el código.

## Aplicación práctica

### Reglas

1. [H] Antes de añadir un borde o fondo, responde (preguntas propuestas por NN/g): ¿es necesario para mostrar el grupo?, ¿bastaría el espacio en blanco?, ¿hay que separar estos elementos de los vecinos?, ¿los usuarios se confundieron sin él en un test?
2. [H] Cada contenedor corresponde a una unidad lógica (un producto, un widget, un bloque de formulario).
3. [H] Los controles van **dentro** de la región sobre la que actúan; los controles globales, en una región distinta y claramente diferenciada.
4. [H] Limita el anidamiento a 2–3 niveles.
5. [H] La etiqueta de una pestaña o acordeón comparte región con su panel.
6. [Norma] Si el límite es lo único que identifica un control (p. ej., el borde de un campo), necesita contraste ≥ 3:1 (WCAG 1.4.11). Si es decorativo y la agrupación se comunica por otros medios, no.
7. [H] No dependas sólo del color de fondo: en modos de colores forzados los fondos desaparecen; añade borde o espacio como respaldo.
8. [H] Cada región visual con semántica equivalente (landmarks, `fieldset`/`legend`, `role="group"` con `aria-labelledby`).

### Por contexto

| Contexto | Aplicación |
|---|---|
| Web/escritorio | Cabecera, pie y navegación con fondo propio, sobre todo si la cabecera es fija; tarjetas para ítems compuestos (imagen, título, metadatos, acción). |
| Móvil/táctil | Tarjetas o filas con fondo para delimitar el área pulsable de cada ítem; hojas inferiores (*bottom sheets*) como región clara de una tarea. |
| Formularios | Bloques como "Dirección de envío" con fondo o borde sutil; paneles sólo cuando el formulario es largo y heterogéneo. |
| Navegación | Panel de submenú que comparte región con su ítem padre. |
| Dashboards/datos | Cada widget en su contenedor con título y filtros locales dentro; filtros globales en una región aparte. Bandas sombreadas para agrupar periodos en gráficos (campañas, recesiones). Cebrado de filas en tablas comparativas. |
| E-commerce | Tarjeta de producto que encierra precio, valoración y botón, para que no se asocien al vecino; resumen de pedido como región propia. |
| Interfaces conversacionales/IA | Burbuja o bloque por turno; código, tablas y artefactos en contenedor propio con sus acciones dentro; razonamiento o llamadas a herramientas en una región plegable distinta de la respuesta; fuentes en una región asociada a la respuesta. |
| Sistemas de diseño | Pocos tipos de contenedor (tarjeta, panel, sección) con reglas explícitas de cuándo usar cada uno y de cómo se anidan. |

### Ejemplos

- **Bueno: rejilla de recetas convertida en tarjetas.** Antes, las valoraciones y los tiempos de preparación flotaban entre dos fotos y se asociaban a la receta equivocada; al encerrar cada receta en una tarjeta, la pertenencia queda clara (caso descrito por NN/g).
- **Malo: franja de color a ancho completo a mitad de página.** Un bloque promocional con fondo intenso parece el pie; parte de los usuarios deja de desplazarse y no ve el contenido de debajo.
- **Malo: filtros globales dentro de un widget.** Un selector de fechas que afecta a todo el dashboard está dentro de la tarjeta de un gráfico; el usuario cree que sólo filtra ese gráfico.

## Anti-patrones

- Bordes y fondos "por si acaso", sin unidad lógica detrás.
- Anidamiento de cuatro o más niveles de contenedores.
- Controles fuera de la región sobre la que actúan.
- Franjas de fondo que crean un falso final de página.
- Agrupación que depende sólo del color de fondo.

## Ética y accesibilidad

- **Líneas rojas:**
  - Usar una región para que un anuncio parezca parte de un módulo editorial.
  - Meter en el mismo panel un complemento de pago junto a las opciones obligatorias para que parezca incluido.
- **WCAG 1.3.1 Información y relaciones (A):** las regiones visuales necesitan semántica: `fieldset`/`legend`, landmarks (`header`, `nav`, `main`, `aside`, `footer`), `role="group"` con nombre.
- **WCAG 1.4.11 Contraste no textual (AA):** 3:1 cuando el límite identifica un componente.
- **Modo de colores forzados** (`forced-colors: active`): los fondos se sustituyen; si el grupo dependía sólo del fondo, se pierde (comportamiento documentado de CSS).

## Cómo auditarla

### Señales observables
- Usuarios que asocian precio, valoración o autor al ítem equivocado en rejillas sin contenedor.
- Usuarios que dejan de desplazarse tras una franja de color.
- "Cajas" sin propósito; paneles anidados en más de 2–3 niveles.

### Preguntas
- ¿Cada contenedor corresponde a una unidad lógica?
- ¿Los controles están dentro de la región sobre la que actúan?
- ¿Qué pasa en `forced-colors: active`?
- ¿Bastaría el espacio en blanco (PER-01) en lugar de este borde?

### Métricas
- **Recuento de niveles de anidamiento** por vista (objetivo heurístico ≤ 3).
- **Tarea de asociación** en test: porcentaje de aciertos al relacionar atributos (precio, valoración) con su ítem.
- **Profundidad de scroll** en analítica antes y después de franjas de fondo a ancho completo.
- Revisión del árbol de accesibilidad: cada región visual tiene landmark o grupo con nombre.

## Relaciones

- Refuerza / se apoya en:
  - PER-01 Ley de proximidad — refuerzo mutuo: contenedor y espacio en la misma dirección.
  - MEM-04 Fragmentación — la tarjeta es un fragmento visual.
  - PER-05 Ley de Prägnanz — formas cerradas y simples se leen como unidad.
  - MEM-01 Carga cognitiva — una estructura clara reduce el esfuerzo de interpretación.
- Tensiona con:
  - PER-01 Proximidad y PER-02 Semejanza — suele imponerse a ambas; si se contradicen, gana el contenedor, así que alinéalos.
  - DEC-04 Efecto estética-usabilidad y SIS-04 Navaja de Occam — el exceso de contenedores añade complejidad visual innecesaria.
  - PER-06 Atención selectiva — una región con aspecto de anuncio se ignora.
  - T5 — para tareas cortas, una sola pantalla bien agrupada en regiones suele ser mejor que dividir en pasos.
- Se confunde a menudo con:
  - PER-04 Conectividad uniforme: lawsofux y otras fuentes incluyen "marcos" como conectividad. Para auditar: contenedor cerrado → región común; conector lineal → conectividad.

## Fuentes

- Laws of UX (Jon Yablonski): https://lawsofux.com/law-of-common-region/ — síntesis divulgativa.
- Primarias:
  - Palmer, S. E. (1992). Common region: A new principle of perceptual grouping. *Cognitive Psychology*, 24(3), 436–447. doi:10.1016/0010-0285(92)90014-S. PubMed: https://pubmed.ncbi.nlm.nih.gov/1516361/ (sólo resumen).
  - Wagemans, J. et al. (2012). A century of Gestalt psychology in visual perception: I. *Psychological Bulletin*, 138(6), 1172–1217. doi:10.1037/a0029333
- Secundarias consultadas:
  - Harley, A. (2020). The Principle of Common Region: Containers Create Groupings. NN/g: https://www.nngroup.com/articles/common-region/
  - Bradley, S. (2014). Design Principles: Visual Perception And The Principles Of Gestalt. Smashing Magazine: https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/
  - Wikipedia, *Principles of grouping*: https://en.wikipedia.org/wiki/Principles_of_grouping
