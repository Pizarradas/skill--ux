---
id: MEM-04
nombre: Fragmentación (chunking)
nombre_en: Chunking
alias: [agrupamiento, chunking, recodificación, recoding, agrupamiento de contenido]
familia: MEM
evidencia: E2
etiquetas: [agrupacion, escaneo, jerarquia, formato-de-datos, contenido]
refuerza: [MEM-03, MEM-02, MEM-01, PER-01, PER-02, PER-03, PER-04, PER-05, DEC-01, MOT-02]
tensiona: [ACC-01, MOT-04, SIS-01]
tensiones: [T5, T11]
fuente_laws_of_ux: https://lawsofux.com/chunking/
---

# MEM-04 · Fragmentación (*Chunking*)

> La fragmentación es el proceso por el que elementos sueltos se integran en unidades con significado, de modo que cada unidad ocupa un solo "hueco" de memoria. En diseño, designa la práctica de dividir y agrupar el contenido en bloques visual y semánticamente distintos, con jerarquía, para que se escanee, se entienda y se recuerde mejor.

**Idea clave para quien diseña:** el objetivo es la *estructura*, no la escasez: agrupa por significado para que la persona procese bloques, no piezas.

## Resumen operativo
- **Qué dice:** integrar elementos sueltos en unidades con significado reduce lo que hay que sostener en memoria y acelera el escaneo.
- **Evidencia:** E2 — muy replicado en memoria (Miller, Chase & Simon); depende del conocimiento previo: un chunk solo lo es para quien sabe darle sentido.
- **Haz:** 1) agrupa por significado, con un encabezado que nombre cada grupo 2) formatea automáticamente las cadenas largas según la convención (tarjeta 4-4-4-4, IBAN, teléfono) 3) valida los grupos con card sorting o tree testing.
- **Evita:** confundir chunking con "pocos elementos" y paginar o recortar resultados que no hay que memorizar.
- **Sospecha de esta ley cuando…:** hay muros de texto, cadenas largas sin separar o grupos visuales que no coinciden con el modelo mental del usuario.
- **Mide con:** prueba de 5 segundos sobre la estructura; tasa de error de entrada con y sin formato agrupado.
- **Vecinas:** PER-01 Ley de proximidad (refuerza) · MEM-03 Ley de Miller (refuerza) · ACC-01 Ley de Fitts (tensiona, T5)

## Origen
- **Miller (1956)**, "The magical number seven, plus or minus two", *Psychological Review*, 63(2), 81–97 (DOI 10.1037/h0043158). Introduce el término *chunk* y la **recodificación**: un sujeto (Sidney Smith) que se entrenó en agrupar dígitos binarios y renombrar cada grupo retuvo 36 dígitos binarios con grupos de 3 (octales) y unos 40 con grupos de 4 y 5. Miller observó que, a diferencia de otras tareas, la memoria inmediata no se ajustaba a una capacidad constante en bits, sino en unidades.
- **Chase & Simon (1973)**, "Perception in chess", *Cognitive Psychology*, 4(1), 55–81 (DOI 10.1016/0010-0285(73)90004-2). Los expertos recuerdan mucho mejor posiciones *legales* porque las codifican en chunks; la ventaja se reduce en gran medida con posiciones aleatorias. Demuestra que el chunking depende del conocimiento del dominio.
- **Gobet et al. (2001)**, "Chunking mechanisms in human learning", *Trends in Cognitive Sciences*, 5(6), 236–243.
- **Mathy & Feldman (2012)**, *Cognition*: el chunking como compresión de datos.
- Traslado a UX: Moran (2016, NN/g), "How Chunking Helps Content Processing".

## Mecanismo
Hay dos sentidos que conviene separar:
1. **Cognitivo:** agrupar reduce el número de unidades independientes que hay que sostener en la memoria de trabajo (MEM-02). Un chunk lo es solo para quien tiene el conocimiento que le da sentido.
2. **Perceptivo y de diseño:** el agrupamiento visual se apoya en la Gestalt (proximidad, región común, semejanza, conectividad). El sistema perceptivo agrupa antes del procesamiento consciente, lo que permite decidir qué bloque leer y cuál ignorar. Un encabezado o una etiqueta convierte un grupo en una unidad recuperable con un nombre.

El efecto práctico es doble: menos unidades que retener y un escaneo más rápido hacia lo relevante para la meta.

## Evidencia y límites
- **Nivel: E2** — el chunking en memoria está muy replicado (Miller, Chase & Simon, Gobet et al.). Que el texto estructurado y escaneable mejora la lectura en web procede de estudios de NN/g sobre lectura en pantalla; la magnitud depende del contenido y la tarea.
- **Depende del conocimiento previo:** un agrupamiento "lógico" para el equipo puede no serlo para el usuario. Hay que validarlo (card sorting, tree testing).
- **No es una regla de cantidad:** IxDF advierte que el chunking ayuda cuando hay que **memorizar o transcribir**, pero no justifica limitar resultados de búsqueda, menús, desplegables o viñetas a 5–6 elementos. Paginar resultados en grupos minúsculos obliga a más navegación y comparación.
- **Malentendido: "chunking = tener pocos elementos".** Corrección: es organizar en grupos con sentido; una página con 40 elementos bien agrupados puede ser más fácil que una con 10 mezclados.
- **Malentendido: "cualquier caja agrupa".** Corrección: separadores y tarjetas sin relación semántica generan "falso chunking" y añaden carga extrínseca (MEM-01).
- Las cifras tipográficas (líneas de unos 50–75 caracteres, NN/g) son una heurística ampliamente aceptada, no un resultado de chunking en sentido estricto.

## Aplicación práctica
### Reglas
1. [E] Agrupa por significado, no por número: cada grupo debe poder nombrarse con un encabezado descriptivo.
2. [E] Formatea cadenas largas en grupos (teléfono según la convención local, tarjeta 4-4-4-4, IBAN en bloques de 4) y aplica el formato al escribir, sin obligar a teclear separadores (NN/g, Moran 2016).
3. [H] Contenido web: párrafos cortos, subtítulos descriptivos, palabras clave resaltadas, listas y resúmenes; líneas de unos 50–75 caracteres (NN/g).
4. [H] Formularios largos: divide en secciones o pasos temáticos ("Datos de envío", "Pago"), no en cortes arbitrarios, con indicador de progreso (T5).
5. [H] Haz que la agrupación visual coincida con la semántica y con la estructura del código (encabezados, `fieldset`/`legend`, listas, *landmarks*).
6. [E] Valida los grupos con el modelo mental del usuario (card sorting, tree testing).
7. [H] No uses el chunking para limitar resultados de búsqueda o escaneo.
8. [H] Muestra junto lo que se compara; oculta en bloques plegables solo lo que se consulta por separado (T11).

### Por contexto
| Contexto | Aplicación |
|---|---|
| Web/escritorio | Encabezados que resumen cada bloque, listas, espacio en blanco, conclusión al principio. |
| Formularios | Secciones temáticas con `fieldset`/`legend`; formato automático de números largos; pasos que coinciden con unidades de significado. |
| Navegación | Categorías paraguas y megamenús con encabezados de grupo; vigilar el coste en descubribilidad. |
| Dashboards/datos | KPI agrupados por pregunta de negocio, con contenedor (región común), alineación y título por grupo. |
| Onboarding | Un concepto por vez, en el momento en que se necesita. |
| Interfaces conversacionales/IA | Respuestas con encabezados, listas cortas y conclusión primero; si se piden varios datos, por grupos o con un formulario, no diez preguntas en un mensaje [H]. |
| Voz | Leer números en grupos (p. ej., un teléfono por bloques) y ofrecer opciones agrupadas por tema. |
| Sistemas de diseño | Componentes de agrupación (secciones, tarjetas, `fieldset`) con reglas de uso semántico; máscaras de entrada para formatos comunes. |

### Ejemplos
- **Bueno:** una página de configuración organizada en secciones con títulos claros ("Cuenta", "Privacidad", "Notificaciones"), cada una con sus controles relacionados; se escanea por títulos y se entra solo en la sección necesaria.
- **Incumple:** un campo de número de referencia que obliga a escribir 20 caracteres seguidos, sin agrupar y sin permitir pegar, y que en la confirmación lo muestra también sin separar.
- **Incumple (falso chunking):** un panel que reparte métricas en tarjetas con el mismo estilo pero sin criterio común; se percibe orden visual, pero los grupos no significan nada.

## Anti-patrones
- Muros de texto sin encabezados ni listas.
- Cajas y separadores sin relación semántica (falso chunking).
- Paginación en grupos minúsculos "para no saturar".
- Asistentes con un paso por campo (cortes arbitrarios que multiplican clics, T5).
- Acordeones que separan información que debe compararse (T11).
- Agrupación solo visual, inexistente para lectores de pantalla.

## Ética y accesibilidad
- **Línea roja:** agrupar para ocultar (meter costes o condiciones en un bloque plegado con un título ambiguo).
- La agrupación debe existir también en la estructura del documento para que la perciban las tecnologías de apoyo.
- WCAG 2.2: **1.3.1 Información y relaciones** (A); **2.4.6 Encabezados y etiquetas** (AA); **2.4.10 Encabezados de sección** (AAA); **1.4.8 Presentación visual** (AAA, longitud de línea).
- W3C COGA (nota no normativa): 4.3.5 "Break media into chunks", 4.4.10 "Use white spacing", 4.4.5 "Keep text succinct".

## Cómo auditarla
### Señales observables
Bloques de más de unas pocas líneas sin subtítulos; cadenas largas sin separar; formularios de una sola página con más de una docena de campos sin secciones; grupos visuales que no coinciden con el modelo mental del usuario.
### Preguntas
- ¿Se entiende de qué trata cada bloque leyendo solo su título?
- ¿Los grupos visuales coinciden con los semánticos?
- ¿El DOM refleja esa agrupación (encabezados, `fieldset`, listas)?
- ¿Algún límite de elementos se justifica con "chunking" sin que haya nada que memorizar?
### Métricas
- Prueba de 5 segundos: ¿identifican la estructura de la página?
- Card sorting y tree testing para validar grupos y etiquetas.
- Eye-tracking o mapas de calor: ¿se escanean los encabezados?
- Tasa de error de entrada en campos con y sin formato agrupado.

## Relaciones
- Refuerza / se apoya en: MEM-03 Ley de Miller — el concepto de chunk nace allí; agrupar sortea el límite.
- Refuerza / se apoya en: MEM-02 Memoria de trabajo — menos unidades que sostener.
- Refuerza / se apoya en: MEM-01 Carga cognitiva — reduce carga extrínseca si los grupos tienen sentido.
- Refuerza / se apoya en: PER-01 Proximidad, PER-02 Semejanza, PER-03 Región común, PER-04 Conectividad uniforme, PER-05 Prägnanz — son los mecanismos perceptivos del chunking visual.
- Refuerza / se apoya en: DEC-01 Ley de Hick — las categorías reducen las opciones por decisión.
- Refuerza / se apoya en: MOT-02 Gradiente de meta — pasos agrupados hacen visible el progreso.
- Tensiona con: ACC-01 Ley de Fitts y MOT-04 Ley de Parkinson — cada nivel o paso añade interacción y tiempo (T5).
- Tensiona con: escaneo y comparación — fragmentar oculta lo que se compara (T11).
- Tensiona con: SIS-01 Ley de Jakob — agrupar distinto de la convención desorienta.
- Se confunde a menudo con: "reducir elementos" (SIS-04 Occam) — chunking estructura; Occam elimina.

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/chunking/ — síntesis divulgativa.
- Primarias:
  - Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review*, 63(2), 81–97. https://doi.org/10.1037/h0043158 (texto: https://psychclassics.yorku.ca/Miller/)
  - Chase, W. G. & Simon, H. A. (1973). Perception in chess. *Cognitive Psychology*, 4(1), 55–81. https://doi.org/10.1016/0010-0285(73)90004-2 (contenido según la literatura conocida; texto no leído: tras muro de pago, sin copia abierta localizada)
  - Gobet, F., Lane, P., Croker, S., Cheng, P. et al. (2001). Chunking mechanisms in human learning. *Trends in Cognitive Sciences*, 5(6), 236–243. https://doi.org/10.1016/S1364-6613(00)01662-4
  - Mathy, F. & Feldman, J. (2012). What's magic about magic numbers? Chunking and data compression in short-term memory. *Cognition*, 122(3), 346–362. https://doi.org/10.1016/j.cognition.2011.11.003
- Secundarias consultadas:
  - Moran, K. (2016). How Chunking Helps Content Processing. NN/g. https://www.nngroup.com/articles/chunking/
  - IxDF, Chunking (glosario). https://ixdf.org/literature/book/the-glossary-of-human-computer-interaction/chunking
  - Halarewich, D. (2016). Reducing Cognitive Overload For A Better User Experience. Smashing Magazine. https://www.smashingmagazine.com/2016/09/reducing-cognitive-overload-for-a-better-user-experience/
  - W3C COGA, Making Content Usable. https://www.w3.org/TR/coga-usable/
