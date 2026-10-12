---
id: SIS-04
nombre: Navaja de Occam
nombre_en: Occam's Razor
alias: [navaja de Ockham, lex parsimoniae, principio de parsimonia]
familia: SIS
evidencia: H
etiquetas: [simplicidad, parsimonia, reduccion, sistemas-de-diseno, priorizacion]
refuerza: [DEC-01, DEC-02, MEM-01, PER-05, PER-06, SIS-05, DEC-04]
tensiona: [SIS-03, SIS-01, SIS-02, PER-07, ACC-03]
tensiones: [T1]
fuente_laws_of_ux: https://lawsofux.com/occams-razor/
---

# SIS-04 · Navaja de Occam (*Occam's Razor*)

> Entre explicaciones que dan cuenta de los hechos igual de bien, elige la que necesita menos supuestos. Llevado al diseño: entre soluciones que cumplen igual de bien el objetivo de la persona, elige la que introduce menos elementos, conceptos, pasos y dependencias.

**Idea clave para quien diseña:** quita todo lo que no cambie el resultado, pero nunca lo que la persona necesita para no tener que adivinar.

## Resumen operativo
- **Qué dice:** entre soluciones que cumplen igual de bien, elige la que introduce menos elementos, conceptos, pasos y dependencias.
- **Evidencia:** H — heurística con respaldo indirecto (carga cognitiva, Hick; en previsión, lo complejo aumentó el error un 27 % de media); el matiz olvidado: es un **desempate** entre alternativas igual de eficaces, no una orden de recortar.
- **Haz:** 1) antes de añadir algo, nombra la función que cumple y que nada existente cubre; 2) aplica la prueba de retirada: ¿qué empeora, de forma medible, si lo quitamos?; 3) prefiere un buen default a un ajuste nuevo.
- **Evita:** confundir Occam con minimalismo estético: quitar etiquetas, contraste o navegación visible traslada supuestos a la persona.
- **Sospecha de esta ley cuando…:** hay variantes de componentes casi idénticas, ajustes que nadie cambia o pasos que no añaden información.
- **Mide con:** éxito y tiempo de tarea antes y después de retirar elementos; uso por componente, variante y ajuste.
- **Vecinas:** DEC-01 Ley de Hick (refuerza) · SIS-05 Principio de Pareto (refuerza) · SIS-03 Ley de Tesler (tensiona, T1)

## Origen

- **Guillermo de Ockham (c. 1287–1347)**, fraile franciscano inglés. En su comentario a las *Sentencias* de Pedro Lombardo aparecen formulaciones del tipo «no ha de postularse la pluralidad sin necesidad» (*Numquam ponenda est pluralitas sine necessitate*; libro I, dist. 27, q. 2, según Wikipedia; texto latino no consultado).
- **La frase famosa no es suya.** «No se deben multiplicar los entes sin necesidad» no aparece en Ockham. La forma más antigua localizada la da **John Punch (Poncius)** en su comentario a Duns Escoto incluido en la edición de Wadding (1639): *Non sunt multiplicanda entia sine necessitate*, presentada como «axioma vulgar» que los escolásticos usan con frecuencia (texto comprobado en la reedición Vivès, vol. 15, dist. 34, p. 483). La variante con *praeter necessitatem* es posterior. Precursores: Aristóteles, Ptolomeo, Roberto Grosseteste.
- **En diseño:** Jon Yablonski (2017), «Designing with Occam's Razor» (Medium; republicado en https://lawsofux.com/articles/2017/designing-with-occams-razor/).
- Ideas afines: Antoine de Saint-Exupéry, *Terre des hommes* (1939) — la perfección se alcanza cuando ya no queda nada que quitar, no cuando no queda nada que añadir (cap. III, «L'Avion», según Wikiquote, con la cautela «il semble que…»; edición no consultada; el contexto original es la ingeniería aeronáutica, no la estética); Dieter Rams, «menos, pero mejor».
- **Sesgo de complejidad:** Farnam Street y Yablonski lo ilustran con Farris & Revlin (1989), «Sensible reasoning in two tasks: Rule discovery and hypothesis evaluation», *Memory & Cognition*, 17(2), 221–232, sobre la tarea 2-4-6; se ha sugerido que los participantes proponen reglas más complejas que la real, pero el resumen del artículo trata de estrategias de contrastación de hipótesis y no menciona la complejidad (no verificado: texto completo de pago).

## Mecanismo

**Epistémico:** cada supuesto adicional es un punto más de posible fallo, y las hipótesis con menos parámetros hacen predicciones más nítidas (argumentos bayesianos de Jefferys & Berger en *American Scientist* y de MacKay en *Information Theory, Inference, and Learning Algorithms*, cap. 28; vía Wikipedia, textos no leídos).

**En diseño:** cada elemento añadido compite por la atención (PER-06), aumenta la carga cognitiva (MEM-01) y añade estados que mantener, pruebas que escribir y textos que traducir. Menos piezas significa menos modos de fallo para la persona y para el equipo. Proceso propuesto por Yablonski (2017), parafraseado: partir de lo mínimo y añadir solo cuando haga falta; cuestionar la necesidad de cada elemento; editar sin contemplaciones (sustituir por algo más simple o eliminar); y exponer las decisiones en críticas de diseño, donde tener que justificarlas revela sus debilidades.

## Evidencia y límites

- **Nivel: H** — heurística con respaldo indirecto. La carga cognitiva y la ley de Hick apoyan reducir opciones; en predicción, Green & Armstrong (2015, *Journal of Business Research*, 68, 1678–1685) revisan 97 comparaciones en 32 artículos y hallan que el 81 % de las comparaciones favorecen o igualan al método simple y que la complejidad aumentó el error de previsión en un 27 % de media (26,7 % ponderado) en los 25 artículos con comparación cuantitativa. No hay un estudio que «pruebe» la navaja en UX.
- **Es un desempate, no una prueba:** solo elige entre alternativas **igualmente adecuadas**. Si la solución simple no cumple, se descarta. Existen «anti-navajas» explícitas: Walter Chatton (si tres cosas no bastan, añade una cuarta) y Karl Menger (no reducir entidades hasta la insuficiencia).
- **Cita apócrifa:** «todo debe hacerse tan simple como sea posible, pero no más» se atribuye a Einstein, pero es una paráfrasis popular de una conferencia de 1933, no una cita literal.
- **Malentendidos frecuentes:**
  - **Occam ≠ minimalismo estético.** La navaja recorta *supuestos innecesarios*, no rótulos, contraste ni affordances. Una UI «limpia» sin etiquetas obliga a adivinar: añade supuestos a la persona y es *menos* parsimoniosa cognitivamente.
  - *«Lo más simple es siempre lo mejor.»* El artículo de IxDF lo dice en el título, pero matiza «casi siempre» en el cuerpo.
  - **Simplicidad percibida frente a operativa** (Norman, *Living with Complexity*, 2010): un aparato de un solo botón puede ser complicadísimo de usar.
  - Recortar funcionalidad necesaria para que «parezca simple» viola la condición «sin comprometer la función».

## Aplicación práctica

### Reglas

1. [H] Antes de añadir un elemento, nombra la función que cumple y que nada existente cubre; si no la tiene, no entra.
2. [H] Prueba de retirada: «¿qué empeora, de forma medible, si quitamos esto?». Si nada, sobra.
3. [H] Sistemas de diseño: un componente o variante nuevos requieren una propuesta con caso de uso que demuestre que ninguno existente basta; depreca variantes con uso residual; usa el menor número de niveles de tokens que permita el tematizado necesario.
4. [E] No ocultes la navegación principal de escritorio en un menú fuera de pantalla solo por limpieza; mide la descubribilidad con test de tareas (Yablonski 2017 cita este caso como simplificación que estorba).
5. [H] Prefiere un buen default a un ajuste nuevo: cada ajuste es una pregunta que el producto no supo responder (enlaza con SIS-03).
6. [H] Animación y decoración solo si comunican estado, relación o causalidad; respeta `prefers-reduced-motion`.
7. [H] En investigación, prueba primero la explicación más simple de un problema (etiqueta confusa, contraste bajo) antes de teorías elaboradas — y valídala con datos.
8. [H] Cada función nueva lleva hipótesis de valor y criterio de retirada; contabiliza el coste de mantener la complejidad.

### Por contexto

| Contexto | Aplicación |
|---|---|
| Navegación | Fusionar categorías solapadas; cada categoría justifica su existencia con contenido y demanda (tree testing antes/después). |
| Formularios | Eliminar campos opcionales sin uso; un campo, una pregunta. |
| Dashboards/datos | Quitar decoración que no codifica datos; no eliminar ejes, unidades ni leyendas. |
| Onboarding | Un solo objetivo por pantalla; diferir lo no esencial. |
| Interfaces conversacionales/IA | Respuesta con la mínima longitud que resuelve la pregunta, detalle bajo demanda; no encadenar pasos de «agente» cuando basta una respuesta directa. En explicaciones de IA, la más simple *suficiente*: Kulesza et al. (2013, IEEE VL/HCC, DOI 10.1109/VLHCC.2013.6645235) hallaron que, para formar modelos mentales fieles, la **completitud** de la explicación importa más que su exactitud (*soundness*), y que simplificar en exceso aumenta el esfuerzo mental y resta confianza. |
| Sistemas de diseño | Inventario de componentes y variantes; deprecación con plan. |

### Ejemplos

- **Bueno:** una pantalla de configuración sustituye seis ajustes que casi nadie toca por un default bien elegido y un enlace «Opciones avanzadas».
- **Incumple:** una barra de herramientas con solo iconos sin etiqueta «para limpiar»; parece más simple pero obliga a pasar el cursor por cada icono para saber qué hace.
- **Incumple:** un equipo crea la quinta variante de botón casi idéntica a las otras cuatro; el sistema crece sin función nueva.

## Anti-patrones

- Minimalismo que oculta: iconos sin texto, controles visibles solo al pasar el cursor, enlaces sin subrayado ni contraste.
- Eliminar fricción protectora (confirmaciones de acciones destructivas, avisos de privacidad).
- Recortar contenido de accesibilidad (texto alternativo, transcripciones, enlaces de salto) por «limpieza».
- Sesgo de complejidad en el equipo: soluciones barrocas para parecer expertos.
- Sesgo de simplicidad: negar la complejidad real del dominio (choca con SIS-03).

## Ética y accesibilidad

- **Línea roja:** usar «simplificar» como coartada para quitar opciones que protegen a la persona (baja, privacidad, borrado de datos). La simplicidad legítima facilita la salida (cancelar en un clic) en lugar de esconderla. El principio «Intentional» de *Humane by Design* recuerda que cierta fricción es deliberada y protectora.
- Lo que parece ruido visual (etiquetas, ayudas, subrayados) suele ser función para personas con baja visión, dificultades cognitivas o motoras, o en táctil.
- **WCAG 2.2:** 1.1.1 Contenido no textual; 1.4.1 Uso del color; 1.4.11 Contraste no textual; 1.4.13 Contenido con hover o foco; 2.4.4 Propósito de los enlaces; 2.5.3 Etiqueta en el nombre; 2.3.3 Animación por interacciones; 3.3.2 Etiquetas o instrucciones.

## Cómo auditarla

### Señales observables
- Elementos sin función identificable; acciones duplicadas.
- Variantes de componentes casi idénticas; ajustes que nadie cambia.
- Pasos de flujo que no añaden información.
- Y también simplicidad falsa: iconos sin texto, navegación escondida, ausencia de etiquetas.

### Preguntas
- ¿Qué pasaría si quitamos este elemento?
- ¿Esta simplificación traslada supuestos a la persona?
- ¿Las alternativas comparadas son *igual de eficaces*?
- ¿Qué complejidad se añadió por presión interna y no por necesidad de la persona?

### Métricas
- Éxito y tiempo de tarea antes/después de retirar elementos (la retirada no debe empeorarlos).
- Descubribilidad de funciones en test de tareas.
- Uso por componente/variante y por ajuste.
- Errores y consultas a ayuda tras una «simplificación».

## Relaciones

- Refuerza / se apoya en: DEC-01 Ley de Hick y DEC-02 Sobrecarga de opciones — menos alternativas, decisiones más rápidas.
- Refuerza: MEM-01 Carga cognitiva y PER-06 Atención selectiva — menos elementos compitiendo.
- Refuerza: PER-05 Ley de Prägnanz — preferencia perceptiva por lo simple.
- Refuerza: SIS-05 Principio de Pareto — ayuda a decidir qué conservar.
- Refuerza: DEC-04 Estética-usabilidad — lo ordenado se percibe más usable.
- Tensiona con: SIS-03 Ley de Tesler — hay un mínimo irreducible; recortarlo lo traslada a la persona (T1).
- Tensiona con: SIS-01 Ley de Jakob y SIS-02 Modelo mental — simplificar puede eliminar pistas convencionales o dejar sin modelo.
- Tensiona con: PER-07 Efecto Von Restorff — el elemento distintivo puede parecer «innecesario» sin serlo.
- Tensiona con: ACC-03 Ley de Postel — aceptar entradas variadas exige más lógica interna.
- Se confunde a menudo con: minimalismo visual — Occam reduce supuestos, no información útil.

## Fuentes

- Laws of UX (Jon Yablonski): https://lawsofux.com/occams-razor/ — síntesis divulgativa.
- Primarias:
  - Guillermo de Ockham, comentario a las *Sentencias*, I, dist. 27, q. 2 (vía https://en.wikipedia.org/wiki/Occam%27s_razor; texto latino no consultado).
  - Poncius [Punch], J. (1639). Comentario a Duns Escoto, *Opus Oxoniense*, III, dist. 34, q. única, en L. Wadding (Ed.), *Opera omnia*; reed. Vivès, París, vol. 15, p. 483. https://archive.org/details/operaomni15duns
  - Farris, H. H. & Revlin, R. (1989). Sensible reasoning in two tasks: Rule discovery and hypothesis evaluation. *Memory & Cognition*, 17(2), 221–232. DOI 10.3758/BF03197071 (solo leído el resumen)
  - Green, K. C. & Armstrong, J. S. (2015). Simple versus complex forecasting: The evidence. *Journal of Business Research*, 68(8), 1678–1685. DOI 10.1016/j.jbusres.2015.03.026 (texto leído en la versión de trabajo de repository.upenn.edu/marketing_papers/366)
  - Kulesza, T. et al. (2013). Too much, too little, or just right? Ways explanations impact end users' mental models. IEEE VL/HCC, 3–10. DOI 10.1109/VLHCC.2013.6645235 (solo leído el resumen)
  - Saint-Exupéry, A. de (1939). *Terre des hommes*, cap. III «L'Avion» (según Wikiquote; edición no consultada).
- Secundarias consultadas:
  - Yablonski, J. (2017). Designing with Occam's Razor. https://lawsofux.com/articles/2017/designing-with-occams-razor/
  - Farnam Street. Occam's Razor. https://fs.blog/occams-razor/
  - Farnam Street. Complexity Bias. https://fs.blog/complexity-bias/
  - IxDF. Occam's Razor. https://ixdf.org/literature/article/occam-s-razor-the-simplest-solution-is-always-the-best
  - Norman, D. A. (2010). *Living with Complexity*. MIT Press. (libro no leído; la idea se toma de fuentes secundarias)
