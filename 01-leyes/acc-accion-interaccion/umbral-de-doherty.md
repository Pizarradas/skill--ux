---
id: ACC-02
nombre: Umbral de Doherty
nombre_en: Doherty Threshold
alias: [respuesta subsegundo, regla de los 400 ms, tiempo de respuesta del sistema]
familia: ACC
evidencia: E2
etiquetas: [rendimiento, latencia, feedback, estados-de-carga, progreso, inp, streaming]
refuerza: [MOT-01, MOT-05, MOT-02, MOT-03, ACC-01]
tensiona: [MOT-04, DEC-04, DEC-03]
tensiones: [T6, T10]
fuente_laws_of_ux: https://lawsofux.com/doherty-threshold/
---

# ACC-02 · Umbral de Doherty (*Doherty Threshold*)

> Cuando el sistema responde tan deprisa que ni la persona ni la máquina tienen que esperarse, el ritmo de trabajo se acelera y la productividad crece más de lo que el ahorro de segundos explicaría; como referencia práctica se usa un ciclo de respuesta por debajo de unos 400 ms.

**Idea clave para quien diseña:** responde a cada acción al instante (< 100 ms) aunque el resultado tarde, y cuida que el ciclo completo orden-respuesta no rompa el hilo del pensamiento.

## Resumen operativo
- **Qué dice:** si el sistema responde sin hacer esperar, el ritmo de trabajo y la productividad suben más de lo que explica el tiempo ahorrado.
- **Evidencia:** E2 — dirección robusta, magnitud no; los 400 ms no aparecen en el texto del folleto de IBM de 1982 (regla práctica derivada de su gráfica).
- **Haz:** 1) eco visible de cada acción en < 100 ms 2) INP p75 ≤ 200 ms y ciclo de órdenes frecuentes por debajo de ~400 ms 3) > 10 s: porcentaje, estimación y cancelar.
- **Evita:** inventar esperas o progreso falso para aparentar esfuerzo (T6).
- **Sospecha de esta ley cuando…:** hay clics repetidos sobre el mismo control o abandonos durante cargas.
- **Mide con:** INP/LCP p75 en campo; tiempo acción→respuesta visible en vídeo con CPU lenta; TTFT en IA.
- **Vecinas:** MOT-01 Flujo (refuerza) · MOT-02 Gradiente de meta (refuerza) · DEC-03 Sesgo cognitivo / ilusión del trabajo (tensiona, T6) · MOT-04 Ley de Parkinson (tensiona)

## Origen
- **Doherty, W. J. y Thadhani, A. J. (noviembre de 1982). *The Economic Value of Rapid Response Time*. IBM, formulario GE20-0752-0.** Es un **folleto técnico de IBM** de 12 páginas (catálogo del Computer History Museum), no un artículo revisado por pares. El apellido del segundo autor aparece como "Thadani" o "Thadhani".
- **Corrección a Laws of UX:** la página de Laws of UX afirma que se publicó en el *IBM Systems Journal*. No se encontró evidencia de ello; el documento de 1982 es el folleto. La confusión probablemente viene de trabajos previos en esa revista: Doherty y Kelisky (1979), citado dentro del folleto, y el artículo de Thadhani (1981), "Interactive user productivity", *IBM Systems Journal*, 20(4), 407–423, doi:10.1147/sj.204.0407, origen de la curva que el folleto reutiliza.
- **La cifra de 400 ms no figura en el texto del folleto**, ni la palabra "adictivo" (búsqueda en la transcripción completa conservada por J. L. Elliott). Rupert (2015) la atribuye a la gráfica del informe ("sub-400 millisecond") y toma lo de "adictivo" de la serie de televisión *Halt and Catch Fire*, no del folleto. **Debe tratarse como una regla práctica derivada, no como resultado textual.**
- Lo que el folleto sí contiene: con la curva de Thadhani, un programador pasaba de unas 180 a 371 transacciones por hora al bajar la respuesta de 3 s a 0,3 s (+106 %), y la productividad se dispara por debajo de 1 s; otros casos internos (cableado de tarjetas, proyecto de Portsmouth) muestran mejoras al reducir la respuesta, y con respuesta subsegundo los ingenieros medios rendían como expertos con respuesta lenta.
- Antecedentes y marco: Miller (1968), AFIPS FJCC, doi:10.1145/1476589.1476628 (según el folleto, 2 s como espera máxima aceptable; Shneiderman (1984) lo describe como una revisión analítica con 17 situaciones de respuesta, no como un experimento); Card, Robertson y Mackinlay (CHI '91, doi:10.1145/108844.108874); Nielsen (1993), *Usability Engineering*, con los **tres límites de 0,1 s / 1 s / 10 s**.

## Mecanismo
Una espera interrumpe la continuidad del pensamiento: mientras el sistema no responde, la atención decae, el plan de la tarea se desvanece de la memoria de trabajo y la persona empieza a hacer otra cosa. Doherty y Kelisky (1979, citado en el folleto) observaron que cada segundo de demora del sistema añadía una demora parecida al tiempo que el usuario tardaba en emitir la orden siguiente: la lentitud se contagia al humano. Con respuesta rápida, las acciones se encadenan sin reorientarse.

Los límites de Nielsen describen el mismo fenómeno: **~0,1 s** se percibe como manipulación directa; **~1 s** el hilo se mantiene aunque se nota la demora; **~10 s** es el límite de la atención sostenida en la tarea.

## Evidencia y límites
- **Nivel: E2** — la dirección del efecto (más rapidez, más productividad y mejor experiencia) está ampliamente respaldada; la magnitud y el valor concreto de 400 ms no lo están. Los datos de origen son estudios internos de IBM de los años 70 y 80, con terminales de *mainframe*, usuarios expertos y un evidente interés comercial.
- **Condiciones de validez:** ciclos interactivos frecuentes de tipo orden-respuesta. Para esperas largas inevitables pesa más la **percepción** del tiempo (indicadores de progreso) que el umbral. La variabilidad de la respuesta podría importar, pero Myers (CHI '85), en otra parte del mismo experimento, no encontró preferencia significativa por la respuesta constante frente a la variable, en contra de resultados previos.
- **Progreso percibido:** Myers (1985) mostró preferencia significativa por los indicadores de porcentaje completado (al 86,1 % de los participantes les gustaron); Harrison et al. (UIST 2007; CHI 2010) muestran que el comportamiento y el aspecto de la barra alteran la duración percibida; el estudio citado por NN/g (Sherwin, 2014) encontró que con una barra animada la gente aceptaba esperar unas 3 veces más.
- **"Ilusión del trabajo"** (Buell y Norton, 2011, *Management Science*, 57(9), 1564–1579): en cinco experimentos (viajes y citas en línea), cuando la web muestra el esfuerzo que está haciendo (transparencia operativa), la gente puede preferir esperas más largas a resultados instantáneos idénticos. Laws of UX lo convierte en "añadir retardo puede aumentar el valor percibido"; esta lectura es éticamente delicada (T6).
- **Malentendidos frecuentes:**
  - "400 ms es el objetivo para todo" → el eco visual de una pulsación debe estar muy por debajo de 100 ms; los 400 ms son un techo orientativo para el ciclo completo en tareas iterativas.
  - "Con una barra de progreso cualquier espera es tolerable" → la tolerancia tiene límite y una barra mentirosa erosiona la confianza.
  - "Doherty demostró 400 ms en el *IBM Systems Journal*" → ver Origen.

## Aplicación práctica
### Reglas
1. [E/N] Eco de entrada (estado pulsado, cambio optimista) en **< 100 ms** — Nielsen (0,1 s); el modelo RAIL de Google reserva ~50 ms de presupuesto real de manejo.
2. [N] Web: **INP ≤ 200 ms** = bueno; 200–500 ms mejorable; **> 500 ms** malo; medido en el **percentil 75** de visitas de campo, por separado en móvil y escritorio (web.dev). El INP sustituyó a FID como Core Web Vital el 12 de marzo de 2024 (web.dev).
3. [H] Ciclo completo de una orden frecuente (filtrar, navegar dentro de la app, guardar) por debajo de ~400 ms como referencia práctica, no como norma.
4. [H con base empírica] Elige el feedback por duración esperada (NN/g): < 1 s sin indicador más allá del cambio de estado; 2–10 s indicador indeterminado; **> 10 s porcentaje completado, estimación y opción de cancelar**; si la estimación varía mucho, baja ese umbral; en lotes, "3 de 50".
5. [H] Rendimiento percibido: interfaz optimista con reversión clara si falla; precarga por intención (*hover*, foco); pintado progresivo. Las pantallas esqueleto tienen evidencia mixta (no cubierta por las fuentes revisadas).
6. [H] Autocompletado y búsqueda incremental: respuesta en < ~200 ms tras el *debounce*; validación en línea que no bloquee la escritura.
7. [H] IA con *streaming*: mide por separado el **tiempo hasta el primer token (TTFT)** y la latencia total; acusa recibo en < 100 ms (el mensaje aparece y el botón cambia a "Detener"); estado honesto ("buscando…") mientras no hay tokens; siempre opción de detener. Las cifras tipo "TTFT < 500 ms se siente instantáneo" no tienen fuente identificable.
8. [H] Nunca añadas demora artificial a tareas rutinarias; si una operación compleja termina rápido, muestra el trabajo realmente hecho en lugar de inventar espera (T6).

### Por contexto
| Contexto | Aplicación |
|---|---|
| Web/escritorio | INP p75 ≤ 200 ms; evitar tareas largas (> 50 ms) en el hilo principal; navegación interna sin recarga completa. |
| Móvil/táctil | Estado pulsado inmediato; probar con CPU lenta y red móvil; UI optimista en acciones frecuentes (me gusta, marcar). |
| Formularios | Validación en línea sin bloqueo; el botón de envío muestra que el primer clic se registró en vez de pedir "no pulse dos veces". |
| Dashboards/datos | Carga progresiva por widget; no bloquear toda la vista por un panel lento; consultas largas con progreso y cancelación. |
| E-commerce | Búsqueda y filtros por debajo del umbral; pago con estado claro y sin dobles cargos. |
| Interfaces conversacionales/IA | TTFT como KPI; *streaming*; "Detener" siempre visible; estados de trabajo veraces. |
| Voz | Señal sonora o visual de "escuchado" casi inmediata; los silencios de varios segundos rompen el turno. |
| Sistemas de diseño | Componentes de estado (cargando, vacío, error, parcial, éxito) con anuncio accesible y respeto a `prefers-reduced-motion`. |

### Ejemplos
- **Bueno:** una lista de tareas que marca el elemento como hecho al instante y sincroniza en segundo plano; si falla, lo desmarca y avisa.
- **Incumple:** un filtro de catálogo que tarda 1,5 s en cada cambio y no da señal alguna: la persona pulsa dos veces y se pierde.
- **Incumple (ética):** un comparador que muestra "Analizando 2.000 ofertas…" durante 8 s cuando el resultado ya estaba listo.

## Anti-patrones
- *Spinners* indefinidos sin contexto ni cancelación en procesos de más de 10 s.
- Barras de progreso falsas o atascadas en el 99 %.
- Animaciones de transición largas que retrasan la tarea.
- Bloquear toda la interfaz por una carga parcial.
- Demoras artificiales (`setTimeout` fijo) para aparentar esfuerzo.

## Ética y accesibilidad
- **Línea roja:** fabricar esperas o progreso que no reflejan trabajo real. Solo es legítimo mostrar el trabajo que de verdad ocurre; una demora deliberada solo se justifica para la comprensión (p. ej. confirmar una acción grave) y nunca debe bloquear a quien tiene prisa.
- WCAG 2.2: **2.2.1 Timing Adjustable** (A); **2.2.2 Pause, Stop, Hide** (A: animaciones de carga de más de 5 s junto a otro contenido deben poder pausarse); **2.2.6 Timeouts** (AAA: avisar de cuánta inactividad provoca pérdida de datos, salvo que se conserven más de 20 horas); **2.3.3 Animation from Interactions** (AAA) y `prefers-reduced-motion`; **4.1.3 Status Messages** (AA: "Cargando" o "Guardado" anunciados sin mover el foco, `role="status"` / `aria-live`). Un *spinner* solo visual deja sin información a quien usa lector de pantalla.

## Cómo auditarla
### Señales observables
- Clics repetidos sobre el mismo control; abandonos durante cargas.
- Controles que no cambian de estado al pulsarlos.
- Long Tasks > 50 ms en el panel de rendimiento; TBT alto.
### Preguntas
- ¿Cada acción tiene respuesta visible en < 100 ms?
- ¿Las operaciones de más de 10 s muestran porcentaje y permiten cancelar?
- ¿El estado de carga se anuncia a tecnologías de apoyo?
- ¿Hay demoras fijas en flujos de "análisis"?
### Métricas
- INP, LCP y CLS p75 (CrUX, PageSpeed Insights, RUM); marcar INP > 200 ms.
- Tiempo de acción a respuesta visible medido fotograma a fotograma en vídeo, con CPU ×4 y red lenta.
- IA: TTFT y tiempo total p50/p95; existencia del control "Detener".
- Revisión de código: búsqueda de `setTimeout` o retardos fijos en flujos de procesamiento.

## Relaciones
- Refuerza / se apoya en: MOT-01 Flujo — la retroalimentación inmediata es condición del flujo.
- Refuerza / se apoya en: MOT-05 Regla pico-final — una espera larga puede convertirse en el pico negativo recordado.
- Refuerza / se apoya en: MOT-02 Gradiente de meta — el progreso visible sostiene la espera.
- Refuerza / se apoya en: MOT-03 Efecto Zeigarnik — las tareas cortadas por esperas quedan abiertas en la mente.
- Refuerza / se apoya en: ACC-01 Ley de Fitts — el tiempo total suma movimiento y respuesta del sistema.
- Tensiona con: DEC-03 Sesgo cognitivo / "labor illusion" — la espera puede aumentar el valor percibido; resolver mostrando trabajo real, nunca inventado (T6).
- Tensiona con: MOT-04 Ley de Parkinson — tentación de "rellenar" la espera con animación; no confundir duración de la tarea con latencia.
- Tensiona con: DEC-04 Efecto estética-usabilidad — transiciones vistosas que alargan el ciclo.
- Se confunde a menudo con: los límites de Nielsen (0,1/1/10 s) — son el marco perceptivo; Doherty es la afirmación sobre productividad. Y con la duración total de la tarea (Parkinson).

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/doherty-threshold/ — síntesis divulgativa (su atribución al *IBM Systems Journal* no se pudo verificar).
- Primarias:
  - Doherty, W. J. y Thadhani, A. J. (1982). *The Economic Value of Rapid Response Time*. IBM, GE20-0752-0. Transcripción: https://jlelliotton.blogspot.com/p/the-economic-value-of-rapid-response.html
  - Miller, R. B. (1968). Response time in man-computer conversational transactions. *AFIPS FJCC*, 33, 267–277. doi:10.1145/1476589.1476628 (metadatos verificados; texto original no consultado: descarga bloqueada por ACM; contenido según el folleto de IBM y Shneiderman, 1984)
  - Thadhani, A. J. (1981). Interactive user productivity. *IBM Systems Journal*, 20(4), 407–423. doi:10.1147/sj.204.0407
  - Card, S. K., Robertson, G. G. y Mackinlay, J. D. (1991). The information visualizer, an information workspace. *CHI '91*, 181–186. doi:10.1145/108844.108874
  - Nielsen, J. (1993). *Usability Engineering*, cap. 5. Academic Press.
  - Myers, B. A. (1985). The importance of percent-done progress indicators for computer-human interfaces. *CHI '85*, 11–17. doi:10.1145/317456.317459 (PDF del autor: https://www.cs.cmu.edu/~bam/papers/percentdoneCHI85.pdf)
  - Harrison, C., Amento, B., Kuznetsov, S. y Bell, R. (2007). Rethinking the progress bar. *UIST '07*, 115–118. doi:10.1145/1294211.1294231
  - Harrison, C., Yeo, Z. y Hudson, S. E. (2010). Faster progress bars: manipulating perceived duration with visual augmentations. *CHI '10*, 1545–1548. doi:10.1145/1753326.1753556
  - Buell, R. W. y Norton, M. I. (2011). The Labor Illusion: How Operational Transparency Increases Perceived Value. *Management Science*, 57(9), 1564–1579. doi:10.1287/mnsc.1110.1376
- Secundarias consultadas:
  - Nielsen, J. Response Times: The 3 Important Limits. NN/g: https://www.nngroup.com/articles/response-times-3-important-limits/
  - Sherwin, K. (2014). Artículo sobre indicadores de progreso. NN/g: https://www.nngroup.com/articles/progress-indicators/
  - Rupert, D. (2015). The Doherty Threshold: https://daverupert.com/2015/06/doherty-threshold/
  - Shneiderman, B. (1984). Response time and display rate in human performance with computers. *ACM Computing Surveys*, 16(3): https://www.cs.umd.edu/users/ben/papers/Shneiderman1984Response.pdf
  - web.dev (2024). Interaction to Next Paint is officially a Core Web Vital: https://web.dev/blog/inp-cwv-launch
  - web.dev — Interaction to Next Paint: https://web.dev/articles/inp · RAIL: https://web.dev/articles/rail
