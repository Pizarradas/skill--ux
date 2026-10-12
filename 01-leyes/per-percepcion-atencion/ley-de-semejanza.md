---
id: PER-02
nombre: Ley de semejanza
nombre_en: Law of Similarity
alias: [ley de similitud, agrupación por semejanza]
familia: PER
evidencia: E2
etiquetas: [gestalt, agrupacion, color, consistencia, sistemas-de-diseno]
refuerza: [SIS-01, SIS-02, MEM-04, PER-03]
tensiona: [PER-07, PER-01, PER-06, DEC-04]
tensiones: [T3]
fuente_laws_of_ux: https://lawsofux.com/law-of-similarity/
---

# PER-02 · Ley de semejanza (*Law of Similarity*)

> Los elementos que comparten un atributo visual (color, luminosidad, forma, tamaño, orientación, textura, movimiento o estilo tipográfico) se perciben como relacionados aunque estén separados en el espacio, y se les supone el mismo significado o la misma función.

**Idea clave para quien diseña:** cada atributo visual es una promesa; un mismo estilo debe significar una misma cosa en todo el producto, y lo que es distinto debe verse distinto.

## Resumen operativo
- **Qué dice:** lo que comparte color, forma, tamaño u otro atributo visual se percibe como relacionado aunque esté lejos, y se le supone la misma función.
- **Evidencia:** E2 — robusta en psicofísica; con proximidad se suma de forma aditiva en retículas (Kubovy y van den Berg 2008); se olvida que suele ceder ante proximidad y región común.
- **Haz:** 1) un atributo, un significado en todo el producto 2) un solo primario por vista; el resto homogéneo 3) doble codificación (color + forma o texto).
- **Evita:** dar a lo decorativo o no interactivo el estilo de lo interactivo.
- **Sospecha de esta ley cuando…:** clics en elementos no interactivos o enlaces que nadie reconoce; varios "primarios" compitiendo.
- **Mide con:** inventario de variantes de estilo; test "¿qué es pulsable?" también en escala de grises.
- **Vecinas:** SIS-01 Ley de Jakob (refuerza) · SIS-02 Modelo mental (refuerza) · PER-07 Von Restorff (tensiona, T3) · PER-01 Proximidad (tensiona)

## Origen

- **Max Wertheimer (1923)**, *Untersuchungen zur Lehre von der Gestalt II*, *Psychologische Forschung*, 4, 301–350 [verificada]. Usa hileras de puntos claros y oscuros y secuencias de sonidos fuertes y débiles. Introduce la noción de **grado de desemejanza**: la semejanza no es binaria, y diferencias graduales deciden la agrupación.
- **Kubovy, M. y van den Berg, M. (2008)**, *Psychological Review*, 115(1), 131–154, doi:10.1037/0033-295X.115.1.131: modelo probabilístico; en retículas de puntos, la fuerza conjunta de semejanza y proximidad es igual a la suma de sus efectos por separado (combinación aditiva).
- **Base atencional relacionada:** Treisman, A. y Gelade, G. (1980), "A feature-integration theory of attention", *Cognitive Psychology*, 12(1), 97–136, doi:10.1016/0010-0285(80)90005-5 — explica por qué una diferencia en un solo rasgo salta a la vista (*pop-out*) y una conjunción de rasgos no (resumen del contenido según fuentes secundarias; original tras muro de pago, no leído).

## Mecanismo

El sistema visual registra en paralelo rasgos básicos (color, orientación, tamaño, movimiento) y agrupa las regiones con valores parecidos; así segmenta superficies, porque un objeto real suele tener material y color homogéneos. Según NN/g (Harley 2020), el **color** es el atributo más saliente y puede unir incluso elementos de tipos distintos.

En las interfaces la semejanza funciona además como **código aprendido**: "lo azul y subrayado es un enlace", "lo relleno con el color de marca es la acción principal". Esa convención se convierte en modelo mental (SIS-02) y en expectativa transferida de otros productos (SIS-01).

## Evidencia y límites

- **Nivel: E2.** Efecto robusto en psicofísica desde Wertheimer; en UX, NN/g informa de investigación propia según la cual los indicadores con **formas únicas** se localizan más rápido y con más precisión, pero no publica cifras en el artículo consultado. La magnitud depende del contexto.
- **Condiciones de validez:**
  - Suele perder frente a la proximidad (PER-01) y a la región común (PER-03) (NN/g). Su ventaja es que agrupa **a distancia**: todos los enlaces de una página, todos los estados de error, todos los elementos seleccionados.
  - Sólo funciona si la diferencia es **discriminable** por la persona concreta: daltonismo, baja visión, pantallas en escala de grises, modo oscuro mal calibrado.
- **Malentendidos frecuentes:**
  1. *"La semejanza sólo sirve para agrupar."* También crea **relaciones no deseadas**: un icono decorativo del mismo color que los botones parece pulsable (caso descrito por NN/g).
  2. *"Todos los botones iguales = consistencia."* Si todos comparten estilo, la acción principal se pierde.
  3. *"Distinto = más importante."* Lo muy distinto puede leerse como **anuncio** e ignorarse (ver PER-06 y ceguera a los banners).

## Aplicación práctica

### Reglas

1. [H] Un atributo, un significado: el color de enlace sólo para lo interactivo; nunca para palabras clave, títulos no pulsables o iconos decorativos (NN/g).
2. [H] Mismo icono para la misma función en todo el producto; nunca iconos casi idénticos para funciones distintas.
3. [H] Jerarquía de botones: un único primario por vista o sección con tratamiento propio; secundarios homogéneos entre sí; terciarios como texto.
4. [E/norma] Los enlaces dentro de texto deben distinguirse por algo más que el tono: subrayado, o contraste de luminancia ≥ 3:1 frente al texto circundante (técnica suficiente G183 de WCAG); una señal adicional al enfocar o pasar el puntero es recomendable (C15).
5. [H] Elementos no interactivos sin estilo de interactivos, y al revés.
6. [H] Doble codificación (color + forma, patrón o etiqueta) para todo lo que transmita información.
7. [H] En datos, la misma serie o categoría con el mismo color en todos los gráficos de la vista; paletas categóricas cortas (unas 6–8 tonalidades distinguibles es una recomendación común en visualización, no una cifra experimental).
8. [H] El estado activo o seleccionado se marca con más de un atributo (peso, marcador y color).

### Por contexto

| Contexto | Aplicación |
|---|---|
| Web/escritorio | Enlaces reconocibles y coherentes; estilos de encabezado que no imiten enlaces. |
| Móvil/táctil | Chips de filtro (interactivos) y etiquetas informativas con formas distintas, para que no todo parezca pulsable. |
| Formularios | Mismo marcador para campos obligatorios (símbolo + texto); errores con el mismo icono, color y posición en todo el formulario. |
| Navegación | Ítems del mismo nivel con el mismo estilo; ítem activo diferenciado por varios canales. |
| Dashboards/datos | Color estable por serie entre gráficos; doble codificación; color de alerta reservado a valores fuera de umbral. |
| E-commerce | Precios, descuentos y etiquetas de envío con estilos estables; publicidad distinguible del catálogo orgánico. |
| Interfaces conversacionales/IA | Estilos distintos y constantes para mensajes de la persona, del asistente, del sistema, llamadas a herramientas y contenido citado; sugerencias de *prompt* con aspecto distinto al de acciones irreversibles; un indicador único para el contenido generado por IA. |
| Sistemas de diseño | Tokens semánticos (no sólo cromáticos): `color-action-primary`, `color-feedback-error`. Inventario periódico para eliminar variantes casi iguales. |

### Ejemplos

- **Bueno: lista de tareas con estados.** "Completado", "En curso" y "Bloqueado" tienen cada uno un icono, un color y un texto propios, idénticos en todas las vistas; el usuario reconoce el estado sin leer.
- **Malo: icono decorativo con el color de los botones.** Una ilustración de una tarjeta de producto usa el mismo rojo que el botón "Comprar"; los usuarios la pulsan esperando una acción.
- **Malo: todos los botones iguales.** "Pagar", "Volver", "Editar dirección" y "Aplicar cupón" con el mismo relleno de color: nada indica cuál es el siguiente paso.

## Anti-patrones

- Un mismo color con varios significados (marca, enlace, error).
- Varios estilos de "primario" compitiendo en la misma vista.
- Inventario con variantes casi iguales: cinco grises parecidos, tres radios de borde.
- Información codificada sólo por color.
- Estilo de enlace en texto no pulsable.

## Ética y accesibilidad

- **Líneas rojas:**
  - Publicidad con el mismo estilo que el contenido editorial (anuncios nativos sin etiqueta): explota la semejanza para engañar.
  - "Aceptar todo" como primario y "Rechazar" como enlace gris: patrón oscuro. Encaja en la "falsa jerarquía" (*false hierarchy*: dar a una opción precedencia visual sobre otras que deberían ser paralelas), subtipo de *interface interference* en la taxonomía de Gray et al. (2018, CHI); su ejemplo es un instalador, no un banner de cookies.
- **WCAG 1.4.1 Uso del color (A):** el color no puede ser el único medio visual para transmitir información, indicar una acción o distinguir un elemento. Fallos típicos: F73 (enlaces distinguibles sólo por color sin contraste 3:1) y F81 (obligatorios o errores marcados sólo por color).
- **WCAG 1.4.11 Contraste no textual (AA):** si un borde o forma es lo que distingue un componente o su estado, necesita 3:1.

## Cómo auditarla

### Señales observables
- Usuarios que pulsan elementos decorativos o no reconocen enlaces.
- Varios "primarios" en la misma vista.
- Un color o icono usado con significados distintos.

### Preguntas
- ¿Cada atributo visual (color, forma, peso, icono) tiene un único significado en todo el producto?
- ¿Se entiende la interfaz en escala de grises o con un simulador de deuteranopía?
- ¿Hay elementos no interactivos con aspecto interactivo, o al revés?

### Métricas
- **Inventario de estilos:** número de variantes de color, radio, sombra y botón; objetivo: tantas como significados, no más.
- **Prueba en escala de grises / simulador de daltonismo** con éxito en tareas de identificación de estado.
- **Test de "¿qué es pulsable?"**: porcentaje de aciertos al marcar elementos interactivos en una captura.
- Mapas de clics: clics en elementos no interactivos.

## Relaciones

- Refuerza / se apoya en:
  - SIS-01 Ley de Jakob — las convenciones son semejanzas compartidas entre productos.
  - SIS-02 Modelo mental — el estilo constante enseña el significado.
  - MEM-04 Fragmentación — agrupa elementos dispersos en categorías.
  - PER-03 Región común — tarjetas con tratamiento homogéneo se leen como serie.
- Tensiona con:
  - PER-07 Efecto Von Restorff — **T3**: la semejanza crea el fondo homogéneo y Von Restorff la excepción; sin semejanza no hay aislamiento. Resolución: un único énfasis por zona de atención.
  - PER-01 Ley de proximidad — pueden contradecirse; alinea color y espaciado.
  - PER-06 Atención selectiva — lo que se parece a un anuncio se ignora.
  - DEC-04 Efecto estética-usabilidad — una uniformidad estética excesiva puede borrar diferencias funcionales.
- Se confunde a menudo con:
  - "Consistencia" en abstracto: la semejanza exige consistencia **entre estilo y significado**, no que todo se vea igual.
  - PER-07 Von Restorff: aquí se agrupa lo parecido; allí destaca lo diferente.

## Fuentes

- Laws of UX (Jon Yablonski): https://lawsofux.com/law-of-similarity/ — síntesis divulgativa.
- Primarias:
  - Wertheimer, M. (1923). Untersuchungen zur Lehre von der Gestalt II. *Psychologische Forschung*, 4, 301–350. Trad. ingl.: https://www.yorku.ca/pclassic/Wertheimer/Forms/forms.htm
  - Kubovy, M. y van den Berg, M. (2008). The whole is equal to the sum of its parts: A probabilistic model of grouping by proximity and similarity in regular patterns. *Psychological Review*, 115(1), 131–154. doi:10.1037/0033-295X.115.1.131 (sólo resumen).
  - Treisman, A. y Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, 12(1), 97–136. doi:10.1016/0010-0285(80)90005-5 (texto no leído: muro de pago).
  - Gray, C. M., Kou, Y., Battles, B., Hoggatt, J. y Toombs, A. L. (2018). The Dark (Patterns) Side of UX Design. *Proceedings of CHI 2018*, paper 534, 1–14. doi:10.1145/3173574.3174108
  - W3C. Understanding SC 1.4.1 Use of Color (WCAG 2.2): https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html
- Secundarias consultadas:
  - Harley, A. (2020). Similarity Principle in Visual Design. NN/g: https://www.nngroup.com/articles/gestalt-similarity/
  - Wikipedia, *Principles of grouping*: https://en.wikipedia.org/wiki/Principles_of_grouping
  - Wikipedia, *Feature integration theory* (sólo vía buscador): https://en.wikipedia.org/wiki/Feature_integration_theory
