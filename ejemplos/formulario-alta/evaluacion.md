# Evaluación de la prueba ciega (12/10/2026)

**Resultado: 23,5 / 24 defectos sembrados detectados**, todos con ley pertinente, mecanismo,
recomendación concreta y forma de verificarlo.

| Defecto | Detectado | Dónde |
|---|---|---|
| D1 Placeholder como etiqueta | ✔ | H6 |
| D2 Dos columnas / espaciado uniforme | ✔ | H6, H11 |
| D3 Teléfono rígido | ✔ | H5 |
| D4 Fecha rígida | ✔ | H5 |
| D5 Campos innecesarios | ✔ | H9 |
| D6 Datos deducibles / país sin default | ✔ | H9 |
| D7 Email y contraseña repetidos | ✔ | H9 (3.3.7) |
| D8 Reglas de contraseña ocultas | ✔ | H5 |
| D9 Error genérico que borra datos | ✔ | H5 |
| D10 Casillas premarcadas (marketing, cesión, seguro de pago) | ✔ | H1 |
| D11 Confirmshaming | ✔ | H1 |
| D12 Cuenta atrás falsa y parpadeo | ✔ | H2 (2.2.2) |
| D13 Jerarquía de botones invertida | ✔ | H3 |
| D14 Objetivos pequeños | ✔ | H1, H3 |
| D15 9 planes sin precio ni comparación | ✔ | H4 |
| D16 Condiciones en letra pequeña | ✔ | H4 |
| D17 Requisito crítico con aspecto de anuncio | ✔ | H10 |
| D18 Captcha aritmético | ✔ | H7 |
| D19 Sin autocomplete / tipos | ✔ | H5 |
| D20 Espera de 5 s sin indicador / doble envío | ✔ | H8 |
| D21 Final con alert y redirección | ✔ | H8 |
| D22 Sin progreso ni estimación de tiempo | ½ | Argumenta que una sola pantalla es adecuada (T5); no propone estimar la duración |
| D23 Obligatorio sólo con asterisco rojo; títulos grises | ✔ | H6 |
| D24 Botón de envío alejado del último campo | ✔ | H3 |

**Hallazgos reales no sembrados** (el formulario de verdad los tiene): `pw2` nunca se compara
con `pw`; los campos con * no se validan; "¿Cómo nos conoció?" envía la pregunta como respuesta;
el layout no hace `flex-wrap` (en 360 px los campos quedan de ~120 px); el captcha con la
respuesta en el JS no protege de bots.

**Comportamiento respecto al sistema:** eligió H1 (+ H8), siguió los pasos del proceso, aplicó la
severidad y la regla "ética = 4", declaró supuestos y límites, citó niveles de evidencia y
corrigió por su cuenta los malos usos (Parkinson para justificar urgencia; la cifra de 400 ms
de Doherty; Hick con su matiz de búsqueda lineal). Leyó 26 archivos con carga progresiva.

**Fallos del sistema detectados y corregidos tras la prueba:**
1. La tabla de sesgos de DEC-03 usaba una subescala A/B/C no conectada con E1–H → ahora se mapea explícitamente.
2. El auditor dejó 16 puntos de la checklist sin marcar → `04-procesos/auditar.md` y la plantilla exigen ahora rendir cuentas de todos.

---

# Segunda prueba: sólo con el prompt compacto (12/10/2026)

Simula una plataforma que sólo admite un prompt de sistema (GPT sin archivos, Gem, modelo
local): el modelo recibió `adaptadores/prompt-sistema-compacto.md` y el HTML, sin acceso a la carpeta.

| | Sistema completo | Prompt compacto v1 | Prompt compacto v2 |
|---|---|---|---|
| Defectos sembrados | **23,5 / 24** | 22 / 24 | 22,5 / 24 |
| Fallos | D22 ½ | D22 ✘, D24 ✘ | D22 ½, D24 ✘ |
| Hallazgos reales extra | 5 | 4 | 6 |
| Escala de severidad 0–4 | ✔ | ✘ (etiquetas libres) | ✔ |
| "Lo que funciona" | ✔ | ✘ | ✔ |
| Plan de validación con umbrales | ✔ | Parcial (próximos pasos) | ✔ |
| Reflujo móvil (320 px) | ✔ | ✘ | ✔ |
| Niveles de evidencia y matices (Hick, sobrecarga, Doherty, Pareto) | ✔ | ✔ | ✔ |
| Patrones oscuros a severidad máxima | ✔ | ✔ | ✔ |
| Extensión | 5.870 palabras | 2.840 | 4.020 |
| Contexto que consume | ~26 archivos | ~3.900 tokens | ~4.100 tokens |

**Cambio entre v1 y v2:** se añadió al prompt compacto la checklist rápida de 10 preguntas
(ya existente en `05-checklists/checklist-rapida.md`) como repaso final obligatorio, y el
formato completo del informe (severidad 0–4, conservar, límites, plan de validación).
No se ajustó a los defectos concretos de esta prueba (D24 sigue sin detectarse).

**Conclusión:** el prompt compacto rinde casi como el sistema completo en detección
(22,5 frente a 23,5) y en rigor de evidencia y ética. El sistema completo aporta más
profundidad (cifras de contraste, citas de estudios concretos, trazabilidad por línea y la
checklist de 66 puntos). Para auditorías formales conviene el sistema completo; para
asistentes de uso diario basta con el compacto.
