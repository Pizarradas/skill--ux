*Habilidad: H1 auditar (con H8, porque también reviso el código del formulario).*

## Resumen

El formulario de alta de FitPlus tiene **varios patrones oscuros que hay que quitar ya**: una cuenta atrás falsa, casillas de pago y de cesión de datos ya marcadas, un enlace de "confirmshaming" y la renovación automática escondida en letra de 10 px. Además, **el botón que más destaca es "Borrar formulario"** y el de enviar parece desactivado. La validación borra datos, oculta sus reglas y no dice qué campo falla. Y el formulario pide más campos de los necesarios mientras esconde lo importante: precios, permanencia y la obligación de llevar el DNI en 7 días.
**Qué cambiar primero** (el ~20 % de cambios con más efecto): (1) quitar los patrones oscuros, (2) invertir la jerarquía de botones, (3) etiquetas visibles y validación por campo que no borre nada, (4) eliminar campos sobrantes, (5) elegir el plan viendo precios y (6) dar respuesta durante el envío y una pantalla final útil.

---

## Hallazgos priorizados

Severidad: 4 crítico · 3 alto · 2 medio · 1 bajo. Los patrones oscuros y las barreras de accesibilidad bloqueantes cuentan como 4.

### 1. Cuenta atrás falsa que parpadea — Severidad 4 (patrón oscuro + accesibilidad)
- **Observación:** "¡OFERTA EXPIRA EN 05:00!" en rojo, parpadeando a 1 Hz. El script vuelve a empezar al llegar a 0 y en cada visita (`s = s > 0 ? s - 1 : 300`), y la oferta no existe en ningún sitio del formulario.
- **Leyes y mecanismo:** DEC-03 Sesgo cognitivo (C): explota la aversión a la pérdida y la urgencia para que la persona decida antes de leer las condiciones. PER-06 Atención selectiva (E2) y PER-07 Von Restorff (E2): el parpadeo se lleva la atención que debería ir a la tarea. MOT-01 Flujo (C): es una interrupción constante.
- **Ética:** no pasa la prueba. Si se explicara ("el contador es falso y se reinicia"), dejaría de funcionar. Perjudica sobre todo a personas ansiosas o con TDAH.
- **Accesibilidad:** incumple WCAG 2.2.2 (Pausar, detener, ocultar): se mueve más de 5 s sin control. No respeta `prefers-reduced-motion`. Además, el texto blanco sobre #e00 baja de contraste en la fase de opacidad 0,3.
- **Recomendación:** eliminarla. Si hay una promoción real con fecha de fin, poner un texto estático con la fecha exacta ("Matrícula gratis hasta el 31/10"), sin animación.
- **Cómo verificar:** auditoría con axe/Lighthouse sin avisos de movimiento. Test A/B midiendo altas completadas **y** bajas o reclamaciones a 30 días (la urgencia falsa puede subir altas y subir también las cancelaciones).
- **Tensión:** "conversión inmediata ↔ ética". Aquí gana la ética sin discusión.

### 2. Casillas preseleccionadas: seguro de pago, publicidad y cesión a terceros — Severidad 4 (patrón oscuro)
- **Observación:** vienen marcadas por defecto "Añadir seguro de lesiones (+4,99 €/mes)", "Acepto ceder mis datos a terceros con fines comerciales" y "Quiero recibir ofertas de FitPlus y sus partners".
- **Leyes y mecanismo:** DEC-03 Sesgo cognitivo (C), en concreto el efecto default o sesgo del statu quo: la gente tiende a dejar lo que viene marcado. PER-06 Atención selectiva (E2): las casillas son de 12×12 px, están al final y quien rellena el formulario no las ve.
- **Ética y legal:** una preselección de pago es un patrón oscuro explícito. En la UE, el consentimiento para cesión y marketing tiene que ser una acción afirmativa: una casilla premarcada no vale como consentimiento (RGPD, art. 4.11 y considerando 32; sentencia Planet49 del TJUE). Confirmadlo con vuestro asesor legal.
- **Recomendación:** todas las casillas opcionales desmarcadas. Presentar el seguro como una opción aparte, con su precio y qué cubre, y sin marcar. Separar "ofertas de FitPlus" de "ofertas de partners". Eliminar la cesión a terceros o pedirla aparte y bien explicada.
- **Cómo verificar:** revisión del código (ningún `checked` en opciones opcionales o de pago). Medir la tasa de contratación del seguro con consentimiento activo, y las reclamaciones o devoluciones del seguro antes y después.

### 3. Enlace de "confirmshaming" — Severidad 4 (patrón oscuro)
- **Observación:** "No gracias, no me interesa cuidar mi salud", en 10 px gris claro y sin ninguna función (`href="#"`).
- **Leyes y mecanismo:** DEC-03 Sesgo cognitivo (C): usa la culpa para desanimar el rechazo. SIS-02 Modelo mental (C): no está claro a qué dice "no" (¿al seguro?, ¿al alta?).
- **Recomendación:** eliminarlo. Si se refiere al seguro, ya lo resuelve una casilla desmarcada.
- **Cómo verificar:** prueba con 5 personas: "¿Qué hace este enlace?". Ahora mismo seguramente nadie sabrá decirlo.

### 4. Condiciones esenciales en letra mínima: renovación automática, permanencia y precios fuera — Severidad 4 (patrón oscuro por ocultación)
- **Observación:** "Permanencia mínima según plan. Renovación automática." aparece en 10 px, #aaa sobre blanco (contraste aproximado de 2,3:1). Los precios no están en el formulario: hay que ir a otra web.
- **Leyes y mecanismo:** PER-06 Atención selectiva (E2): lo que no se ve no se ha leído. MEM-02 Memoria de trabajo (E2): obligar a consultar precios en otra página exige recordarlos al volver (pregunta 4 del repaso). DEC-03 (C): ocultar el coste total favorece decisiones de las que luego la persona se arrepiente.
- **Accesibilidad:** contraste por debajo de 4,5:1 (WCAG 1.4.3) y tamaño muy pequeño.
- **Recomendación:** junto a cada plan, mostrar el precio mensual, la permanencia en meses, si se renueva automáticamente y cómo se cancela, en texto ≥ 14–16 px con contraste ≥ 4,5:1. En el botón final, resumir "Plus 12 meses · 39 €/mes · renovación automática" (precio ilustrativo).
- **Cómo verificar:** prueba de comprensión tras el alta: "¿Cuánto pagas al mes, cuánto tiempo te comprometes y se renueva solo?". Objetivo ≥ 90 % de aciertos. Seguir también las reclamaciones por permanencia o renovación.

### 5. "Borrar formulario" es el botón principal y "enviar" parece desactivado — Severidad 4 (bloqueante y destruye datos)
- **Observación:** `.btn-reset` es verde, 16 px, padding 14×32, y está a la derecha, donde la mirada espera la acción principal. `.btn-submit` es gris #ccc con texto #666, 12 px, padding 4×10: unos 22 px de alto. El reset borra todo sin confirmar ni poder deshacer.
- **Leyes y mecanismo:** PER-07 Von Restorff (E2): lo distinto se nota, y aquí lo distinto es la acción destructiva. SIS-01 Jakob (H): por convención, el botón primario y a la derecha es "Enviar", y el gris significa desactivado. ACC-01 Fitts (E1): el objetivo correcto es el pequeño. PER-02 Semejanza (E2): el gris del botón de enviar se parece al de un control desactivado.
- **Accesibilidad:** el texto #666 sobre #ccc tiene un contraste aproximado de 3,7:1 (no llega a 4,5:1). El alto (unos 22 px) queda por debajo del mínimo de 24×24 px (WCAG 2.5.8) y muy lejos de los 44–48 px recomendables en táctil.
- **Recomendación:** eliminar el botón de reset (casi nunca aporta nada en un alta). Un solo botón primario, ancho completo en móvil, ≥ 48 px de alto, con un texto que diga lo que hace: "Darme de alta" o "Continuar al pago".
- **Cómo verificar:** grabaciones o analítica: clics en reset → abandono (esperado: 0 tras el cambio). Prueba de 5 segundos: "¿Dónde pulsarías para terminar?", con ≥ 95 % de aciertos.

### 6. Sin etiquetas: sólo placeholders de bajo contraste — Severidad 4 (barrera de accesibilidad)
- **Observación:** ningún `<input>` tiene `<label>`. El nombre del campo, el asterisco de obligatorio y el formato ("DD/MM/AAAA", "9 dígitos") están en el placeholder, #bbb sobre blanco (contraste aproximado de 1,9:1), y desaparecen al escribir. El asterisco rojo es sólo color.
- **Leyes y mecanismo:** MEM-02 Memoria de trabajo (E2): al escribir desaparece la pista y hay que recordar qué pedía el campo y en qué formato. MEM-01 Carga cognitiva (C). PER-06 (E2): con ese contraste, el placeholder parece vacío. Para lectores de pantalla, el placeholder no es un nombre accesible fiable.
- **Accesibilidad:** incumple WCAG 1.3.1, 3.3.2 (Etiquetas o instrucciones), 1.4.3 y 1.4.11 (el borde #ddd de los campos tampoco llega a 3:1).
- **Recomendación:** un `<label for>` visible encima de cada campo. Las pistas de formato en un texto de ayuda permanente asociado con `aria-describedby`. Marcar como "(opcional)" los pocos campos opcionales en lugar de poner asteriscos en todos. Bordes de campo con contraste ≥ 3:1.
- **Cómo verificar:** axe o Lighthouse sin errores de "form label". Navegación completa con NVDA/VoiceOver sólo con teclado. Contraste comprobado con una herramienta.

### 7. Validación hostil: error genérico, reglas ocultas y borra lo escrito — Severidad 4 (bloqueante)
- **Observación:**
  - Un único mensaje "Hay errores en el formulario. Revise los datos." arriba del todo, sin decir qué campo falla, sin mover el foco y sin `role="alert"` ni `aria-live`.
  - Al fallar **borra contraseña, repetición y captcha**.
  - La contraseña exige ≥ 10 caracteres, una mayúscula y un símbolo, pero esas reglas no aparecen en ningún sitio.
  - Teléfono: sólo acepta exactamente 9 dígitos, sin espacios ni prefijo +34.
  - Fecha: sólo acepta exactamente `dd/mm/aaaa`.
  - Email: `type="text"`, sin validación de formato (sólo compara las dos copias).
  - Los atributos `pattern` no hacen nada por el `novalidate`. Nombre, apellidos, DNI y dirección no se validan.
- **Leyes y mecanismo:** ACC-03 Postel (H): hay que aceptar "612 34 56 78", "+34 612345678" o "1/3/1990" y normalizarlos dentro del sistema. SIS-03 Tesler (H): el formato es complejidad que debe cargar el sistema, no cada persona. ACC-04 Paradoja del usuario activo (E2): nadie lee reglas antes de escribir, así que tienen que estar a la vista mientras se escribe. MEM-02 (E2): hay que recordar qué se escribió para encontrar el error. MOT-05 Pico-final (E2): un fallo que además borra lo escrito es un pico negativo muy memorable.
- **Accesibilidad:** incumple WCAG 3.3.1 (Identificación de errores), 3.3.3 (Sugerencias ante errores), 4.1.3 (Mensajes de estado) y 3.3.7 (Entrada redundante), y probablemente 3.3.8 (Autenticación accesible) por el captcha (ver hallazgo 9).
- **Recomendación:**
  - Validar cada campo al salir de él (on blur), con un mensaje junto al campo que diga cómo arreglarlo ("El teléfono debe tener 9 cifras; puedes escribirlo con espacios").
  - Al enviar: un resumen con enlaces a cada error y el foco en él.
  - **No borrar nunca** lo escrito.
  - Mostrar las reglas de la contraseña en vivo, con una marca por cada regla cumplida y sin depender sólo del color, y añadir un botón "mostrar contraseña" en lugar del campo de repetición.
  - `type="email"`, `type="tel"` con `inputmode="numeric"` y `autocomplete` (`given-name`, `family-name`, `email`, `tel`, `bday`, `postal-code`, `street-address`, `new-password`).
  - Normalizar espacios, guiones y prefijos en el servidor.
- **Cómo verificar:** tasa de error por campo y número de envíos fallidos por alta (registrar los eventos). Objetivo: menos del 10 % de altas con más de un envío fallido. Test de usabilidad con 5–8 personas en móvil.
- **Tensión:** Postel ↔ seguridad. Ser flexibles en la forma (espacios, prefijo) y estrictos en el significado (el DNI tiene que ser válido, letra de control incluida).

### 8. Sin respuesta durante el envío y un final pobre — Severidad 3
- **Observación:** el envío tarda entre 4 y 6 s sin ningún indicador y con el botón activo, así que se puede enviar dos veces. Al terminar aparece un `alert('OK')`, se resetea el formulario y redirige a "/" sin decir qué pasa ahora. Y lo que pasa ahora es importante: hay que llevar el DNI y un justificante en 7 días.
- **Leyes y mecanismo:** ACC-02 Doherty (E2; los "400 ms" son una regla práctica, no un dato literal): con más de 1 s hace falta algo que indique que se está trabajando, y con unos 10 s se pierde la atención. MOT-05 Pico-final (E2): el final es justo lo que se recuerda, y ahora es un "OK" seco. SIS-02 Modelo mental (C): la persona cree que ya es socia y no sabe que el alta no está activa.
- **Recomendación:**
  - Al pulsar: desactivar el botón, cambiar su texto a "Creando tu alta…" con un spinner que respete `prefers-reduced-motion`, y anunciarlo con `aria-live`.
  - Si se puede, reducir la latencia del servidor.
  - Al terminar: una página de confirmación con nombre y plan, los siguientes pasos ("Trae tu DNI original y un justificante bancario a recepción antes del 19/10"), horario y dirección del centro, y la misma información por email. Quitar el `alert`.
- **Cómo verificar:** altas duplicadas (objetivo: 0). Porcentaje de personas que se presentan en recepción dentro de los 7 días. Encuesta de una pregunta en la confirmación. INP ≤ 200 ms en la interacción del botón.

### 9. Captcha aritmético — Severidad 3
- **Observación:** "¿Cuánto es 7 × 8 + 3?" (59). Si te equivocas, se borra.
- **Leyes y mecanismo:** SIS-03 Tesler (H): la protección contra bots es un problema del sistema y no debería cargarla cada persona. MEM-01 Carga cognitiva (C): obliga a calcular a mitad de una tarea. Es una barrera para personas con discalculia (WCAG 3.3.8 pide no exigir pruebas cognitivas para autenticarse; aquí no se autentica, pero el espíritu es el mismo). Además es una protección débil, porque la respuesta está fija en el código.
- **Recomendación:** quitarlo y sustituirlo por un campo trampa (honeypot), limitación de envíos y verificación del email.
- **Cómo verificar:** tasa de fallos en ese campo ahora mismo, y volumen de spam antes y después.

### 10. Campos innecesarios y datos que el sistema podría deducir — Severidad 3
- **Observación:** se piden Fax, Empresa, Cargo, el email repetido y la contraseña repetida. Ciudad y provincia se pueden deducir del código postal. El país es una lista alfabética desde "Afganistán" para un gimnasio que trabaja en España. Ahora mismo son 22 campos o controles.
- **Leyes y mecanismo:** SIS-04 Occam (H): cada campo sin propósito es un coste más. SIS-03 Tesler (H): deducir ciudad y provincia del CP traslada la complejidad al sistema. MEM-01 Carga cognitiva (C). MOT-02 Gradiente de meta (E2): cuantos menos campos, más cerca se percibe el final. SIS-01 Jakob (H): el fax es un anacronismo que resta credibilidad.
- **Recomendación:** quitar Fax, Empresa y Cargo (si hacen falta para convenios de empresa, pedirlos después del alta y como opcionales). Quitar las dos confirmaciones (email: `type="email"` más verificación por correo; contraseña: botón "mostrar"). Autocompletar ciudad y provincia a partir del CP, con posibilidad de editarlas. País: España por defecto, o quitarlo. Pedir sólo los datos que se usan.
- **Cómo verificar:** tiempo medio de compleción (objetivo: -30 % o más) y tasa de abandono por campo, comparando la versión actual con la reducida en un test A/B.
- **Tensión:** reducir ↔ necesidades de negocio. Antes de quitar un campo, preguntar quién usa ese dato.

### 11. Elegir el plan: 9 opciones en un desplegable sin precios ni diferencias — Severidad 3
- **Observación:** "Básico Mañanas 12m / 6m / Total / Plus / Premium / Premium Family", sin precio, sin explicar qué incluye cada uno y con la duración mezclada en el nombre. El plan, que es la decisión principal, aparece en mitad del formulario, después de los datos personales.
- **Leyes y mecanismo:** DEC-02 Sobrecarga de opciones (E3; el efecto medio es casi nulo, pero **aquí concurren sus moderadores**: opciones difíciles de comparar, preferencias poco definidas en alguien nuevo y atributos ocultos). DEC-01 Hick (E1) sólo se aplica de forma parcial, porque las opciones no son conocidas: leer una lista desconocida crece de forma lineal. MEM-04 Fragmentación (E2): son dos dimensiones (nivel y duración) mezcladas en una sola lista.
- **Recomendación:** dos decisiones separadas. Primero el nivel (4 tarjetas: Básico Mañanas, Básico Total, Plus y Premium, cada una con 3–4 diferencias clave y su precio). Después la duración (6 o 12 meses), con el precio mensual y el total y la permanencia visibles. Sin preselección, o con una recomendación honesta basada en lo que la persona ha dicho, no en el margen. Considerar poner este paso **al principio**: es lo que la persona viene a hacer (Jakob, modelo mental de "elijo y luego pago").
- **Cómo verificar:** tiempo hasta elegir plan, cambios de plan en los primeros 30 días y prueba de comprensión ("¿Qué diferencia hay entre Plus y Premium?").
- **Tensión:** fragmentar ↔ comparar. Las tarjetas tienen que permitir ver el nivel y el precio lado a lado.

### 12. El requisito de DNI y justificante en 7 días aparece como un anuncio en el lateral — Severidad 3
- **Observación:** está en un `<aside>` con un degradado amarillo-naranja, un borde rojo discontinuo y el título "¡IMPORTANTE!" en mayúsculas.
- **Leyes y mecanismo:** PER-06 Atención selectiva (E2): ese estilo provoca "ceguera a banners", porque parece publicidad. PER-03 Región común (E2): al estar fuera del formulario, no se percibe como parte del proceso. PER-02 Semejanza (E2): se parece a la promoción de la cuenta atrás. MOT-05 Pico-final (E2): es información que hace falta **al final**, no al principio.
- **Recomendación:** decirlo en una línea sobria al inicio ("Necesitarás tu DNI y un justificante bancario en recepción") y en detalle en la página de confirmación y en el email.
- **Cómo verificar:** porcentaje de personas que llegan a recepción con la documentación completa.

### 13. Maquetación: no se adapta al móvil, agrupa campos sin relación y la jerarquía es débil — Severidad 3
- **Observación:**
  - `main` es un flex con un aside y `.grid` tiene 2 columnas fijas, sin media queries: a 320 px hay dos columnas estrechas más un aside del 25 %, así que no hay reflujo real (WCAG 1.4.10).
  - Los pares de la cuadrícula juntan cosas que no tienen que ver (Teléfono | Fax, DNI | Empresa).
  - Los títulos de sección (`h2`) son de 15 px, gris #999 y peso normal (contraste aproximado de 2,8:1), y el espacio sobre y bajo ellos es el mismo que entre campos (14 px).
  - Los campos son de 13 px de letra con padding de 6 px: unos 28 px de alto, y en iOS se hace zoom al enfocar porque la letra es menor de 16 px.
  - Las casillas son de 12×12 px.
- **Leyes y mecanismo:** PER-01 Proximidad (E2): si el espacio interno de un grupo es igual al externo, los grupos no se leen como grupos. PER-02 Semejanza (E2): los títulos se parecen a los placeholders. ACC-01 Fitts (E1) para los campos y las casillas. SIS-01 Jakob (H): el estándar en móvil es una sola columna.
- **Recomendación:** una sola columna (como mucho, CP y ciudad juntos en escritorio). Más espacio entre secciones que dentro de ellas (por ejemplo, 32 px entre secciones y 16 px entre campos). `h2` oscuro y en negrita. Letra de 16 px en los campos y ≥ 44–48 px de alto. Casillas de ≥ 24 px con toda la etiqueta clicable (ya lo es, y hay que mantenerlo). El aside, debajo del formulario o integrado en él, en una sola columna en móvil.
- **Cómo verificar:** probar con zoom al 400 % y a 320 px sin scroll horizontal. Medir la tasa de abandono en móvil frente a escritorio.

### 14. Detalles menores — Severidad 1–2
- "¿Cómo nos conoció?" tiene como valor seleccionado el propio texto de la pregunta, así que se envía como si fuera una respuesta. Debe ser opcional y con `value=""`. (2)
- La fecha de nacimiento se escribe como texto libre. Mejor tres campos (día, mes, año) o un campo que acepte varios formatos, con `autocomplete="bday"`. Ponedla junto a los datos personales. (2)
- El DNI no se valida ni acepta variaciones (minúsculas, guion, NIE). Normalizarlo y comprobar la letra de control. (2)
- Las listas de provincia y país incluyen la opción "…" como si fuera un valor seleccionable. (1)
- El botón dice "enviar" en minúscula y de forma genérica. Usar un verbo concreto. (1)

---

## Lo que funciona (conservar)
- `lang="es"`, `meta viewport` y un `<title>` descriptivo.
- Las secciones (Datos, Dirección, Plan, Acceso) son una buena base para fragmentar; sólo falta que se vean como tales (MEM-04).
- Las casillas van dentro de `<label>`, así que el texto también es clicable.
- La casilla de privacidad viene **desmarcada** y es obligatoria, como debe ser.
- Se avisa del requisito de documentación antes de enviar. El problema es cómo se presenta, no que se diga.

---

## Supuestos y límites del análisis
- **Persona y tarea:** gente que quiere apuntarse a un gimnasio en España, probablemente desde el **móvil** (por ejemplo, desde redes o un QR en el local). Lo hace una sola vez y es una tarea **de alta criticidad**: firma un contrato con pagos recurrentes y permanencia.
- Analizo sólo el HTML, el CSS y el JS entregados. No conozco el servidor, el pago (que no aparece en el formulario), la analítica ni a vuestro público real.
- Los contrastes son aproximados y hay que confirmarlos con una herramienta. Las referencias legales (RGPD y TJUE) son orientativas: consultadlo con un asesor.
- Las leyes son lentes, no dogma: las prioridades deben confirmarse con datos reales de vuestros socios.

---

## Plan de validación

| Hipótesis | Método | Métrica | Umbral de éxito |
|---|---|---|---|
| Sin cuenta atrás ni preselecciones, las altas no bajan de forma relevante y las reclamaciones bajan | Test A/B (≥ 2 semanas) | Altas completadas; reclamaciones, devoluciones y bajas a 30 días | Altas ≥ -5 %; reclamaciones ≤ -30 % |
| Con un botón primario claro y sin reset desaparecen los borrados accidentales | Analítica y grabaciones | Clics en reset seguidos de abandono; tiempo hasta enviar | 0 borrados; ≥ 95 % de aciertos en la prueba de 5 s |
| La validación por campo, sin borrar nada y aceptando varios formatos, reduce la frustración | Test de usabilidad (5–8 personas, móvil) y eventos | Envíos fallidos por alta; errores por campo | < 10 % de altas con más de 1 envío fallido |
| Menos campos y CP con autocompletado reducen el tiempo y el abandono | Test A/B | Tiempo medio de compleción; abandono por campo | -30 % de tiempo; -20 % de abandono |
| Las tarjetas de plan con precio mejoran la comprensión de lo contratado | Test de comprensión tras la tarea | % que acierta precio, permanencia y renovación | ≥ 90 % |
| La confirmación con los pasos siguientes aumenta las activaciones | Datos de recepción | % que presenta la documentación en ≤ 7 días | +20 % sobre la línea base |
| El formulario es accesible | axe/Lighthouse, teclado, NVDA/VoiceOver, 320 px y zoom al 400 % | Errores WCAG 2.2 AA | 0 errores bloqueantes |

---

## Repaso final (10 preguntas)
1. ¿Se entiende en 5 s qué es y qué hacer? **No**: el contador y el banner compiten con la tarea y el botón principal es el equivocado (hallazgos 1, 5 y 12).
2. ¿Lo que se ve junto está relacionado? **No**: los pares de la cuadrícula no tienen relación y los grupos son débiles (13).
3. ¿Hay una sola acción principal, destacada y correcta? **No**: la que destaca es la destructiva (5).
4. ¿Hay que recordar algo de otra pantalla? **Sí**: los precios están en otra web y los formatos desaparecen al escribir (4 y 6).
5. ¿Las opciones están acotadas y con un default honesto? **No**: preselecciones de pago y de datos, y planes sin comparar (2 y 11).
6. ¿Los objetivos son grandes y están donde va la mano? **No**: botón de enviar pequeño, casillas de 12 px y campos bajos (5 y 13).
7. ¿Responde al instante y explica las esperas? **No**: 5 s sin indicador (8).
8. ¿Acepta la entrada como la escribe la gente y explica los errores? **No** (7).
9. ¿Se ve el progreso y el final deja buen recuerdo? **No**: el final es un `alert('OK')` y no dice los pasos siguientes (8). No hay indicador de progreso, pero es un formulario de una sola página: basta con hacerlo más corto (10).
10. ¿Es honesto y accesible? **No**: patrones oscuros, colores con poco contraste, color como única señal, parpadeo y no se adapta a 320 px (1–4, 6 y 13).

Todos los "no" ya aparecen en los hallazgos.
