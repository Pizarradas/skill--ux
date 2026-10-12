# Tensiones entre leyes y cómo resolverlas

Las leyes no son un sistema de axiomas coherente: a menudo empujan en direcciones
opuestas. Un buen criterio de UX consiste en **reconocer la tensión, nombrar el contexto
que la decide y elegir conscientemente**. Cada tensión incluye una regla de resolución.

---

### T1 · Reducir opciones (DEC-01 Hick, SIS-04 Occam) ↔ No trasladar complejidad (SIS-03 Tesler)

- **Choque:** quitar opciones o pasos simplifica la pantalla, pero si la complejidad era
  inherente, reaparece en otro sitio (más pantallas, más errores, la persona tiene que hacerlo a mano).
- **Resolución:** antes de quitar, pregunta "¿quién hará esto ahora?". Elimina lo
  **innecesario** (Occam); **absorbe en el sistema** lo necesario (defaults, inferencia,
  automatización — Tesler); **difiere** lo avanzado (divulgación progresiva). No simplifiques
  "hasta la abstracción": si quitar etiquetas o pasos obliga a adivinar, has movido la carga
  a la memoria de trabajo.
- **Contexto que decide:** frecuencia (expertos diarios toleran densidad y la prefieren),
  criticidad de la tarea.

### T2 · Familiaridad (SIS-01 Jakob) ↔ Innovación y diferenciación

- **Choque:** las convenciones reducen el aprendizaje, pero congelan malos patrones y
  anulan la diferenciación.
- **Resolución:** sé convencional en lo **estructural** (navegación, formularios, iconos
  universales, gestos estándar) y diferencia en **contenido, tono y valor**. Innova sólo si
  la mejora es medible y puedes ofrecer transición: convivencia temporal con la versión
  anterior, introducción gradual, ayuda contextual (ACC-04).
- **Contexto:** base instalada grande → más conservador; producto nuevo en una categoría
  nueva → hay más margen (pero sigue habiendo convenciones de plataforma).

### T3 · Destacar (PER-07 Von Restorff) ↔ Coherencia (PER-02 Semejanza)

- **Choque:** destacar rompe la uniformidad; si todo destaca, nada destaca y la
  interfaz parece ruidosa o publicitaria (PER-06).
- **Resolución:** un único énfasis por zona de atención; el énfasis se reserva a lo que
  la persona más probablemente necesita. El resto obedece a la semejanza.
  Evita que lo destacado parezca un anuncio (banner blindness).

### T4 · Estética (DEC-04) ↔ Validez de la evaluación

- **Choque:** una interfaz atractiva recibe mejores valoraciones subjetivas y oculta
  problemas reales en los tests.
- **Resolución:** cuida la estética, pero evalúa con **medidas de comportamiento**
  (éxito, tiempo, errores) además de las de opinión. Prueba prototipos de baja fidelidad
  para validar estructura antes de pulir.

### T5 · Dividir en pasos (MEM-04 Chunking, MEM-01) ↔ Coste de interacción (ACC-01 Fitts, MOT-04 Parkinson)

- **Choque:** los asistentes paso a paso reducen la carga por pantalla pero añaden
  clics, esperas y puntos de abandono.
- **Resolución:** divide por **unidades de significado** (datos personales, envío, pago),
  no por número arbitrario de campos. Pocos pasos con progreso visible (MOT-02) y datos
  arrastrados (MEM-02). Para tareas cortas y conocidas, una sola pantalla bien agrupada
  (PER-01, PER-03) suele ser mejor.

### T6 · Velocidad (ACC-02 Doherty) ↔ Valor percibido del trabajo ("labor illusion")

- **Choque:** responder más rápido casi siempre mejora la experiencia, pero en tareas
  donde la persona espera "trabajo duro" (búsqueda de vuelos, análisis, cálculo de un
  presupuesto) una respuesta instantánea puede parecer poco fiable.
- **Resolución:** nunca ralentices tareas rutinarias. Si una operación compleja termina
  muy rápido, puedes **mostrar el trabajo realizado** (qué se comprobó) en vez de inventar
  esperas. Cualquier demora añadida debe ser breve, honesta y nunca bloquear a quien
  tiene prisa.

### T7 · Motivar con progreso (MOT-02, MOT-03) ↔ Ética

- **Choque:** las barras de progreso, rachas y tareas "pendientes" motivan… y también
  generan compulsión.
- **Resolución:** el progreso debe ser **real** y la meta debe ser **de la persona**, no
  de la métrica de negocio. Permite pausar sin castigo. Aplica la prueba de
  `06-etica-accesibilidad/etica-y-patrones-oscuros.md`.

### T8 · Tolerancia de entrada (ACC-03 Postel) ↔ Seguridad y precisión

- **Choque:** aceptar cualquier formato puede introducir ambigüedad (01/02/2026: ¿enero o
  febrero?) o errores silenciosos; en protocolos, la tolerancia excesiva ha causado
  problemas de seguridad e interoperabilidad (crítica recogida en RFC 9413).
- **Resolución:** sé tolerante en la **forma** (espacios, guiones, mayúsculas, formatos
  equivalentes) pero **explícito en el significado**: normaliza y **muestra** la
  interpretación ("Entendido: 2 de enero de 2026"); pide confirmación cuando haya
  ambigüedad real; nunca descartes datos sin avisar.

### T9 · Optimizar para la mayoría (SIS-05 Pareto) ↔ Inclusión

- **Choque:** centrarse en el 20 % de funciones/usuarios que generan el 80 % del valor
  puede abandonar a minorías — a menudo personas con discapacidad o casos límite críticos.
- **Resolución:** usa Pareto para **priorizar el orden**, no para excluir. La accesibilidad
  y los caminos críticos de error/recuperación no entran en el "80 % prescindible".

### T10 · Inmersión (MOT-01 Flow) ↔ Interrupciones necesarias

- **Choque:** confirmaciones, avisos de privacidad o de seguridad rompen el flujo.
- **Resolución:** interrumpe sólo en acciones destructivas, irreversibles o costosas;
  para lo demás, permite **deshacer** en lugar de confirmar. Agrupa avisos y elige el
  momento (al final de una unidad de trabajo).

### T11 · Fragmentar contenido (MEM-04) ↔ Ver el conjunto (escaneo y comparación)

- **Choque:** acordeones y pestañas reducen la carga visible, pero ocultan información
  necesaria para comparar y obligan a recordar (MEM-02).
- **Resolución:** oculta lo que se consulta **por separado**; muestra junto lo que se
  **compara**. Para comparación, tablas lado a lado.

### T12 · Valor por defecto (DEC-03, sesgo de statu quo) ↔ Autonomía

- **Choque:** los defaults son la herramienta más potente de la arquitectura de la
  elección, y por eso la más peligrosa.
- **Resolución:** el default debe ser la opción que la mayoría elegiría estando
  informada y la más segura/privada en caso de duda. Siempre visible y fácil de cambiar.

### T13 · Posición serial (MEM-05) ↔ Convenciones de colocación (SIS-01)

- **Choque:** poner lo importante "al final" puede romper convenciones (p. ej. el
  carrito suele estar a la derecha, el logo a la izquierda).
- **Resolución:** la convención de plataforma prevalece para elementos de navegación
  global; la posición serial se usa para ordenar **dentro** de listas y menús propios.

### T14 · Ayuda contextual (ACC-04) ↔ Atención selectiva y saturación (PER-06)

- **Choque:** tooltips, coach marks y tours compiten por la atención y se ignoran o molestan.
- **Resolución:** ayuda **bajo demanda** y **en el momento de necesidad** (primera vez
  que se encuentra el control, tras un error), descartable y que no se repita.

---

## Cómo razonar una tensión en una respuesta

```
Tensión: {Ley A} ↔ {Ley B}
En este contexto pesa más {A/B} porque {persona, frecuencia, criticidad, dispositivo}.
Decisión: {…}
Mitigación del lado que cede: {…}
Señal de que nos equivocamos: {métrica}
```
