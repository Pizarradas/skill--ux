---
id: ACC-03
nombre: Ley de Postel (principio de robustez)
nombre_en: Postel's Law
alias: [principio de robustez, Robustness Principle, tolerancia de entrada]
familia: ACC
evidencia: H
etiquetas: [formularios, validacion, entrada-flexible, normalizacion, robustez, multimodal, ia]
refuerza: [SIS-03, ACC-04, SIS-02, MEM-01, MEM-02, SIS-01, MOT-04, ACC-02]
tensiona: [SIS-04, PER-02]
tensiones: [T8, T1]
fuente_laws_of_ux: https://lawsofux.com/postels-law/
---

# ACC-03 · Ley de Postel (*Postel's Law*)

> Un sistema debe aceptar con flexibilidad la forma en que las personas le dan información, traduciéndola a su formato interno dentro de límites claros, y a la vez entregar sus propias salidas de forma estricta, correcta y previsible.

**Idea clave para quien diseña:** sé flexible en la forma, explícito en el significado: normaliza lo que te dan, muestra cómo lo has entendido y pregunta cuando haya ambigüedad real.

## Resumen operativo
- **Qué dice:** acepta con flexibilidad la forma en que la gente introduce datos y emite tus salidas de forma estricta.
- **Evidencia:** H — principio de ingeniería trasladado por analogía; se olvida que en su dominio original está cuestionado (RFC 3117, RFC 9413: la tolerancia silenciosa oculta errores).
- **Haz:** 1) normaliza formatos (espacios, guiones, mayúsculas) en vez de rechazar 2) muestra cómo has interpretado la entrada y pregunta si es ambigua 3) salidas validadas y saneamiento en servidor.
- **Evita:** "aceptar cualquier cosa" en silencio: interpretar mal fechas o importes, o guardar sin sanear.
- **Sospecha de esta ley cuando…:** abundan los errores de formato o el abandono tras un error de validación; se bloquea el pegado.
- **Mide con:** batería de entradas variantes por campo (tasa de rechazo); errores y abandono por campo en analítica de formularios.
- **Vecinas:** SIS-03 Ley de Tesler (refuerza) · ACC-04 Paradoja del usuario activo (refuerza) · SIS-04 Navaja de Occam (tensiona, T1) · Seguridad y precisión (tensiona, T8)

## Origen
- **Jon Postel (ed.), RFC 760, *DoD Standard Internet Protocol* (enero de 1980), §3.2:** pide que una implementación sea conservadora en su comportamiento al enviar y liberal en su comportamiento al recibir. RFC 9413 la identifica como la primera formulación; Wikipedia la sitúa en la especificación IPv4 de 1979.
- **RFC 761, *DoD Standard Transmission Control Protocol* (enero de 1980), §2.10 "Robustness Principle":** las implementaciones TCP deben ser conservadoras en lo que hacen y liberales en lo que aceptan de otros. La frase se repite literalmente en RFC 793 (septiembre de 1981), §2.10.
- **Braden, RFC 1122 (octubre de 1989), §1.2.2** lo formula como "Be liberal in what you accept, and conservative in what you send" y lo matiza: el software debe prepararse para cualquier error concebible, conviene suponer que la red está llena de entidades malévolas, y toda enumeración de valores debe darse por incompleta (un código no definido puede registrarse, pero no debe provocar un fallo).
- **Crítica:** Rose, RFC 3117 (noviembre de 2001), §4.5: el principio de robustez suele causar problemas de despliegue, porque los errores de una implementación nueva pasan inadvertidos ante receptores tolerantes hasta que topan con uno menos liberal; recomienda comprobaciones de consistencia explícitas. Allman (2011), "The Robustness Principle Reconsidered", *ACM Queue*, 9(6) (no verificado: texto bloqueado por el sitio de ACM). **Thomson y Schinazi, RFC 9413, *Maintaining Robust Protocols* (junio de 2023, IAB, informativo):** la tolerancia hace que los errores se conviertan en estándares de hecho, provoca deriva entre implementaciones y debilita la seguridad; propone **mantenimiento activo** de los protocolos, **"intolerancia virtuosa"** (fallar de forma visible ante entradas fuera de especificación) y extensibilidad diseñada explícitamente en vez de confiada a la tolerancia accidental.
- **Traslado a la web y UX:** Mullican, "Your Website has Two Faces" (*A List Apart*, 2013); Keith, "Robustness and least power" (*Adactio*, 2018); Garrity, "Design with Difficult Data" (*A List Apart*, 2018); Boulton, "Design Systems and Postel's Law" (2016, URL caída).

## Mecanismo
Las personas no comparten el modelo de datos del sistema: escriben fechas, teléfonos, nombres y direcciones según su idioma, su costumbre y su dispositivo. Si el sistema exige su formato interno, le traspasa a la persona un trabajo de traducción que genera errores, frustración y abandono. Si lo absorbe (normalizar, interpretar, confirmar), el coste de interacción baja: es un caso concreto de la conservación de la complejidad (SIS-03).

La mitad "conservadora" es igual de importante: lo que el sistema emite (datos a otros sistemas, mensajes, componentes) debe ser estricto para no propagar ambigüedad. Mullican lo resume como dos caras: flexible hacia el humano, estricta hacia la máquina.

## Evidencia y límites
- **Nivel: H** — principio de ingeniería trasladado por analogía. Hay apoyo indirecto en la investigación sobre formularios (los errores de formato causan abandono) y en las WCAG, pero no existe un estudio canónico de "Postel en UX".
- **Está cuestionado en su dominio original (RFC 9413).** Traducción a UX de esa crítica:
  - La tolerancia debe ser **explícita, acotada y con retroalimentación**, nunca silenciosa.
  - Interpretar mal en silencio es peor que pedir aclaración (¿03/04 es 3 de abril o 4 de marzo?).
  - La "intolerancia virtuosa" en UX es rechazar de forma visible y explicada lo que no se puede interpretar con seguridad, en lugar de adivinar.
  - Las extensiones de comportamiento deben documentarse (qué formatos se aceptan), no depender de que "algo funcione por casualidad".
  - En seguridad (autenticación, pagos, inyección de código) "liberal" nunca significa ejecutar o guardar sin sanear: validación y escape en servidor siempre.
- **Caso HTML:** los navegadores toleraron durante años el HTML mal formado; HTML5 terminó especificando el algoritmo de recuperación de errores. Es el modelo deseable: tolerancia, pero definida y uniforme.
- **Malentendidos frecuentes:**
  - "Aceptar cualquier cosa" → aceptar variaciones de forma y confirmar la interpretación.
  - Aplicarla a lo que el sistema muestra → la salida debe ser estricta.
  - Usarla como excusa para un sistema de diseño incoherente ("los componentes aceptan cualquier variante").

## Aplicación práctica
### Reglas
1. [H] Normaliza en vez de rechazar: teléfonos con espacios, guiones, paréntesis o prefijo internacional; tarjetas e IBAN con o sin espacios; recorta espacios iniciales y finales; ignora mayúsculas en correos y códigos — Mullican, Keith.
2. [H] Muestra la interpretación: "15 mar 2026 → domingo, 15 de marzo de 2026". Resuelve día/mes según el *locale* y pregunta si sigue siendo ambiguo — T8.
3. [H] Acepta equivalentes ("CA" y "California"; sinónimos; unidades) cuando el significado es inequívoco — Keith.
4. [N] Nombres sin patrones restrictivos: acentos, apóstrofos, guiones, un solo nombre, nombres largos, escrituras no latinas.
5. [N] Permite pegar en todos los campos, incluidos contraseñas y códigos; usa `autocomplete` (incluido `one-time-code`) — WCAG 3.3.8, 1.3.5.
6. [N] Formato esperado en la etiqueta o descripción, no solo en el *placeholder* (3.3.2); valida al salir del campo, no a cada pulsación; sugiere la corrección ("¿Quisiste decir gmail.com?", 3.3.3).
7. [H] Confirmación explícita para valores de alto impacto (importes, transferencias) — Mullican; WCAG 3.3.4.
8. [H] Elige el control según la fecha: texto para fechas conocidas (nacimiento), calendario para fechas que hay que situar — Mullican.
9. [H] Diseña con datos difíciles: nombres larguísimos, listas vacías o de cientos de elementos, imágenes de proporción rara, traducciones largas, RTL — Garrity.
10. [H] Sé conservador en lo que emites: datos normalizados, HTML válido, salidas estructuradas validadas contra esquema.

### Por contexto
| Contexto | Aplicación |
|---|---|
| Formularios | Normalizar formatos; ejemplos visibles; sugerencias de corrección; pegado permitido; confirmación en importes. |
| Web/escritorio | Soportar ratón, teclado, lápiz, tacto y conmutadores; no asumir *hover*; reflow a 320 px CSS (1.4.10), zoom 200 % (1.4.4), espaciado de texto (1.4.12). |
| Móvil/táctil | `type` e `inputmode` correctos; alternativas a gestos de trayectoria o multipunto (2.5.1) y al arrastre (2.5.7). |
| Navegación/búsqueda | Tolerar erratas, plurales y sinónimos; mostrar "Resultados para X" cuando se corrige la consulta. |
| E-commerce | Direcciones con normalización asistida o campo único; pago con tarjeta en cualquier formato de espaciado. |
| Interfaces conversacionales/IA | Entender paráfrasis, erratas y fechas relativas ("el jueves que viene"); confirmar antes de acciones irreversibles; salidas JSON validadas contra esquema en llamadas a herramientas (intolerancia virtuosa aplicada a LLM). |
| Voz | Aceptar formulaciones libres y errores de transcripción; repetir lo entendido en acciones críticas. |
| Sistemas de diseño | Componentes que toleran contenido variable (truncado con acceso al texto completo, ajuste de línea) con una API de *props* estricta y documentada. |

### Ejemplos
- **Bueno:** un campo de teléfono que acepta "+34 612-345-678", lo guarda normalizado y lo muestra formateado al salir del campo.
- **Bueno (IA):** un asistente que, ante "transfiere 500 a Ana", responde "Voy a transferir 500 € a Ana López (cuenta …1234). ¿Confirmo?".
- **Incumple:** un formulario que rechaza el teléfono por contener un espacio con el mensaje "Formato no válido", y una máscara que borra lo escrito al pegar.

## Anti-patrones
- Rechazo por formato sin sugerencia de corrección.
- Máscaras de entrada rígidas que mueven el cursor o borran texto (muy problemáticas con lector de pantalla y dictado).
- Interpretación silenciosa errónea de fechas o importes.
- Validaciones de nombre o dirección que excluyen culturas minoritarias.
- `onpaste="return false"` en contraseñas o códigos.
- Aceptar sin sanear: "liberal" convertido en vulnerabilidad.

## Ética y accesibilidad
- **Línea roja:** validaciones que discriminan (nombres "no válidos" de otras culturas) y tolerancias que se usan para registrar consentimientos o importes que la persona no confirmó.
- WCAG 2.2: **3.3.1 Error Identification** (A), **3.3.2 Labels or Instructions** (A), **3.3.3 Error Suggestion** (AA), **3.3.4 Error Prevention (Legal, Financial, Data)** (AA), **3.3.7 Redundant Entry** (A), **3.3.8 Accessible Authentication (Minimum)** (AA), **1.3.5 Identify Input Purpose** (AA), **1.4.10 Reflow** (AA), **2.5.7 Dragging Movements** (AA).

## Cómo auditarla
### Señales observables
- Mensajes de error de formato frecuentes; atributos `pattern` muy restrictivos; bloqueo del pegado; máscaras JavaScript; falta de normalización en servidor.
### Preguntas
- ¿Qué variaciones razonables de cada campo se rechazan?
- ¿El sistema muestra cómo ha interpretado lo introducido?
- ¿Las acciones de alto impacto se confirman?
- ¿Las salidas hacia otros sistemas son estrictas y validadas?
### Métricas
- Batería de entradas por campo: teléfono (`612345678`, `612 34 56 78`, `+34 612-345-678`, `(612) 345 678`), fechas (`1/2/26`, `01-02-2026`, `2 feb 2026`), correo con mayúsculas o espacio final, nombres (`María-José O'Neil`, `李小龍`, un solo nombre, 60 caracteres), IBAN y código postal con espacios, pegado en todos los campos. Registrar rechazos y si el mensaje sugiere corrección.
- Analítica de formularios: errores de validación por campo, correcciones por campo, abandono tras error.
- Contenido extremo: 200 % y 400 % de zoom, traducciones largas, RTL, datos vacíos.
- IA/voz: tasa de "no te he entendido" sobre un conjunto de paráfrasis por intención; porcentaje de salidas estructuradas conformes al esquema.

## Relaciones
- Refuerza / se apoya en: SIS-03 Ley de Tesler — el sistema absorbe la complejidad de la traducción.
- Refuerza / se apoya en: ACC-04 Paradoja del usuario activo — quien no lee instrucciones de formato necesita tolerancia.
- Refuerza / se apoya en: SIS-02 Modelo mental — aceptar el formato que la persona tiene en la cabeza.
- Refuerza / se apoya en: MEM-01 Carga cognitiva / MEM-02 Memoria de trabajo — no obligar a recordar formatos.
- Refuerza / se apoya en: SIS-01 Ley de Jakob — formatos convencionales del *locale*.
- Refuerza / se apoya en: MOT-04 Parkinson / ACC-02 Doherty — menos correcciones, menos tiempo por tarea.
- Tensiona con: seguridad y precisión — ambigüedad y errores silenciosos (crítica de RFC 9413); resolución: tolerante en la forma, explícito en el significado (T8).
- Tensiona con: SIS-04 Navaja de Occam — la tolerancia añade complejidad de implementación y pruebas; acotarla a las variaciones frecuentes (T1).
- Tensiona con: PER-02 Ley de semejanza — en sistemas de diseño, aceptar cualquier variante de componente erosiona la consistencia.
- Se confunde a menudo con: "el cliente siempre tiene razón" o con aceptar todo — Postel exige límites claros y salida estricta.

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/postels-law/ — síntesis divulgativa.
- Primarias:
  - Postel, J. (ed.) (1980). RFC 760, DoD Standard Internet Protocol: https://www.rfc-editor.org/rfc/rfc760.html
  - Postel, J. (ed.) (1980). RFC 761, DoD Standard Transmission Control Protocol: https://www.rfc-editor.org/rfc/rfc761.html
  - Postel, J. (ed.) (1981). RFC 793, Transmission Control Protocol: https://www.rfc-editor.org/rfc/rfc793.html
  - Braden, R. (ed.) (1989). RFC 1122, Requirements for Internet Hosts — Communication Layers: https://www.rfc-editor.org/rfc/rfc1122.html
  - Rose, M. (2001). RFC 3117, On the Design of Application Protocols: https://www.rfc-editor.org/rfc/rfc3117.html
  - Allman, E. (2011). The Robustness Principle Reconsidered. *ACM Queue*, 9(6), 40–47. doi:10.1145/1989748.1999945 (también en *CACM*, 54(8), 40–45; texto no accesible)
  - Thomson, M. y Schinazi, D. (2023). RFC 9413, Maintaining Robust Protocols: https://www.rfc-editor.org/rfc/rfc9413.html
  - W3C. WCAG 2.2 Understanding 3.3.3 Error Suggestion: https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html
- Secundarias consultadas:
  - Mullican, L. (2013). Your Website has Two Faces. *A List Apart*: https://alistapart.com/article/your-website-has-two-faces
  - Keith, J. (2018). Robustness and least power. *Adactio*: https://adactio.com/journal/14327
  - Garrity, S. (2018). Design with Difficult Data. *A List Apart*: https://alistapart.com/article/design-with-difficult-data/
  - https://en.wikipedia.org/wiki/Robustness_principle
  - No accesibles: Boulton (2016), Design Systems and Postel's Law (404).
