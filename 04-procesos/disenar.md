# H2 · Diseñar o proponer una solución guiada por las leyes

**Objetivo:** pasar de un problema o requisito a una propuesta de interfaz/flujo
justificada ley a ley.
**Salida:** propuesta estructurada (descripción, wireframe textual o código) + racional + plan de validación.

---

## Paso 1 · Definir el trabajo a resolver

- ¿Quién? ¿Qué intenta conseguir? ¿Qué cuenta como éxito (métrica)?
- ¿Cuál es el **20 % de tareas** que concentra el uso (SIS-05 Pareto)? Diseña primero para
  ellas; el resto, accesible pero secundario.

## Paso 2 · Partir de lo conocido (SIS-01 Jakob, SIS-02 Modelo mental)

- Identifica el **patrón convencional** para este problema (búsqueda, carrito, ajustes,
  chat, tabla de datos…). Empieza por él.
- Desvíate sólo si puedes nombrar la ventaja concreta y cómo enseñarás el cambio sin
  manual (ACC-04).

## Paso 3 · Decidir dónde vive la complejidad (SIS-03 Tesler, SIS-04 Occam)

- Lista toda la complejidad inherente (datos que hacen falta, reglas, excepciones).
- Para cada pieza: ¿la puede resolver el sistema (default inteligente, autocompletado,
  inferencia, memoria del sistema)? Si sí, muévela al sistema.
- Elimina todo lo que no contribuya a la tarea (Occam). Lo que quede: **divulgación
  progresiva** (lo básico visible, lo avanzado a un paso).

## Paso 4 · Estructurar la decisión (DEC-01, DEC-02, DEC-03)

- Reduce opciones simultáneas a las relevantes para *este* momento.
- Ofrece un **valor por defecto honesto** o una opción recomendada destacada (PER-07).
- Si hay que comparar, habilita la comparación lado a lado con los mismos atributos.
- Revisa encuadres, anclas y defaults contra `06-etica-accesibilidad/etica-y-patrones-oscuros.md`.

## Paso 5 · Componer la percepción (PER-01…07, MEM-04, MEM-05)

- Agrupa con espacio primero (proximidad), luego con contenedores (región común) y sólo
  si hace falta con líneas (conectividad). La agrupación visual debe **coincidir** con la lógica.
- Mismo aspecto = misma función (semejanza); distinto aspecto = distinta función.
- **Un** elemento destacado por zona (Von Restorff); destaca la acción principal.
- Coloca lo crítico al principio y al final de las secuencias (posición serial).
- Formas simples y reconocibles (Prägnanz); nada que parezca publicidad (atención selectiva).

## Paso 6 · Hacer fácil la acción (ACC-01…04)

- Objetivos grandes y cercanos a donde está la atención/el pulgar (Fitts; mínimo WCAG
  2.5.8: 24×24 px CSS; recomendado 44–48 px en táctil).
- Respuesta perceptible < 100 ms a cada acción; trabajo largo con indicador (Doherty).
- Entrada tolerante: acepta formatos variados, normaliza, valida en línea con mensajes claros (Postel).
- Ayuda contextual en el punto de uso, no en un manual (Usuario activo).

## Paso 7 · Diseñar el recorrido en el tiempo (MOT-01…05)

- Progreso visible y honesto; el primer paso ya cuenta (gradiente de meta).
- Permite pausar y retomar; recuerda el estado (Zeigarnik, memoria del sistema).
- Fija expectativas de duración realistas y cúmplelas o mejóralas (Parkinson).
- Identifica el **pico** probable (positivo o negativo) y el **final**; diseña ambos a
  propósito (pico-final). Elimina picos negativos evitables (errores, sorpresas de coste).
- Ajusta el reto a la habilidad; feedback inmediato; sin fricción innecesaria (flow).

## Paso 8 · Pulir (DEC-04 Estética-usabilidad)

Cuida la calidad visual: aumenta la confianza y la tolerancia a pequeños fallos. Pero no la
uses para tapar problemas: valida con tareas, no con opiniones.

## Paso 9 · Racional y validación

Entrega cada decisión con: **ley → mecanismo → decisión → métrica**. Añade las tensiones
asumidas y un plan de validación (`04-procesos/validar.md`).
