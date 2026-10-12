---
id: PER-01
nombre: Ley de proximidad
nombre_en: Law of Proximity
alias: [principio de cercanía, agrupación por proximidad]
familia: PER
evidencia: E2
etiquetas: [gestalt, agrupacion, espaciado, layout, formularios]
refuerza: [PER-03, MEM-04, MEM-01, MEM-02, ACC-01, DEC-04]
tensiona: [PER-02, PER-03, PER-04, PER-06, SIS-01]
tensiones: [T5, T11]
fuente_laws_of_ux: https://lawsofux.com/law-of-proximity/
---

# PER-01 · Ley de proximidad (*Law of Proximity*)

> Los elementos separados entre sí por menos espacio que el que los separa del resto se leen como un mismo grupo, y se les atribuye una función o un significado comunes. Lo que agrupa no es la distancia absoluta, sino la diferencia entre el espacio interno y el externo.

**Idea clave para quien diseña:** el espacio en blanco es estructura, no decoración: si el hueco dentro del grupo no es claramente menor que el hueco entre grupos, no hay grupo.

## Resumen operativo
- **Qué dice:** lo que está más cerca entre sí que del resto se lee como un grupo con función común; agrupa la diferencia de espacio, no la distancia absoluta.
- **Evidencia:** E2 — psicofísica sólida y hasta cuantificada en retículas de puntos (Kubovy y Wagemans 1995; Kubovy et al. 1998); se olvida que en interfaces reales compite con región común, conectividad y color.
- **Haz:** 1) espacio entre grupos claramente mayor que dentro (≥ 2:1 como convención) 2) etiqueta, error y acción pegados a su elemento 3) comprueba la agrupación a 320 px y con zoom al 200 %.
- **Evita:** el espaciado uniforme, o creer que "poner cerca" basta sin contraste entre hueco interno y externo.
- **Sospecha de esta ley cuando…:** los usuarios asocian una etiqueta, un precio o una acción al elemento vecino equivocado.
- **Mide con:** prueba de desenfoque y razón de espaciado entre grupos / dentro del grupo; tarea de asociación etiqueta–campo.
- **Vecinas:** PER-03 Región común (refuerza) · MEM-04 Fragmentación (refuerza) · PER-02 Semejanza (tensiona) · PER-06 Atención selectiva (tensiona) · Fragmentar↔comparar (tensiona, T11)

## Origen

- **Max Wertheimer (1923)**, *Untersuchungen zur Lehre von der Gestalt II*, *Psychologische Forschung*, 4, 301–350 [verificada]. Traducción inglesa: "Laws of organization in perceptual forms", en W. D. Ellis (ed.), *A Source Book of Gestalt Psychology* (1938), pp. 71–88; disponible en *Classics in the History of Psychology* (York University). La demostración clásica es una hilera de puntos con intervalos alternos, cortos y largos: se ven parejas unidas por el intervalo corto. Wertheimer señala que lo mismo ocurre con secuencias de golpes sonoros y que los factores de agrupación pueden sumarse o competir.
- **Kubovy, M. y Wagemans, J. (1995).** "Grouping by proximity and multistability in dot lattices: A quantitative Gestalt theory." *Psychological Science*, 6(4), 225–234. doi:10.1111/j.1467-9280.1995.tb00597.x (verificado en resumen). En retículas de puntos presentadas brevemente, la atracción entre puntos decae de forma exponencial con la distancia, con un modelo de un solo parámetro (la constante de atracción).
- **Kubovy, M., Holcombe, A. O. y Wagemans, J. (1998).** "On the lawfulness of grouping by proximity." *Cognitive Psychology*, 35(1), 71–98. doi:10.1006/cogp.1997.0673. Reanaliza esos datos: la fuerza relativa de agrupación es función exponencial decreciente de la **distancia relativa** y no depende de la configuración global de la retícula. Wagemans et al. (2012) llaman a este resultado "ley de distancia pura" (*Pure Distance law*).
- **Kubovy, M. y van den Berg, M. (2008).** "The whole is equal to the sum of its parts…", *Psychological Review*, 115(1), 131–154. doi:10.1037/0033-295X.115.1.131: en tres experimentos con retículas de puntos, la fuerza del efecto conjunto de proximidad y semejanza es igual a la suma de sus efectos por separado (combinación aditiva).

## Mecanismo

En el mundo físico, las partes que están juntas suelen pertenecer al mismo objeto; el sistema visual usa la cercanía como indicio estadístico de pertenencia (lectura "probabilística" al estilo de Helmholtz, frente a la explicación por simplicidad de la Gestalt). Al agrupar, el número de unidades que hay que procesar baja, lo que conecta la proximidad con el *chunking* (MEM-04) y con el alivio de la memoria de trabajo (MEM-02).

La agrupación por proximidad parece producirse muy temprano. Han, Humphreys y Chen (1999) hallan que la agrupación por proximidad puede ser tan rápida y eficiente como la conectividad uniforme, y más rápida que la agrupación por semejanza de forma; Han y Humphreys (2003) precisan que esa igualdad se da con uno o dos objetos globales, y que con más objetos la conectividad gana.

## Evidencia y límites

- **Nivel: E2.** El efecto es robusto y está medido en psicofísica (incluso con modelos cuantitativos de laboratorio), pero en interfaces reales su magnitud depende del contexto y de los demás principios en juego. En UX la evidencia es sobre todo observacional (NN/g, Harley 2020), sin experimentos controlados publicados con cifras.
- **Condiciones de validez.** Las leyes Gestalt son tendencias *ceteris paribus*. La proximidad puede perder frente a la región común (Palmer 1992, ver PER-03), la conectividad (Palmer y Rock 1994, ver PER-04) o una semejanza muy saliente, sobre todo de color (PER-02). Quién gana depende de cuánto difieran los espaciados; no hay un ranking universal fijo.
- **Malentendidos frecuentes:**
  1. *"Basta con poner las cosas cerca."* Falso: lo que agrupa es el **contraste** entre espacio interno y externo. Todo cerca equivale a nada agrupado.
  2. *"Si se ve bien en escritorio, está resuelto."* El reflujo responsivo puede alejar elementos relacionados (NN/g cita un caso de Transport for London en móvil).
  3. *"La cercanía visual comunica la relación a todo el mundo."* Un lector de pantalla no percibe espaciado; la relación debe existir también en el código.

## Aplicación práctica

### Reglas

1. [H] El espacio entre grupos debe ser claramente mayor que el espacio dentro del grupo. Convención extendida (no derivada de un experimento): razón de al menos 2:1, por ejemplo 8 px dentro y 16–24 px entre grupos, sobre una escala de espaciado en múltiplos de 4 u 8. [E] El respaldo empírico es cualitativo: lo que manda es la distancia relativa (Kubovy y Wagemans 1995; Kubovy et al. 1998).
2. [H] Un encabezado debe estar más cerca del bloque que introduce que del bloque anterior: margen superior mayor que el inferior (recomendación de NN/g).
3. [H] Cada etiqueta, pegada a su campo; nunca a la misma distancia de dos campos.
4. [H] Cada mensaje de error, junto al campo que lo provoca.
5. [H] Cada acción, junto al contenido sobre el que actúa; no mezcles en un mismo racimo acciones de naturaleza distinta (navegar, guardar, añadir, cancelar).
6. [H] Separa con distancia las acciones destructivas de las frecuentes: cerca significa también más fácil de alcanzar (ACC-01), y por tanto más fácil de pulsar por error.
7. [H] Verifica la agrupación en cada punto de ruptura, a 320 px de ancho y con zoom al 200 %.
8. [H] Haz que la estructura visual coincida con la estructura semántica (`fieldset`, listas, `section` con encabezado, `aria-describedby`).

### Por contexto

| Contexto | Aplicación |
|---|---|
| Web/escritorio | Escala de espaciado con niveles relacionales: interno < entre elementos < entre grupos < entre secciones. Separa búsqueda y utilidades del menú principal con espacio. |
| Móvil/táctil | Comprueba que lo relacionado no quede varias pantallas más abajo tras el reflujo. Distancia suficiente entre objetivos táctiles de acciones distintas. |
| Formularios | Agrupa campos por significado (envío, facturación, pago) con más aire entre bloques; etiqueta y error pegados a su campo. |
| Navegación | Ítems del mismo nivel con espaciado regular; grupos de enlaces separados por un salto mayor. |
| Dashboards/datos | Cada KPI pegado a su contexto (periodo, comparación, tendencia); más espacio entre tarjetas que dentro. Etiquetado directo junto a la serie en lugar de leyenda lejana; barras que se comparan, agrupadas por categoría. |
| E-commerce | Precio, valoración y botón de compra cerca del producto al que pertenecen, y lejos del producto vecino. |
| Interfaces conversacionales/IA | Más espacio entre turnos que entre párrafos de un turno; acciones (copiar, regenerar, votar) adyacentes a su mensaje; cada cita junto a la afirmación que respalda. |
| Sistemas de diseño | Tokens de espaciado con nombres relacionales (no sólo de tamaño) para que el equipo aplique la jerarquía de forma consistente. |

### Ejemplos

- **Bueno: página de resultados de un buscador.** Cada resultado (título, URL, fragmento) tiene interlineado compacto y un hueco claramente mayor lo separa del siguiente; el usuario escanea "bloques" sin necesidad de bordes.
- **Malo: formulario con espaciado uniforme.** Doce campos a la misma distancia vertical y etiquetas centradas entre dos inputs. El usuario duda de qué etiqueta corresponde a qué campo y percibe el formulario como más largo de lo que es. Reagrupado en tres bloques de cuatro con más espacio entre bloques, se vuelve más abordable (ejemplo ilustrativo de NN/g, no un estudio).
- **Malo: racimo de botones mezclados.** "Añadir otro elemento" colocado entre "Siguiente", "Guardar borrador" y "Cancelar" queda camuflado como si fuera navegación (caso descrito por NN/g).

## Anti-patrones

- Espaciado uniforme en toda la pantalla: sin jerarquía no se percibe agrupación.
- Etiquetas o títulos equidistantes entre dos bloques.
- Botón de acción lejos del objeto que modifica (p. ej., "Aplicar" de un filtro al final de la página).
- Acción destructiva pegada a la acción más frecuente.
- Reflujo responsivo que separa elementos relacionados.
- Usar sólo la proximidad cuando el contenido es heterogéneo y el espacio disponible no permite contraste suficiente (ahí conviene un contenedor, PER-03).

## Ética y accesibilidad

- **Línea roja:** colocar un *opt-in* de marketing o un cargo adicional pegado al botón principal para que parezca parte obligatoria del flujo.
- **WCAG 1.3.1 Información y relaciones (A):** la agrupación visual debe estar en la estructura (`fieldset`/`legend`, listas, landmarks, `aria-describedby` para errores); la proximidad no llega al lector de pantalla.
- **WCAG 1.4.10 Reflujo (AA)** y **1.4.12 Espaciado del texto (AA):** al ampliar o aumentar el espaciado, las relaciones de proximidad deben mantenerse.
- **WCAG 2.5.8 Tamaño del objetivo (mínimo) (AA):** objetivos pequeños y muy juntos aumentan los toques erróneos; el espaciado también cuenta para cumplirlo.
- Usuarios de magnificadores ven una porción pequeña de la pantalla: mantener juntos los elementos relacionados les beneficia especialmente (Nielsen 2012, NN/g).

## Cómo auditarla

### Señales observables
- Etiquetas a la misma distancia de dos campos; títulos equidistantes entre secciones.
- Botones lejos del objeto que modifican.
- En test, usuarios que pulsan la acción equivocada de un racimo o no encuentran un control "visible" alejado de su foco.

### Preguntas
- ¿El espaciado interno es sistemáticamente menor que el externo según los tokens?
- ¿La agrupación sobrevive a 320 px y con zoom al 200 %?
- ¿El árbol de accesibilidad refleja los mismos grupos que se ven?

### Métricas
- **Prueba de desenfoque (*blur/squint test*):** al desenfocar la captura, ¿los bloques visibles coinciden con los grupos lógicos?
- **Razón de espaciado** medida en el inspector: espacio entre grupos / espacio dentro del grupo (objetivo heurístico ≥ 2).
- **Test de 5 segundos** o tarea de asociación: ¿qué porcentaje de participantes asigna correctamente etiqueta–campo o precio–producto?
- Tasa de errores de clic en acciones agrupadas (analítica o test moderado).

## Relaciones

- Refuerza / se apoya en:
  - MEM-04 Fragmentación (chunking) — la proximidad produce los fragmentos visuales.
  - MEM-01 Carga cognitiva y MEM-02 Memoria de trabajo — menos unidades que procesar.
  - PER-03 Ley de región común — el contenedor refuerza el grupo creado por el espacio.
  - ACC-01 Ley de Fitts — la acción junto a su objeto es también más rápida de alcanzar.
  - DEC-04 Efecto estética-usabilidad — un espaciado ordenado se percibe como más cuidado.
- Tensiona con:
  - PER-02 Ley de semejanza — un color compartido puede crear grupos que contradicen el espaciado; decide cuál manda y alinea ambas señales.
  - PER-03 Región común y PER-04 Conectividad uniforme — suelen imponerse a la proximidad; no pongas un contenedor o una línea que contradiga los huecos.
  - PER-06 Atención selectiva — lo bien agrupado pero lejos del foco de la tarea puede no verse.
  - SIS-01 Ley de Jakob — las convenciones de posición pueden imponer distancias.
  - T5 — dividir en pasos frente a coste de interacción: para tareas cortas, una sola pantalla bien agrupada por proximidad suele bastar.
  - T11 — fragmentar frente a comparar: separar en grupos no debe impedir comparar elementos que el usuario necesita ver juntos.
- Se confunde a menudo con:
  - "Densidad" o "minimalismo": la proximidad no pide más ni menos espacio, sino espacio **diferencial**.
  - PER-03 Región común: aquí agrupa el hueco; allí, un límite explícito.

## Fuentes

- Laws of UX (Jon Yablonski): https://lawsofux.com/law-of-proximity/ — síntesis divulgativa.
- Primarias:
  - Wertheimer, M. (1923). Untersuchungen zur Lehre von der Gestalt II. *Psychologische Forschung*, 4, 301–350. Trad. ingl.: https://www.yorku.ca/pclassic/Wertheimer/Forms/forms.htm
  - Kubovy, M. y Wagemans, J. (1995). Grouping by proximity and multistability in dot lattices: A quantitative Gestalt theory. *Psychological Science*, 6(4), 225–234. doi:10.1111/j.1467-9280.1995.tb00597.x
  - Kubovy, M., Holcombe, A. O. y Wagemans, J. (1998). On the lawfulness of grouping by proximity. *Cognitive Psychology*, 35(1), 71–98. doi:10.1006/cogp.1997.0673
  - Kubovy, M. y van den Berg, M. (2008). The whole is equal to the sum of its parts: A probabilistic model of grouping by proximity and similarity in regular patterns. *Psychological Review*, 115(1), 131–154. doi:10.1037/0033-295X.115.1.131
  - Wagemans, J. et al. (2012). A century of Gestalt psychology in visual perception: I. *Psychological Bulletin*, 138(6), 1172–1217. doi:10.1037/a0029333
  - Han, S., Humphreys, G. W. y Chen, L. (1999). Uniform connectedness and classical Gestalt principles of perceptual grouping. *Perception & Psychophysics*, 61(4), 661–674. doi:10.3758/BF03205537
  - Han, S. y Humphreys, G. W. (2003). Relationship between uniform connectedness and proximity in perceptual grouping. *Science in China, Series C*, 46(2), 113–126. doi:10.1360/03yc9013
- Secundarias consultadas:
  - Harley, A. (2020). Proximity Principle in Visual Design. NN/g: https://www.nngroup.com/articles/gestalt-proximity/
  - NN/g, visión de túnel y atención selectiva: https://www.nngroup.com/articles/tunnel-vision-and-selective-attention/
  - IxDF: https://ixdf.org/literature/article/laws-of-proximity-uniform-connectedness-and-continuation-gestalt-principles-2
  - Wikipedia, *Principles of grouping*: https://en.wikipedia.org/wiki/Principles_of_grouping
