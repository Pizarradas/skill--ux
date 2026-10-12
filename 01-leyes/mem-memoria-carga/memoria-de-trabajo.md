---
id: MEM-02
nombre: Memoria de trabajo
nombre_en: Working Memory
alias: [memoria operativa, memoria a corto plazo, short-term memory, almacén a corto plazo, memoria primaria]
familia: MEM
evidencia: E2
etiquetas: [memoria, reconocimiento-vs-recuerdo, interferencia, memoria-externa, persistencia]
refuerza: [MEM-01, MEM-03, MEM-04, PER-06, SIS-01, SIS-02, ACC-02, SIS-03]
tensiona: [SIS-04]
tensiones: [T1, T5, T11]
fuente_laws_of_ux: https://lawsofux.com/working-memory/
---

# MEM-02 · Memoria de trabajo (*Working Memory*)

> La memoria de trabajo es el sistema de capacidad muy limitada que mantiene activa y manipula, durante segundos, la información necesaria para la tarea en curso. Lo que se sostiene en ella se pierde con facilidad por interferencia y por falta de ensayo.

**Idea clave para quien diseña:** pon la carga de memoria en el sistema, no en la persona: que vea lo que necesita en el momento en que lo necesita.

## Resumen operativo
- **Qué dice:** mantenemos activos muy pocos datos durante segundos, y se pierden con facilidad por interferencia o distracción.
- **Evidencia:** E2 — capacidad limitada e interferencia muy replicadas; las cifras (4–7 elementos, 20–30 s) dependen del material y del ensayo, y no son especificaciones.
- **Haz:** 1) reconocimiento antes que recuerdo: muestra opciones, valores y estados 2) arrastra los datos entre pasos; nada de transcribir 3) permite pegar y gestores de contraseñas (WCAG 3.3.7 y 3.3.8).
- **Evita:** pensar "si son menos de 7, cabe": dos datos se pierden si hay una interrupción entre verlos y usarlos.
- **Sospecha de esta ley cuando…:** la gente toma notas, hace capturas, alterna pestañas o vuelve atrás para releer.
- **Mide con:** tasa de error de transcripción; recuento por paso de datos que hay que recordar sin verlos (objetivo: cero).
- **Vecinas:** MEM-01 Carga cognitiva (refuerza) · MEM-04 Fragmentación (refuerza) · SIS-04 Navaja de Occam (tensiona, T1/T11)

## Origen
- El término lo introdujeron **Miller, Galanter & Pribram (1960)**, *Plans and the Structure of Behavior*, para un almacén temporal de información relevante para la acción (así lo afirman Oberauer et al. 2018 y Cowan 2010; libro no consultado: en archive.org solo está en préstamo restringido).
- **Atkinson & Shiffrin (1968)**, "Human memory: A proposed system and its control processes", *Psychology of Learning and Motivation*, 89–195 (DOI 10.1016/S0079-7421(08)60422-3): modelo multialmacén con un "almacén a corto plazo".
- **Baddeley & Hitch (1974)**, "Working memory", *Psychology of Learning and Motivation*, vol. 8, 47–89 (DOI 10.1016/S0079-7421(08)60452-1; el volumen consta en la lista de referencias de Cowan 2001, no en Crossref): modelo multicomponente con **ejecutivo central**, **bucle fonológico** y **agenda visoespacial**.
- **Baddeley (2000)**, *Trends in Cognitive Sciences*, 4(11), 417–423: añade el **buffer episódico**, que integra información en episodios y la conecta con la memoria a largo plazo. **Allen, Baddeley & Hitch (2026)**, *Trends in Cognitive Sciences*, lo rebautizan "*awareness buffer*" (búfer de conciencia) y lo sitúan en el centro del modelo (resumen leído).
- Olvido a corto plazo: **Peterson & Peterson (1959)** mostraron que, con el ensayo bloqueado por una tarea distractora (contar hacia atrás), el recuerdo de trigramas de consonantes cae con rapidez en unos 18 s; en este paradigma, el olvido suele ser pronunciado en los primeros 15–18 s y después se estabiliza. **Keppel & Underwood (1962)** observaron que en el primer ensayo apenas hay olvido, lo que apunta a la **interferencia proactiva** (lo aprendido antes estorba a lo nuevo) y no solo al paso del tiempo. (Ambos resultados, según Oberauer et al. 2018 y Cowan 2001; originales tras muro de pago.)
- Marco de referencia actual: **Oberauer et al. (2018)**, "Benchmarks for models of short-term and working memory", *Psychological Bulletin*, 144(9), 885–958 (texto leído, versión de autor en repositorio).

## Mecanismo
La información se mantiene activa gracias a la atención y al ensayo (repetir mentalmente un número). Cualquier cosa que desvíe la atención —una notificación, un cambio de pantalla, una tarea secundaria— degrada lo mantenido. Hay tres explicaciones que no se excluyen:
- **Decaimiento:** la huella se desvanece con el tiempo si no se refresca.
- **Interferencia:** información nueva o anterior compite con la que se intenta mantener; la evidencia de Keppel & Underwood indica que este factor pesa mucho.
- **Reparto de recursos en el tiempo** (*time-based resource sharing*): lo que importa es cuánto tiempo la atención está ocupada en otra cosa.

Para el diseño, la consecuencia es la misma: lo que el usuario tenga que sostener mentalmente compite con la tarea que intenta resolver. El **reconocimiento** es más fácil que el **recuerdo**, porque la interfaz aporta las claves de recuperación (heurística n.º 6 de Nielsen, *recognition rather than recall*). Cuando la memoria interna no basta, la gente recurre a la **memoria externa**: papel, pestañas, capturas, carritos, tablas comparativas (NN/g, Budiu 2018).

## Evidencia y límites
- **Nivel: E2** — que la capacidad es muy limitada, varía entre personas y se degrada con la interferencia está muy replicado; los valores concretos dependen del material, del ensayo y de la tarea.
- **La cifra de Laws of UX ("4–7 chunks que se desvanecen en 20–30 s") es una simplificación.** El rango 4–7 mezcla la estimación de Cowan (~4) con la de Miller (~7); los 20–30 s proceden de paradigmas con el ensayo bloqueado y no son una constante. Úsala como orden de magnitud, nunca como especificación.
- **Diferencias individuales:** la capacidad se correlaciona con la comprensión lectora y la inteligencia fluida; NN/g señala que aumenta con la educación y disminuye con la edad. El equipo de diseño suele tener más capacidad disponible y más familiaridad con el producto que su público (Budiu 2018).
- **Entrenamiento:** el entrenamiento de memoria de trabajo mejora la tarea entrenada, pero la transferencia a otras capacidades es discutida (metaanálisis en desacuerdo). No diseñes suponiendo que los usuarios "entrenarán" su memoria.
- **Malentendido: "mientras quepa en 7, vale".** Corrección: la carga real depende de la interferencia y del tiempo; incluso 2 o 3 datos se pierden si hay una distracción entre verlos y usarlos.
- **Malentendido: confundir memoria de trabajo con atención o con "lo que cabe en pantalla".** Corrección: lo que está visible no ocupa memoria de trabajo; lo que hay que recordar porque ya no se ve, sí.

## Aplicación práctica
### Reglas
1. [E] Prefiere reconocimiento a recuerdo: muestra opciones, valores y estados en lugar de pedir que se recuerden (NN/g, Budiu 2024).
2. [E] No pidas transcribir de una pantalla a otra; arrastra los datos entre pasos. Cada transcripción expone el dato a la interferencia.
3. [H] Repite el contexto clave en cada paso (qué se compra, total, destino), sobre todo en móvil.
4. [H] Coloca juntos los valores que se comparan, en la misma vista y escala.
5. [H] Distingue visualmente los enlaces visitados y ofrece migas de pan (Laws of UX; práctica asentada).
6. [E] No pidas un dato que ya se proporcionó (WCAG 2.2 SC 3.3.7).
7. [E] Permite pegar y usar gestores de contraseñas; ningún paso de autenticación debe depender de recordar o transcribir sin alternativa (WCAG 2.2 SC 3.3.8).
8. [H] Minimiza las interrupciones entre ver un dato y usarlo (notificaciones, cambios de contexto, esperas).

### Por contexto
| Contexto | Aplicación |
|---|---|
| Web/escritorio | Historial, "vistos recientemente", migas de pan, enlaces visitados diferenciados. |
| E-commerce | Tablas comparativas, carrito y lista de deseos persistentes, resumen de pedido visible (NN/g, Budiu 2018 y 2024). |
| Formularios | Autocompletar lo ya introducido; permitir pegar códigos; OTP con autocompletado; no bloquear el pegado. |
| Móvil/táctil | La pantalla pequeña obliga a recordar lo que quedó fuera; resúmenes fijos (*sticky*) en los procesos. |
| Dashboards/datos | Comparables en la misma vista; filtros activos siempre visibles. |
| Onboarding | Ayuda contextual en el momento de uso, no un tutorial inicial que haya que recordar (Budiu 2024). |
| Interfaces conversacionales/IA | Resúmenes de estado, artefactos persistentes, citas visibles, posibilidad de fijar decisiones; sugerencias de siguiente acción como botones o *chips*. |
| Voz | Nada permanece visible: pocas opciones por turno, opción de repetir, enviar por texto lo que haya que usar después. |

### Ejemplos
- **Bueno:** un comparador de seguros que fija las columnas de los productos elegidos y permite desplazarse por las características sin perder de vista qué columna es cuál.
- **Incumple:** una verificación en dos pasos que muestra un código en una app, obliga a cambiar a otra app para escribirlo y bloquea el pegado. Transcripción + interferencia + presión de tiempo.
- **Incumple:** un asistente de IA que, diez turnos después, da por hecho que el usuario recuerda qué opción eligió y no la muestra en ningún sitio.

## Anti-patrones
- Códigos que hay que leer en una pantalla y teclear en otra; campos con el pegado bloqueado.
- Tiempos de sesión agresivos que borran el progreso.
- Iconos sin etiqueta cuyo significado hay que recordar.
- Acordeones o pestañas que separan lo que se compara (T11).
- Mensajes de error que desaparecen antes de que se puedan corregir los campos.
- Pedir el mismo dato dos veces en un proceso.

## Ética y accesibilidad
- **Línea roja:** aprovechar el olvido para que la persona pierda de vista condiciones, costes o plazos que aceptó al principio de un proceso largo.
- Personas con discapacidades cognitivas o de aprendizaje, personas mayores y quien está con estrés o fatiga tienen menos capacidad disponible.
- WCAG 2.2: **3.3.7 Entrada redundante** (A); **3.3.8 Autenticación accesible (mínima)** (AA); **2.2.1 Tiempo ajustable** (A); **1.3.1 Información y relaciones** (A).
- W3C COGA (nota no normativa): objetivo 6 "Ensure processes do not rely on memory"; patrones 4.7.5 "Do not rely on users' calculations or memorizing information", 4.5.9 "Avoid data loss and timeouts", 4.8.7 "Provide reminders".

## Cómo auditarla
### Señales observables
Usuarios que toman notas, hacen capturas, alternan pestañas, vuelven atrás para releer, cometen errores de transcripción o abandonan en pasos con códigos.
### Preguntas
- ¿Qué debe recordar el usuario entre el paso N y el N+1?
- ¿Se pide algún dato dos veces?
- ¿Algún paso de autenticación depende de recordar o transcribir?
- En el momento de decidir, ¿ve toda la información que necesita?
- ¿Qué pasa si se interrumpe la tarea y se vuelve diez minutos después?
### Métricas
- Tasa de error de transcripción y tiempo por paso.
- Frecuencia de navegación hacia atrás y de cambio de pestaña (analítica o sesiones grabadas).
- NASA-TLX tras la tarea; en laboratorio, doble tarea.
- Inventario de "datos que hay que recordar sin verlos" por paso (objetivo: tender a cero).

## Relaciones
- Refuerza / se apoya en: MEM-01 Carga cognitiva — la carga es la demanda sobre este recurso.
- Refuerza / se apoya en: MEM-03 Ley de Miller — estimación histórica de su capacidad.
- Refuerza / se apoya en: MEM-04 Fragmentación — estrategia para meter más información por unidad.
- Refuerza / se apoya en: PER-06 Atención selectiva — mantener información exige atención; distraerla la degrada.
- Refuerza / se apoya en: SIS-01 Ley de Jakob y SIS-02 Modelo mental — lo convencional no hay que retenerlo.
- Refuerza / se apoya en: ACC-02 Umbral de Doherty — esperar aumenta el olvido y la interferencia.
- Refuerza / se apoya en: SIS-03 Ley de Tesler — trasladar la carga de memoria al sistema.
- Tensiona con: SIS-04 Navaja de Occam — esconder información para "limpiar" puede obligar a recordarla (T1, T11).
- Tensiona con: dividir en pasos — cada paso nuevo exige arrastrar datos o se pierden (T5).
- Se confunde a menudo con: memoria a corto plazo — esta enfatiza el almacenamiento; la memoria de trabajo, el mantenimiento *y* la manipulación.

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/working-memory/ — síntesis divulgativa (sus cifras son órdenes de magnitud).
- Primarias:
  - Atkinson, R. C. & Shiffrin, R. M. (1968). Human memory: A proposed system and its control processes. *Psychology of Learning and Motivation*, 89–195. https://doi.org/10.1016/S0079-7421(08)60422-3
  - Baddeley, A. D. & Hitch, G. (1974). Working memory. *Psychology of Learning and Motivation*, 47–89. https://doi.org/10.1016/S0079-7421(08)60452-1 (vol. 8)
  - Baddeley, A. (2000). The episodic buffer: a new component of working memory? *Trends in Cognitive Sciences*, 4(11), 417–423. https://doi.org/10.1016/S1364-6613(00)01538-2
  - Allen, R. J., Baddeley, A. D. & Hitch, G. J. (2026). Awareness as the heart of working memory. *Trends in Cognitive Sciences*. https://doi.org/10.1016/j.tics.2026.04.001 (resumen leído)
  - Peterson, L. R. & Peterson, M. J. (1959). Short-term retention of individual verbal items. *Journal of Experimental Psychology*, 58(3), 193–198. https://doi.org/10.1037/h0049234
  - Keppel, G. & Underwood, B. J. (1962). Proactive inhibition in short-term retention of single items. *Journal of Verbal Learning and Verbal Behavior*, 1(3), 153–161. https://doi.org/10.1016/S0022-5371(62)80023-1
  - Oberauer, K., Lewandowsky, S., Awh, E., Brown, G. D. A. et al. (2018). Benchmarks for models of short-term and working memory. *Psychological Bulletin*, 144(9), 885–958. https://doi.org/10.1037/bul0000153
  - Cowan, N. (2001). The magical number 4 in short-term memory. *Behavioral and Brain Sciences*, 24(1), 87–114. https://doi.org/10.1017/S0140525X01003922
  - Cowan, N. (2010). The magical mystery four. *Current Directions in Psychological Science*, 19(1), 51–57. https://doi.org/10.1177/0963721409359277
- Secundarias consultadas:
  - Budiu, R. (2018). Working Memory and External Memory. NN/g. https://www.nngroup.com/articles/working-memory-external-memory/
  - Budiu, R. (2024). Memory Recognition and Recall in User Interfaces. NN/g. https://www.nngroup.com/articles/recognition-and-recall/
  - W3C, Understanding SC 3.3.7 Redundant Entry. https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html
  - W3C, Understanding SC 3.3.8 Accessible Authentication (Minimum). https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html
  - W3C COGA, Making Content Usable. https://www.w3.org/TR/coga-usable/
  - Wikipedia, Working memory. https://en.wikipedia.org/wiki/Working_memory
