# Rendimiento percibido, estados de carga y feedback

**Leyes clave:** ACC-02 Umbral de Doherty · MOT-01 Flow · MOT-02 Gradiente de meta ·
MOT-05 Pico-final · PER-06 Atención selectiva · MOT-04 Parkinson

## Umbrales de referencia

| Tiempo | Percepción (Miller 1968; Card, Robertson y Mackinlay 1991; Nielsen 1993) | Qué hacer |
|---|---|---|
| ≤ 100 ms | Instantáneo; sensación de manipulación directa | Feedback visual de cada acción (estado pulsado, cambio optimista) |
| ≤ 400 ms | Umbral de Doherty (regla práctica derivada de Doherty y Thadhani, IBM, 1982; la cifra no aparece literal en el documento): la interacción no interrumpe el pensamiento | Objetivo para respuestas de interacción habituales |
| ≤ 1 s | Se nota la demora pero se mantiene el hilo | Sin indicador o con indicador sutil |
| 1–10 s | La atención empieza a irse | Indicador de actividad; skeleton; si > ~2–3 s, progreso |
| > 10 s | Se pierde la atención; cambian de tarea | Barra de progreso con estimación, posibilidad de seguir trabajando, aviso al terminar |

Web (Core Web Vitals): INP "bueno" ≤ 200 ms en el percentil 75; LCP ≤ 2,5 s; CLS ≤ 0,1.

## Reglas

| # | Regla | Ley |
|---|---|---|
| R1 | Cada acción produce feedback perceptible inmediato, aunque el resultado tarde. | ACC-02 |
| R2 | UI optimista para acciones con alta probabilidad de éxito (me gusta, marcar, mover), con reversión clara si fallan. | ACC-02, MOT-01 |
| R3 | Skeletons con la forma real del contenido para cargas de 1–3 s; evita saltos de layout. | ACC-02, PER-05 |
| R4 | Barras de progreso deterministas para procesos largos; que no se detengan al 99 %. Las barras que aceleran al final se perciben más rápidas (Harrison et al., 2007/2010). | MOT-02, MOT-05 |
| R5 | Carga progresiva: primero lo que la persona necesita para empezar. | SIS-05 |
| R6 | En procesos largos, permite seguir con otra cosa y notifica al terminar. | MOT-01 |
| R7 | Respuestas generadas por IA: transmite (streaming) el texto en cuanto esté disponible; muestra en qué está trabajando si hay pasos largos. | ACC-02 |
| R8 | Estados vacío, cargando, error, parcial y éxito diseñados para cada vista. | MOT-05 |
| R9 | Anuncia los cambios de estado a tecnologías de apoyo (WCAG 4.1.3). | Accesibilidad |

## Anti-patrones

Spinners indefinidos sin contexto; pantallas en blanco; animaciones largas que retrasan
la tarea; demoras artificiales en tareas rutinarias; bloquear toda la UI por una carga parcial.
