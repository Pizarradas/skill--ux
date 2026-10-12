# Auditoría UX — FitPlus · Formulario de alta de socio
Fecha: 2026-10-12 · Alcance: formulario de alta completo (una sola pantalla, envío y salida) · Material analizado: código fuente `ejemplos/formulario-alta/formulario.html` (HTML, CSS y JS en línea). No se ha ejecutado en navegador ni hay datos de uso.

> Modo de trabajo: **H1 · Auditar** (`04-procesos/auditar.md`), con la lente de **H8 · Revisar código de UI** como apoyo, porque el material es código. Las referencias `L00` remiten a líneas de `formulario.html`.

## 1. Resumen ejecutivo

- El formulario **funciona en contra de la persona que se quiere dar de alta**. Tiene seis patrones oscuros: consentimientos y un seguro de pago ya marcados, una cuenta atrás falsa, *confirmshaming* y condiciones escondidas. La jerarquía de botones está invertida: lo grande y verde es "Borrar formulario" y el envío es un botón gris de unos 22 px. Además, la validación rechaza datos correctos sin decir por qué y borra lo que la persona escribió. Es muy probable que mucha gente abandone o pierda sus datos. El negocio, por su parte, se expone a quejas y a riesgo regulatorio (RGPD, DSA art. 25).
- **Los 3 cambios de mayor impacto** (esfuerzo bajo o medio; resuelven la mayor parte del problema):
  1. **Quitar los patrones oscuros.** Desmarcar las tres casillas, separar los consentimientos, eliminar la cuenta atrás y el enlace "No gracias, no me interesa cuidar mi salud", y mostrar precio, permanencia y renovación junto al plan (H1, H2, H4).
  2. **Arreglar los botones.** "Darme de alta" como única acción primaria, grande, junto al último campo. Eliminar "Borrar formulario" (H3).
  3. **Arreglar la entrada de datos y los errores.** Etiquetas visibles, formatos flexibles, reglas de contraseña a la vista, errores junto a cada campo sin borrar lo escrito, sin captcha aritmético, y estado de envío con confirmación final (H5, H6, H7, H8).

## 2. Contexto y supuestos

- **Personas usuarias:** público general que se da de alta en un gimnasio. Mayoría novata en este formulario, de uso **único** (no hay aprendizaje que amortice la fricción). La edad y la soltura digital son variadas (R7).
- **Tarea principal y métrica de éxito:** completar el alta con el plan deseado y los consentimientos que la persona elige de verdad. Métricas: tasa de finalización, tiempo hasta completar, errores por campo y, como contrapeso, quejas, bajas tempranas y revocación de consentimientos.
- **Dispositivo / modalidad:** *supuesto*: muchas altas desde **móvil** (enlace en redes o en el propio gimnasio), con dedo y teclado en pantalla. También escritorio.
- **Supuestos declarados:**
  - El servidor tarda de verdad entre 4 y 6 s (comentario en L128; en el código está simulado con `setTimeout`).
  - No hay ninguna oferta real que caduque en 5 minutos (el contador se reinicia: L108–110).
  - El requisito de presentar el DNI original y un justificante bancario en recepción es real.
- **Límites del análisis:**
  - Análisis estático del código. No se han medido tiempos reales, foco ni reflujo, ni se ha probado con lector de pantalla.
  - Los contrastes se han calculado a partir de los colores CSS.
  - No hay analítica: severidad y frecuencia son estimaciones de experto, con falsos positivos posibles (R10).

## 3. Hallazgos priorizados

Severidad 0–4 según `04-procesos/auditar.md` §Paso 3. Los problemas éticos y las barreras de accesibilidad bloqueantes valen 4 por defecto. Orden: severidad y, después, esfuerzo inverso. Los hallazgos con la misma causa raíz van agrupados.

| # | Severidad | Pantalla / elemento | Problema | Ley(es) | Esfuerzo |
|---|---|---|---|---|---|
| 1 | 4 Crítico | Casillas "Otros" (L87–91) | Marketing, cesión a terceros y seguro de pago **premarcados**; *confirmshaming* | DEC-03, PER-07 | Bajo |
| 2 | 4 Crítico | Cabecera, temporizador (L10–11, 34, 108–110) | Cuenta atrás **falsa** que se reinicia y parpadea sin fin | MOT-04 (mal uso), DEC-03, PER-07 | Bajo |
| 3 | 4 Crítico | Botones (L25–27, 93–96) | "Borrar formulario" primario; "enviar" diminuto, gris y de bajo contraste | PER-07, ACC-01 | Bajo |
| 4 | 4 Crítico | Plan y condiciones (L64–71) | Planes sin precio; permanencia y renovación automática en 10 px gris claro | PER-06, DEC-03, DEC-01 | Medio |
| 5 | 4 Crítico | Validación y errores (L38–39, 47, 49, 112–127) | Formatos rígidos, reglas ocultas, error genérico arriba que **borra** contraseñas y captcha | ACC-03, MEM-02, PER-06 | Medio |
| 6 | 4 Crítico | Todos los campos (L18–21, 41–77) | Placeholder como única etiqueta, sin estructura semántica, contrastes de 1,4–2,9:1 | MEM-02, PER-01 | Medio |
| 7 | 3 Alto | Verificación (L79–81, 120) | Captcha aritmético ("7 × 8 + 3") | MEM-02 | Bajo |
| 8 | 3 Alto | Envío (L128–133) | 5 s sin feedback; doble envío posible; final con `alert('OK')` y redirección sin confirmación | ACC-02, MOT-05 | Bajo |
| 9 | 3 Alto | Campos (L45–52, 58–61, 75–77, 84) | Campos innecesarios o deducibles; email y contraseña pedidos dos veces; país sin valor por defecto | SIS-04, SIS-03, MOT-04 | Bajo |
| 10 | 3 Alto | Columna derecha (L99–104) | Requisito crítico (DNI y justificante en 7 días) con aspecto de anuncio | PER-06 | Bajo |
| 11 | 3 Alto | Maquetación (L12–17) | Dos columnas de campos y `main` sin `flex-wrap`: en móvil, todo se comprime | PER-01, ACC-01 | Bajo |

### H1 · Consentimientos y seguro de pago premarcados, con *confirmshaming*
- **Observación:**
  - Tres casillas aparecen marcadas por defecto: "Quiero recibir ofertas de FitPlus y sus partners", "Acepto ceder mis datos a terceros con fines comerciales" y "Añadir seguro de lesiones (+4,99 €/mes)" (L87–89).
  - Debajo hay un enlace de 10 px que dice "No gracias, no me interesa cuidar mi salud" (L91).
  - Las casillas miden 12×12 px (L24). Están dentro de su `<label>`, así que el texto también es clicable.
- **Ley(es) y mecanismo:** **DEC-03 Sesgo cognitivo (*Cognitive Bias*)**: efecto por defecto y statu quo. Quien rellena con prisa (Sistema 1) tiende a dejar lo que ya está marcado. Así se cuela un cargo mensual y una cesión de datos que la persona no ha elegido de forma activa. El texto del enlace es *confirmshaming*: un encuadre que culpa a quien rechaza. *Evidencia: C (constructo); el efecto por defecto concreto está clasificado como robusto, A, en la ficha.* La **prueba de cuatro preguntas** (`06-etica-accesibilidad/etica-y-patrones-oscuros.md`) falla en interés, transparencia y reversibilidad.
- **Impacto:**
  - Cobros no deseados, spam y datos personales cedidos.
  - Cuando la persona lo descubre (en el extracto del banco), aparece un pico negativo que domina el recuerdo de la marca (MOT-05).
  - Riesgo legal: el RGPD exige un consentimiento libre e inequívoco, que no puede darse con casillas premarcadas (orientativo, no es asesoramiento legal).
- **Recomendación:**
  - Las tres casillas, **sin marcar**.
  - Separar marketing propio, cesión a terceros y seguro en tres decisiones independientes, cada una con una línea que explique qué implica.
  - Mostrar el seguro como **extra opcional** junto al resumen de precio, con el importe anual ("+4,99 €/mes · 59,88 €/año").
  - Eliminar el enlace de *confirmshaming*. Si hace falta una alternativa, el texto neutro "Sin seguro".
  - Área de toque de cada fila ≥ 24 px de alto (WCAG 2.5.8) y casilla nativa a tamaño estándar.
- **Cómo verificar:**
  - Tasa de alta del seguro y de los consentimientos antes y después. Bajará, y es lo esperable.
  - Métricas de contrapeso: devoluciones o cancelaciones del seguro en los primeros 30 días, quejas y solicitudes de baja de comunicaciones.
- **Tensiones / riesgos:** **T12 Valor por defecto ↔ Autonomía**. El default legítimo es el más privado y el que no cobra. Ingresará menos el seguro, pero con clientes que lo han elegido (menos devoluciones y menos reclamaciones).

### H2 · Cuenta atrás falsa y parpadeante
- **Observación:**
  - En la cabecera, una banda roja dice "¡OFERTA EXPIRA EN 05:00!" con la animación `blink` de 1 s en bucle infinito (L10–11, 34).
  - El script **reinicia el contador a 300 s** al llegar a cero y en cada visita (L108–110).
  - No se dice en ningún sitio qué oferta es.
- **Ley(es) y mecanismo:**
  - **DEC-03 Sesgo cognitivo** (escasez y urgencia): presión para decidir sin comparar. La ficha lo clasifica literalmente como línea roja ("contadores que se reinician"). *Evidencia: C.*
  - **MOT-04 Ley de Parkinson (*Parkinson's Law*)**: su ficha advierte que usarla para justificar urgencia artificial es un **mal uso**. La forma legítima de acortar una tarea es quitar trabajo, no meter prisa. *Evidencia: H.*
  - **PER-07 Efecto Von Restorff (*Von Restorff Effect*)**: el único elemento destacado y en movimiento de la página es el que no ayuda a la tarea, y le roba atención. *Evidencia: E2.*
- **Impacto:**
  - Prisa y errores al rellenar.
  - Desconfianza al recargar y ver que el contador vuelve a empezar.
  - Distracción constante para personas con TDAH o trastornos vestibulares.
- **Recomendación:**
  - **Eliminar el temporizador.** Si existe una promoción real, mostrar su fecha de fin verificable ("Matrícula gratis hasta el 31/10"), estática y sin parpadeo.
  - Cualquier animación debe respetar `prefers-reduced-motion`.
- **Cómo verificar:**
  - Prueba de recarga: ningún indicador de urgencia cambia sin un cambio real.
  - Pregunta posterior en el test ("¿Te sentiste presionado/a?").
  - Comparar la finalización y las quejas.
- **Tensiones / riesgos:** el equipo puede temer perder conversión. Medirlo con un test. Ningún resultado justifica mantener una urgencia falsa (R4). Accesibilidad: WCAG **2.2.2** Pausar, detener, ocultar (contenido que parpadea más de 5 s sin control) y **2.2.1** Tiempo ajustable.

### H3 · Jerarquía de acciones invertida: "Borrar formulario" domina y "enviar" casi no se ve
- **Observación:**

  | Botón | Estilo (L26–27) | Contraste |
  |---|---|---|
  | `reset` "Borrar formulario" | Verde, 16 px, padding 14×32 px | 2,99:1 |
  | `submit` "enviar" | Gris #ccc, texto #666 de 12 px, padding 4×10 px (unos 22 px de alto) | 3,58:1 (menos de 4,5:1) |

  - Están pegados (L93–96) y a 48 px del último bloque (L25).
  - "Borrar formulario" no pide confirmación.
- **Ley(es) y mecanismo:**
  - **PER-07 Efecto Von Restorff**: la persona busca "el botón destacado" para terminar y encuentra el que lo borra todo. *Evidencia: E2.*
  - **ACC-01 Ley de Fitts (*Fitts's Law*)**: el objetivo útil es pequeño y el destructivo, grande y contiguo. Así aumentan el tiempo y los errores al pulsar, sobre todo con el dedo. *Evidencia: E1.*
- **Impacto:** se borra el formulario entero por error (bloqueo y pico negativo); además, cuesta encontrar cómo enviar.
- **Recomendación:**
  - Un único botón primario, de ancho completo en móvil y al menos 44 px de alto: "Darme de alta".
  - Colocarlo justo debajo del último campo o del resumen del plan, con contraste ≥ 4,5:1 en el texto.
  - **Eliminar el botón de reset**: no tiene un caso de uso real en un alta (SIS-04). Si se mantuviera, debería ser secundario, estar separado y pedir confirmación.
- **Cómo verificar:**
  - Test con 5 personas: tiempo hasta localizar el envío y número de borrados accidentales.
  - En analítica, eventos `reset` seguidos de abandono (objetivo: 0).
- **Tensiones / riesgos:** ninguna relevante. Cumple WCAG **2.5.8** (≥ 24×24 px; recomendado 44 px, 2.5.5) y **1.4.3** (contraste).

### H4 · Precio, permanencia y renovación escondidos; elegir plan es adivinar
- **Observación:**
  - Un `<select>` con 9 planes ("Básico Mañanas 12m", "Plus 6m", "Premium Family 12m"…) **sin precio ni descripción** (L65–70).
  - Las condiciones ("Permanencia mínima según plan. Renovación automática.") aparecen en `.small`: 10 px, color #aaa, contraste 2,32:1 (L23, 71). Remiten a otra web.
  - Los encabezados de sección son grises claros (#999; 2,85:1).
- **Ley(es) y mecanismo:**
  - **PER-06 Atención selectiva (*Selective Attention*)**: lo diminuto y gris queda fuera del foco de la tarea, y la ficha lo considera línea roja si esconde costes o condiciones. *Evidencia: E2.*
  - **DEC-03 Sesgo cognitivo** (encuadre incompleto): se compromete una permanencia y una renovación sin verlas. *Evidencia: C.*
  - **DEC-01 Ley de Hick (*Hick's Law*)**: con alternativas desconocidas, la persona tiene que *leer* y comparar. El coste crece de forma lineal y, sin atributos comparables, ni siquiera puede decidir. *Evidencia: E1, aplicada con su matiz: aquí manda la búsqueda visual, no el log₂.*
- **Impacto:**
  - Abandono para ir a buscar precios fuera.
  - Elecciones equivocadas, y reclamaciones al descubrir la permanencia o la renovación (pico negativo; MOT-05).
- **Recomendación:**
  - Cambiar el `<select>` por **tarjetas o botones de radio agrupados**: primero el nivel (Básico Mañanas / Básico Total / Plus / Premium / Family), después la duración (6 o 12 meses).
  - En cada tarjeta: precio mensual, total, permanencia y renovación en texto legible (≥ 14–16 px, contraste ≥ 4,5:1).
  - Una tabla comparativa con los atributos homogéneos.
  - Si se recomienda un plan, que sea el que conviene a la persona, con la etiqueta "Más elegido" solo si es verdad (T3, T12).
- **Cómo verificar:**
  - Test: "elige el plan más barato para ir por las mañanas un año" (tasa de acierto y tiempo).
  - Tickets y reclamaciones por permanencia o renovación.
  - Bajas en el primer mes.
- **Tensiones / riesgos:** **T11 Fragmentar ↔ Ver el conjunto**: no esconder precios en acordeones, porque se comparan. **T1**: reducir opciones sin quitar planes necesarios (agrupar en dos decisiones en lugar de nueve opciones planas). WCAG **1.4.3**.

### H5 · La validación rechaza datos correctos, no explica nada y borra lo escrito
- **Observación:**
  - `novalidate` con validación solo al enviar (L38, 112–127).
  - El error es un único mensaje genérico arriba: "Hay errores en el formulario. Revise los datos." (L39). No indica qué campo falla ni cómo arreglarlo.
  - Al fallar, **vacía las contraseñas y el captcha** (L124–125).
  - El teléfono exige exactamente 9 dígitos (L47, 116): rechaza "612 34 56 78" y "+34…".
  - La fecha exige `DD/MM/AAAA` exacto (L49, 116).
  - La contraseña exige ≥ 10 caracteres, una mayúscula y un símbolo (L118–119), **pero esas reglas no aparecen en ninguna parte**.
  - Los campos marcados con * (nombre, apellidos, DNI, dirección, CP…) no se validan. En cambio, `pw2` ni se compara con `pw`.
  - Email y teléfono son `type="text"`, sin `inputmode` ni `autocomplete`.
- **Ley(es) y mecanismo:**
  - **ACC-03 Ley de Postel (*Postel's Law*)**: el sistema obliga a la persona a traducir su formato al formato interno, en vez de normalizarlo él. *Evidencia: H.*
  - **MEM-02 Memoria de trabajo (*Working Memory*)**: hay que recordar qué se escribió, adivinar reglas ocultas y volver a teclear lo que se borró. *Evidencia: E2.*
  - **PER-06 Atención selectiva**: el error aparece lejos del foco (arriba, mientras la persona está abajo, junto al botón), así que puede no verse. *Evidencia: E2.*
- **Impacto:** bucles de intento y error, frustración y abandono. Es probablemente el mayor punto de fuga tras los patrones oscuros, y un bloqueo para quien usa lector de pantalla (no sabe qué falla).
- **Recomendación:**
  - Validar **al salir de cada campo**, con el mensaje **junto al campo** que diga cómo corregirlo ("El teléfono debe tener 9 cifras; puedes usar espacios"). Al enviar con errores: resumen con enlaces a cada campo y foco en el primero.
  - **No borrar nada** de lo introducido.
  - Normalizar el teléfono (quitar espacios, guiones y prefijo +34) y la fecha (aceptar `1/2/1990`, `01-02-1990`), y **mostrar la interpretación** ("1 de febrero de 1990").
  - Reglas de contraseña visibles desde el principio, con indicador en vivo y botón "mostrar contraseña".
  - `type="email"`, `inputmode="tel"`, y `autocomplete` (`given-name`, `family-name`, `email`, `tel`, `bday`, `street-address`, `postal-code`, `new-password`).
  - Validación equivalente en el servidor.
- **Cómo verificar:**
  - Batería de entradas de la ficha ACC-03: teléfono `612 34 56 78`, `+34 612-345-678`; fecha `1/2/90`; email con espacio final. Registrar los rechazos.
  - Analítica de errores por campo y de abandono tras error.
  - axe o Lighthouse para `autocomplete`.
- **Tensiones / riesgos:** **T8 Postel ↔ precisión**: ser flexible en la forma pero explícito en el significado. Ante una fecha ambigua, mostrar cómo se ha interpretado. WCAG **3.3.1**, **3.3.2**, **3.3.3**, **1.3.5**, **4.1.3**.

### H6 · Campos sin etiqueta visible, sin estructura semántica y casi invisibles
- **Observación:**
  - Ningún `<input>`/`<select>` tiene `<label>`. La etiqueta es el placeholder, en #bbb (contraste 1,92:1; L19), que **desaparece al escribir**.
  - El borde de los campos es #ddd (1,36:1 frente a blanco; L18), así que los propios campos apenas se distinguen.
  - Las "secciones" son `<h2>` grises (2,85:1; L21), sin `fieldset`/`legend`.
  - Los formatos ("9 dígitos", "DD/MM/AAAA") solo aparecen en el placeholder (L47, L49).
  - El asterisco de obligatorio es rojo puro (#f00, 4,0:1) y no se explica.
- **Ley(es) y mecanismo:**
  - **MEM-02 Memoria de trabajo**: al escribir, la persona pierde la pista de qué campo es cuál y de qué formato se pedía. Al revisar, no puede reconocer, tiene que recordar. *Evidencia: E2.*
  - **PER-01 Ley de proximidad (*Law of Proximity*)**: el *gap* uniforme de 14 px dentro y entre campos, y los encabezados sin más aire antes que después, no dejan ver grupos. *Evidencia: E2.*
- **Impacto:** errores de campo (escribir el CP en la ciudad), imposibilidad de revisar y barrera para personas con baja visión o lector de pantalla.
- **Recomendación:**
  - `<label>` visible y persistente **encima** de cada campo, con el formato en un texto de ayuda enlazado mediante `aria-describedby`.
  - `fieldset` + `legend` para Datos personales, Dirección, Plan y Acceso.
  - Espaciado relacional: unos 8 px entre etiqueta y campo, ≥ 24 px entre campos y ≥ 40 px entre grupos.
  - Borde del campo con contraste ≥ 3:1; texto ≥ 4,5:1.
  - Marcar los opcionales con "(opcional)" en lugar de llenar todo de asteriscos.
- **Cómo verificar:**
  - axe/Lighthouse (sin errores de etiqueta ni de contraste).
  - Recorrido con NVDA o VoiceOver: cada campo se anuncia con su nombre y su ayuda.
  - En el test, tasa de datos en el campo equivocado.
- **Tensiones / riesgos:** el formulario crecerá en altura (más aire y etiquetas). Se compensa quitando campos (H9). WCAG **1.3.1**, **3.3.2**, **1.4.3**, **1.4.11**, **2.4.6**.

### H7 · Captcha aritmético
- **Observación:** "¿Cuánto es 7 × 8 + 3?", obligatorio (L79–81). Se valida contra la cadena `'59'` (L120) y se borra cuando cualquier otro campo falla (L125).
- **Ley(es) y mecanismo:** **MEM-02 Memoria de trabajo**: es una prueba de función cognitiva que exige sostener y operar cifras mentalmente, sin ninguna relación con la tarea. *Evidencia: E2.* Excluye de forma desproporcionada a personas con discalculia o con carga o estrés.
- **Impacto:** fricción para todo el mundo y bloqueo para una parte. Además, un acertijo con la respuesta fija en el JavaScript del cliente no protege de los bots.
- **Recomendación:** eliminarlo. Si hace falta protección antibots, usar medidas invisibles en el servidor (límite de frecuencia, campo trampa oculto a la tecnología de apoyo, verificación del email tras el alta).
- **Cómo verificar:** abandono en ese campo (antes) y volumen de altas fraudulentas tras retirarlo (vigilar 4 semanas).
- **Tensiones / riesgos:** posible aumento de spam, que se mitiga en el servidor sin trasladar la carga a la persona (SIS-03). El sistema relaciona este patrón con WCAG **3.3.8** (sin pruebas de función cognitiva) y con la guía COGA de no depender de la memoria ni del cálculo.

### H8 · Envío de 5 s a ciegas y final abrupto
- **Observación:**
  - Tras pulsar "enviar" hay una espera de 4–6 s **sin indicador**, y el botón sigue activo (L128–129).
  - Después llega un `alert('OK')`, se resetea el formulario y se redirige a `/` (L130–132).
  - No hay número de socio, resumen ni siguiente paso, aunque luego hay que ir a recepción con documentación en 7 días.
- **Ley(es) y mecanismo:**
  - **ACC-02 Umbral de Doherty (*Doherty Threshold*)**: sin eco inmediato (< 100 ms), la persona no sabe si el clic se registró, y es probable que vuelva a pulsar (doble alta o doble cobro) o que abandone. *Evidencia: E2. La cifra de ≈400 ms es una regla práctica derivada, no un resultado textual del folleto de IBM de 1982.*
  - **MOT-05 Regla pico-final (*Peak-End Rule*)**: el final del episodio decide el recuerdo, y aquí es un diálogo del sistema con "OK" seguido de un salto a otra página. *Evidencia: E2.*
- **Impacto:** envíos duplicados, incertidumbre ("¿me he dado de alta?") y llamadas o visitas de soporte.
- **Recomendación:**
  - Al pulsar: botón deshabilitado con el texto "Creando tu alta…" y `aria-busy`, más un mensaje de estado anunciado (`role="status"`).
  - Página de **confirmación** con número de socio, plan y precio contratados, y qué hacer ahora: "Trae tu DNI original y un justificante bancario a recepción antes del 19/10". Enviar lo mismo por email.
  - Sin ventas adicionales en ese momento.
- **Cómo verificar:**
  - Tasa de envíos duplicados (objetivo: 0).
  - Contactos a soporte del tipo "no sé si me registré".
  - Pregunta SEQ al final del test.
- **Tensiones / riesgos:** **T6**: no añadir esperas artificiales para aparentar trabajo; mostrar solo progreso real. WCAG **4.1.3**.

### H9 · Se piden datos innecesarios, deducibles o repetidos
- **Observación:**
  - Fax, Empresa y Cargo en la empresa (L48, L51–52).
  - Ciudad, Provincia y País además del código postal (L58–61). El país no trae España por defecto y aparece enterrada en mitad de la lista.
  - Email y contraseña se piden dos veces (L46, L76).
  - "¿Cómo nos conoció?", cuya opción por defecto es la propia pregunta y se enviaría como respuesta (L84).
- **Ley(es) y mecanismo:**
  - **SIS-04 Navaja de Occam (*Occam's Razor*)**: cada campo sin función compite por la atención y alarga la tarea. *Evidencia: H.*
  - **SIS-03 Ley de Tesler (*Tesler's Law*)**: lo deducible (ciudad y provincia a partir del CP, país por defecto) lo está cargando la persona en vez del sistema. *Evidencia: H.*
  - **MOT-04 Ley de Parkinson**: en su uso legítimo, acortar quitando trabajo. *Evidencia: H.*
- **Impacto:** más tiempo y más puntos de error en móvil. Los datos laborales despiertan desconfianza ("¿para qué quieren mi empresa?").
- **Recomendación:**
  - Eliminar Fax, Empresa y Cargo (o pedir Empresa solo si existe un convenio corporativo, con una casilla "Tengo descuento de empresa").
  - Deducir ciudad y provincia del CP (editables).
  - País con España por defecto y búsqueda.
  - Quitar "Repita el email" y "Repita contraseña", y usar en su lugar "mostrar contraseña" y la confirmación del email por enlace.
  - "Cómo nos conoció": opcional, sin valor falso, o mejor fuera del alta.
- **Cómo verificar:**
  - Número de campos (de 22 controles a unos 12).
  - Tiempo mediano hasta completar.
  - Errores de tipeo en el email (rebotes del email de confirmación).
- **Tensiones / riesgos:** **T1**: antes de quitar, preguntar "¿quién lo hará ahora?". El sistema (CP→ciudad) y el email de verificación absorben lo que se quita. WCAG **3.3.7** (no pedir de nuevo un dato ya dado).

### H10 · Un requisito imprescindible presentado como anuncio
- **Observación:** la condición para activar el alta ("presentar tu DNI original y un justificante bancario en recepción en los 7 días siguientes") está en la columna derecha, en una caja con degradado amarillo-naranja, borde rojo discontinuo y "¡IMPORTANTE!" (L15–16, 99–104).
- **Ley(es) y mecanismo:** **PER-06 Atención selectiva**: columna lateral más rectángulo de color chillón son las señales típicas de anuncio, y la gente ha aprendido a no mirarlas. En el estudio de NN/g (Pernice 2018) que cita la ficha, la columna derecha recibió 1 de 132 fijaciones. *Evidencia: E2.*
- **Impacto:** personas que creen estar dadas de alta y no lo están. Es una sorpresa negativa tardía (MOT-05).
- **Recomendación:**
  - Contar el requisito **antes de empezar** ("Para completar el alta necesitarás venir con tu DNI y un justificante bancario en 7 días"), en el flujo y con estilo de contenido normal.
  - Repetirlo en la confirmación (H8) y en el email.
  - Valorar si el sistema puede absorber esa verificación (subir el documento, domiciliación online: SIS-03).
- **Cómo verificar:** porcentaje de altas que caducan por no presentar la documentación, y pregunta de comprensión en el test ("¿Qué tienes que hacer después?").
- **Tensiones / riesgos:** ninguna. Evitar sustituir un anuncio por otro elemento llamativo (T3).

### H11 · Maquetación que no se adapta al móvil y rompe el recorrido
- **Observación:**
  - `.grid` en dos columnas fijas (L17) intercala campos no relacionados en zigzag (Teléfono | Fax, Fecha | DNI).
  - `main` es `display:flex` **sin `flex-wrap`** ni *media queries* (L12): en un móvil de 360 px, el formulario (flex 3) y el aviso (flex 1) comparten el ancho. Cada campo queda en unos 120 px de ancho y unos 25 px de alto (padding 6 px, fuente 13 px).
- **Ley(es) y mecanismo:**
  - **PER-01 Ley de proximidad**: en dos columnas, el ojo no sabe si se lee por filas o por columnas, y agrupa lo que no va junto. *Evidencia: E2.*
  - **ACC-01 Ley de Fitts**: los objetivos estrechos y bajos se fallan más con el dedo. *Evidencia: E1.*
- **Impacto:** campos saltados u olvidados, errores de toque y zoom manual constante en el dispositivo que probablemente más se usa (supuesto).
- **Recomendación:**
  - **Una sola columna** para el formulario lineal; como mucho, agrupar en la misma fila pares indivisibles (CP + ciudad) en escritorio.
  - `flex-wrap` o *media query* para que el contenido lateral pase debajo (o integrarlo, ver H10).
  - Campos de ≥ 44 px de alto y fuente ≥ 16 px (además evita el zoom automático de iOS).
- **Cómo verificar:** revisión a 320 px de ancho y con zoom al 200 %, y test en un móvil real (tasa de campos omitidos y errores de toque).
- **Tensiones / riesgos:** **T5**: no partir en muchos pasos. Una sola pantalla bien agrupada basta para unos 12 campos tras H9. WCAG **1.4.10** (reflujo), **2.5.8**.

## 4. Lo que funciona bien (conservar)
- `lang="es"` y `meta viewport` declarados: la base para el lector de pantalla y el móvil existe — SIS-01 (convenciones de plataforma).
- La casilla de **privacidad no está premarcada** (L86). Es el patrón correcto, que hay que extender al resto — DEC-03.
- Las casillas están **dentro de su `<label>`**, así que el texto entero es clicable — ACC-01.
- La intención de **agrupar por temas** (Datos, Dirección, Plan, Acceso) es correcta. Falta materializarla visual y semánticamente — PER-01, PER-03, MEM-04.
- Formulario en **una sola pantalla**: para un alta corta, bien agrupada, es la opción adecuada — T5.

## 5. Ética y accesibilidad
- **Patrones oscuros detectados (6):**
  1. Casillas premarcadas de marketing y de cesión a terceros (L87–88).
  2. Extra de pago premarcado: seguro +4,99 €/mes (L89). Es *sneak into basket*.
  3. Urgencia falsa: cuenta atrás que se reinicia (L108–110).
  4. *Confirmshaming* (L91).
  5. Condiciones escondidas: permanencia y renovación automática en 10 px gris (L71).
  6. Interferencia visual: la acción contraria al interés de la persona (borrar) destaca y la acción que busca (enviar) se esconde (L26–27).

  Todos fallan la prueba de cuatro preguntas. Marco normativo orientativo: RGPD (consentimiento), DSA art. 25 y la directiva de prácticas comerciales desleales.
- **Barreras de accesibilidad (WCAG 2.2):**

  | Criterio | Dónde falla |
  |---|---|
  | 1.3.1 Información y relaciones | Sin `label` ni `fieldset` |
  | 3.3.2 Etiquetas o instrucciones | Placeholder como etiqueta; reglas de contraseña ocultas |
  | 1.4.3 Contraste mínimo | Placeholder 1,92:1; `h2` 2,85:1; `.small` 2,32:1; texto de "enviar" 3,58:1; "Borrar formulario" 2,99:1 |
  | 1.4.11 Contraste no textual | Borde de los campos 1,36:1 |
  | 1.3.5 Identificar el propósito de la entrada | Sin `autocomplete` |
  | 3.3.1 Identificación de errores / 3.3.3 Sugerencias ante errores | Mensaje genérico arriba |
  | 4.1.3 Mensajes de estado | Espera de 5 s sin anuncio; error que no se anuncia |
  | 2.2.2 Pausar, detener, ocultar | Parpadeo infinito |
  | 2.2.1 Tiempo ajustable | Temporizador |
  | 2.5.8 Tamaño del objetivo | Botón "enviar" de unos 22 px de alto |
  | 1.4.10 Reflujo | Sin adaptación a 320 px |
  | 3.3.7 Entrada redundante | Email y contraseña repetidos |
  | 3.3.8 (prueba de función cognitiva) | Captcha aritmético |

## 6. Plan de validación

| Hipótesis | Método | Métrica | Umbral |
|---|---|---|---|
| Con los cambios 1–3 del resumen, más personas completan el alta sin ayuda | Test moderado con 5–6 personas en móvil (versión actual frente a la corregida), tarea "date de alta en el plan que te convenga" | Tasa de éxito sin ayuda; tiempo mediano; errores por campo | Éxito ≥ 5/6 en la versión nueva; tiempo −30 % orientativo |
| Las personas entienden qué contratan | Preguntas de comprensión tras el test ("¿Cuánto pagarás al mes? ¿Tiene permanencia? ¿Qué te falta hacer?") | Respuestas correctas | 100 % en precio y permanencia |
| Quitar los patrones oscuros no hunde el negocio y reduce el arrepentimiento | Despliegue con seguimiento de 8 semanas (o A/B si el tráfico lo permite) | Finalización; contratación del seguro; cancelaciones del seguro en 30 días; quejas; bajas en el primer mes | Finalización ≥ actual; cancelación temprana y quejas a la baja |
| La validación flexible elimina rechazos injustos | Batería de entradas de ACC-03 y analítica de errores por campo | Rechazos de entradas válidas; abandono tras error | 0 rechazos de formatos válidos |
| El formulario es accesible | axe/Lighthouse + recorrido con NVDA/VoiceOver + revisión a 320 px y zoom al 200 % | Incidencias WCAG A/AA | 0 bloqueantes |

## 7. Anexo: cobertura por familia
PER ☑ (H3, H4, H6, H10, H11) · MEM ☑ (H5, H6, H7) · DEC ☑ (H1, H2, H4) · ACC ☑ (H3, H5, H8, H11) · MOT ☑ (H2, H8, H9) · SIS ☑ (H9, H10)

**Comprobación con `05-checklists/checklist-auditoria.md`** (red de seguridad tras el recorrido):

| Resultado | Puntos |
|---|---|
| ✘ | C-05, C-06, C-10, C-12, C-15, C-16, C-17, C-18, C-20, C-21, C-23, C-31, C-32, C-33, C-34, C-40, C-41, C-42, C-43, C-44, C-45, C-53, C-54, C-60, C-61, C-62, C-63, C-64, C-65, C-66 |
| ✔ | C-04, salvo las reglas ocultas de contraseña |
| N/A | C-08, C-13, C-50 (una sola pantalla, sin pasos) |

C-61 queda sin verificar: no se ve el proceso de baja. Se marca ✘ preventivamente por "Renovación automática" sin información de baja.

---

## Anexo · Traza de uso del sistema

Archivos leídos, en orden, y paso del proceso en que se usó cada uno. Antes de leer, se listó la estructura de la carpeta `ux-skill/` (sin abrir archivos) para localizar las rutas.

| # | Archivo | Capa / paso | Uso |
|---|---|---|---|
| 1 | `AGENTS.md` | Capa 0 · Arranque | Rol, carga progresiva, elección de la habilidad **H1 Auditar** (disparadores "audita", "qué falla"), reglas R1–R10, formato mínimo de salida |
| 2 | `00-indice/mapa-global.md` | Capa 0 · Paso 1 | Ciclo SIS→PER→MEM→DEC→ACC→MOT para recorrer el formulario; tabla §6 ("Abandonan formularios", "Datos introducidos con errores") para preseleccionar leyes; tensiones T1–T10 |
| 3 | `ejemplos/formulario-alta/formulario.html` | Objeto auditado · Pasos 0–2 | Material analizado: observaciones con número de línea (no es un archivo de conocimiento del sistema) |
| 4 | `04-procesos/auditar.md` | Capa 4 · Proceso H1 | Pasos 0 (encuadre), 1 (recorrido), 2 (registro), 3 (severidad 0–4; ética y accesibilidad = 4), 4 (Pareto), 5 (tensiones), 6 (entrega); límites honestos |
| 5 | `03-aplicacion/formularios.md` | Capa 2 · Pasos 1–2 | Reglas F1–F15 y antipatrones de formularios como lente específica del contexto; métricas |
| 6 | `07-plantillas/informe-auditoria.md` | Capa 4 · Paso 6 | Estructura de este informe (secciones 1–7) |
| 7 | `00-indice/indice-leyes.md` | Capa 1 · Paso 2 | Ids estables, nombres en inglés y nivel de evidencia de cada ley citada |
| 8 | `06-etica-accesibilidad/etica-y-patrones-oscuros.md` | Transversal · Pasos 2–3 | Prueba de cuatro preguntas; tabla de uso legítimo / línea roja para clasificar H1, H2, H4 y H3 como patrones oscuros (severidad 4) |
| 9 | `06-etica-accesibilidad/accesibilidad.md` | Transversal · Pasos 2–3 | Correspondencia ley ↔ criterio WCAG 2.2 de cada hallazgo; regla del segundo canal |
| 10 | `04-procesos/revisar-codigo-ui.md` | Capa 4 · Lente H8 en Paso 1 | Señales en código (`await` sin estado, `pattern` rígidos, placeholder como etiqueta, botones pequeños, animaciones sin `prefers-reduced-motion`); formato `archivo:línea` |
| 11 | `02-relaciones/tensiones.md` | Capa 3 · Paso 5 | T1, T3, T5, T6, T8, T11 y T12 en el apartado "Tensiones / riesgos" de cada hallazgo |
| 12 | `05-checklists/checklist-auditoria.md` | Capa 4 · Tras el Paso 1 | Red de seguridad: resultado en la sección 7 |
| 13 | `00-indice/niveles-de-evidencia.md` | R2 · Paso 2 | Cómo declarar E1/E2/C/H sin convertirlos en cifras duras |
| 14 | `01-leyes/dec-decision-juicio/sesgo-cognitivo.md` (DEC-03) | Capa 3 · Paso 2 | H1, H2, H4: efecto por defecto, escasez, encuadre, *confirmshaming*; contexto "Formularios". Primer intento de lectura conjunta por terminal (con otras tres fichas) truncado; releída completa con el lector |
| 15 | `01-leyes/mot-motivacion-tiempo/ley-de-parkinson.md` (MOT-04) | Capa 3 · Paso 2 | H2 (urgencia como mal uso), H9 (`autocomplete`, no repetir datos) |
| 16 | `01-leyes/acc-accion-interaccion/ley-de-postel.md` (ACC-03) | Capa 3 · Paso 2 | H5: normalización, mostrar la interpretación, batería de entradas de prueba (líneas 1–110) |
| 17 | `01-leyes/mem-memoria-carga/memoria-de-trabajo.md` (MEM-02) | Capa 3 · Paso 2 | H5, H6, H7: reconocimiento frente a recuerdo, 3.3.7/3.3.8, COGA (líneas 1–110) |
| 18 | `01-leyes/acc-accion-interaccion/ley-de-fitts.md` (ACC-01) | Capa 3 · Paso 2 | H3, H11: tamaños de objetivo, separar lo destructivo, botón junto al último campo (líneas 1–110) |
| 19 | `01-leyes/per-percepcion-atencion/efecto-von-restorff.md` (PER-07) | Capa 3 · Paso 2 | H2, H3: un único énfasis, jerarquía falsa (líneas 1–110) |
| 20 | `01-leyes/acc-accion-interaccion/umbral-de-doherty.md` (ACC-02) | Capa 3 · Paso 2 | H8: eco < 100 ms, indicadores por duración, matiz sobre el origen de los 400 ms (líneas 1–80) |
| 21 | `01-leyes/mot-motivacion-tiempo/regla-pico-final.md` (MOT-05) | Capa 3 · Paso 2 | H8, H1, H10: picos negativos y diseño del final (líneas 1–80) |
| 22 | `01-leyes/per-percepcion-atencion/atencion-selectiva.md` (PER-06) | Capa 3 · Paso 2 | H4, H5, H10: ceguera a los banners (Pernice 2018), error junto al foco (líneas 1–80) |
| 23 | `01-leyes/sis-sistema-complejidad/navaja-de-occam.md` (SIS-04) | Capa 3 · Paso 2 | H3, H9: prueba de retirada de elementos (líneas 1–80) |
| 24 | `01-leyes/sis-sistema-complejidad/ley-de-tesler.md` (SIS-03) | Capa 3 · Pasos 2 y 5 | H9, H10: inferir lo inferible, "¿quién lo hará ahora?" (líneas 1–70) |
| 25 | `01-leyes/dec-decision-juicio/ley-de-hick.md` (DEC-01) | Capa 3 · Paso 2 | H4: límites de Hick (búsqueda lineal en listas desconocidas), listas con búsqueda (líneas 1–70) |
| 26 | `01-leyes/per-percepcion-atencion/ley-de-proximidad.md` (PER-01) | Capa 3 · Paso 2 | H6, H11: razón de espaciado interno/externo, etiqueta pegada al campo (líneas 1–70) |

**No se consultaron**, y por qué:
- `03-aplicacion/por-sintoma.md`: la petición no describe un síntoma con datos; su función la cubrió la tabla §6 del mapa global.
- `08-fuentes/`: las citas proceden de las fichas de cada ley y no se añadió ninguna fuente externa.
- `datos/`, `dist/`, `adaptadores/`, `herramientas/`: son versiones empaquetadas o utilidades, no necesarias en un entorno que lee los Markdown directamente.

Los contrastes se calcularon con un script local (fórmula de luminancia relativa de WCAG) a partir de los colores CSS del archivo. No se leyó nada fuera de `ux-skill/` y no se modificó ningún archivo existente.
