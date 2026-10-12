# H1 · Auditar una interfaz o flujo

**Objetivo:** detectar problemas de UX con base en las leyes, priorizarlos y proponer
correcciones verificables.
**Entradas posibles:** capturas, URL descrita, prototipo, código, descripción textual, datos de analítica.
**Salida:** informe con `07-plantillas/informe-auditoria.md`.

---

## Paso 0 · Encuadre (1 minuto)

Fija (o supón y declara) estos factores; cambian qué leyes pesan más:

| Factor | Pregunta | Leyes que modula |
|---|---|---|
| Persona | ¿Novata, ocasional, experta? | Jakob, Hick (expertos memorizan), Usuario activo, Flow |
| Tarea | ¿Cuál es la tarea principal y cómo se mide el éxito? | Pareto, Selección de foco (Atención selectiva) |
| Frecuencia | ¿Uso diario o esporádico? | Tesler, Chunking, Memoria de trabajo |
| Dispositivo y modalidad | ¿Táctil, puntero, teclado, voz, conversacional? | Fitts, Doherty, Postel |
| Contexto | ¿Prisa, distracción, estrés, entorno público? | Carga cognitiva, Atención selectiva |
| Criticidad | ¿Qué cuesta un error (dinero, salud, datos)? | Postel, Sesgos, Hick (respuesta crítica) |

## Paso 1 · Recorrido por el ciclo de interacción

Recorre el flujo **como la persona usuaria**, pantalla a pantalla, y en cada una aplica las
lentes en el orden del ciclo (`00-indice/mapa-global.md` §2):

1. **SIS – Expectativas:** ¿Se parece a lo que la persona ya conoce? ¿El modelo del sistema
   (cómo funciona por dentro) se filtra a la interfaz? ¿Quién carga la complejidad?
2. **PER – Percepción:** ¿La agrupación visual (espacios, contenedores, colores, líneas)
   coincide con la agrupación lógica? ¿Qué destaca? ¿Lo que destaca es lo importante?
   ¿Hay algo con aspecto de anuncio?
3. **MEM – Comprensión:** ¿Cuántas cosas debe sostener a la vez? ¿Debe recordar algo de
   una pantalla anterior? ¿El contenido está fragmentado? ¿Lo clave está al principio o al final?
4. **DEC – Decisión:** ¿Cuántas opciones hay y qué tan comparables son? ¿Hay
   recomendación o valor por defecto razonable? ¿Hay sesgos explotados o encuadres engañosos?
5. **ACC – Acción:** ¿Tamaño y distancia de los objetivos? ¿Respuesta < 400 ms o
   feedback inmediato? ¿Acepta formatos variados de entrada? ¿Se puede usar sin leer instrucciones?
6. **MOT – Experiencia en el tiempo:** ¿Se ve el progreso? ¿Hay picos negativos
   (errores, esperas, sorpresas de precio)? ¿Cómo termina? ¿Se puede retomar lo inacabado?

Usa `05-checklists/checklist-auditoria.md` como red de seguridad al terminar el recorrido
(no como sustituto del recorrido). **Rinde cuentas de todos los puntos** (✔ / ✘ / N/A o
"no evaluable con este material"); un punto sin marcar es un punto no revisado.

## Paso 2 · Registrar hallazgos

Cada hallazgo: **observación concreta → ley(es) + mecanismo → impacto en la persona →
recomendación → cómo verificar**. Evita hallazgos sin evidencia observable.

## Paso 3 · Severidad

Escala 0–4 (adaptada de Nielsen), calculada sobre tres factores:

- **Frecuencia:** ¿ocurre a muchas personas o rara vez?
- **Impacto:** ¿molestia, retraso, error recuperable, bloqueo, daño?
- **Persistencia:** ¿se supera una vez aprendido o molesta siempre?

| Severidad | Etiqueta | Criterio orientativo |
|---|---|---|
| 4 | **Crítico** | Bloquea la tarea principal, provoca errores con coste o excluye a personas (accesibilidad). |
| 3 | **Alto** | Retrasa o confunde a muchas personas en la tarea principal; abandono probable. |
| 2 | **Medio** | Fricción notable en tareas secundarias o a parte de las personas. |
| 1 | **Bajo** | Cosmético o de pulido; mejora percepción. |
| 0 | — | No es un problema de usabilidad. |

Los problemas éticos (patrones oscuros) y de accesibilidad bloqueante son **4** por defecto.

## Paso 4 · Priorizar (Pareto)

Ordena por severidad y luego por **esfuerzo inverso**. Marca explícitamente el pequeño
conjunto de cambios ("quick wins" de alta severidad) que resuelve la mayor parte del
problema. Agrupa hallazgos con la misma causa raíz.

## Paso 5 · Comprobar tensiones y efectos secundarios

Para cada recomendación, consulta `02-relaciones/tensiones.md`: ¿qué podría empeorar?
(p. ej. dividir un formulario en pasos reduce carga pero añade navegación.) Anótalo.

## Paso 6 · Entregar

Usa `07-plantillas/informe-auditoria.md`. Incluye supuestos, límites del análisis
(p. ej. "sólo capturas estáticas: no se evalúa rendimiento") y plan de validación.

---

## Límites honestos de una auditoría por expertos/IA

- Encuentra muchos problemas, pero también **falsos positivos** y no detecta lo que sólo
  aparece con personas reales (vocabulario, modelos mentales concretos, contexto real).
- Con capturas estáticas no se pueden evaluar tiempos de respuesta, animaciones,
  comportamiento de foco o lectores de pantalla: dilo.
- Recomienda siempre al menos una validación ligera (5 personas en test moderado
  suelen descubrir los problemas más graves de un flujo concreto — heurística de Nielsen,
  no garantía).
