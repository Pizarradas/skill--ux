# H8 · Revisar código de interfaz con lentes de UX

**Objetivo:** detectar en HTML/CSS/JS (o frameworks) problemas de UX que se ven en el código
antes de verse en pantalla.

## Qué buscar en el código, por ley

| Ley | Señales en el código | Recomendación típica |
|---|---|---|
| ACC-01 Fitts | Botones/enlaces con `padding` mínimo, iconos de 16 px sin área ampliada, objetivos muy juntos | `min-block-size`/`min-inline-size` ≥ 44px en táctil (mínimo 24px, WCAG 2.5.8), ampliar área con padding o pseudo-elemento, separación ≥ 8px |
| ACC-02 Doherty | `await` sin estado de carga, botones sin estado `aria-busy`/deshabilitado durante envío, sin UI optimista, listas enormes sin virtualizar, imágenes sin dimensiones (saltos de layout) | Feedback inmediato (< 100 ms), skeletons, UI optimista con reversión, indicadores con progreso real cuando > 1 s |
| ACC-03 Postel | `pattern` rígidos, rechazo de espacios/guiones en teléfonos o tarjetas, `type="number"` para datos que no son cantidades, fechas en formato único | Normalizar (`trim`, quitar separadores), `inputmode`, `autocomplete` correcto, validación en línea con mensajes que digan cómo arreglarlo |
| MEM-02 Memoria de trabajo | Mensajes de error genéricos o lejos del campo, placeholder como única etiqueta, datos que hay que copiar de otra pantalla | `<label>` visible persistente, `aria-describedby` para ayuda/errores junto al campo, resúmenes y datos arrastrados entre pasos |
| PER-01…04 Gestalt | Espaciados arbitrarios (márgenes iguales dentro y entre grupos), `<div>` sin agrupación semántica | Tokens de espaciado con escala (espacio interno < externo), `<fieldset>`/`<legend>`, `<section>` con encabezado |
| PER-02 Semejanza | Enlaces sin subrayado ni diferencia más allá del color, estilos de botón distintos para la misma acción | Componentes únicos por función; enlaces distinguibles sin depender sólo del color (WCAG 1.4.1) |
| PER-07 Von Restorff | Varias variantes "primary" en la misma vista | Una acción primaria por contexto |
| DEC-01/02 | `<select>` con cientos de opciones sin búsqueda; filtros sin recuento | Combobox con búsqueda, agrupación `<optgroup>`, defaults, recuentos |
| SIS-01 Jakob | Controles personalizados que imitan nativos pero se comportan distinto (scroll secuestrado, checkbox no accesible) | Usar elementos nativos o patrones ARIA APG con comportamiento estándar de teclado |
| MOT-03/02 | Formularios largos sin guardado; progreso sin indicador | Autoguardado (borrador), indicador de pasos `aria-current="step"` |
| Movimiento | Animaciones sin respetar preferencias | `@media (prefers-reduced-motion: reduce)` |

## Formato de salida

Hallazgos con `archivo:línea`, ley, impacto en la persona usuaria y parche sugerido.
Prioriza por severidad (`04-procesos/auditar.md`).
