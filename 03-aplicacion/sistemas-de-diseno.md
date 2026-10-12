# Sistemas de diseño

Un sistema de diseño es la forma de **codificar las leyes de UX una sola vez** para que
todo el producto las cumpla por defecto.

| Ley | Qué codificar en el sistema |
|---|---|
| PER-01 Proximidad | Escala de espaciado con relaciones (interno < entre elementos < entre grupos < entre secciones). |
| PER-02 Semejanza | Un componente por función; variantes con significado (primario, secundario, destructivo) que no se mezclan. |
| PER-03 Región común | Superficies/tarjetas con reglas de uso (cuándo contenedor, cuándo sólo espacio). |
| PER-07 Von Restorff | Regla de "una acción primaria por contexto"; tokens de énfasis limitados. |
| PER-06 / WCAG | Contraste, foco visible, estados (hover, foco, activo, deshabilitado, error) para todos los componentes. |
| ACC-01 Fitts | Tamaño mínimo de objetivo como token (p. ej. `--target-min: 44px`) y área táctil ampliada en iconos. |
| ACC-02 Doherty | Componentes con estados de carga, skeleton, UI optimista; duraciones de movimiento cortas (100–300 ms) y `prefers-reduced-motion`. |
| ACC-03 Postel | Campos con normalización y validación estándar (teléfono, fecha, importe, email); mensajes de error con patrón. |
| MEM-02 | Etiquetas persistentes, ayuda y error asociados, migas, resúmenes. |
| SIS-01 Jakob | Comportamientos estándar de teclado y ARIA (WAI-ARIA APG); no reinventar controles nativos. |
| SIS-03 Tesler | Patrones de divulgación progresiva, defaults, autocompletado. |
| DEC-04 Estética | Coherencia tipográfica y de color; la calidad visual consistente genera confianza. |
| MOT-05 | Patrones de confirmación, éxito y recuperación de errores. |
| Ética | Patrones prohibidos documentados (confirmshaming, asimetría de botones de consentimiento…). |

**Postel en sistemas de diseño** (Mark Boulton): los componentes deben **aceptar** contenido
variable (textos largos, traducciones, datos vacíos, imágenes de proporciones distintas) y
**producir** siempre una salida coherente.
