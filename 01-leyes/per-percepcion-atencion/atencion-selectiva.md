---
id: PER-06
nombre: Atención selectiva
nombre_en: Selective Attention
alias: [ceguera a los banners, banner blindness, ceguera al cambio, change blindness, ceguera por falta de atención, inattentional blindness, visión de túnel, efecto cóctel]
familia: PER
evidencia: E2
etiquetas: [atencion, banner-blindness, ceguera-al-cambio, feedback, notificaciones, saliencia]
refuerza: [MEM-01, MEM-02, ACC-02, PER-01, SIS-01, MOT-01, MOT-03]
tensiona: [PER-07, DEC-04, DEC-01, DEC-02, ACC-04]
tensiones: [T3, T10, T14]
fuente_laws_of_ux: https://lawsofux.com/selective-attention/
---

# PER-06 · Atención selectiva (*Selective Attention*)

> Solo procesamos a fondo una fracción de lo que tenemos delante, normalmente lo que sirve al objetivo del momento; el resto se atenúa o se descarta. Que algo esté en pantalla no significa que haya sido visto.

**Idea clave para quien diseña:** pon la respuesta del sistema donde ya está la mirada, y nunca disfraces lo importante de algo que la gente ha aprendido a ignorar.

## Resumen operativo
- **Qué dice:** solo procesamos a fondo una parte de lo visible, la que sirve al objetivo del momento; estar en pantalla no equivale a ser visto.
- **Evidencia:** E2 — ceguera por falta de atención, al cambio y a los banners muy replicadas; la magnitud depende de tarea, carga y semejanza (el 46 % del gorila no es una tasa universal).
- **Haz:** 1) muestra el feedback donde está la mirada (junto a la acción o al campo) 2) no des a contenido propio aspecto ni ubicación de anuncio 3) un cambio por actualización, señalado con una transición breve.
- **Evita:** "hacerlo más llamativo" para que se vea: lo llamativo y separado puede filtrarse como anuncio.
- **Sospecha de esta ley cuando…:** la gente repite una acción porque no vio la confirmación; un aviso clave "no existe" en las sesiones observadas.
- **Mide con:** tasa de detección (tarea + pregunta posterior) o fijaciones en eyetracking; tasa de acciones repetidas.
- **Vecinas:** ACC-02 Umbral de Doherty (refuerza) · PER-01 Ley de proximidad (refuerza) · PER-07 Efecto Von Restorff (tensiona, T3) · ACC-04 Paradoja del usuario activo (tensiona, T14)

## Origen

- **Cherry (1953)**, *JASA*, 25(5), 975–979, escucha dicótica y "problema del cóctel": quien repite el mensaje de un oído apenas puede decir nada del otro; el cambio de voz masculina a femenina y un tono puro se detectaban casi siempre, pero el paso del inglés al alemán pasaba inadvertido.
- **Broadbent (1958)**, *Perception and Communication*: modelo de filtro de selección temprana por rasgos físicos. Cuestionado por Moray (1959), que encontró que el propio nombre es casi lo único que atraviesa la barrera del canal ignorado (*QJEP*, 11(1), 56–60; la cifra divulgada de "un tercio" de participantes **no verificada: texto tras muro de pago**), y por Gray & Wedderburn (1960, *QJEP*, 12(3), 180–184).
- **Treisman (1960, *QJEP*, 12(4), 242–248; 1964, *American Journal of Psychology*, 77(2), 206 ss.)**: modelo de **atenuación**; el filtro eleva los umbrales de lo no atendido en vez de bloquearlo del todo (con pasajes intercambiados de oído, a veces se repetían una o dos palabras del oído "equivocado"). **Deutsch & Deutsch (1963)**, *Psychological Review*, 70(1), 80–90: selección tardía. **Kahneman (1973)**, *Attention and Effort*: atención como recurso limitado.
- **Lavie (1995)**, "Perceptual load as a necessary condition for selective attention", *JEP: HPP*, 21(3), 451–468: en tres estudios, los distractores solo interfirieron con carga perceptiva baja; con carga alta apenas se procesaron, aunque estuvieran claramente separados del objetivo. Murphy, Groeger & Greene (2016) matizan que la carga de **memoria de trabajo** aumenta la distracción.
- **Ceguera por falta de atención:** Simons, D. J. & Chabris, C. F. (1999). "Gorillas in our midst". *Perception*, 28, 1059–1074. doi:10.1068/p281059 **[verificada]**. Con 192 observadores, el 46 % no detectó el evento inesperado (54 % sí). Lo detectaron más con la tarea fácil (64 %) que con la difícil (45 %), más con el vídeo opaco (67 %) que con el superpuesto transparente (42 %), y más a la mujer del paraguas (65 %) que al gorila (44 %); el gorila se vio en el 58 % de los casos cuando se atendía al equipo de negro y en el 27 % cuando se atendía al de blanco.
- **Ceguera al cambio:** Rensink, O'Regan & Clark (1997), *Psychological Science*, 8, 368–373 **[verificada]** (paradigma de parpadeo: cambios grandes pasan inadvertidos si hay un blanco breve entre versiones; una pista verbal acelera la detección). Simons & Levin (1998), *Psychonomic Bulletin & Review*, 5(4), 644–649 **[verificada]**: solo la mitad de los peatones notó que su interlocutor había sido sustituido.
- **Ceguera a los banners:** Benway & Lane (1998), boletín *Internet Technical Group* (Rice University); versión en *Proceedings of the HFES 42nd Annual Meeting*, 42(5), 463–467 (Benway, 1998). Dan nombre al fenómeno: en un piloto (N = 6) los banners que llevaban al objetivo se encontraron el 58 % de las veces frente al 94 % de los enlaces de control; en un segundo experimento (72 estudiantes) solo 17 de 71 recordaban haber visto los banners de ayuda y solo el 20 % recordaba anuncio alguno. La ceguera afectó también a destacados de texto que no parecían anuncios, y ni la animación ni la agrupación por región común la redujeron. **Pernice (NN/g, 2018)**, eyetracking con 26 participantes (incluye observaciones en móvil) **[leída]**: el fenómeno se ha documentado durante tres décadas; en una página, de 132 fijaciones en el área de contenido solo 1 cayó en la columna derecha.

## Mecanismo

La capacidad de procesamiento consciente es limitada, así que la atención selecciona por dos vías: **de arriba abajo** (el objetivo de la tarea dirige dónde mirar) y **de abajo arriba** (lo saliente captura la mirada). Con la experiencia se forman filtros aprendidos: la gente descubre qué zonas y qué aspectos no le sirven (los anuncios) y deja de mirarlos, incluso de forma preventiva en otras páginas ("patata caliente", NN/g 2018).

Percibir un cambio exige atención focal en el objeto que cambia. Si el cambio no va acompañado de un transitorio visible —porque coincide con un *scroll*, una recarga, una transición o sucede lejos del foco— no se registra (Budiu, NN/g 2018). Con una tarea absorbente aparece la **visión de túnel**: se busca donde se espera encontrar y el resto no se escanea (Nielsen 2012).

## Evidencia y límites

- **Nivel: E2 (efecto robusto).** La ceguera al cambio y por falta de atención están ampliamente replicadas en laboratorio; la ceguera a los banners tiene datos de eyetracking (NN/g). La magnitud depende de tarea, carga y semejanza.
- **No es todo o nada:** lo no atendido se procesa parcialmente; el propio nombre o palabras relevantes pueden "colarse" (atenuación).
- **La carga modula el filtro** (Lavie), y la carga de memoria de trabajo puede empeorar la distracción.
- **La ceguera al cambio disminuye** con movimiento visible, cuando el cambio ocurre en el foco o cuando la persona lo espera.
- **Malentendidos:**
  1. "Hazlo más llamativo" no cura la ceguera a los banners; puede agravarla, porque lo llamativo parece anuncio.
  2. "Está en pantalla, luego lo han visto": falso.
  3. Tomar el ~50 % del gorila como tasa universal: depende de la tarea y de la semejanza.

## Aplicación práctica

### Reglas

1. [E, NN/g 2018] No coloques contenido propio importante en ubicaciones típicas de anuncio (banner superior, columna derecha) ni con su aspecto (rectángulo con fondo de color, texto dentro de imagen, animación); sepáralo visualmente de la publicidad.
2. [E, Rensink et al. 1997; Budiu 2018] Muestra el feedback donde está la atención: junto al campo, al botón pulsado o al elemento modificado, no en una barra lejana.
3. [H, Budiu 2018] Un cambio por actualización de pantalla cuando sea posible; si hay varios, agrúpalos en la misma región.
4. [H, Budiu 2018] Señala los cambios con una animación sutil y breve; evita animaciones simultáneas que compitan.
5. [H] Al abrir algo nuevo (búsqueda, panel), atenúa el resto para guiar la mirada.
6. [H] Tras un envío con errores, lleva el foco o la vista al primer error y ofrece un resumen.
7. [H] Mensajes de estado persistentes el tiempo suficiente y anunciados a tecnologías de apoyo.
8. [H] Limita estímulos que compiten (badges, chips, tooltips, banners): lo omnipresente se habitúa y se ignora.
9. [H] Valida con observación real; el *cognitive walkthrough* sobreestima lo visible porque quien diseña ya sabe dónde mirar (Nielsen 2012).

### Por contexto

| Contexto | Aplicación |
|---|---|
| Web/escritorio | Contenido clave fuera de zonas de anuncio; barras que aparecen al hacer *scroll* con contraste suficiente frente al contenido. |
| Móvil/táctil | Imágenes grandes o bloques muy distintos pueden tomarse por anuncios (NN/g 2018); los *toasts* inferiores compiten con teclado y pulgar. |
| Formularios | Error junto al campo + resumen; mover el foco al primer error; confirmación visible donde se pulsó. |
| Navegación | Si un clic altera un elemento lejano (icono que cambia de función), la persona no lo verá; acerca el efecto a la causa. |
| Dashboards/datos | Cambios en tiempo real con indicación transitoria (delta, destello suave) e histórico; alertas críticas que no dependan de mirar una esquina. |
| E-commerce | Cambios de precio o de disponibilidad durante el flujo, señalados explícitamente en el punto de decisión. |
| Onboarding | Ayuda en el momento de necesidad, descartable, sin tours que compitan con la tarea (T14). |
| Interfaces conversacionales/IA | Cuando el asistente edita código o documentos, mostrar diff o resaltado de cambios; en *streaming*, que lo ya leído no salte; avisos de incertidumbre, permisos o irreversibilidad en el flujo, no en un pie gris; pocas sugerencias/chips. |
| Voz | Lo importante al principio o al final del mensaje y con confirmación explícita; no se puede "mirar" de nuevo. |

### Ejemplos

- **Bueno:** al añadir al carrito, el contador del icono se actualiza con una breve animación **y** aparece una confirmación junto al botón pulsado.
- **Bueno:** un asistente de IA que reescribe un párrafo y marca en verde/rojo (con texto, no solo color) lo añadido y lo eliminado.
- **Lo incumple:** un aviso de "envío gratuito a partir de 50 €" en un rectángulo de color animado en la columna derecha: tiene todas las señales de anuncio y no se ve.

## Anti-patrones

- Contenido propio con estilo de anuncio, o pegado a anuncios.
- Mensajes de éxito/error en un lugar alejado de la acción o que desaparecen enseguida.
- Varias animaciones o cambios simultáneos en zonas distintas.
- Elementos fijos que tapan el foco o el contenido que se está editando.
- Inundar de *badges*, tooltips y *coach marks*.
- Asistentes que modifican contenido sin mostrar qué cambió.

## Ética y accesibilidad

- **Línea roja:** explotar la falta de atención: condiciones o cargos en zonas que se sabe que se ignoran, casillas premarcadas fuera del foco, cambios de precio sin señal, contenido patrocinado con estilo editorial para esquivar el filtro antianuncios, temporizadores o animaciones que desvían la mirada de los términos.
- **WCAG 4.1.3 Mensajes de estado (AA):** anunciar sin mover el foco (`role="status"`, `aria-live`).
- **WCAG 3.3.1 Identificación de errores (A)** y **3.3.3 Sugerencias ante errores (AA)**.
- **WCAG 3.2.2 Al recibir entradas (A):** sin cambios de contexto inesperados.
- **WCAG 2.4.11 Foco no oculto (mínimo) (AA, 2.2):** cabeceras o banners fijos no deben tapar el elemento con foco.
- **WCAG 2.2.2 Pausar, detener, ocultar (A):** el movimiento que compite por la atención debe poder pausarse.
- **Magnificadores:** quien amplía ve muy poco; lo que cambia fuera del área visible no existe para esa persona (Nielsen 2012).

## Cómo auditarla

### Señales observables
- Mapas de calor o eyetracking sin actividad en zonas con contenido clave.
- Personas que no ven una confirmación o un error y repiten la acción.
- Contenido propio con aspecto de anuncio; varias animaciones a la vez.
- Efectos de un clic que aparecen lejos de él.
- Ediciones de IA sin diff.

### Preguntas
- Tras cada acción, ¿dónde mira la persona y aparece ahí la respuesta del sistema?
- ¿Cuántas cosas cambian a la vez en pantalla?
- ¿Hay algo importante en ubicaciones o estilos asociados a publicidad?
- ¿Los cambios se anuncian a lectores de pantalla?

### Métricas
- Eyetracking: fijaciones sobre el elemento clave (proporción respecto a su área).
- Tarea + pregunta posterior ("¿viste el aviso de…?"): tasa de detección.
- Tasa de acciones repetidas (doble envío, doble clic) tras acciones con feedback.
- Tiempo hasta detectar un cambio o error en test moderado.
- Test de primera impresión: qué recuerda la persona de la página.

## Relaciones

- Refuerza / se apoya en: MEM-01 Carga cognitiva y MEM-02 Memoria de trabajo — mismos recursos limitados; la carga de memoria aumenta la distracción.
- Refuerza / se apoya en: ACC-02 Umbral de Doherty — feedback rápido y en el foco.
- Refuerza / se apoya en: PER-01 Ley de proximidad — feedback junto a la acción.
- Refuerza / se apoya en: SIS-01 Ley de Jakob — las ubicaciones aprendidas dirigen la mirada, para bien (convenciones) y para mal (zonas de anuncio).
- Refuerza / se apoya en: MOT-01 Flujo — atención absorbida equivale a visión de túnel.
- Refuerza / se apoya en: MOT-03 Efecto Zeigarnik — las tareas incompletas reclaman atención.
- Tensiona con: PER-07 Efecto Von Restorff — lo saliente capta la mirada, pero el exceso se habitúa o parece anuncio; T3.
- Tensiona con: DEC-04 Efecto estética-usabilidad — lo decorativo compite por la atención.
- Tensiona con: DEC-01 Ley de Hick y DEC-02 Sobrecarga de opciones — más estímulos implican más filtrado.
- Tensiona con: ACC-04 Paradoja del usuario activo — la ayuda contextual satura; T14. Interrupciones necesarias frente a inmersión: T10.
- Se confunde a menudo con: Von Restorff — Von Restorff es un efecto de **memoria** por distintividad; la atención selectiva es el **filtro** que decide qué se procesa (y puede descartar justo lo distinto).

## Fuentes

- Laws of UX (Jon Yablonski): https://lawsofux.com/selective-attention/ — síntesis divulgativa.
- Primarias:
  - Simons, D. J., & Chabris, C. F. (1999). Gorillas in our midst: Sustained inattentional blindness for dynamic events. *Perception*, 28, 1059–1074. doi:10.1068/p281059
  - Rensink, R. A., O'Regan, J. K., & Clark, J. J. (1997). To see or not to see: The need for attention to perceive changes in scenes. *Psychological Science*, 8, 368–373.
  - Simons, D. J., & Levin, D. T. (1998). Failure to detect changes to people during a real-world interaction. *Psychonomic Bulletin & Review*, 5(4), 644–649.
  - Rensink, R. A. (2002). Change detection. *Annual Review of Psychology*, 53, 245–277 (citada por NN/g).
  - Lavie, N. (1995). Perceptual load as a necessary condition for selective attention. *JEP: Human Perception and Performance*, 21(3), 451–468. doi:10.1037/0096-1523.21.3.451 (resumen).
  - Cherry, E. C. (1953). Some experiments on the recognition of speech, with one and with two ears. *Journal of the Acoustical Society of America*, 25(5), 975–979. doi:10.1121/1.1907229
  - Broadbent, D. E. (1958). *Perception and Communication*. Londres: Pergamon Press.
  - Moray, N. (1959). Attention in dichotic listening: Affective cues and the influence of instructions. *QJEP*, 11(1), 56–60. doi:10.1080/17470215908416289 (resumen).
  - Treisman, A. M. (1960). Contextual cues in selective listening. *QJEP*, 12(4), 242–248. doi:10.1080/17470216008416732 (resumen); Treisman, A. M. (1964). Verbal cues, language, and meaning in selective attention. *American Journal of Psychology*, 77(2), 206 ss.. doi:10.2307/1420127 (extracto).
  - Deutsch, J. A., & Deutsch, D. (1963). Attention: Some theoretical considerations. *Psychological Review*, 70(1), 80–90. doi:10.1037/h0039515 (metadatos).
  - Kahneman, D. (1973). *Attention and Effort*. Prentice-Hall; Mack, A., & Rock, I. (1998). *Inattentional Blindness*. MIT Press (metadatos).
  - Benway, J. P., & Lane, D. M. (1998). Banner blindness: Web searchers often miss "obvious" links. *Internet Technical Group Newsletter*, Rice University. https://www.ruf.rice.edu/~lane/papers/banner_blindness.pdf ; Benway, J. P. (1998). Banner blindness: The irony of attention grabbing on the World Wide Web. *Proceedings of the HFES Annual Meeting*, 42(5), 463–467. doi:10.1177/154193129804200504
- Secundarias consultadas:
  - https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/ (Pernice, 2018)
  - https://www.nngroup.com/articles/change-blindness-definition/ (Budiu, 2018)
  - https://www.nngroup.com/articles/tunnel-vision-and-selective-attention/ (Nielsen, 2012)
  - https://www.simplypsychology.org/attention-models.html
