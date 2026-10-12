---
id: MOT-04
nombre: Ley de Parkinson
nombre_en: Parkinson's Law
alias: [el trabajo se expande hasta llenar el tiempo, inflación de la tarea]
familia: MOT
evidencia: H
etiquetas: [tiempo, plazos, formularios, autocompletado, timeboxing, urgencia-falsa]
refuerza: [MOT-02, MOT-03, MEM-01, SIS-04, SIS-05, ACC-03]
tensiona: [DEC-02, MOT-01, ACC-02, DEC-03, MEM-04, MOT-05]
tensiones: [T5]
fuente_laws_of_ux: https://lawsofux.com/parkinsons-law/
---

# MOT-04 · Ley de Parkinson (*Parkinson's Law*)

> Aforismo satírico según el cual el trabajo se dilata hasta consumir todo el tiempo que se le concede. En UX se usa para recordar que una tarea sin fin claro ni ayudas tiende a alargarse, y que conviene que dure menos de lo que la persona espera.

**Idea clave para quien diseña:** acorta la tarea quitando trabajo (autocompletar, valores por defecto, no pedir lo que ya sabes), **nunca** añadiendo presión de tiempo.

## Resumen operativo
- **Qué dice:** una tarea sin final claro ni ayudas tiende a alargarse; en UX se aplica acortándola con menos trabajo, no con prisa.
- **Evidencia:** H — aforismo satírico de 1955 sobre burocracia; el apoyo experimental es indirecto (fijación de metas) y el estudio de plazos más citado (Ariely y Wertenbroch, 2002) está retractado y no se replicó.
- **Haz:** 1) `autocomplete`, `inputmode` y valores por defecto en todos los campos 2) no pidas lo que ya sabes ni lo pidas dos veces 3) declara el alcance al empezar y marca un final explícito.
- **Evita:** usarla para justificar urgencia artificial (cuentas atrás, escasez inventada): es un patrón oscuro.
- **Sospecha de esta ley cuando…:** campos con mucha permanencia o reediciones; pasos sin un "hecho" visible; temporizadores que se reinician al recargar.
- **Mide con:** tiempo por paso frente a la mediana esperada; auditoría automática de `autocomplete` e inventario de límites de tiempo ajustables.
- **Vecinas:** MEM-01 Carga cognitiva (refuerza) · MOT-02 Gradiente de meta (refuerza) · MEM-04 Fragmentación (tensiona, T5) · DEC-03 Sesgo cognitivo (tensiona)

## Origen
- **C. Northcote Parkinson (19 de noviembre de 1955)**, "Parkinson's Law", ensayo **satírico** en *The Economist* sobre el crecimiento de la burocracia británica (Almirantazgo, Oficina Colonial). Su tesis central era organizativa: la plantilla crece año tras año (su "fórmula" da entre un 5,17 % y un 6,56 % anual) con independencia del trabajo real, por la multiplicación de subordinados y de trabajo entre ellos. La frase sobre el trabajo que se expande ("work expands so as to fill the time available for its completion") es sólo la apertura. Se recopiló en *Parkinson's Law: The Pursuit of Progress* (Houghton Mifflin, 1957; John Murray, 1958).
- Parkinson parodiaba la ciencia administrativa: **no es una ley científica** y su "fórmula" es humorística.
- Apoyo empírico afín, posterior y parcial:
  - **Bryan y Locke (1967)**, "Parkinson's law as a goal-setting phenomenon", *Organizational Behavior and Human Performance*, 2, 258–275: ante la misma tarea con distintos límites de tiempo, el tiempo empleado se ajustó al disponible (no verificado: texto tras muro de pago; metadatos comprobados, descripción de fuentes secundarias).
  - **Ariely y Wertenbroch (2002)**, "Procrastination, deadlines, and performance", *Psychological Science*, 13(3), 219–224, informó de que los plazos externos funcionaban mejor que los autoimpuestos. **El artículo fue retractado por la revista en 2026** (nota de retractación en *Psychological Science*, 37(9), 665; motivo no consultado), y una replicación de su estudio 2 (Hyndman y Bisin, 2026, *Psychological Science*, 37(8), 557–571) encontró que cambiar los plazos tuvo un efecto insignificante en el rendimiento. No debe usarse como apoyo.
- Corolarios populares: ley de la trivialidad (*bike-shedding*), "los datos se expanden hasta llenar el almacenamiento".

## Mecanismo
Las explicaciones son psicológicas y más modernas que Parkinson:
- **Fijación de metas (Locke):** el plazo actúa como meta implícita de ritmo; con más tiempo, el ritmo baja.
- **Procrastinación:** el esfuerzo se concentra cerca del final.
- **Refinamiento excesivo:** el tiempo sobrante se gasta puliendo.
- **Falacia de planificación:** estimaciones optimistas más holgura que se consume.

En una interfaz, cuando no hay un fin claro, ni valores por defecto, ni ayudas de entrada, la persona delibera, compara, reescribe y revisa más de lo necesario. La solución eficaz no es meter prisa, sino **reducir el trabajo** y **marcar el final**.

## Evidencia y límites
- **Nivel: H (heurística de diseño).** Origen humorístico y anecdótico; apoyo experimental indirecto en la investigación sobre fijación de metas y plazos; el estudio más citado sobre plazos (Ariely y Wertenbroch, 2002) está retractado y no se replicó. **No hay estudios de UX** que validen "la ley de Parkinson en interfaces". Las recomendaciones habituales (autocompletado, ahorrar tiempo) son buenas, pero se justifican mejor por coste de interacción (ACC-01), carga cognitiva (MEM-01) y prevención de errores.
- Condiciones de validez: tareas sin un fin natural o con tiempo holgado (rellenar perfiles, redactar, configurar, investigación con plazos abiertos). No aplica a tareas breves con un fin definido.
- Malentendidos frecuentes:
  - **Usarla para justificar urgencia artificial** (cuentas atrás, "la oferta expira en 10:00", stock inventado). Eso es un **patrón oscuro**, no una aplicación de la ley.
  - Confundir duración de la tarea con latencia del sistema (eso es ACC-02 Doherty).
  - Atribuirle base científica propia.
  - Tratar todo tiempo "expandido" como desperdicio: en tareas creativas o de aprendizaje puede ser valor (MOT-01).

## Aplicación práctica
### Reglas
1. **[H, norma]** Usa `autocomplete` con tokens estándar (`name`, `email`, `street-address`, `postal-code`, `cc-number`, `one-time-code`); WCAG 1.3.5 lo exige para datos personales de la persona usuaria.
2. **[H]** Usa `type` e `inputmode` adecuados (`email`, `tel`, `numeric`) para el teclado correcto.
3. **[H, norma]** No pidas lo que ya sabes ni lo vuelvas a pedir (WCAG 3.3.7); deduce lo deducible (dirección a partir del código postal).
4. **[H]** Ofrece atajos de compleción: pago exprés, passkeys, importar desde documento.
5. **[H]** Declara el alcance antes de empezar ("4 preguntas, unos 2 minutos") y cúmplelo; esta táctica se justifica mejor por MOT-02 que por Parkinson.
6. **[H]** Marca un final explícito: botón de envío claro y estado "hecho" visible, para evitar la revisión indefinida.
7. **[H]** En equipos de diseño e investigación (el uso más fiel al original), pon *timebox* a sprints, ideación y pruebas rápidas.
8. **[H]** Si hay plazos, que sean reales, razonables y ajustables; que un plazo externo ayude a terminar es plausible (Bryan y Locke, 1967), pero el apoyo experimental más citado (Ariely y Wertenbroch, 2002) está retractado y no se replicó.
9. **[H]** En respuestas de IA, proporcionalidad: la verbosidad es expansión que consume el tiempo de quien lee.

### Por contexto
| Contexto | Aplicación |
|---|---|
| formularios | `autocomplete`, `inputmode`, valores por defecto sensatos, sin entrada redundante, permitir pegar. |
| e-commerce | Checkout exprés, dirección guardada, pago con un toque; plazos de oferta sólo si son reales. |
| onboarding | Pedir lo mínimo y diferir el resto; perfil completable más tarde. |
| móvil/táctil | Teclado adecuado por campo; rellenado de códigos de un solo uso desde el sistema. |
| interfaces conversacionales/IA | Borradores generados que la persona edita; respuestas proporcionadas; límites de longitud configurables. |
| dashboards/datos | Vistas guardadas y valores por defecto que evitan reconfigurar cada sesión. |
| procesos de equipo | Timeboxing de sprints, sesiones de ideación y tests de guerrilla. |
| sistemas de diseño | Componentes de campo con `autocomplete` e `inputmode` correctos por defecto. |

### Ejemplos
- **Bueno:** un checkout que rellena la dirección desde el código postal, permite pago exprés y muestra "Pedido confirmado" con número y siguiente paso; la tarea dura menos de lo esperado.
- **Lo incumple:** una reserva que pide el mismo correo tres veces, bloquea el pegado en el campo de código y no indica cuándo se ha terminado.
- **Mal uso de la "ley":** un temporizador "Tu reserva expira en 09:59" que se reinicia al recargar la página.

## Anti-patrones
- Urgencia falsa: cuentas atrás que se reinician, "solo quedan 2" inventado (documentado en comercio electrónico por Mathur et al., 2019, CSCW).
- Presión de tiempo en decisiones financieras o de privacidad.
- Límites de sesión que borran el trabajo sin aviso.
- Bloquear el pegado o forzar la escritura de contraseñas o códigos.
- Formularios abiertos sin final claro que invitan a revisar sin fin.

## Ética y accesibilidad
- **Línea roja:** la presión de tiempo artificial es un patrón oscuro y puede vulnerar normativa de consumo (prácticas comerciales desleales) y la prohibición de interfaces engañosas de la DSA (art. 25). Aplica la prueba de cuatro preguntas de `06-etica-accesibilidad/etica-y-patrones-oscuros.md`.
- WCAG 2.2:
  - **2.2.1 Timing Adjustable (A):** todo límite de tiempo debe poder desactivarse, ajustarse o ampliarse, salvo excepciones (tiempo real, esencial o más de 20 h).
  - **2.2.5 Re-authenticating (AAA):** al expirar la sesión no se pierden los datos.
  - **2.2.6 Timeouts (AAA):** avisar de la inactividad que provoca pérdida de datos.
  - **1.3.5 Identify Input Purpose (AA):** propósito de los campos identificable (autocompletado).
  - **3.3.7 Redundant Entry (A):** no pedir de nuevo información ya aportada.
  - **3.3.8 Accessible Authentication (Minimum) (AA):** no bloquear pegado ni gestores de contraseñas.
- Personas con discapacidad cognitiva, motora o visual, o que usan lector de pantalla, necesitan más tiempo: optimizar la duración nunca debe castigar a quien va despacio.

## Cómo auditarla
### Señales observables
- Campos sin `autocomplete` o con `inputmode` incorrecto.
- Datos pedidos dos veces; pegado bloqueado.
- Temporizadores, carruseles automáticos y *timeouts* sin aviso ni ampliación.
- Contadores que se reinician al recargar; escasez no verificable.
- Pasos sin final claro.
### Preguntas
- ¿Qué parte del tiempo de tarea es trabajo que el sistema podría hacer?
- ¿La persona sabe cuándo ha terminado?
- ¿Algún límite de tiempo es artificial? ¿Se puede ampliar?
- ¿Estamos citando Parkinson donde la razón real es carga cognitiva o coste de interacción?
### Métricas
- Tiempo por paso frente a la mediana esperada; campos con permanencia alta o reediciones.
- Porcentaje de uso de autocompletado y pago exprés.
- Test A/B de tiempo de tarea con y sin valores por defecto/autocompletado.
- Auditoría automática (axe, Lighthouse) de atributos `autocomplete`.
- Inventario de límites de tiempo con su mecanismo de ajuste.

## Relaciones
- Refuerza / se apoya en:
  - MOT-02 Gradiente de meta — un final visible y cercano acelera y acota la tarea.
  - MOT-03 Efecto Zeigarnik — tareas abiertas sin plan se alargan; un plan con fecha las cierra.
  - MEM-01 Carga cognitiva — menos decisiones, menos deliberación.
  - SIS-04 Navaja de Occam — pedir menos.
  - SIS-05 Principio de Pareto — optimizar primero los campos que concentran el tiempo.
  - ACC-03 Ley de Postel — aceptar formatos flexibles acorta la entrada.
- Tensiona con:
  - MEM-04 Fragmentación — más pasos reducen carga pero suman tiempo e interacciones (**T5**).
  - DEC-02 Sobrecarga de opciones — muchas opciones invitan a deliberar más.
  - MOT-01 Flujo — en tareas creativas, el tiempo "expandido" puede ser valioso.
  - ACC-02 Umbral de Doherty — no confundir duración de tarea con latencia.
  - DEC-03 Sesgo cognitivo — la urgencia artificial explota sesgos.
  - MOT-05 Regla pico-final — alargar un proceso para mejorar su final rara vez se justifica en interfaces.
- Se confunde a menudo con: la gestión de la espera percibida (ACC-02) y con la escasez/urgencia (DEC-03).

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/parkinsons-law/ — síntesis divulgativa.
- Primarias:
  - Parkinson, C. N. (1955, 19 de noviembre). Parkinson's Law. *The Economist*. https://www.economist.com/news/1955/11/19/parkinsons-law
  - Parkinson, C. N. (1957/1958). *Parkinson's Law: The Pursuit of Progress*. Houghton Mifflin / John Murray.
  - Bryan, J. F. y Locke, E. A. (1967). Parkinson's law as a goal-setting phenomenon. *Organizational Behavior and Human Performance*, 2(3), 258–275. https://doi.org/10.1016/0030-5073(67)90021-9 (texto no leído: muro de pago).
  - Ariely, D. y Wertenbroch, K. (2002). Procrastination, deadlines, and performance: self-control by precommitment. *Psychological Science*, 13(3), 219–224. https://doi.org/10.1111/1467-9280.00441 — **RETRACTADO** (2026): https://doi.org/10.1177/09567976261488042
  - Hyndman, K. y Bisin, A. (2026). Replication of "Procrastination, deadlines, and performance: Self-control by precommitment". *Psychological Science*, 37(8), 557–571. https://doi.org/10.1177/09567976261460772 (leído el resumen).
  - Mathur, A., Acar, G., Friedman, M. J., Lucherini, E., Mayer, J., Chetty, M. y Narayanan, A. (2019). Dark patterns at scale: Findings from a crawl of 11K shopping websites. *Proceedings of the ACM on Human-Computer Interaction*, 3(CSCW), art. 81, 1–32. https://doi.org/10.1145/3359183
- Secundarias consultadas:
  - https://en.wikipedia.org/wiki/Parkinson%27s_law
  - https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html
