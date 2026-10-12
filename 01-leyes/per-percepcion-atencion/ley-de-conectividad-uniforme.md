---
id: PER-04
nombre: Ley de conectividad uniforme
nombre_en: Law of Uniform Connectedness
alias: [ley de conexión uniforme, conectividad, element connectedness]
familia: PER
evidencia: E2
etiquetas: [gestalt, agrupacion, conectores, diagramas, steppers, visualizacion]
refuerza: [PER-03, MOT-02, MEM-04, PER-05]
tensiona: [PER-01, PER-02, MEM-01, SIS-04]
tensiones: []
fuente_laws_of_ux: https://lawsofux.com/law-of-uniform-connectedness/
---

# PER-04 · Ley de conectividad uniforme (*Law of Uniform Connectedness*)

> Los elementos unidos por un conector visual continuo (una línea, una flecha, un trazo o una superficie de color que los enlaza) se perciben como más relacionados que los elementos no conectados, aunque estén más lejos o se parezcan menos.

**Idea clave para quien diseña:** una línea es una afirmación de relación; dibújala sólo donde la relación exista, porque el ojo la creerá.

## Resumen operativo
- **Qué dice:** los elementos unidos por un conector visual continuo se perciben más relacionados que los no conectados, aunque estén lejos o se parezcan poco.
- **Evidencia:** E2 — la conexión agrupa en laboratorio, pero su ventaja sobre la proximidad depende del número de objetos (Han y Humphreys 2003); se olvida que en Palmer y Rock (1994) "conectividad uniforme" es otra cosa (regiones homogéneas como unidades primitivas) y lo de unir con líneas es *element connectedness*.
- **Haz:** 1) cada línea, una relación real 2) un estilo de conector, un significado, con leyenda 3) alternativa textual o estructural para la relación.
- **Evita:** líneas decorativas que crucen grupos y gráficos de líneas sobre categorías nominales.
- **Sospecha de esta ley cuando…:** los usuarios leen como un bloque secciones distintas cruzadas por un filete, o no asocian pasos o pestañas con su contenido.
- **Mide con:** número de cruces y estilos sin leyenda por diagrama; tarea de interpretación de la secuencia representada.
- **Vecinas:** PER-03 Región común (refuerza) · MOT-02 Gradiente de meta (refuerza) · PER-01 Proximidad (tensiona) · MEM-01 Carga cognitiva (tensiona)

## Origen

- **Palmer, S. E. y Rock, I. (1994).** "Rethinking perceptual organization: The role of uniform connectedness." *Psychonomic Bulletin & Review*, 1(1), 29–55. doi:10.3758/BF03200760 (verificado en Crossref; texto completo leído).
- **Dos significados que conviene no mezclar:**
  - **En Palmer y Rock**, la conectividad uniforme es el principio por el que el sistema visual divide la imagen en **regiones conectadas de propiedades homogéneas** (luminosidad, color, textura…); admiten también regiones con gradientes suaves. Proponen que esas regiones son las **unidades primitivas** de la percepción y que se forman *antes* de la agrupación clásica (proximidad, semejanza).
  - **En la divulgación UX** (lawsofux incluido), "conectividad uniforme" significa "une con una línea o un marco lo que quieras relacionar". Eso corresponde a lo que los propios Palmer y Rock llaman **conectividad de elementos** (*element connectedness*): la tendencia de dos o más elementos ya diferenciados a agruparse en una unidad superior cuando están conectados. A diferencia de la conectividad uniforme, presupone elementos previos y es un factor de agrupación clásico; ellos mismos la describen como un caso límite de la proximidad (distancia cero).
- **Debate posterior** (leídos los resúmenes):
  - Peterson (1994), comentario en la misma revista (vol. 1, n.º 4): la teoría implica un orden serial de procesos que choca con la evidencia sobre figura-fondo, fusión estereoscópica y reconocimiento de objetos; señala además que Koffka (1935) ya había planteado la necesidad de un principio de formación de unidades parecido.
  - Kimchi (2000), *Vision Research*: la conectividad uniforme no es *necesaria* para designar unidades de nivel básico; colinealidad y cierre organizan muy pronto segmentos desconectados.
  - Han, Humphreys y Chen (1999): la agrupación por proximidad puede ser tan rápida como la conectividad uniforme, y la de semejanza de forma es más lenta. Han y Humphreys (2003): la igualdad se da con uno o dos objetos globales; con más objetos, la conectividad es más rápida.

## Mecanismo

En el mundo físico, un conector continuo (un cable, una rama, una carretera) indica con mucha fiabilidad que dos cosas forman parte del mismo objeto o sistema. La línea convierte elementos separados en una única región conectada, que el sistema visual trata como unidad.

En interfaces y diagramas la línea añade una **semántica aprendida**: relación, flujo, secuencia o dependencia. Por eso un conector no sólo agrupa, también sugiere dirección y orden.

## Evidencia y límites

- **Nivel: E2.** Evidencia de laboratorio sólida de que la conexión agrupa; su fuerza relativa frente a la proximidad depende del número de objetos y de la tarea, y el estatus teórico (si es "primitiva" o "anterior a todo") está discutido. En UX no hay estudios controlados con cifras en las fuentes revisadas.
- **Límites:**
  - La conexión puede imponer relaciones **falsas**: una línea decorativa que pasa entre dos elementos no relacionados los une perceptivamente.
  - Muchos conectores producen "espaguetis": cruces, ambigüedad y carga.
  - Smashing Magazine (Bradley 2014) sostiene que la línea no necesita tocar los elementos para conectarlos; es razonable, pero no se ha localizado respaldo experimental.
- **Malentendidos frecuentes:**
  1. *"Es el principio de agrupación más fuerte."* Afirmación divulgativa (Smashing Magazine); la investigación muestra que depende del contexto.
  2. *"Marcos y colores también son conectividad."* lawsofux los incluye, lo que la solapa con PER-03 y PER-02. Para diseñar y auditar, sepáralos: **conector lineal → conectividad; contenedor cerrado → región común; atributo compartido → semejanza.**

## Aplicación práctica

### Reglas

1. [H] Cada conector debe representar una relación real (secuencia, pertenencia, dependencia); elimina líneas decorativas que crucen grupos.
2. [H] Un estilo de conector, un significado (p. ej., continua = dependencia, discontinua = relación opcional), con leyenda si hay más de uno.
3. [H] Minimiza los cruces en diagramas y organigramas; si son inevitables, usa puentes o reorganiza.
4. [H] En visualización, no unas con línea categorías sin orden: la línea sugiere continuidad y tendencia inexistentes (práctica estándar de visualización).
5. [H] Usa *leader lines* (líneas guía) cuando la etiqueta no puede ir junto al dato.
6. [H] Fusiona visualmente la pestaña activa con su panel (sin borde entre ambos).
7. [Norma] Si el conector es necesario para entender la relación, contraste ≥ 3:1 (WCAG 1.4.11) y una alternativa textual o estructural (WCAG 1.1.1, 1.3.1).
8. [H] Si el tipo de conexión se codifica por color, añade también estilo de línea o etiqueta (WCAG 1.4.1).

### Por contexto

| Contexto | Aplicación |
|---|---|
| Web/escritorio | Pestañas fusionadas con su panel; en mega-menús, fondo o conector continuo entre ítem y submenú. |
| Móvil/táctil | Líneas de tiempo verticales (seguimiento de pedido); conectores en indicadores de pasos. |
| Formularios | Línea o corchete que une campos interdependientes (rango "desde–hasta") o una opción con sus subopciones condicionales. |
| Onboarding | *Steppers* con línea entre pasos que comunica secuencia y pertenencia; el tramo recorrido, resaltado, refuerza el progreso (MOT-02). |
| Dashboards/datos | La línea de un gráfico de líneas es la serie; *slope charts* y *dumbbell plots* conectan dos valores de la misma entidad; nunca líneas sobre categorías nominales. |
| E-commerce | Checkout con pasos conectados; no conectar visualmente un complemento opcional con un paso obligatorio. |
| Interfaces conversacionales/IA | Hilos con línea vertical que une respuesta y mensaje original; indicador que conecta una cita en el texto con su fuente; línea de tiempo con los pasos de herramienta de un agente. |
| Sistemas de diseño | Componentes de conector (stepper, timeline, árbol) con estilos y significados documentados. |

### Ejemplos

- **Bueno: seguimiento de un pedido.** Pedido, preparado, enviado y entregado, unidos por una línea vertical; el tramo completado tiene otro tono. El usuario entiende orden y estado de un vistazo; el lector de pantalla recibe una lista ordenada con el paso actual marcado.
- **Malo: gráfico de líneas sobre categorías.** Ventas por región (norte, sur, este, oeste) unidas por una línea: sugiere una "tendencia" entre regiones que no existe; un gráfico de barras es lo correcto.
- **Malo: filete decorativo.** Una línea ornamental horizontal atraviesa dos tarjetas de secciones distintas y las hace parecer un mismo bloque.

## Anti-patrones

- Líneas u ornamentos que atraviesan secciones no relacionadas.
- Diagramas con muchos cruces o con varios estilos de línea sin leyenda.
- Gráficos de líneas sobre variables nominales.
- *Steppers* sin conector, o pestañas visualmente separadas de su panel.
- Relación transmitida sólo por la línea, sin texto ni estructura.

## Ética y accesibilidad

- **Línea roja:** conectar visualmente una oferta de pago con un paso obligatorio del flujo para que parezca necesaria (*sneaking*).
- **WCAG 1.4.11 Contraste no textual (AA):** conectores necesarios para entender la relación, ≥ 3:1 con el fondo.
- **WCAG 1.1.1 Contenido no textual (A)** y **1.3.1 Información y relaciones (A):** la relación expresada por líneas necesita alternativa: lista ordenada para pasos, `aria-current="step"`, descripción del diagrama.
- **WCAG 1.4.1 Uso del color (A):** tipos de conexión no codificados sólo por color.

## Cómo auditarla

### Señales observables
- Líneas que unen elementos sin relación; diagramas "espagueti".
- Gráficos de líneas sobre categorías.
- Pasos o pestañas que el usuario no asocia con su contenido.

### Preguntas
- ¿Cada conector significa una relación real?
- ¿La relación se entiende sin ver la línea (lector de pantalla, bajo contraste)?
- ¿Cada estilo de conector tiene un único significado?
- ¿Se está llamando "conectividad" a algo que en realidad es un contenedor (PER-03) o un color compartido (PER-02)?

### Métricas
- **Número de cruces** por diagrama y número de estilos de conector sin leyenda.
- **Contraste** de cada conector necesario (≥ 3:1).
- **Tarea de interpretación** en test: ¿los participantes describen correctamente la secuencia o dependencia representada?
- Revisión con lector de pantalla: la secuencia y el paso actual se anuncian.

## Relaciones

- Refuerza / se apoya en:
  - PER-03 Ley de región común — principio hermano (Palmer 1992), a menudo confundido con este.
  - MOT-02 Efecto de gradiente de meta — el progreso conectado y visible motiva.
  - MEM-04 Fragmentación — el conector convierte varios elementos en una unidad.
  - PER-05 Ley de Prägnanz — conexiones simples y regulares se leen mejor.
- Tensiona con:
  - PER-01 Proximidad y PER-02 Semejanza — en ciertas condiciones la conexión se impone a ambas; una línea mal puesta anula un buen espaciado.
  - MEM-01 Carga cognitiva — el exceso de conectores satura.
  - SIS-04 Navaja de Occam — cada línea que no comunica relación sobra.
- Se confunde a menudo con:
  - PER-03 Región común (marcos y fondos) y PER-02 Semejanza (colores): ver la regla de separación en "Evidencia y límites".
  - El sentido original de Palmer y Rock (regiones uniformes como unidades primitivas) frente al sentido divulgativo (unir con líneas).

## Fuentes

- Laws of UX (Jon Yablonski): https://lawsofux.com/law-of-uniform-connectedness/ — síntesis divulgativa.
- Primarias:
  - Palmer, S. E. y Rock, I. (1994). Rethinking perceptual organization: The role of uniform connectedness. *Psychonomic Bulletin & Review*, 1(1), 29–55. doi:10.3758/BF03200760
  - Kimchi, R. (2000). The perceptual organization of visual objects: A microgenetic analysis. *Vision Research*, 40(10–12), 1333–1347. doi:10.1016/S0042-6989(00)00027-4 (sólo resumen).
  - Peterson, M. A. (1994). The proper placement of uniform connectedness. *Psychonomic Bulletin & Review*, 1(4), 509–514. doi:10.3758/BF03210956 (sólo resumen).
  - Han, S., Humphreys, G. W. y Chen, L. (1999). Uniform connectedness and classical Gestalt principles of perceptual grouping. *Perception & Psychophysics*, 61(4), 661–674. doi:10.3758/BF03205537 (sólo resumen).
  - Han, S. y Humphreys, G. W. (2003). Relationship between uniform connectedness and proximity in perceptual grouping. *Science in China, Series C*, 46(2), 113–126. doi:10.1360/03yc9013 (sólo resumen).
  - Wagemans, J. et al. (2012). *Psychological Bulletin*, 138(6), 1172–1217. doi:10.1037/a0029333
- Secundarias consultadas:
  - IxDF, Laws of Proximity, Uniform Connectedness, and Continuation: https://ixdf.org/literature/article/laws-of-proximity-uniform-connectedness-and-continuation-gestalt-principles-2
  - Bradley, S. (2014). Smashing Magazine: https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/
  - Wikipedia, *Principles of grouping*: https://en.wikipedia.org/wiki/Principles_of_grouping
