# Formularios y entrada de datos

**Leyes clave:** MEM-01 Carga cognitiva · MEM-02 Memoria de trabajo · MEM-04 Chunking ·
ACC-03 Postel · ACC-01 Fitts · PER-01 Proximidad · PER-03 Región común · MOT-02 Gradiente
de meta · MOT-03 Zeigarnik · MOT-04 Parkinson · SIS-03 Tesler · DEC-03 Sesgos (defaults)

## Reglas

| # | Regla | Ley |
|---|---|---|
| F1 | Pide sólo lo imprescindible; cada campo debe justificar su existencia. Lo deducible (ciudad por código postal, tipo de tarjeta por número) lo deduce el sistema. | SIS-04, SIS-03 |
| F2 | Etiqueta visible y persistente encima del campo; nunca sólo placeholder. | MEM-02 |
| F3 | Etiqueta pegada a su campo y más lejos del campo anterior (espacio interno < espacio entre grupos). | PER-01 |
| F4 | Agrupa campos relacionados con `fieldset` + `legend` o contenedor (dirección, pago). | PER-03, MEM-04 |
| F5 | Una columna para formularios lineales (el ojo sigue una ruta; menos saltos). | PER-05, ACC-01 |
| F6 | Acepta formatos variados (espacios, guiones, mayúsculas, prefijos), normaliza y muestra la interpretación. | ACC-03 |
| F7 | Valida en línea al salir del campo (no mientras se escribe el primer carácter), mensaje junto al campo que explique **cómo arreglarlo**. | ACC-03, MEM-02 |
| F8 | Usa `autocomplete`, `inputmode` y tipos correctos; permite pegar; muestra contraseña. | MOT-04, ACC-03 |
| F9 | Fragmenta datos largos en grupos visuales (IBAN, tarjeta, teléfono) sin obligar a escribir en varias casillas. | MEM-04, ACC-03 |
| F10 | Si es largo: pasos por unidades de significado, con progreso visible y estimación de tiempo. | MOT-02, MOT-04, T5 |
| F11 | Guarda el progreso (borrador) y permite retomar. | MOT-03 |
| F12 | Defaults inteligentes y honestos (país por localización, opción más común). | DEC-03, SIS-03 |
| F13 | Botón principal amplio, claramente primario, cerca del último campo; secundario con menos peso. | ACC-01, PER-07 |
| F14 | No pidas el mismo dato dos veces (rellénalo). | MEM-02 · WCAG 3.3.7 |
| F15 | Confirmación final clara con resumen y siguiente paso: es el "final" de la regla pico-final. | MOT-05 |

## Anti-patrones

- Placeholder como etiqueta; errores sólo arriba del formulario tras enviar; reset que borra todo.
- Teléfono que rechaza espacios; fecha con un único formato rígido; contraseña con reglas ocultas.
- Captchas cognitivos o limitaciones de tiempo injustificadas (WCAG 3.3.8, 2.2.1).
- Casillas de marketing preseleccionadas (patrón oscuro).

## Métricas

Tasa de finalización, abandono por campo, errores por campo, tiempo hasta completar,
correcciones, tickets relacionados.
