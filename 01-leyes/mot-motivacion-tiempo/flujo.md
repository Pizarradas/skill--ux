---
id: MOT-01
nombre: Flujo (flow)
nombre_en: Flow
alias: [estado de flujo, experiencia óptima, "estar en la zona"]
familia: MOT
evidencia: C
etiquetas: [concentracion, feedback, reto-habilidad, interrupciones, productividad, atencion]
refuerza: [ACC-02, ACC-01, MOT-02, MEM-01, PER-06, SIS-04]
tensiona: [ACC-04, DEC-01, DEC-02, SIS-03, MOT-05]
tensiones: [T10]
fuente_laws_of_ux: https://lawsofux.com/flow/
---

# MOT-01 · Flujo (*Flow*)

> Estado de absorción plena en una actividad, con concentración sin esfuerzo aparente, sensación de control, pérdida de la autoconciencia y distorsión del tiempo. Tiende a aparecer cuando hay metas claras, retroalimentación inmediata y un reto que se ajusta a una habilidad alta.

**Idea clave para quien diseña:** no puedes "fabricar" el flujo, pero sí puedes destruirlo; tu trabajo es quitar todo lo que obliga a la persona a preguntarse "¿qué hago ahora?" o "¿ha funcionado?".

## Resumen operativo
- **Qué dice:** la absorción plena aparece con metas claras, feedback inmediato y un reto ajustado a una habilidad alta; la interfaz no la crea, pero puede destruirla.
- **Evidencia:** C — constructo bien medido (ESM, escalas FSS-2/DFS-2) pero no predictivo; lo que sí está probado es el coste de interrumpir (Mark et al., 2008: más estrés y frustración aunque se termine antes).
- **Haz:** 1) no interrumpas la tarea activa con avisos no críticos 2) tras cada acción, lleva a la siguiente acción probable con feedback inmediato 3) autoguardado y deshacer en lugar de confirmaciones.
- **Evita:** confundir flujo con tiempo en la app: scroll infinito y autoplay son absorción sin meta, no flujo.
- **Sospecha de esta ley cuando…:** modales o encuestas a mitad de tarea; pausas de duda largas tras completar algo.
- **Mide con:** recuento de interrupciones no solicitadas por tarea; NASA-TLX o FSS-2 en tareas largas.
- **Vecinas:** ACC-02 Umbral de Doherty (refuerza) · MOT-02 Gradiente de meta (refuerza) · ACC-04 Paradoja del usuario activo (tensiona) · Interrupciones necesarias (tensiona, T10)

## Origen
- Mihály Csíkszentmihályi acuñó el concepto en *Beyond Boredom and Anxiety* (Jossey-Bass, 1975) y lo popularizó en *Flow: The Psychology of Optimal Experience* (Harper & Row, 1990). Lo estudió con el método de muestreo de experiencias (ESM): avisos aleatorios durante el día en los que las personas describían qué hacían y cómo se sentían.
- Massimini, Csíkszentmihályi y Carli (1987, *Journal of Nervous and Mental Disease*, 175(9), 545–549), con muestreo de experiencias en 47 adolescentes, hallaron que la razón entre reto y habilidad percibidos predecía la experiencia óptima, el aburrimiento y la ansiedad; esa línea refinó el modelo de "canal" en un modelo de **ocho canales**: el flujo exige reto y habilidad **ambos por encima de la media personal**, no sólo equilibrados. Si el reto supera la habilidad aparece ansiedad; si la habilidad supera el reto, aburrimiento o relajación. (No verificado: el detalle de los ocho canales no figura en el resumen y el texto está tras muro de pago.)
- Traslado a HCI: Webster, Trevino y Ryan (1993), "The dimensionality and correlates of flow in human-computer interactions", *Computers in Human Behavior*, 9(4), 411–426. Hoffman y Novak lo aplicaron a la navegación web en "Marketing in hypermedia computer-mediated environments: Conceptual foundations" (1996), *Journal of Marketing*, 60(3), 50–68, con un modelo estructural de navegación que incorpora el flujo, y revisaron el campo en "Flow Online: Lessons Learned and Future Prospects" (2009), *Journal of Interactive Marketing*, 23(1), 23–34.

## Mecanismo
La atención es un recurso limitado. Cuando la tarea ocupa toda la capacidad disponible sin desbordarla, no sobra atención para vigilarse a uno mismo ni para notar el paso del tiempo. Las metas claras y el feedback inmediato eliminan la incertidumbre que obliga a reorientarse; el ajuste entre reto y habilidad mantiene la activación en un nivel óptimo.

Cualquier ambigüedad, espera o interrupción fuerza a la persona a salir de la tarea para reevaluar, y recuperar el estado cuesta. Por eso, en interfaces, el flujo depende más de **lo que no ocurre** (esperas, modales, dudas, errores) que de lo que se añade.

## Evidencia y límites
- **Nivel: C (constructo teórico).** El flujo está bien establecido como constructo en psicología, con instrumentos de medida (ESM, escalas FSS-2 y DFS-2 de Jackson), pero **no es una ley predictiva**: no hay fórmula ni umbrales. En UX funciona como **marco orientador** y casi toda la literatura de diseño (Ramsey en A List Apart, 2007; Vohra en el blog de Superhuman) es práctica, no experimental.
- Problemas reconocidos: definiciones no unificadas; medida sobre todo retrospectiva y autoinformada; el modelo de canales no garantiza que el equilibrio *percibido* se produzca; algunos estudios encuentran disfrute con poco reto (relajación), lo que no encaja con el modelo.
- **Lo que sí tiene respaldo experimental directo es el coste de interrumpir:** Mark, Gudith y Klocke (2008) observaron que las personas interrumpidas terminaban antes y con calidad similar, pero con **más estrés, frustración, presión temporal y esfuerzo**; el contexto de la interrupción no cambió el resultado.
- Condiciones de validez: pertinente en tareas prolongadas y que exigen habilidad (escribir, programar, diseñar, analizar datos, jugar, aprender). En tareas transaccionales breves (pagar, reservar) la meta realista no es "inducir flujo" sino **no interrumpir**.
- Malentendidos frecuentes:
  - *"Flujo = engagement = tiempo en la app."* Falso. El scroll infinito o el autoplay producen absorción sin meta, sin reto y sin habilidad: **el diseño adictivo no es flujo**, aunque se le parezca desde fuera.
  - *"Quitar toda dificultad crea flujo."* Quitar fricción innecesaria elimina ansiedad, pero quitar el reto propio de la tarea lleva al aburrimiento.
  - *"El flujo hace X veces más productivo."* Cifras como el "5×" de Superhuman carecen de fuente verificable.

## Aplicación práctica
### Reglas
1. **[H]** Tras completar una unidad de trabajo, lleva a la siguiente acción probable (abrir el siguiente elemento, siguiente campo, siguiente tarea) en lugar de devolver a una pantalla neutra.
2. **[E]** No interrumpas una tarea activa con avisos no críticos: pospón, agrupa o entrega en una pausa natural (Mark et al., 2008, sobre el coste de las interrupciones).
3. **[H]** Da feedback inmediato en manipulación directa; usa las cifras de latencia de ACC-02 Doherty como referencia, no inventes umbrales nuevos.
4. **[H]** Escala con la habilidad: atajos de teclado, paleta de comandos y aceleradores para expertos, sin obligar al novato a usarlos (divulgación progresiva).
5. **[H]** Haz visibles meta y progreso en tareas largas (véase MOT-02).
6. **[H]** Guardado automático y deshacer: permiten actuar sin miedo y sustituyen confirmaciones que cortan el ritmo (T10).
7. **[H]** Ofrece un modo concentración que el usuario active y desactive, no uno impuesto.
8. **[H]** Mide éxito con métricas de valor (tareas completadas, tiempo hasta completar) y no con métricas de captura (tiempo en la app, sesiones sin meta).

### Por contexto
| Contexto | Aplicación |
|---|---|
| web/escritorio | Edición sin modales; atajos descubribles (tooltips con la tecla); autoguardado silencioso con estado visible ("Guardado"). |
| móvil/táctil | Agrupar notificaciones; gestos estándar; evitar saltos de pantalla tras cada acción; retomar donde se dejó al volver a la app. |
| formularios | No validar de forma agresiva mientras se escribe; validar al salir del campo; mantener el foco donde la persona lo espera. |
| dashboards/datos | Filtros que responden sin recargar toda la vista; conservar contexto (zoom, selección) al profundizar. |
| onboarding | Dificultad creciente: primero tareas fáciles con éxito garantizado, luego funciones avanzadas cuando haya habilidad. |
| interfaces conversacionales/IA | Sugerencias en línea rechazables con una tecla, sin robar el foco; streaming para evitar la espera muerta; no desplazar el texto mientras se lee; ni preguntar en exceso ni actuar sin confirmar en lo irreversible. |
| voz | Turnos breves, confirmaciones implícitas, sin repreguntas innecesarias. |
| sistemas de diseño | Componentes de notificación con prioridad (crítico/informativo) y política de "no interrumpir" documentada. |

### Ejemplos
- **Bueno:** un cliente de correo que, al archivar un mensaje, abre directamente el siguiente, con atajos para cada acción y feedback inmediato del estado. La persona procesa la bandeja sin volver a decidir dónde está.
- **Lo incumple:** un editor de documentos que, a mitad de un párrafo, muestra un modal de "¿Te gusta la app? Valóranos", o una encuesta NPS que bloquea la tarea.
- **Falso flujo:** un feed con scroll infinito y reproducción automática que se celebra internamente por su "tiempo de sesión"; hay absorción, pero no meta ni habilidad, y el coste lo paga el bienestar.

## Anti-patrones
- Diseño adictivo presentado como flujo: scroll infinito, autoplay, recompensas variables, especialmente con menores.
- Interrupciones de crecimiento: upsells, encuestas, peticiones de valoración en plena tarea.
- Confirmaciones en acciones reversibles (en vez de deshacer).
- Esperas sin feedback y spinners en acciones que deberían ser instantáneas.
- Optimizar sólo para el experto (todo con atajos, nada visible) o sólo para el novato (asistentes que el experto no puede saltar).
- Autoavance del foco que desorienta a usuarios de lector de pantalla.

## Ética y accesibilidad
- **Línea roja:** usar la absorción contra el interés de la persona (maximizar tiempo de uso con autoplay, feed sin fin o recompensas variables). Aplica la prueba de cuatro preguntas de `06-etica-accesibilidad/etica-y-patrones-oscuros.md`; la vulnerabilidad (menores, adicción) pesa especialmente.
- WCAG 2.2:
  - **2.2.1 Timing Adjustable (A):** un flujo "rápido" no puede imponer límites de tiempo no ajustables.
  - **2.2.2 Pause, Stop, Hide (A):** el contenido en movimiento o autoactualizable debe poder pausarse.
  - **2.2.4 Interruptions (AAA):** las interrupciones deben poder posponerse o suprimirse (salvo emergencias).
  - **2.4.3 Focus Order (A):** el avance automático no debe romper un orden de foco con sentido.
  - **3.2.2 On Input (A):** cambiar de contexto automáticamente al introducir datos requiere aviso previo.

## Cómo auditarla
### Señales observables
- Modales, toasts que exigen acción o cambios de pantalla no solicitados durante la tarea principal.
- Pantallas sin siguiente paso claro tras completar algo.
- Esperas largas sin feedback; confirmaciones en acciones reversibles.
- Atajos inexistentes o no descubribles.
- KPIs del producto centrados en tiempo de uso.
### Preguntas
- ¿Cuántas interrupciones no pedidas hay en el recorrido principal y cuáles son realmente críticas?
- Tras cada acción, ¿la persona sabe qué ha pasado y qué viene después?
- ¿El producto escala con la habilidad o trata igual al novato y al experto?
- ¿La absorción que medimos sirve a una meta de la persona?
### Métricas
- Recuento de interrupciones no solicitadas por tarea.
- Pausas de duda largas en test con usuarios (umbral de observación práctico de unos 3 s [H]).
- Carga y frustración con NASA-TLX; escala FSS-2 en tareas largas.
- Tasa de uso de atajos; abandono tras una interrupción del sistema; tiempo de retorno a la tarea.

## Relaciones
- Refuerza / se apoya en:
  - ACC-02 Umbral de Doherty — sin respuesta rápida no hay feedback inmediato ni flujo.
  - ACC-01 Ley de Fitts — menos fricción motora, menos cortes de ritmo.
  - MOT-02 Efecto de gradiente de meta — metas y progreso visibles son condición del flujo.
  - MEM-01 Carga cognitiva — el flujo exige carga extrínseca baja.
  - PER-06 Atención selectiva — cada distracción compite por la atención que sostiene el estado.
  - SIS-04 Navaja de Occam — menos elementos superfluos, menos decisiones laterales.
  - MOT-03 Efecto Zeigarnik — facilitar la reanudación restaura lo que la interrupción rompe.
- Tensiona con:
  - Interrupciones necesarias (avisos de seguridad, privacidad, confirmaciones) — **T10**: interrumpe sólo en lo destructivo, irreversible o costoso; para lo demás, deshacer.
  - ACC-04 Paradoja del usuario activo — la persona quiere actuar ya, pero sin habilidad no hay flujo, sólo ansiedad; ayuda contextual mínima.
  - DEC-01 Ley de Hick / DEC-02 Sobrecarga de opciones — demasiadas alternativas destruyen la "siguiente acción obvia".
  - SIS-03 Ley de Tesler — la complejidad inevitable debe vivir en algún sitio sin interrumpir.
  - MOT-05 Regla pico-final — el flujo es un estado vivido; el recuerdo lo marcan picos y finales.
- Se confunde a menudo con: *engagement*/tiempo en la app — el flujo exige meta, reto y habilidad; la absorción compulsiva no.

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/flow/ — síntesis divulgativa.
- Primarias:
  - Csíkszentmihályi, M. (1975). *Beyond Boredom and Anxiety*. Jossey-Bass.
  - Csíkszentmihályi, M. (1990). *Flow: The Psychology of Optimal Experience*. Harper & Row.
  - Massimini, F., Csíkszentmihályi, M. y Carli, M. (1987). The monitoring of optimal experience: A tool for psychiatric rehabilitation. *Journal of Nervous and Mental Disease*, 175(9), 545–549. https://doi.org/10.1097/00005053-198709000-00006 (leído el resumen; los ocho canales no se han comprobado en el texto).
  - Webster, J., Trevino, L. K. y Ryan, L. (1993). The dimensionality and correlates of flow in human-computer interactions. *Computers in Human Behavior*, 9(4), 411–426. https://doi.org/10.1016/0747-5632(93)90032-N
  - Hoffman, D. L. y Novak, T. P. (1996). Marketing in hypermedia computer-mediated environments: Conceptual foundations. *Journal of Marketing*, 60(3), 50–68. https://doi.org/10.1177/002224299606000304
  - Hoffman, D. L. y Novak, T. P. (2009). Flow Online: Lessons Learned and Future Prospects. *Journal of Interactive Marketing*, 23(1), 23–34. https://doi.org/10.1016/j.intmar.2008.10.003
  - Mark, G., Gudith, D. y Klocke, U. (2008). The cost of interrupted work: more speed and stress. *CHI '08*, 107–110. https://doi.org/10.1145/1357054.1357072
- Secundarias consultadas:
  - https://en.wikipedia.org/wiki/Flow_(psychology) (lectura parcial)
  - Ramsey, J. (2007). Designing for Flow. https://alistapart.com/article/designingforflow/
  - Vohra, R. How to design for flow. https://blog.superhuman.com/how-to-design-for-flow/
  - W3C, WCAG 2.2 Understanding: https://www.w3.org/WAI/WCAG22/Understanding/
