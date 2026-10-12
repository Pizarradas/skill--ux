# Móvil e interfaces táctiles

**Leyes clave:** ACC-01 Fitts · SIS-01 Jakob (convenciones de plataforma) · ACC-02 Doherty ·
DEC-01 Hick · PER-06 Atención selectiva · ACC-03 Postel · MEM-01 Carga cognitiva

## Tamaños de objetivo de referencia

| Fuente | Referencia |
|---|---|
| WCAG 2.2 · 2.5.8 (AA) | 24×24 px CSS (o espaciado que garantice un círculo de 24 px sin solaparse) |
| WCAG 2.2 · 2.5.5 (AAA) | 44×44 px CSS |
| Apple Human Interface Guidelines | iOS/iPadOS: 44×44 pt tamaño por defecto; 28×28 pt mínimo absoluto (visionOS 60×60 pt) |
| Material Design | 48×48 dp (≈ 9 mm), separación ≥ 8 dp |

## Reglas

| # | Regla | Ley |
|---|---|---|
| M1 | Objetivos ≥ 44–48 px con separación; ampliar área táctil de iconos pequeños. | ACC-01 |
| M2 | No diseñes para un único "mapa del pulgar": la gente cambia de agarre constantemente (Hoober). Lo frecuente, en zonas fáciles y estables (centro de la pantalla y barras inferiores convencionales); objetivos más grandes en bordes y esquinas (Hoober sugiere ≈ 7 mm en el centro y ≈ 12 mm en bordes); destructivas lejos de las frecuentes. | ACC-01 |
| M3 | Respeta gestos y patrones de la plataforma (atrás, deslizar, hojas inferiores). | SIS-01 |
| M4 | Todo gesto tiene una alternativa visible (botón). | ACC-04 · WCAG 2.5.7 |
| M5 | Teclado adecuado (`inputmode`), autocompletado, sin campos innecesarios. | ACC-03, MOT-04 |
| M6 | Una acción principal por pantalla; navegación inferior con 3–5 destinos. | DEC-01, PER-07 |
| M7 | Contenido y controles resilientes a interrupciones (llamadas, cambio de app): guardar estado. | MOT-03 |
| M8 | Feedback táctil/visual inmediato; tolera redes lentas (estados offline). | ACC-02 |

## Anti-patrones

Enlaces de texto muy juntos, cierres de modal diminutos en esquinas, carruseles con puntos
como única navegación, gestos ocultos sin pista.
