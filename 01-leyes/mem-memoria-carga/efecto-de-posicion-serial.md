---
id: MEM-05
nombre: Efecto de posición serial
nombre_en: Serial Position Effect
alias: [efecto de primacía, efecto de recencia, primacy effect, recency effect, curva de posición serial, curva en U]
familia: MEM
evidencia: E2
etiquetas: [memoria, orden, primacia, recencia, secuencia, voz]
refuerza: [MEM-02, PER-07, MOT-05, PER-06]
tensiona: [SIS-01, DEC-01, DEC-02, DEC-03]
tensiones: [T13]
fuente_laws_of_ux: https://lawsofux.com/serial-position-effect/
---

# MEM-05 · Efecto de posición serial (*Serial Position Effect*)

> Cuando se presenta una secuencia y después se pide recordarla, los primeros elementos (primacía) y los últimos (recencia) se recuerdan mejor que los intermedios. La forma de la curva depende de la longitud de la lista, del ritmo de presentación y, sobre todo, del tiempo y la distracción entre la presentación y el recuerdo.

**Idea clave para quien diseña:** úsalo cuando la información llega en secuencia y no se puede volver a ver (voz, vídeo, onboarding, mensajes largos); en listas y menús visibles manda el orden de escaneo, no la memoria.

## Resumen operativo
- **Qué dice:** al recordar una secuencia, los primeros y los últimos elementos se recuerdan mejor que los intermedios.
- **Evidencia:** E2 en recuerdo libre de listas en laboratorio; su traslado a interfaces es heurístico. Se olvida que la recencia desaparece con unos segundos de distracción.
- **Haz:** 1) lo esencial primero y una recapitulación o acción al final en lo secuencial (voz, vídeo, respuestas largas) 2) persiste lo que haya que usar después (texto, correo, copiable) 3) nunca pongas en medio información necesaria para decidir.
- **Evita:** justificar la colocación en menús visibles por "primacía/recencia": ahí manda el escaneo y la convención (T13).
- **Sospecha de esta ley cuando…:** la gente no recuerda una instrucción dada a mitad de una secuencia o pide repetir opciones en menús de voz.
- **Mide con:** prueba de recuerdo diferido cruzada con la posición de cada dato; tasa de "repetir" en menús de voz.
- **Vecinas:** PER-07 Efecto Von Restorff (refuerza) · MOT-05 Regla pico-final (refuerza) · SIS-01 Ley de Jakob (tensiona, T13)

## Origen
- **Ebbinghaus (1885)**, *Über das Gedächtnis* (trad. inglesa *Memory*, 1913): autoexperimentos con sílabas sin sentido que inauguran el estudio experimental de las listas seriales. Fuentes divulgativas le atribuyen el término "efecto de posición serial", pero no aparece en la traducción inglesa de 1913 (consultada en psychclassics.yorku.ca); no cites esa atribución.
- **Murdock (1962)**, "The serial position effect of free recall", *Journal of Experimental Psychology*, 64(5), 482–488 (DOI 10.1037/h0045106). Curva canónica en recuerdo libre inmediato, con primacía y recencia (Oberauer et al. 2018). Los detalles por longitud de lista (las posiciones iniciales y medias bajan con listas más largas; la recencia se mantiene) proceden de resúmenes secundarios (original tras muro de pago APA).
- **Glanzer & Cunitz (1966)**, "Two storage mechanisms in free recall", *JVLVB*, 5(4), 351–360 (DOI 10.1016/S0022-5371(66)80044-0). Una tarea distractora rellena al final de la lista (contar) **elimina la recencia** pero conserva la primacía (Oberauer et al. 2018; Cowan 2001); presentar más despacio mejora el recuerdo libre (Oberauer et al. 2018). Disociación clásica a favor de dos almacenes. (La duración de 30 s de la demora más larga figura en fuentes divulgativas; original tras muro de pago Elsevier.)
- **Rundus (1971)**, *Journal of Experimental Psychology*, 89(1), 63–77 (DOI 10.1037/h0031185): con ensayo en voz alta, los primeros ítems se repasan más, lo que explica la primacía.
- **Bjork & Whitten (1974)**, *Cognitive Psychology*, 6(2), 173–189 (DOI 10.1016/0010-0285(74)90009-7): existe **recencia a largo plazo** incluso con distractores entre ítems, lo que complica la explicación de dos almacenes y favorece la de distintividad temporal.
- Extensión a juicios: Asch (1946), "Forming impressions of personality", *Journal of Abnormal and Social Psychology*, 41(3), 258–290 (DOI 10.1037/h0055756): formación de impresiones según el orden de los rasgos (metadatos verificados; **no verificado** en el texto: tras muro de pago APA).

**Toda esta evidencia procede de listas de palabras o sílabas en laboratorio.** Su traslado a interfaces es una extrapolación.

## Mecanismo
- **Primacía:** los primeros ítems reciben más ensayo y atención, y pasan con más probabilidad a la memoria a largo plazo.
- **Recencia:** los últimos ítems siguen activos en la memoria de trabajo en el momento del recuerdo; desde modelos de almacén único se explica por su distintividad temporal o por su semejanza con el contexto de la prueba.
- **Intermedios:** sufren interferencia por ambos lados y reciben menos ensayo.

## Evidencia y límites
- **Nivel: E2** — uno de los hallazgos más replicados de la psicología de la memoria, **en recuerdo libre de listas en laboratorio**. Las recomendaciones de interfaz derivadas son **heurísticas [H]**, no resultados probados.
- **La recencia es frágil:** desaparece con unos segundos de distracción (Glanzer & Cunitz). En una interfaz real, entre ver una lista y "recordarla" suele haber interacción, así que la ventaja del final es poco fiable.
- **La primacía depende del ritmo:** presentar más despacio mejora el recuerdo libre (Glanzer & Cunitz 1966, según Oberauer et al. 2018); con presentación rápida hay menos ensayo de los primeros ítems (Rundus 1971).
- **En reconocimiento el efecto apenas aplica:** en un menú visible la persona no recuerda, ve. Lo que opera ahí es la atención y el patrón de escaneo (se mira primero el principio, a menudo arriba y a la izquierda), que es un fenómeno distinto, de lectura y no de memoria (los estudios de eye-tracking de NN/g muestran fijaciones concentradas arriba y a la izquierda: Pernice 2017).
- **Evidencia en interfaces:** tanto IxDF como Laws of UX ilustran el efecto con marcas conocidas (Apple, Nike, Electronic Arts) sin aportar datos de rendimiento. Son ejemplos, no pruebas.
- **Malentendido: "pon las acciones clave en los extremos de la navegación para que se memoricen".** Es una extrapolación no probada (la sugiere Laws of UX): la navegación persistente se reconoce, no se recuerda, y en móvil el último elemento de un menú horizontal puede quedar oculto por desbordamiento.
- **Cifra sin respaldo:** IxDF menciona que las pantallas deberían mostrar "menos de cinco elementos" sin citar fuente; no la uses.

## Aplicación práctica
### Reglas
1. [H] Aplícalo solo cuando la persona recibe información en secuencia y debe recordarla después sin poder volver a verla.
2. [H] Lo más importante, al principio (conclusión primero); una síntesis o llamada a la acción, al final; el detalle secundario, en medio.
3. [E] No confíes datos críticos a la recencia: cualquier distracción la borra. Haz persistente (texto, correo, copiable) lo que haya que usar después (Glanzer & Cunitz 1966).
4. [H] En listas visibles, ordena por relevancia de arriba abajo: el factor dominante es el escaneo.
5. [H] En navegación global, la convención de plataforma prevalece sobre la posición serial (T13).
6. [H] Nunca coloques en posiciones intermedias información que la persona necesita para decidir (costes, condiciones, cancelación).
7. [H] Si un elemento intermedio es importante, destácalo (PER-07) en lugar de depender de su posición.

### Por contexto
| Contexto | Aplicación |
|---|---|
| Voz | Opción más solicitada primero; "repetir opciones" al final; enviar por texto los datos que haya que usar después. |
| Interfaces conversacionales/IA | Conclusión inicial y recapitulación final con próximos pasos; códigos, fechas y decisiones en elementos persistentes y copiables. |
| Onboarding | Propuesta de valor en la primera pantalla y acción en la última; mejor aún, ayudas en contexto para no depender del recuerdo. |
| Web/escritorio (contenido) | Pirámide invertida: lo esencial arriba, resumen o CTA al cierre. |
| Navegación | Primera posición valiosa por escaneo; el final, para acciones con convención fuerte (perfil, carrito, ajustes) según SIS-01, no por recencia. |
| E-commerce | En presentaciones secuenciales (carruseles, *stories*) los extremos atraen más; en listados visibles, ordenar por relevancia. |
| Formularios | No aplica directamente: los errores van junto a cada campo, no en una lista final que haya que recordar al subir. |
| Móvil/táctil | Comprobar que el último elemento de menús horizontales no queda oculto por desbordamiento. |

### Ejemplos
- **Bueno:** un asistente de voz bancario que dice primero "Tu saldo es…", luego los movimientos y termina con "¿Quieres que te lo envíe por SMS?". Lo crítico está al principio y lo que hay que conservar se persiste.
- **Incumple:** un vídeo de onboarding de dos minutos que menciona a mitad de recorrido el único ajuste de privacidad importante, sin mostrarlo después en la interfaz.
- **Incumple (mal uso):** reordenar la barra de navegación para colocar "Suscribirse" en el extremo derecho "porque se recuerda mejor", rompiendo la convención de que ahí va la cuenta del usuario.

## Anti-patrones
- Enterrar en medio condiciones, costes o la opción de cancelar.
- Ordenar planes de precio para anclar en el primero y dejar el más conveniente para la persona en el centro, sin destacar.
- Menús de voz largos sin opción de repetir.
- Justificar la colocación en la navegación con "primacía/recencia" sin datos.
- Mostrar información crítica solo una vez, en una secuencia que no se puede revisar.

## Ética y accesibilidad
- **Línea roja:** usar la posición intermedia para ocultar información relevante para la decisión. Es un patrón oscuro (ver DEC-03 y `06-etica-accesibilidad/etica-y-patrones-oscuros.md`).
- En audio y lectores de pantalla la información es secuencial por naturaleza: ofrece resúmenes, encabezados navegables y opción de repetir.
- Las personas con memoria de trabajo reducida dependen más de la persistencia que del orden; en la enfermedad de Alzheimer se ha descrito una primacía significativamente reducida, con una recencia pequeña similar a la de los controles (Burkart, Heun & Benkert 1998).
- WCAG 2.2: **1.3.2 Secuencia significativa** (A); **2.4.6 Encabezados y etiquetas** (AA); **1.2.2 Subtítulos (grabados)** (A) y **1.2.3 Audiodescripción o alternativa** (A) para que el contenido secuencial sea revisable; **2.2.1 Tiempo ajustable** (A).

## Cómo auditarla
### Señales observables
Información crítica en posiciones intermedias de textos largos, *stories* o menús de voz; usuarios que no recuerdan una instrucción dada a mitad de una secuencia; usuarios que solo atienden al primer y último resultado.
### Preguntas
- ¿Hay información que la persona recibe en secuencia y debe recordar después sin poder volver a ella? ¿Dónde está?
- ¿Lo más importante está primero?
- ¿Hay algo crítico en el medio?
- ¿Alguna colocación se justifica con este efecto sin datos propios?
### Métricas
- Test de recuerdo diferido tras un onboarding o un mensaje de voz ("¿qué recuerdas?"), cruzado con la posición de cada dato.
- Tasa de "repetir" en menús de voz y de selección por posición.
- Pruebas A/B de orden en listas visibles (clics por posición), interpretadas como efecto de escaneo, no de memoria.

## Relaciones
- Refuerza / se apoya en: MEM-02 Memoria de trabajo — la recencia es lo que aún está activo en ella.
- Refuerza / se apoya en: PER-07 Efecto Von Restorff — destacar un ítem intermedio compensa su desventaja de posición.
- Refuerza / se apoya en: MOT-05 Regla pico-final — también pondera el final, aunque en experiencias, no en listas.
- Refuerza / se apoya en: PER-06 Atención selectiva — en listas visibles, el orden de escaneo es atencional.
- Tensiona con: SIS-01 Ley de Jakob — la convención de colocación prevalece en navegación global (T13).
- Tensiona con: DEC-01 Ley de Hick y DEC-02 Sobrecarga de opciones — en listas largas los intermedios se pierden aún más; acortar o agrupar.
- Tensiona con: DEC-03 Sesgo cognitivo — el efecto de orden puede explotarse de forma manipuladora.
- Se confunde a menudo con: el patrón de escaneo en listas visibles — es atención/lectura, no memoria.
- Se confunde a menudo con: el efecto de anclaje (DEC-03) — el anclaje sesga juicios numéricos por un valor inicial; la posición serial afecta al recuerdo.

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/serial-position-effect/ — síntesis divulgativa (sus recomendaciones de navegación son extrapolaciones).
- Primarias:
  - Murdock, B. B. (1962). The serial position effect of free recall. *Journal of Experimental Psychology*, 64(5), 482–488. https://doi.org/10.1037/h0045106
  - Glanzer, M. & Cunitz, A. R. (1966). Two storage mechanisms in free recall. *Journal of Verbal Learning and Verbal Behavior*, 5(4), 351–360. https://doi.org/10.1016/S0022-5371(66)80044-0
  - Rundus, D. (1971). Analysis of rehearsal processes in free recall. *Journal of Experimental Psychology*, 89(1), 63–77. https://doi.org/10.1037/h0031185
  - Bjork, R. A. & Whitten, W. B. (1974). Recency-sensitive retrieval processes in long-term free recall. *Cognitive Psychology*, 6(2), 173–189. https://doi.org/10.1016/0010-0285(74)90009-7
  - Ebbinghaus, H. (1885). *Über das Gedächtnis*. Trad. inglesa: *Memory: A contribution to experimental psychology* (1913). https://psychclassics.yorku.ca/Ebbinghaus/ (traducción consultada)
  - Asch, S. E. (1946). Forming impressions of personality. *Journal of Abnormal and Social Psychology*, 41(3), 258–290. https://doi.org/10.1037/h0055756 (texto no leído)
  - Burkart, M., Heun, R. & Benkert, O. (1998). Serial position effects in dementia of the Alzheimer type. *Dementia and Geriatric Cognitive Disorders*, 9(3), 130–136. https://doi.org/10.1159/000017036 (resumen leído)
  - Oberauer, K., Lewandowsky, S., Awh, E., Brown, G. D. A. et al. (2018). Benchmarks for models of short-term and working memory. *Psychological Bulletin*, 144(9), 885–958. https://doi.org/10.1037/bul0000153
  - Cowan, N. (2001). The magical number 4 in short-term memory. *Behavioral and Brain Sciences*, 24(1), 87–114. https://doi.org/10.1017/S0140525X01003922
- Secundarias consultadas:
  - Wikipedia, Serial-position effect. https://en.wikipedia.org/wiki/Serial-position_effect
  - IxDF, Serial Position Effect. https://ixdf.org/literature/topics/serial-position-effect
  - Pernice, K. (2017). F-Shaped Pattern of Reading on the Web: Misunderstood, But Still Relevant (Even on Mobile). NN/g. https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/
