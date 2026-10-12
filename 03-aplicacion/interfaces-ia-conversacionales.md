# Interfaces conversacionales y productos con IA

Las leyes de UX nacieron antes de la IA generativa, pero aplican con fuerza — y algunas
cambian de forma. Esta guía es especialmente relevante si el propio modelo que la lee
forma parte de un producto.

**Leyes clave:** SIS-02 Modelo mental · SIS-01 Jakob · ACC-04 Usuario activo · ACC-02
Doherty · ACC-03 Postel · DEC-03 Sesgos (automatización, anclaje) · MEM-02 Memoria de
trabajo · MEM-01 Carga cognitiva · DEC-01/02 Hick y sobrecarga · MOT-05 Pico-final ·
SIS-03 Tesler · DEC-04 Estética-usabilidad

## Problemas característicos y leyes

| Problema | Ley | Respuesta de diseño |
|---|---|---|
| **El "lienzo en blanco"**: no saben qué pedir ni qué puede hacer el sistema | SIS-02, ACC-04 | Sugerencias de inicio contextuales, ejemplos, capacidades y límites explícitos |
| **Modelo mental erróneo** (lo creen un buscador, una persona, una base de datos infalible) | SIS-02, DEC-03 | Comunicar qué es y qué no; mostrar fuentes; indicar incertidumbre; no antropomorfizar en exceso |
| **Sesgo de automatización / exceso de confianza** | DEC-03, DEC-04 | Fuentes verificables, señales de confianza calibradas, revisión humana en acciones con consecuencias |
| **Respuestas largas que saturan** | MEM-01, MEM-04, MEM-05 | Respuesta directa primero, luego detalle; estructura con encabezados/listas; resumen al final si es largo |
| **Latencia** de generación | ACC-02 | Streaming del texto, indicador de pasos ("buscando…", "leyendo 3 documentos"), cancelar/detener |
| **Entrada ambigua** | ACC-03 | Interpretar con generosidad, explicitar la interpretación cuando haya ambigüedad relevante, preguntar sólo si cambia el resultado |
| **Recordar el contexto de la conversación** | MEM-02, SIS-03 | Que el sistema mantenga y muestre el contexto (archivos, preferencias, memoria) en lugar de que la persona lo repita |
| **Demasiadas opciones de respuesta/acción** | DEC-01, DEC-02 | 2–4 sugerencias de seguimiento como máximo, relevantes |
| **Acciones del agente con consecuencias** | DEC-03, MOT-05, ACC-03 | Vista previa y confirmación de acciones irreversibles, deshacer, registro de lo realizado |
| **Familiaridad de la interfaz** | SIS-01 | Respeta convenciones ya establecidas (campo de entrada abajo, historial, editar/regenerar, copiar) |
| **Final de la tarea** | MOT-05 | Cerrar con resultado claro y siguiente paso; recuperar errores con transparencia |

## Reglas

1. Hacer visibles **capacidades, límites y estado** (qué sabe, qué hace ahora, qué no puede).
2. **Reconocer mejor que recordar:** ofrecer sugerencias, plantillas y acciones en lugar de exigir prompts perfectos.
3. **Control y reversibilidad:** detener la generación, editar la petición, deshacer acciones.
4. **Transparencia calibrada:** citar fuentes, distinguir hechos de inferencias, señalar incertidumbre sin saturar.
5. **Progresividad:** respuesta breve por defecto, profundidad bajo demanda.
6. **Ética reforzada:** no explotar la confianza ni la antropomorfización; no simular emociones para retener.

## Métricas

Éxito de tarea, reformulaciones por objetivo, tasa de abandono tras primera respuesta,
correcciones/regeneraciones, confianza calibrada (confianza declarada vs. exactitud),
acciones deshechas.
