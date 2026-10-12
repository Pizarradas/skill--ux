---
id: SIS-02
nombre: Modelo mental
nombre_en: Mental Model
alias: [modelo del usuario, user's model, modelo interno]
familia: SIS
evidencia: C
etiquetas: [modelos-mentales, prediccion, imagen-del-sistema, ia, confianza, explicabilidad]
refuerza: [SIS-01, MEM-01, MEM-02, MEM-04, ACC-04, PER-02, PER-03]
tensiona: [SIS-03, SIS-04, DEC-04, DEC-03]
tensiones: [T1, T2]
fuente_laws_of_ux: https://lawsofux.com/mental-model/
---

# SIS-02 · Modelo mental (*Mental Model*)

> Un modelo mental es la representación interna, simplificada y basada en creencias (no necesariamente en hechos) que una persona tiene de cómo funciona un sistema, y que usa para predecir el resultado de sus acciones, explicar lo que ve y decidir. La usabilidad depende de la distancia entre ese modelo y el comportamiento real del sistema.

**Idea clave para quien diseña:** la persona no ve tu arquitectura, ve una imagen del sistema; diseña esa imagen para que sus predicciones acierten.

## Resumen operativo
- **Qué dice:** cada persona actúa según una representación interna, simplificada y a menudo errónea, de cómo funciona el sistema; la usabilidad depende de la distancia entre ese modelo y el comportamiento real.
- **Evidencia:** C — constructo central en psicología cognitiva y HCI, sin parámetros predictivos; el matiz olvidado: a veces hay que **corregir** el modelo previo, no complacerlo.
- **Haz:** 1) escribe el modelo conceptual (objetos, relaciones, estados) y refléjalo igual en UI, ayuda y errores; 2) haz visibles los estados del sistema; 3) en IA, comunica capacidades, límites y dónde se equivoca, con un comportamiento de error estable.
- **Evita:** tomar personas o journey maps inventados por el equipo como si fueran el modelo mental de los usuarios.
- **Sospecha de esta ley cuando…:** en think-aloud se oye «pensaba que esto…»; hay errores repetidos en el mismo punto o sobreconfianza en la IA.
- **Mide con:** tarea de predicción (aciertos al anticipar la respuesta del sistema); confianza calibrada frente a exactitud de la IA.
- **Vecinas:** SIS-01 Ley de Jakob (refuerza) · MEM-02 Memoria de trabajo (refuerza) · SIS-03 Ley de Tesler (tensiona, T1) · SIS-04 Navaja de Occam (tensiona, T1)

## Origen

- **Kenneth Craik (1943), *The Nature of Explanation*, Cambridge University Press.** Propone que la mente lleva un modelo «a pequeña escala» de la realidad que ejecuta para anticipar acontecimientos (libro no leído: préstamo restringido en archive.org; descripción concordante con la síntesis revisada por pares de Jones et al. 2011).
- **Philip Johnson-Laird (1983), *Mental Models: Towards a Cognitive Science of Language, Inference, and Consciousness*** (Cambridge University Press / Harvard University Press): la mente construye réplicas internas de las relaciones entre objetos y sucesos, y razona manipulándolas (descripción del catálogo y Jones et al. 2011; libro no leído).
- **Gentner, D. & Stevens, A. L. (Eds.) (1983), *Mental Models*, Lawrence Erlbaum**, que incluye **Donald Norman, «Some observations on mental models»** (pp. 15–22 en la reimpresión de Psychology Press, 2014, DOI 10.4324/9781315802725-5; paginación de 1983 no verificada). Norman distingue sistema objetivo, modelo conceptual y modelo mental, y observa que los modelos mentales son incompletos, inestables, de límites difusos y con elementos «supersticiosos» (no verificado en el capítulo, que no es accesible en abierto).
- **Norman (1988), *The Psychology of Everyday Things*** (reeditado como *The Design of Everyday Things*, ed. revisada 2013): tríada **modelo de diseño – modelo del usuario – imagen del sistema**; quien diseña solo se comunica con la persona a través de la imagen del sistema.
- Síntesis moderna: Jones, Ross, Lynam, Perez & Leitch (2011), «Mental models: an interdisciplinary synthesis of theory and methods», *Ecology and Society*, 16(1), art. 46; y Chan (2024, revisado 2026), «Mental Models in User Experience Design», NN/g.

## Mecanismo

Antes de actuar, la persona **simula**: predice qué pasará si pulsa, escribe o espera. Si la predicción falla aparecen errores, sorpresa y pérdida de confianza. Los modelos son **individuales** (dependen de la experiencia previa), **fluidos** (cambian con el uso) y **pegajosos**: una creencia errónea puede contaminar toda una sesión (Chan 2024).

La **discordancia de modelo** es estructural: el equipo conoce su sistema en detalle y sobreestima su claridad (maldición del conocimiento), mientras que el modelo de la persona es más pobre. Hay dos palancas para cerrar la brecha: **adaptar el sistema** al modelo existente, o **mejorar el modelo** de la persona (etiquetas, explicaciones breves sobre conceptos clave, imagen del sistema más transparente). Cuando el modelo previo es incorrecto y peligroso, solo vale la segunda.

## Evidencia y límites

- **Nivel: C** — constructo teórico. Es central y longevo en psicología cognitiva y HCI, pero no es una ley con parámetros predictivos; lawsofux lo cataloga en «Psychology».
- **Evidencia de que importa:** en sistemas inteligentes, Kulesza et al. (CHI 2012, DOI 10.1145/2207676.2207678) encontraron que quienes más mejoraban la solidez de su modelo mental de un recomendador lograban personalizarlo mejor. Bansal et al. (2019, HCOMP, «Beyond Accuracy: The Role of Mental Models in Human-AI Team Performance», DOI 10.1609/hcomp.v7i1.5285) muestran que el rendimiento del equipo persona-IA depende de que la persona se forme un modelo del **límite de error** de la IA, y que límites de error **parsimoniosos** (simples) y **no estocásticos** (estables) facilitan formarse ese modelo (HCOMP 7, pp. 2–11; texto leído).
- **Crítica:** el término es **polisémico** (Jones et al. 2011): imágenes, reglas, analogías, redes causales. Los modelos elicitados son incompletos y contradictorios, y medirlos depende mucho del método (entrevista, dibujo, think-aloud, card sorting).
- **Malentendidos frecuentes:**
  - *«Las personas o los journey maps son el modelo mental.»* Son artefactos del equipo; solo valen si salen de investigación.
  - *«Hay que adaptarse siempre al modelo existente.»* A veces es erróneo y arriesgado (seguridad, privacidad, IA): hay que corregirlo, no complacerlo.
  - *«Un modelo por segmento.»* Hay variación dentro de cada segmento y el modelo cambia de novato a experto.
  - Confundir **modelo mental** (en la cabeza de la persona) con **modelo conceptual** (la explicación que el equipo quiere transmitir).

## Aplicación práctica

### Reglas

1. [H] Escribe el modelo conceptual del producto (objetos, relaciones, estados) y refléjalo igual en UI, ayuda y mensajes de error.
2. [E] Coloca el contenido donde la persona lo busca y valídalo con tree testing; evita varias cajas de búsqueda con alcances distintos en una misma página (NN/g documenta personas que buscan en la caja equivocada y concluyen que no existe la respuesta).
3. [H] El botón atrás se comporta como «deshacer navegación»: vuelve al estado visual inmediatamente anterior, también al cerrar capas superpuestas.
4. [H] Un patrón visual, un significado: no uses el mismo aspecto para un interruptor que aplica al instante y para una casilla que requiere «Guardar».
5. [H] Haz visibles los estados del sistema (sincronizado/pendiente, borrador/publicado).
6. [E] En productos con IA, comunica qué puede y qué no puede hacer el sistema desde el primer contacto, y **dónde se equivoca**; procura que el comportamiento de error sea estable y aprendible (Bansal et al. 2019; guía PAIR de Google, capítulo «Mental Models»).
7. [H] Calibra la «humanización»: la primera persona, el nombre propio y la emoción simulada inducen a atribuir intención, comprensión y memoria; ajústalas a las capacidades reales (PAIR).
8. [H] Tras cambiar de modelo o versión de IA, re-onboarding breve: el comportamiento cambió y el modelo de la persona quedó obsoleto.

### Por contexto

| Contexto | Aplicación |
|---|---|
| Navegación | Etiquetas y agrupaciones que reflejan cómo la persona clasifica, no el organigrama. |
| Formularios | Indicar si los cambios se guardan solos o con botón; estados de validación claros. |
| Dashboards/datos | Explicar qué mide cada indicador, de dónde salen los datos y cuándo se actualizaron. |
| E-commerce | Carrito, ficha y checkout siguen el modelo «yo controlo lo que compro»; nada se añade sin acción explícita. |
| Onboarding | Enseñar 2–3 conceptos clave del modelo, no cada botón. |
| Interfaces conversacionales/IA | Mostrar memoria y contexto (qué recuerda entre sesiones, qué fuentes usó), qué acciones puede ejecutar (sugerir frente a ejecutar), límites de conocimiento e incertidumbre. Desmontar las dos analogías erróneas típicas: «es un buscador» (no siempre hay fuentes verificables) y «es una persona» (no tiene intención ni memoria salvo que se indique). |
| Voz | Anunciar qué comandos o dominios entiende; sin pantalla, el modelo se forma solo con lo que el sistema dice. |
| Sistemas de diseño | Glosario de conceptos del producto y significado único por componente. |

### Ejemplos

- **Bueno:** un asistente de IA indica al empezar «puedo resumir y redactar a partir de tus documentos; no accedo a internet» y, en cada respuesta, enlaza los fragmentos usados; la gente aprende cuándo verificar.
- **Incumple:** un almacenamiento en la nube muestra igual los archivos locales y los que solo existen en el servidor; la persona borra la copia «local» creyendo conservar la remota.
- **Incumple:** una app infantil usa iconos de disquete y cinta; la metáfora no tiene referente para su público. (A la inversa, NN/g cita una app infantil donde metáforas de mapa y puertas sí ayudan a quien carece de modelos digitales.)

## Anti-patrones

- Automatización opaca: el sistema decide sin mostrar qué hizo ni por qué.
- Metáforas obsoletas o culturalmente locales tomadas como universales.
- Personas y journey maps inventados en lugar de investigados.
- Cambios de comportamiento silenciosos (incluidas actualizaciones de modelo de IA) sin aviso.
- IA que expresa la misma seguridad cuando acierta y cuando inventa.

## Ética y accesibilidad

- **Línea roja:** explotar modelos erróneos — una «X» que acepta en lugar de cerrar, una suscripción que parece compra única, una IA que aparenta certeza o comprensión que no tiene.
- **Accesibilidad:** quien usa lector de pantalla construye su modelo desde la estructura semántica (encabezados, regiones, orden de foco), no desde la disposición visual; si estructura y aspecto divergen, coexisten dos modelos incompatibles.
- Personas mayores o con discapacidad cognitiva toleran peor los cambios de modelo; los rediseños abruptos les penalizan más.
- **WCAG 2.2:** 1.3.1 Información y relaciones; 1.3.2 Secuencia significativa; 2.4.3 Orden del foco; 2.4.6 Encabezados y etiquetas; 3.2.2 Al recibir entradas; 3.3.2 Etiquetas o instrucciones; 4.1.2 Nombre, función, valor.

## Cómo auditarla

### Señales observables
- En think-aloud, la persona verbaliza predicciones incorrectas («pensaba que esto…»).
- Errores repetidos en el mismo punto; rodeos (workarounds).
- Términos de la persona ausentes en la UI.
- En IA: sobreconfianza (aceptar sin verificar) o infraconfianza (no usar la función).

### Preguntas
- ¿El modelo conceptual está escrito y la imagen del sistema lo refleja?
- ¿Qué productos condicionan el modelo previo de nuestro público?
- ¿Cuándo y cómo se comunican los límites y errores de la IA?
- ¿Estructura semántica y estructura visual cuentan la misma historia?

### Métricas
- **Tarea de predicción:** pedir a la persona que anticipe la respuesta o acción del sistema antes de verla; medir aciertos.
- **Confianza calibrada:** confianza alta en aciertos y baja en errores de la IA (correlación confianza–exactitud).
- Card sorting y tree testing; tickets tipo «pensaba que…»; tasa de deshacer tras acciones automáticas.

## Relaciones

- Refuerza / se apoya en: SIS-01 Ley de Jakob — aplicación directa: modelos aprendidos en otros productos.
- Refuerza: MEM-01 Carga cognitiva y MEM-02 Memoria de trabajo — un modelo correcto reduce lo que hay que retener y deducir.
- Refuerza: MEM-04 Fragmentación — los conceptos agrupados forman modelos más manejables.
- Refuerza: ACC-04 Paradoja del usuario activo — la gente actúa con su modelo sin leer instrucciones.
- Refuerza: PER-02 Semejanza y PER-03 Región común — agrupar visualmente lo que conceptualmente va junto refuerza el modelo.
- Tensiona con: SIS-03 Ley de Tesler y SIS-04 Navaja de Occam — ocultar complejidad puede dejar a la persona sin modelo de lo que ocurre (T1); absorber sí, pero con visibilidad y vía de corrección.
- Tensiona con: DEC-04 Estética-usabilidad — una interfaz atractiva puede ocultar un modelo erróneo y retrasar su detección.
- Tensiona con: DEC-03 Sesgo cognitivo — el sesgo de confirmación mantiene modelos erróneos.
- Se confunde a menudo con: modelo conceptual — el conceptual es la explicación del equipo; el mental, la creencia de la persona.

## Fuentes

- Laws of UX (Jon Yablonski): https://lawsofux.com/mental-model/ — síntesis divulgativa.
- Primarias:
  - Craik, K. J. W. (1943). *The Nature of Explanation*. Cambridge University Press. (libro no leído; vía Jones et al. 2011)
  - Johnson-Laird, P. N. (1983). *Mental Models: Towards a Cognitive Science of Language, Inference, and Consciousness*. Cambridge University Press / Harvard University Press. (libro no leído; metadatos verificados)
  - Norman, D. A. (1983). Some observations on mental models. En D. Gentner & A. L. Stevens (Eds.), *Mental Models* (viii + 348 pp.). Erlbaum. Reimpr. Psychology Press, 2014, pp. 15–22, DOI 10.4324/9781315802725-5. (capítulo no leído)
  - Norman, D. A. (1988/2013). *The Design of Everyday Things*.
  - Jones, N. A., Ross, H., Lynam, T., Perez, P. & Leitch, A. (2011). Mental models: an interdisciplinary synthesis of theory and methods. *Ecology and Society*, 16(1), 46. DOI 10.5751/ES-03802-160146 — https://www.ecologyandsociety.org/vol16/iss1/art46/
  - Kulesza, T. et al. (2012). CHI 2012. DOI 10.1145/2207676.2207678
  - Bansal, G., Nushi, B., Kamar, E., Lasecki, W. S., Weld, D. S. & Horvitz, E. (2019). Beyond Accuracy: The Role of Mental Models in Human-AI Team Performance. *Proceedings of HCOMP*, 7, 2–11. DOI 10.1609/hcomp.v7i1.5285 — https://ojs.aaai.org/index.php/HCOMP/article/view/5285
- Secundarias consultadas:
  - Chan, M. (2024). Mental Models in User Experience Design. https://www.nngroup.com/articles/mental-models/
  - Google PAIR, People + AI Guidebook, «Mental Models». https://pair.withgoogle.com/chapter/mental-models/
  - https://aura-lab.siue.edu/theories/mental-models/
