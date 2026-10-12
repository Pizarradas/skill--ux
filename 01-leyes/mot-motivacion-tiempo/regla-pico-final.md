---
id: MOT-05
nombre: Regla pico-final
nombre_en: Peak-End Rule
alias: [regla del pico y el final, duration neglect, olvido de la duración, yo que recuerda]
familia: MOT
evidencia: E2
etiquetas: [memoria, emocion, finales, errores, satisfaccion, journey-map, encuestas]
refuerza: [DEC-03, MEM-05, PER-07, MOT-03, ACC-02, DEC-04, MOT-02]
tensiona: [MOT-04, MOT-01]
tensiones: [T4, T7]
fuente_laws_of_ux: https://lawsofux.com/peak-end-rule/
---

# MOT-05 · Regla pico-final (*Peak-End Rule*)

> Al evaluar en retrospectiva un episodio con principio y fin claros, las personas pesan sobre todo el momento de mayor intensidad emocional y el momento final, y apenas tienen en cuenta cuánto duró. El recuerdo se parece más a la media de pico y final que a la suma de todos los momentos.

**Idea clave para quien diseña:** elimina los picos negativos y cierra cada episodio con claridad; el recuerdo, no el minuto a minuto, es lo que decide si la persona vuelve.

## Resumen operativo
- **Qué dice:** el recuerdo de un episodio delimitado se basa sobre todo en su peor (o mejor) momento y en su final; la duración apenas cuenta.
- **Evidencia:** E2 — metaanálisis con r = 0,58 y duración casi nula (Alaybek et al., 2022); se olvida que la media de todos los momentos predice casi igual y que falla en días o relaciones largas.
- **Haz:** 1) elimina primero los picos negativos (errores, cobros inesperados, pérdida de datos) 2) cierra cada episodio con confirmación, resumen y siguiente paso 3) mide también momento a momento, no sólo al final.
- **Evita:** creer que un final bonito compensa un proceso doloroso, o alargar la tarea para "mejorar el final".
- **Sospecha de esta ley cuando…:** valoraciones y tickets que citan un único incidente; flujos que terminan con upsell o en pantalla genérica.
- **Mide con:** intensidad emocional por paso (journey map con datos) frente a satisfacción retrospectiva; intención de volver tras episodios con y sin incidente.
- **Vecinas:** MEM-05 Efecto de posición serial (refuerza) · MOT-02 Gradiente de meta (refuerza) · MOT-04 Ley de Parkinson (tensiona) · MOT-01 Flujo (tensiona)

## Origen
- **Fredrickson y Kahneman (1993)**, "Duration neglect in retrospective evaluations of affective episodes", *Journal of Personality and Social Psychology*, 65(1), 45–55: modelo de "instantáneas" y olvido de la duración.
- **Kahneman, Fredrickson, Schreiber y Redelmeier (1993)**, "When more pain is preferred to less: Adding a better end", *Psychological Science*, 4(6), 401–405. Experimento del agua fría:
  - Ensayo corto: 60 s con la mano en agua a 14 °C.
  - Ensayo largo: esos mismos 60 s más 30 s en los que el agua sube a unos 15 °C (aún desagradable, algo menos).
  - Al elegir cuál repetir, **la mayoría prefirió el largo** (22 de 32, **69 %**), pese a contener más dolor total. Entre los 21 participantes que notaron una mejora clara (≥2 puntos) en los últimos 30 s, 17 (81 %) eligieron el largo; los 11 que apenas la notaron se repartieron 6:5 a favor del corto. El "80 %" que circula en divulgación parece redondear ese subgrupo, no el total. Una réplica sin medida en tiempo real obtuvo 24 de 37.
- **Redelmeier y Kahneman (1996)**, "Patients' memories of painful medical treatments", *Pain*, 66(1), 3–8: en colonoscopia (n = 154) y litotricia (n = 133), el dolor total recordado se correlacionó con el dolor máximo y con el de los últimos 3 minutos, no con la duración.
- **Redelmeier, Katz y Kahneman (2003)**, "Memories of colonoscopy: A randomized trial", *Pain*, 104(1–2), 187–194: en 682 pacientes, prolongar brevemente el final con molestia leve hizo que el procedimiento se recordara como menos desagradable (4,4 frente a 4,9 en escala de 10 cm) y aumentó ligeramente la tasa de regreso para una nueva colonoscopia (OR = 1,41). Evidencia de campo aleatorizada con consecuencias reales.
- **Do, Rupert y Wolford (2008)**, *Psychonomic Bulletin & Review*, 15(1), 96–98: extienden la regla a experiencias placenteras; terminar con algo menos deseable reduce la satisfacción global.

## Mecanismo
La memoria episódica no graba un vídeo continuo: conserva **instantáneas representativas**. El pico es lo más saliente emocionalmente; el final, lo más reciente. La duración no se codifica como un atributo afectivo y por eso se ignora.

Kahneman distingue el **"yo que experimenta"**, que vive cada momento, del **"yo que recuerda"**, que es quien decide volver, recomendar, renovar o cancelar. El diseño atiende a ambos, pero las decisiones futuras las toma el segundo.

## Evidencia y límites
- **Nivel: E2 (efecto robusto, magnitud contextual).** El meta-análisis de **Alaybek, Dalal et al. (2022)**, *Organizational Behavior and Human Decision Processes*, 170, 104149 (174 tamaños de efecto), encuentra un efecto pico-final **grande (r = 0,58; IC 95 % 0,49–0,66)** sobre las evaluaciones retrospectivas y un efecto de la duración prácticamente nulo; pero ese efecto es **comparable al de la media de todos los momentos**, que también predice bien. No es E1 porque no hay un modelo cuantitativo predictivo para interfaces, y sus límites son claros.
- **Límites en experiencias largas o de muchos episodios:**
  - Miron-Shatz (2009, *Emotion*): al evaluar un día completo (≈2.400 participantes), la media de los episodios predijo mejor que pico y final; el final se ignoró.
  - Kemp, Burt y Furneaux (2008, *Memory & Cognition*), con vacaciones: la regla no predice especialmente bien; el periodo más memorable o inusual predecía mejor.
  - Con experiencias positivas simples, Mah y Bernstein (2019, *Journal of Applied Research in Memory and Cognition*, 8(3), 337–346) no observaron la regla ni en niños ni en adultos (según el título; texto no leído).
  - Expectativas, objetivos y estado de ánimo al recordar modulan la evaluación; los picos pueden desvanecerse.
- **Implicación para productos:** sólida para episodios cortos y delimitados (una sesión, un trámite, un checkout, una llamada de soporte); débil para la relación con un producto a lo largo de meses. Una suscripción no tiene un único final: piensa en **muchos episodios**, cada uno con su pico y su final.
- Malentendidos frecuentes:
  - *"Sólo importan pico y final."* El resto sí afecta a la experiencia vivida, al abandono durante el proceso y a la compleción.
  - *"Un final con confeti compensa un proceso doloroso."* Un pico negativo intenso (pérdida de datos, cobro inesperado) domina el recuerdo.
  - *"Los picos negativos pesan más."* Plausible por el sesgo de negatividad, pero la asimetría en contextos de UX no está cuantificada [H].

## Aplicación práctica
### Reglas
1. **[E]** Prioriza eliminar los picos negativos del recorrido (errores, cobros inesperados, pérdidas de datos): pesan en el recuerdo global (Redelmeier y Kahneman, 1996; Alaybek et al., 2022).
2. **[E]** Diseña el final de cada episodio: confirmación clara, resumen y siguiente paso (Kahneman et al., 1993; Do et al., 2008).
3. **[H]** Mapea la intensidad emocional por paso en el *journey map* con datos de investigación, no suposiciones.
4. **[H]** No coloques upsells, pop-ups de retención ni peticiones comerciales en el último momento.
5. **[H]** Mensajes de error que expliquen qué pasó, qué hacer y cuándo se resolverá, sin culpar.
6. **[E, efecto pequeño de laboratorio]** Las barras de progreso que aceleran hacia el final se perciben más rápidas, y las pausas cerca del final, más lentas (Harrison et al., 2007; 22 participantes).
7. **[H]** Interpreta CSAT/NPS de fin de sesión y SUS al final de un test como medidas sesgadas por pico y final; combínalas con medidas por tarea (SEQ, observación, muestreo de experiencias).
8. **[H]** No alargues una tarea de interfaz para mejorar su final: el caso de la colonoscopia es médico, no una licencia para añadir pasos.

### Por contexto
| Contexto | Aplicación |
|---|---|
| e-commerce | Confirmación de pedido con número, fecha de entrega y qué pasa después; sin ofertas en ese momento. |
| formularios | Pantalla de envío que confirma qué se ha recibido y qué ocurrirá; errores recuperables sin perder datos. |
| onboarding | Cerrar con un primer logro real, no con un tour interminable. |
| errores/soporte | Recuperación generosa ante fallos graves; cerrar cada caso con resolución y resumen. |
| offboarding/bajas | Baja sencilla y respetuosa; es el último recuerdo y condiciona el regreso [H]. |
| interfaces conversacionales/IA | Cerrar tareas con resumen de lo hecho y lo pendiente; tratar con transparencia alucinaciones o acciones fallidas (picos negativos). |
| móvil/táctil | Estados de éxito claros tras acciones clave; esperas con feedback. |
| investigación | No pedir valoraciones sólo en el pico positivo; medir también tras fallos. |

### Ejemplos
- **Bueno:** tras presentar una declaración, la pantalla final confirma la recepción, resume el resultado y explica los siguientes plazos, con tono cálido y sin venta adicional.
- **Lo incumple:** un checkout fluido que termina con un modal "¿Añadir seguro premium?" y un cargo inesperado en el resumen; el pico negativo final borra lo bueno.
- **Bueno (pico negativo gestionado):** una app de transporte que, durante la espera, muestra dónde está el vehículo y cuánto falta, en lugar de un spinner sin información.

## Anti-patrones
- Fabricar un final agradable para tapar un proceso abusivo o cobros ocultos.
- Pedir reseñas sólo tras el éxito y nunca tras el fallo (sesgo de selección que infla la prueba social).
- Picos de recompensa variable (loot boxes, rachas) diseñados para crear compulsión.
- Upsells o pop-ups de "¿seguro que te vas?" en el último paso.
- Flujos que terminan en una pantalla genérica o sin confirmación.

## Ética y accesibilidad
- **Línea roja:** usar el final para maquillar un cobro, una condición abusiva o un daño. Si el recuerdo positivo sólo se sostiene porque la persona no ve el resto, es manipulación. Aplica la prueba de cuatro preguntas de `06-etica-accesibilidad/etica-y-patrones-oscuros.md`. Relación con T4: las valoraciones al final de un test están sesgadas.
- WCAG 2.2:
  - **4.1.3 Status Messages (AA):** confirmaciones anunciadas a lectores de pantalla (`role="status"`).
  - **2.3.1 Three Flashes or Below Threshold (A):** celebraciones sin destellos.
  - **2.3.3 Animation from Interactions (AAA):** respetar `prefers-reduced-motion` en animaciones de éxito.
  - **1.4.1 Use of Color (A):** el éxito o el error no se comunican sólo con color (ni sólo con sonido).
  - **3.3.1 Error Identification (A) y 3.3.3 Error Suggestion (AA):** errores identificados y con sugerencia, que reducen el pico negativo.

## Cómo auditarla
### Señales observables
- Flujos que terminan sin confirmación o con pantalla genérica.
- Upsells o pop-ups en el último paso.
- Mensajes de error crípticos; esperas sin feedback.
- Valoraciones polarizadas o tickets que citan un único incidente.
- Solicitudes de reseña sólo tras eventos positivos.
### Preguntas
- ¿Cuál es el peor momento del recorrido según datos (abandono, tickets, verbatims)?
- ¿Cómo termina cada episodio clave: pagar, enviar, cancelar, contactar con soporte?
- ¿Cuándo pedimos valoraciones y por qué en ese momento?
- ¿Tratamos la relación larga como un único final o como muchos episodios?
### Métricas
- Intensidad emocional por paso (investigación) y localización de picos negativos.
- Satisfacción retrospectiva frente a medidas momento a momento (SEQ por tarea).
- Intención de volver o recomendar tras episodios con y sin incidente.
- Tasa de contacto con soporte tras la confirmación (finales poco claros).

## Relaciones
- Refuerza / se apoya en:
  - DEC-03 Sesgo cognitivo — es un caso concreto de sesgo de memoria y juicio.
  - MEM-05 Efecto de posición serial — el final se relaciona con la recencia; el pico es saliencia, no primacía.
  - PER-07 Efecto Von Restorff — lo distinto y saliente se recuerda.
  - MOT-03 Efecto Zeigarnik — una tarea abierta es un final sin cerrar.
  - ACC-02 Umbral de Doherty — la espera percibida genera picos negativos.
  - DEC-04 Efecto estética-usabilidad — un final pulido mejora la percepción global.
  - MOT-02 Gradiente de meta — la meta alcanzada es el final; ciérrala bien.
- Tensiona con:
  - MOT-04 Ley de Parkinson y la eficiencia — alargar un proceso para mejorar su final rara vez se justifica en interfaces.
  - MOT-01 Flujo — el flujo es un estado vivido; el recuerdo lo fijan picos y finales.
- Se confunde a menudo con: el efecto de recencia (MEM-05) — la regla pico-final añade el pico emocional y el olvido de la duración.

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/peak-end-rule/ — síntesis divulgativa.
- Primarias:
  - Fredrickson, B. L. y Kahneman, D. (1993). Duration neglect in retrospective evaluations of affective episodes. *Journal of Personality and Social Psychology*, 65(1), 45–55. https://doi.org/10.1037/0022-3514.65.1.45
  - Kahneman, D., Fredrickson, B. L., Schreiber, C. A. y Redelmeier, D. A. (1993). When more pain is preferred to less: Adding a better end. *Psychological Science*, 4(6), 401–405. https://doi.org/10.1111/j.1467-9280.1993.tb00589.x
  - Redelmeier, D. A. y Kahneman, D. (1996). Patients' memories of painful medical treatments: Real-time and retrospective evaluations of two minimally invasive procedures. *Pain*, 66(1), 3–8. https://doi.org/10.1016/0304-3959(96)02994-6
  - Redelmeier, D. A., Katz, J. y Kahneman, D. (2003). Memories of colonoscopy: A randomized trial. *Pain*, 104(1–2), 187–194. https://doi.org/10.1016/S0304-3959(03)00003-4
  - Do, A. M., Rupert, A. V. y Wolford, G. (2008). Evaluations of pleasurable experiences: The peak-end rule. *Psychonomic Bulletin & Review*, 15(1), 96–98. https://doi.org/10.3758/PBR.15.1.96
  - Alaybek, B., Dalal, R. S., Fyffe, S., Aitken, J. A., Zhou, Y., Qu, X., Roman, A. y Baines, J. I. (2022). All's well that ends (and peaks) well? A meta-analysis of the peak-end rule and duration neglect. *Organizational Behavior and Human Decision Processes*, 170, 104149. https://doi.org/10.1016/j.obhdp.2022.104149
  - Miron-Shatz, T. (2009). Evaluating multiepisode events: Boundary conditions for the peak-end rule. *Emotion*, 9(2), 206–213. https://doi.org/10.1037/a0015295
  - Kemp, S., Burt, C. D. B. y Furneaux, L. (2008). A test of the peak-end rule with extended autobiographical events. *Memory & Cognition*, 36(1), 132–138. https://doi.org/10.3758/MC.36.1.132
  - Mah, E. Y. y Bernstein, D. M. (2019). No peak-end rule for simple positive experiences observed in children and adults. *Journal of Applied Research in Memory and Cognition*, 8(3), 337–346. https://doi.org/10.1037/h0101838 (texto no leído: muro de pago).
  - Harrison, C., Amento, B., Kuznetsov, S. y Bell, R. (2007). Rethinking the progress bar. *UIST '07*, 115–118. https://doi.org/10.1145/1294211.1294231
- Secundarias consultadas:
  - https://en.wikipedia.org/wiki/Peak%E2%80%93end_rule
  - Kane, NN/g. The Peak–End Rule. https://www.nngroup.com/articles/peak-end-rule
  - https://ideas.repec.org/a/eee/jobhdp/v170y2022ics0749597822000334.html
