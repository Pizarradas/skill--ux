---
id: MEM-01
nombre: Carga cognitiva
nombre_en: Cognitive Load
alias: [teoría de la carga cognitiva, Cognitive Load Theory, CLT, esfuerzo mental, sobrecarga cognitiva]
familia: MEM
evidencia: C
etiquetas: [memoria-de-trabajo, carga-extrinseca, carga-intrinseca, atencion-dividida, simplificacion]
refuerza: [MEM-02, MEM-03, MEM-04, DEC-01, DEC-02, SIS-01, SIS-02, SIS-03, SIS-04, PER-05, ACC-02, PER-06, MOT-01]
tensiona: [DEC-04, ACC-04, SIS-04]
tensiones: [T1, T5, T11, T14]
fuente_laws_of_ux: https://lawsofux.com/cognitive-load/
---

# MEM-01 · Carga cognitiva (*Cognitive Load*)

> La carga cognitiva es la demanda que una tarea y su presentación imponen sobre la memoria de trabajo. Cuando esa demanda supera la capacidad disponible, aumentan el tiempo, los errores y la sensación de agobio.

**Idea clave para quien diseña:** no puedes eliminar la complejidad propia de la tarea, pero sí todo el esfuerzo que añade tu manera de presentarla; ese esfuerzo sobrante es tu responsabilidad.

## Resumen operativo
- **Qué dice:** la memoria de trabajo es limitada; todo esfuerzo que la presentación añade a la complejidad propia de la tarea resta recursos a la tarea.
- **Evidencia:** C — marco explicativo sin cifra ni fórmula; sus efectos derivados (atención dividida, redundancia, inversión por pericia) sí están replicados en instrucción. Se olvida que la carga "pertinente" ya no se considera una fuente que se sume.
- **Haz:** 1) junta en espacio y tiempo lo que hay que integrar (error junto al campo, rótulo junto a la serie) 2) elimina ruido y usa convenciones 3) descarga trabajo en el sistema (recordar, calcular, rellenar).
- **Evita:** "simplificar" escondiendo lo necesario: la carga pasa a la memoria del usuario.
- **Sospecha de esta ley cuando…:** hay dudas largas, relecturas o abandono en pasos densos; la gente dice "es mucho" o "me pierdo".
- **Mide con:** escala de esfuerzo mental de Paas o NASA-TLX tras la tarea; tiempo en tarea y tasa de errores.
- **Vecinas:** MEM-02 Memoria de trabajo (refuerza) · SIS-03 Ley de Tesler (refuerza) · SIS-04 Navaja de Occam (tensiona, T1/T11)

## Origen
La teoría de la carga cognitiva (CLT) nace en la psicología de la instrucción, no en la interacción persona-ordenador. John Sweller la formuló a partir de estudios sobre resolución de problemas: observó que ciertas estrategias de resolución consumen tanta memoria de trabajo que impiden aprender del propio problema.

- Publicación fundacional: **Sweller, J. (1988).** "Cognitive load during problem solving: Effects on learning." *Cognitive Science*, 12(2), 257–285. DOI: 10.1207/s15516709cog1202_4.
- **Aviso sobre la fuente divulgativa:** Laws of UX atribuye a la publicación de 1988 el título "Cognitive Load Theory, Learning Difficulty, and Instructional Design". Ese título corresponde a un artículo posterior: Sweller (1994), *Learning and Instruction*, 4(4), 295–312 (DOI 10.1016/0959-4752(94)90003-5), no al de 1988. Cita el de 1988 con el título correcto indicado arriba.
- Formulación clásica de los tres tipos de carga: **Sweller, van Merriënboer & Paas (1998)**, *Educational Psychology Review*, 10(3), 251–296.
- Reformulaciones: **Sweller (2010)**, sobre la interactividad entre elementos, y **Sweller, van Merriënboer & Paas (2019)**, revisión a los 20 años.
- Medición: escala subjetiva de esfuerzo mental de **Paas (1992)** y el NASA-TLX de **Hart & Staveland (1988)**.
- Traslado a UX: Whitenton (2013, NN/g), "Minimize Cognitive Load to Maximize Usability".

## Mecanismo
La memoria de trabajo (MEM-02) es el cuello de botella: sostiene muy pocas unidades a la vez, mientras que la memoria a largo plazo es prácticamente ilimitada. Los esquemas aprendidos —por ejemplo, las convenciones de interfaz— permiten tratar muchos elementos como uno solo. Por eso la carga no es una propiedad fija de la pantalla: depende de la persona. Lo que para un novato son diez piezas sueltas es un único esquema para un experto.

La CLT distingue tres fuentes:
- **Intrínseca:** la complejidad propia de la tarea, determinada por cuántos elementos deben procesarse a la vez porque dependen entre sí (interactividad entre elementos). No se elimina sin cambiar la tarea, pero se puede **secuenciar**.
- **Extrínseca (o extraña):** la que impone la forma de presentar: buscar, descifrar, integrar información separada, ignorar ruido. Es la que controla el diseño y la que hay que minimizar.
- **Pertinente (*germane*):** recursos dedicados a construir esquemas (aprender). Su estatus se ha revisado: ver la sección siguiente.

Cada recurso gastado en descifrar la interfaz se resta de la tarea real.

## Evidencia y límites
- **Nivel: C** (constructo teórico). Es un marco explicativo, no una ley predictiva: no da un número de elementos tolerable ni una fórmula. Varios efectos derivados sí están bien replicados en contextos instruccionales (nivel E2 dentro de ese dominio).
- **Efectos replicados en instrucción:** atención dividida (*split-attention*: separar en el espacio o en el tiempo información que debe integrarse aumenta la carga), redundancia, modalidad y ejemplo resuelto. Proceden de la literatura de la CLT; su traslado a interfaces es razonable pero no siempre se ha probado directamente.
- **Inversión por pericia** (Kalyuga, Ayres, Chandler & Sweller 2003): las ayudas que benefician a los novatos pueden perjudicar a los expertos porque se vuelven redundantes.
- **Revisión de la carga pertinente:** la suma de los tres tipos se ha cuestionado (de Jong 2010). Sweller (2010) propone definir la carga pertinente en términos de la intrínseca. La revisión de Sweller, van Merriënboer & Paas (2019) la define como los recursos de memoria de trabajo dedicados a la carga intrínseca (y no a la extrínseca) y abandona el supuesto de 1998: ya no se suma a la carga total, sino que *redistribuye* recursos de lo extrínseco a lo intrínseco; en la práctica, la carga que cuenta es intrínseca + extrínseca. La propia revisión sigue planteando aumentar el procesamiento pertinente una vez reducida la extrínseca, siempre que la carga total no supere la capacidad. En UX, conviene trabajar con la distinción intrínseca/extrínseca y no apoyarse en "aumentar la carga pertinente".
- **Medición débil:** las escalas subjetivas (Paas, NASA-TLX) son autoinformes; las medidas fisiológicas (pupilometría, EEG) o de doble tarea son indirectas. De Jong (2010) critica que la carga se mida poco y de forma inconsistente.
- **Transferencia a UX:** la teoría busca el aprendizaje; en UX el objetivo suele ser completar una tarea. La distinción intrínseca/extrínseca se traslada bien; la carga pertinente, mucho menos.
- **Malentendido: "menos carga siempre es mejor".** Corrección: una carga intrínseca alta es inevitable y a veces deseada (analizar, aprender). Lo que se reduce es la extrínseca, no el contenido sustantivo.
- **Malentendido: "simplificar = quitar".** Corrección: ocultar lo necesario no elimina la carga; la traslada a la memoria del usuario (T1, T11).

## Aplicación práctica
### Reglas
1. [E] Coloca juntos (en espacio y tiempo) los elementos que deben integrarse: etiqueta, ayuda y error junto al campo; leyenda junto a la serie (efecto de atención dividida, CLT).
2. [H] Elimina el desorden visual que no aporta a la tarea: enlaces redundantes, imágenes decorativas, tipografía sin función (Whitenton 2013).
3. [H] Apóyate en modelos mentales existentes: etiquetas y disposiciones convencionales en lugar de "creativas" (Whitenton 2013; SIS-01).
4. [H] Descarga trabajo en el sistema: calcular, recordar, rellenar, inferir, valores por defecto razonables (Whitenton 2013; SIS-03).
5. [E] Haz retirables las ayudas para novatos y ofrece atajos para expertos (inversión por pericia, Kalyuga et al. 2003).
6. [H] Secuencia la complejidad intrínseca: primero lo esencial, lo avanzado bajo demanda (divulgación progresiva).
7. [H] Una acción primaria clara por vista.
8. [H] No escondas para "limpiar" lo que el usuario necesita ver al decidir.

### Por contexto
| Contexto | Aplicación |
|---|---|
| Web/escritorio | Jerarquía visual clara, etiquetas estándar ("Enviar", "Contacto"), sin elementos decorativos que compitan por la atención. |
| Formularios | Ayuda y error en línea junto al campo; autocompletado y valores por defecto; no pedir lo que el sistema puede inferir. |
| Dashboards/datos | Rotulado directo de series en lugar de leyendas separadas; pocos KPI de primer nivel con detalle bajo demanda; misma escala para lo que se compara. |
| Navegación | Convenciones de plataforma y divulgación progresiva; categorías comprensibles a la primera. |
| Onboarding | Introducir conceptos de uno en uno, en el momento de uso; ayudas que se retiran al aprender. |
| Interfaces conversacionales/IA | Resultado primero, detalle desplegable, formato coherente; no mezclar razonamiento y respuesta; evitar respuestas que se desplazan fuera de vista sin resumen. |
| Voz | La información hablada es transitoria y obliga a retenerla en memoria de trabajo, lo que aumenta la carga extrínseca (efecto de información transitoria: Leahy & Sweller 2011, recogido en Sweller et al. 2019; compensan el ritmo controlado por la persona y la segmentación). Respuestas más breves que en texto y opción de repetir [H en la traducción a voz]. |
| Rendimiento | Las esperas obligan a sostener el objetivo en mente; responder rápido reduce carga (ACC-02). |

### Ejemplos
- **Bueno:** un checkout que muestra cada error junto a su campo, autocompleta la dirección y arrastra el resumen del pedido a cada paso. La persona solo piensa en decidir, no en buscar.
- **Incumple:** un formulario que lista todos los errores en un recuadro al principio de la página, con nombres de campo distintos de las etiquetas visibles. Obliga a leer, recordar, desplazarse y emparejar: pura carga extrínseca.
- **Incumple (minimalismo mal entendido):** una barra de herramientas solo con iconos sin etiqueta "para limpiar la interfaz"; la persona debe recordar qué hace cada uno.

## Anti-patrones
- Interfaces "limpias" que esconden lo necesario y trasladan la carga a la memoria.
- Separar información que debe integrarse (leyendas lejos de gráficos, instrucciones en otra pantalla).
- Carruseles automáticos, animaciones y contenido en movimiento que compiten con la tarea.
- Etiquetas creativas o jerga interna en lugar de términos convencionales.
- Ayudas obligatorias e imposibles de desactivar para usuarios expertos.
- Respuestas de IA largas y sin estructura.

## Ética y accesibilidad
- **Línea roja:** diseñar deliberadamente la sobrecarga para que la persona acepte la opción por defecto (avisos de privacidad o procesos de cancelación intencionadamente complejos). Es un patrón oscuro: explota el límite que esta ley describe.
- La sobrecarga afecta más a personas con TDAH, dislexia, lesiones cerebrales, demencia o ansiedad, a personas mayores y a quien usa una segunda lengua.
- WCAG 2.2: **2.2.2 Pausar, detener, ocultar** (contenido en movimiento); **2.2.1 Tiempo ajustable**; **3.3.2 Etiquetas o instrucciones**; **3.3.7 Entrada redundante**; **1.3.1 Información y relaciones** (que la estructura visual exista también en el código).
- W3C COGA (nota no normativa, 2021): 4.6.2 "Make short critical paths", 4.6.3 "Avoid too much content", 4.4.5 "Keep text succinct", 4.9.1 "Let users control when content moves or changes".

## Cómo auditarla
### Señales observables
Dudas largas antes de actuar, relecturas, errores al interpretar etiquetas, uso frecuente de la ayuda, abandono en pasos densos, comentarios del tipo "es mucho" o "me pierdo".
### Preguntas
- ¿Cada elemento de la pantalla aporta a la tarea?
- ¿Hay información que deba integrarse y está separada?
- ¿Las etiquetas siguen la convención del dominio y la plataforma?
- ¿Qué puede hacer el sistema por el usuario (calcular, recordar, rellenar)?
- ¿Las ayudas se pueden retirar cuando ya no hacen falta?
### Métricas
- Escala de esfuerzo mental de Paas (9 puntos) o NASA-TLX tras la tarea; SEQ (*Single Ease Question*).
- Tiempo en tarea, tasa de errores y de éxito.
- Inventario por vista: clasificar cada elemento como "esencial / apoyo / ruido".
- En laboratorio, tarea secundaria (doble tarea) como indicador indirecto.

## Relaciones
- Refuerza / se apoya en: MEM-02 Memoria de trabajo — es el recurso que la carga consume.
- Refuerza / se apoya en: MEM-03 Ley de Miller — estima (de forma histórica y revisada) la capacidad de ese recurso.
- Refuerza / se apoya en: MEM-04 Fragmentación — agrupar reduce el número de unidades y la carga.
- Refuerza / se apoya en: DEC-01 Ley de Hick y DEC-02 Sobrecarga de opciones — más opciones, más carga de decisión.
- Refuerza / se apoya en: SIS-01 Ley de Jakob y SIS-02 Modelo mental — las convenciones son esquemas que abaratan la carga.
- Refuerza / se apoya en: SIS-03 Ley de Tesler — la complejidad irreducible debe absorberla el sistema.
- Refuerza / se apoya en: ACC-02 Umbral de Doherty — las esperas añaden carga de mantenimiento.
- Refuerza / se apoya en: MOT-01 Flujo — la sobrecarga rompe el estado de flujo.
- Tensiona con: DEC-04 Efecto estética-usabilidad — lo decorativo mejora la percepción pero puede añadir carga extrínseca; decorar sin competir con el contenido.
- Tensiona con: SIS-04 Navaja de Occam — quitar puede trasladar carga a la memoria (T1, T11).
- Tensiona con: ACC-04 Paradoja del usuario activo — la gente no lee las ayudas que reducirían la carga intrínseca; ayuda en contexto (T14).
- Tensiona con: dividir en pasos — reduce carga por pantalla pero añade interacción (T5).
- Se confunde a menudo con: "complejidad visual" o "número de elementos" — la carga depende de la tarea y de la persona, no solo de cuántas cosas hay en pantalla.

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/cognitive-load/ — síntesis divulgativa (contiene un título erróneo para la obra de 1988; ver Origen).
- Primarias:
  - Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257–285. https://doi.org/10.1207/s15516709cog1202_4
  - Sweller, J. (1994). Cognitive load theory, learning difficulty, and instructional design. *Learning and Instruction*, 4(4), 295–312. https://doi.org/10.1016/0959-4752(94)90003-5 (metadatos verificados; es el título que Laws of UX atribuye a 1988)
  - Sweller, J., van Merriënboer, J. J. G. & Paas, F. (1998). Cognitive architecture and instructional design. *Educational Psychology Review*, 10(3), 251–296. https://doi.org/10.1023/A:1022193728205
  - Sweller, J. (2010). Element interactivity and intrinsic, extraneous, and germane cognitive load. *Educational Psychology Review*, 22(2), 123–138. https://doi.org/10.1007/s10648-010-9128-5 (resumen leído)
  - Sweller, J., van Merriënboer, J. J. G. & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review*, 31(2), 261–292. https://doi.org/10.1007/s10648-019-09465-5 (texto completo leído; acceso abierto CC BY)
  - Paas, F. (1992). *Journal of Educational Psychology*, 84(4), 429–434. https://doi.org/10.1037/0022-0663.84.4.429
  - Hart, S. G. & Staveland, L. E. (1988). Desarrollo del NASA-TLX. *Advances in Psychology*, 52, 139–183. https://doi.org/10.1016/S0166-4115(08)62386-9
  - Kalyuga, S., Ayres, P., Chandler, P. & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist*, 38(1), 23–31. https://doi.org/10.1207/S15326985EP3801_4
  - Mayer, R. E. & Moreno, R. (2003). Nine ways to reduce cognitive load in multimedia learning. *Educational Psychologist*, 38(1), 43–52. https://doi.org/10.1207/S15326985EP3801_6
  - Leahy, W. & Sweller, J. (2011). Cognitive load theory, modality of presentation and the transient information effect. *Applied Cognitive Psychology*, 25(6), 943–951. https://doi.org/10.1002/acp.1787 (metadatos verificados; contenido según Sweller et al. 2019)
  - de Jong, T. (2010). Cognitive load theory, educational research, and instructional design: some food for thought. *Instructional Science*, 38, 105–134. https://doi.org/10.1007/s11251-009-9110-0
- Secundarias consultadas:
  - Whitenton, K. (2013). Minimize Cognitive Load to Maximize Usability. NN/g. https://www.nngroup.com/articles/minimize-cognitive-load/
  - Halarewich, D. (2016). Reducing Cognitive Overload For A Better User Experience. Smashing Magazine. https://www.smashingmagazine.com/2016/09/reducing-cognitive-overload-for-a-better-user-experience/
  - W3C COGA, Making Content Usable. https://www.w3.org/TR/coga-usable/
  - Wikipedia, Cognitive load. https://en.wikipedia.org/wiki/Cognitive_load
