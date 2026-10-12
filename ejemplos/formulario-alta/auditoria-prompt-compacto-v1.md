*Habilidad: H1 auditar (con apoyo de H8, porque el formulario incluye código).*

## Resumen

El formulario tiene un problema de **confianza** antes que de usabilidad. Usa varios patrones oscuros: una cuenta atrás falsa que se reinicia, consentimientos y un seguro de pago ya marcados, un enlace de confirmshaming y la renovación automática escondida. Algunos de ellos tienen además **riesgo legal**. Después viene un problema de **acción**: el botón grande y llamativo es «Borrar formulario» y el de enviar apenas se ve. Encima, los errores son genéricos, borran lo que la persona ya escribió y no dicen qué reglas hay que cumplir. Por último hay un problema de **carga**: unos 25 controles, 9 planes sin precio y etiquetas que solo existen como placeholder. Lo primero que hay que cambiar es lo que aparece en los hallazgos 1 a 5. Ese 20 % de los cambios resuelve la mayor parte del daño.

---

## Hallazgos priorizados

Severidad = frecuencia × impacto × persistencia. **Crítica** significa que bloquea, causa daño o tiene riesgo legal. **Alta** significa que provoca abandono o errores frecuentes. **Media** y **Baja** degradan la experiencia.

### 1. [Crítica] Consentimientos y un extra de pago marcados por defecto
- **Observación:** vienen marcadas de serie «Recibir ofertas de FitPlus y sus partners», «Ceder mis datos a terceros» y «Seguro de lesiones (+4,99 €/mes)».
- **Ley y mecanismo:** DEC-03 Sesgo cognitivo (C), en concreto el sesgo por defecto o statu quo: la mayoría no toca lo que viene preseleccionado. PER-06 Atención selectiva (E2): la persona se centra en terminar el alta y no revisa casillas pequeñas al final. Aquí el sesgo se explota **contra** su interés, lo que choca con la regla ética.
- **Riesgo legal (comprobadlo con vuestro DPO o asesoría):** en la UE, el consentimiento con casilla premarcada no es válido según el RGPD (TJUE, caso *Planet49*, 2019). La Directiva 2011/83/UE (art. 22) prohíbe cobrar pagos adicionales que se hayan aceptado mediante opciones por defecto.
- **Recomendación:** dejar todas las casillas **desmarcadas**. Separar el seguro como un añadido opcional, con su precio visible junto al del plan. Separar «ofertas» de «cesión a terceros», o quitar la cesión si no es imprescindible.
- **Cómo verificar:** revisar el HTML (ningún `checked` en consentimientos ni extras). Tras el cambio, medir el % de opt-in real y las reclamaciones o devoluciones relacionadas con el seguro.
- **Tensión:** default ↔ autonomía. Bajará la tasa de opt-in. Es el precio de que el consentimiento sea válido y de no perder la confianza de quien se da de alta.

### 2. [Crítica] Cuenta atrás falsa y parpadeante, y confirmshaming
- **Observación:** «¡OFERTA EXPIRA EN 05:00!» se reinicia en cada visita y al llegar a cero (está en el código). Parpadea sin parar en rojo. Junto a ella está el enlace «No gracias, no me interesa cuidar mi salud».
- **Ley y mecanismo:** DEC-03 (C), porque es urgencia falsa (aversión a la pérdida) y vergüenza inducida. PER-07 Von Restorff (E2): el elemento que más destaca de la página es una mentira, y además quita atención a la tarea. MOT-01 Flujo (C): la interrupción constante rompe la concentración.
- **Accesibilidad:** el parpadeo continuo incumple WCAG 2.2.2 (Pausar, detener, ocultar). Tampoco respeta `prefers-reduced-motion`.
- **Recomendación:** quitar el temporizador. Si existe una promoción real con fecha, mostrar la fecha de fin en texto estático. Sustituir el confirmshaming por un enlace neutro («Ahora no») o eliminarlo, porque no tiene ninguna función en un formulario de alta.
- **Cómo verificar:** prueba ética (¿funcionaría si se lo explicaras a la persona? No). Test A/B de conversión **y** de cancelaciones a 30 días. Comprobación con axe/Lighthouse y con movimiento reducido activado.

### 3. [Crítica] La acción principal es «Borrar formulario»
- **Observación:** «Borrar formulario» es un botón verde, grande (14×32 px de padding, 16 px de texto) y está a la derecha, donde se espera el envío. «enviar» es gris sobre gris, en minúsculas y de 12 px con 4 px de padding. No hay confirmación antes de borrar.
- **Ley y mecanismo:** PER-07 Von Restorff (E2): el botón más distinto se lee como el principal. SIS-01 Jakob (H): por convención, el botón primario y destacado es el que envía. ACC-01 Fitts (E1): el botón de enviar es un objetivo pequeño y lento de alcanzar, mientras que el destructivo es grande. Un solo error borra unos 25 campos (alto impacto).
- **Recomendación:** **eliminar el botón de reset**, que casi nunca es útil. Hacer de «Darme de alta» (con un verbo que diga el resultado) un botón primario de al menos 44–48 px de alto, con contraste suficiente y ancho completo en móvil.
- **Cómo verificar:** prueba de 5 segundos («¿dónde harías clic para terminar?») y test con 5–8 personas. Medir los clics en reset (registrarlos antes de quitarlo) y el ratio de formularios completados frente a enviados.

### 4. [Crítica] Errores genéricos que destruyen datos y reglas ocultas
- **Observación:** con cualquier fallo aparece arriba un único mensaje: «Hay errores en el formulario. Revise los datos.». No indica el campo, no tiene `role="alert"` y no mueve el foco. Además **borra** la contraseña, su repetición y el captcha. Las reglas de la contraseña (≥10 caracteres, una mayúscula, un símbolo) no se muestran en ningún sitio. El teléfono y la fecha exigen un formato rígido.
- **Ley y mecanismo:** MEM-02 Memoria de trabajo (E2): obliga a recordar y localizar qué falló sin ninguna pista. SIS-02 Modelo mental (C): la persona no puede saber qué espera el sistema. SIS-03 Tesler (H): la complejidad del formato recae en cada persona en lugar de en el sistema. ACC-03 Postel (H): se rechazan entradas válidas como «612 34 56 78», «+34 612345678» o «1/3/1990». ACC-04 Usuario activo (E2): nadie lee condiciones ocultas; hay que mostrarlas en el momento en que se necesitan.
- **Recomendación:**
  - Mostrar mensajes **por campo**, junto al campo, que digan qué pasa y cómo arreglarlo, enlazados con `aria-describedby` y con `aria-invalid`. Añadir un resumen con enlaces a cada error y `role="alert"`, y llevar el foco al primer error.
  - **No borrar nunca** lo que la persona ya escribió.
  - Mostrar las reglas de la contraseña antes de escribir, con comprobación en vivo, y un botón de «mostrar contraseña» en lugar de pedirla dos veces.
  - Normalizar el teléfono (quitar espacios y el prefijo +34) y aceptar varios formatos de fecha. Ser tolerante en la forma y estricto en el significado: validar que la fecha existe y que la persona es mayor de edad si hace falta.
  - Validar al salir del campo, no en cada pulsación de tecla.
- **Cómo verificar:** tasa de errores por campo y número de reintentos hasta enviar (analítica de formulario). Prueba con lector de pantalla (NVDA/VoiceOver) en la que se oiga cada error y se llegue a él.
- **Tensión:** Postel ↔ seguridad. La tolerancia se aplica al formato, no a la contraseña ni a la verificación.

### 5. [Alta] Envío de 5 s sin respuesta y un final pobre
- **Observación:** tras pulsar enviar no pasa nada visible durante unos 5 segundos (el botón sigue activo, así que es posible enviar dos veces). Después aparece `alert('OK')`, el formulario se vacía y la página redirige a `/`. La información crítica (presentar el DNI original y un justificante bancario en recepción en 7 días) solo aparece en la barra lateral.
- **Ley y mecanismo:** ACC-02 Doherty (E2; los «400 ms» son una regla práctica). A partir de ~1 s hace falta indicar que el sistema está trabajando, y cerca de los 10 s se pierde la atención. MOT-05 Pico-final (E2): el final del alta es lo que más se recordará, y ahora es un `alert` seco. MEM-05 Posición serial (E2): lo último que se ve es lo que mejor se retiene, así que ese es el lugar de los próximos pasos.
- **Recomendación:** al enviar, desactivar el botón, mostrar un estado de carga («Creando tu alta…», anunciado con `aria-live`) y evitar el doble envío. Al terminar, mostrar una **página de confirmación** con el plan, el precio, la fecha de inicio, la permanencia, la renovación y los pasos siguientes (DNI y justificante, plazo, horario de recepción). Enviar lo mismo por email.
- **Cómo verificar:** medir los envíos duplicados y las consultas a recepción del tipo «¿se ha hecho mi alta?». Medir INP ≤ 200 ms en la interacción del botón. Encuesta breve (CSAT) en la confirmación.

### 6. [Alta] Etiquetas solo como placeholder, contraste insuficiente y textos pequeños
- **Observación:** los campos no tienen `<label>`, solo un placeholder `#bbb` (contraste ≈1,9:1) que desaparece al escribir. Hay más textos con poco contraste: los títulos `#999` (≈2,8:1), la letra pequeña `#aaa` a 10 px (≈2,3:1) y «enviar» `#666` sobre `#ccc` (≈3,6:1). Los asteriscos rojos marcan la obligatoriedad solo con color. Las casillas miden 12×12 px. Los inputs usan 13 px, lo que provoca zoom automático en iOS.
- **Ley y mecanismo:** MEM-02 (E2): al escribir desaparece la etiqueta y hay que recordar qué pedía el campo. MEM-01 Carga cognitiva (C). ACC-01 Fitts (E1), por las casillas.
- **Accesibilidad:** sin etiquetas accesibles se incumple WCAG 1.3.1, 3.3.2 y 4.1.2. El contraste de 1.4.3 no se cumple. La regla de 1.4.1 no se cumple si la obligatoriedad solo se indica con color. El tamaño de objetivo de 2.5.8 queda justo; la etiqueta que envuelve la casilla ayuda, pero conviene ampliarla.
- **Recomendación:** poner un `<label>` visible encima de cada campo. Marcar los campos *opcionales* como «(opcional)» en lugar de llenar todo de asteriscos. Contraste ≥4,5:1 en texto, inputs de ≥16 px y casillas de ≥24×24 px. Usar los tipos e `autocomplete` adecuados (`type="email"`, `type="tel"` + `autocomplete="tel"`, `given-name`, `family-name`, `postal-code`, `bday`, `new-password`).
- **Cómo verificar:** axe/Lighthouse sin errores de etiqueta ni de contraste, recorrido completo solo con teclado y prueba de autocompletado en móvil.

### 7. [Alta] Condiciones del contrato escondidas
- **Observación:** «Permanencia mínima según plan. Renovación automática.» aparece en 10 px gris claro y remite a una URL externa. El plan no muestra ningún precio.
- **Ley y mecanismo:** PER-06 Atención selectiva (E2): está diseñado para no verse. DEC-03 (C): es un ocultamiento contrario al interés de la persona. También afecta a MOT-05: si la persona descubre la permanencia al intentar darse de baja, ese será el «pico» que recuerde de vuestra marca.
- **Recomendación:** mostrar el precio mensual, la permanencia y la renovación **junto a cada plan**, en texto legible, y repetirlo en un resumen antes del botón de alta.
- **Cómo verificar:** prueba de comprensión tras el alta («¿cuánto pagas y hasta cuándo estás comprometido/a?»). Seguir las reclamaciones por permanencia.

### 8. [Alta] Selector de 9 planes en un desplegable, sin precio
- **Observación:** un `<select>` mezcla tres dimensiones (nivel, horario y duración) en etiquetas como «Básico Total 6m» o «Premium Family 12m».
- **Ley y mecanismo:** DEC-02 Sobrecarga de opciones (E3; el efecto medio ≈0, pero aquí se dan sus moderadores: un surtido complejo, preferencias poco definidas en quien se da de alta por primera vez y comparación difícil). DEC-01 Hick (E1) solo aplica en parte, porque las opciones no son conocidas y en un desplegable el tiempo de búsqueda crece de forma lineal. MEM-04 Fragmentación (E2).
- **Recomendación:** separar la elección en dos pasos visibles: (a) nivel, con 3–4 tarjetas con precio y lo que incluye, y (b) duración (6 o 12 meses), con la diferencia de precio y de permanencia. Se puede marcar «el más elegido» si es cierto, pero **sin preseleccionarlo**.
- **Cómo verificar:** tiempo hasta elegir un plan, % de cambios de plan en los primeros 30 días y prueba de comprensión.
- **Tensión:** fragmentar ↔ comparar. Las tarjetas deben poder compararse lado a lado (tabla en escritorio, lista apilada en móvil).

### 9. [Media] Campos que no aportan y que añaden carga
- **Observación:** se piden fax, empresa, cargo, «¿Cómo nos conoció?», repetir el email, repetir la contraseña, país (con Afganistán antes que España) y provincia (que se puede deducir del CP). El captcha aritmético tiene la respuesta (`'59'`) escrita en el propio código del cliente.
- **Ley y mecanismo:** SIS-04 Occam (H): cada campo sobrante es coste sin beneficio. MEM-01 (C). SIS-03 Tesler (H): la provincia, la ciudad y el país los puede resolver el sistema. SIS-05 Pareto (H): unos pocos campos concentran casi todo el valor (aunque probablemente en una proporción menor que 80/20). El captcha no aporta seguridad (se ve en el código) y añade una prueba cognitiva. Para la autenticación, WCAG 3.3.8 pide no exigir este tipo de pruebas sin alternativa.
- **Recomendación:** eliminar fax, empresa y cargo. Dejar «¿Cómo nos conoció?» como opcional o pasarlo a la confirmación. Un solo email con validación de formato y verificación por enlace. Una sola contraseña con la opción de mostrarla. País con España por defecto (o eliminarlo). Rellenar la provincia y la ciudad a partir del CP. Sustituir el captcha por protección en el servidor (honeypot, límite de intentos o un servicio antibots invisible).
- **Cómo verificar:** tiempo de cumplimentación y tasa de abandono por campo, antes y después.
- **Tensión:** Occam ↔ necesidades de negocio. Confirmad con negocio y legal qué datos son **necesarios** (por ejemplo, el DNI para el contrato) frente a los que solo están porque siempre han estado.

### 10. [Media] Estructura visual que no dice la verdad
- **Observación:** la cuadrícula de 2 columnas empareja campos sin relación (teléfono con fax, nacimiento con DNI) y usa el mismo espacio dentro de los grupos que entre ellos. Los títulos de sección son grises, pequeños y sin peso. El aviso importante de la barra lateral parece un anuncio (degradado amarillo, borde rojo discontinuo).
- **Ley y mecanismo:** PER-01 Proximidad (E2): si el espacio interno y el externo son iguales, no se perciben grupos. PER-03 Región común (E2). PER-02 Semejanza (E2). PER-06 Atención selectiva (E2): lo que tiene aspecto de publicidad se ignora (ceguera a los banners). PER-05 Prägnanz (C).
- **Recomendación:** usar una sola columna en móvil y agrupar con más espacio entre secciones que dentro de ellas (por ejemplo, 8 px dentro de un grupo y 32 px entre grupos). Juntar solo los campos realmente emparejados (nombre y apellidos, CP y ciudad). Títulos con jerarquía real. El aviso del DNI y el justificante va **dentro del flujo**, como un aviso informativo sobrio, junto al resumen final y en la confirmación.
- **Cómo verificar:** prueba de 5 segundos sobre la estructura («¿qué te van a pedir?») y recuerdo del requisito de presentar el DNI tras completar el alta.
- **Tensión:** Von Restorff ↔ semejanza. Que destaque solo una cosa: el botón de alta.

### 11. [Baja] Detalles de código (H8)
- `novalidate` sin una validación propia completa: no se comprueban nombre, apellidos, dirección, CP, provincia, país, plan, DNI (ni su letra) ni el formato del email.
- `pw2` nunca se compara con `pw`.
- `pattern` en un `type="text"` con `novalidate` no tiene efecto.
- Tras el éxito se usan `reset()` y la redirección a `/`, con lo que se pierde la confirmación.
- No hay protección contra el doble envío.
- **Cómo verificar:** tests de los casos límite (DNI con letra incorrecta, email sin @, contraseñas distintas, doble clic en enviar).

---

## Qué cambiar primero (el 20 % de mayor efecto)

1. **Esta semana, por riesgo legal y ético:** desmarcar los consentimientos y el seguro, quitar la cuenta atrás y el confirmshaming, y mostrar el precio, la permanencia y la renovación. (Hallazgos 1, 2 y 7.)
2. **Quitar el botón de reset y hacer de «Darme de alta» el botón primario.** (Hallazgo 3.) Es un cambio de una línea con un impacto enorme.
3. **Errores por campo que no borren datos, con las reglas visibles.** (Hallazgo 4.)
4. **Estado de carga y página de confirmación con los próximos pasos.** (Hallazgo 5.)
5. **Etiquetas visibles, contraste y `autocomplete`.** (Hallazgo 6.)

Después: rediseñar el selector de planes (8), recortar campos (9) y reordenar la estructura (10).

## Supuestos
- **Persona:** alguien que se da de alta por primera vez, sin conocer los planes, probablemente desde el **móvil**. La tarea se hace una sola vez, pero es crítica: un contrato con pago recurrente.
- El gimnasio opera en España o en la UE (de ahí las referencias al RGPD y a la Directiva 2011/83/UE). Esto no es asesoramiento jurídico; validadlo con vuestro DPO o asesoría.
- No tengo datos reales de uso. La severidad se basa en el análisis del código y en las leyes, no en métricas. Si tenéis analítica de formulario (abandono por campo, errores), prevalece sobre esta priorización.

## Próximos pasos
1. Antes de cambiar nada, registrad la línea base: tasa de completado, tiempo, abandono por campo, clics en reset, errores por campo y cancelaciones o reclamaciones a 30 días.
2. Aplicad los cambios 1–5 y haced un test de usabilidad moderado con 5–8 personas en móvil, incluida al menos una persona que use lector de pantalla.
3. Medid de nuevo y comparad. Valorad el éxito por el **alta completada y no reclamada**, no solo por los clics en enviar.
4. Si queréis, puedo devolveros el formulario reescrito (HTML/CSS/JS) con estos cambios aplicados.
