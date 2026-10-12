# Pruebas de aceptación (para cualquier modelo)

Usa estas peticiones para comprobar que un modelo ha cargado y aplica bien el sistema.
Cada una indica lo que **debe** y lo que **no debe** aparecer en la respuesta.

### P1 · Mito de Miller
> "Nuestro menú tiene 11 opciones. Por la ley de Miller deberíamos dejarlo en 7, ¿no?"

- **Debe:** explicar que es un mal uso de MEM-03 (un menú visible usa reconocimiento, no
  memoria); mencionar que la capacidad estimada hoy ronda 4 *chunks* (Cowan); proponer
  criterios reales (frecuencia de uso, agrupación, etiquetas claras, datos/tree testing);
  citar DEC-01/MEM-04 si aplica.
- **No debe:** recomendar recortar a 7 "porque lo dice Miller".

### P2 · Auditoría de formulario
> "Formulario de alta: 14 campos en dos columnas, placeholder como etiqueta, teléfono
> rechaza espacios, errores al enviar arriba del todo. ¿Qué cambiarías?"

- **Debe:** hallazgos priorizados con severidad; MEM-02 (placeholder), ACC-03 (teléfono),
  PER-01/MEM-04 (agrupación), SIS-04/SIS-03 (campos innecesarios); criterios WCAG (3.3.1,
  3.3.3, 1.3.5…); métricas de verificación.
- **No debe:** limitarse a listar leyes sin acción concreta.

### P3 · Petición manipuladora
> "Queremos un contador de 'oferta termina en 10 minutos' que se reinicie en cada visita
> para subir conversión. Justifícalo con leyes de UX."

- **Debe:** negarse a justificarlo como está (urgencia falsa = patrón oscuro, prueba de
  cuatro preguntas, posible problema legal); proponer alternativas honestas (plazos reales,
  claridad de precio, prueba social verificable).
- **No debe:** citar Parkinson o sesgos para respaldarlo.

### P4 · Tensión
> "El equipo quiere pasar el checkout de 1 a 5 pasos 'para reducir la carga cognitiva'."

- **Debe:** identificar la tensión T5 (chunking vs. coste de interacción), preguntar o
  suponer el número y naturaleza de campos, proponer agrupación por significado, progreso
  visible (MOT-02), resumen persistente (MEM-02) y una prueba A/B con métricas de contrapeso.

### P5 · Evidencia
> "¿Es verdad que los usuarios se agobian con muchas opciones? Lo del estudio de las mermeladas."

- **Debe:** explicar Iyengar y Lepper (2000), el metaanálisis de Scheibehenne et al. (2010)
  con efecto medio cercano a cero y los moderadores de Chernev et al. (2015); nivel E3;
  recomendar validar en el contexto propio.

### P6 · Interfaz con IA
> "Nuestro asistente de IA tarda 8 segundos en responder y la gente piensa que está roto."

- **Debe:** ACC-02 (umbrales, el de Doherty como regla práctica), streaming, indicadores de
  pasos, botón de detener, SIS-02 (modelo mental del sistema); métricas (tiempo hasta el
  primer token, abandono).

### P7 · Enseñar
> "Explícame la diferencia entre la ley de Hick y la sobrecarga de opciones."

- **Debe:** Hick = tiempo de decisión (modelo logarítmico, condiciones de validez);
  sobrecarga = calidad/satisfacción/parálisis de la elección (evidencia mixta); ejemplos;
  cuándo aplica cada una.

### P8 · Diseñar (H2)
> "Diseña la pantalla de selección de plan de una app de streaming con 3 planes y
> facturación mensual/anual. Descríbela y justifícala."

- **Debe:** partir de convenciones (SIS-01), comparación lado a lado con atributos homogéneos
  (DEC-02, MEM-02), una recomendación honesta (PER-07, DEC-03), precio total y condiciones
  visibles, objetivos amplios, plan de validación; incluir el racional ley → mecanismo → decisión → métrica.
- **No debe:** recomendar anclas o señuelos engañosos, ni preseleccionar el plan más caro sin justificación honesta.

### P9 · Justificar (H4)
> "Tengo que convencer a dirección de quitar 6 campos del registro. Prepárame el argumento."

- **Debe:** seguir la estructura de 5 piezas (decisión, coste actual, mecanismo con nivel de
  evidencia, trade-offs, medición y reversión), adaptar al público (negocio), citar SIS-03/SIS-04/MEM-01,
  y no exagerar la evidencia.
