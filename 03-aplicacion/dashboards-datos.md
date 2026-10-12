# Dashboards, tablas y visualización de datos

**Leyes clave:** PER-01…05 Gestalt · PER-06 Atención selectiva · PER-07 Von Restorff ·
MEM-01 Carga cognitiva · MEM-02 Memoria de trabajo · MEM-04 Chunking · SIS-05 Pareto ·
DEC-01 Hick · ACC-02 Doherty · MOT-01 Flow

## Reglas

| # | Regla | Ley |
|---|---|---|
| D1 | Empieza por las preguntas que el dashboard responde; muestra primero las 3–5 métricas que guían decisiones. | SIS-05, PER-06 |
| D2 | Agrupa métricas relacionadas en regiones con título; espacio interior < exterior. | PER-01, PER-03, MEM-04 |
| D3 | Mismo color = misma serie/categoría en todo el producto; no reutilices colores con otro significado. | PER-02 |
| D4 | Color de alerta sólo para lo que requiere acción; si todo es rojo, nada lo es. Acompaña con icono/texto. | PER-07 · WCAG 1.4.1 |
| D5 | Cada número con contexto (comparación con periodo anterior, objetivo, unidad): la persona no debería recordar el dato de referencia. | MEM-02 |
| D6 | Líneas en series temporales para conectar puntos de la misma serie; leyendas directas junto a la línea. | PER-04, MEM-02 |
| D7 | Tablas: alineación numérica a la derecha, cifras tabulares, ordenación y filtros, cabeceras fijas. | PER-05, MEM-02 |
| D8 | Divulgación progresiva: resumen → detalle por clic. | DEC-01, SIS-03 |
| D9 | Interacciones de filtrado con respuesta < 400 ms o feedback inmediato; mantener el contexto al recargar. | ACC-02, MOT-01 |
| D10 | Para usuarios expertos, densidad alta es aceptable si la estructura es clara; ofrece vistas guardadas y atajos. | SIS-03, MOT-01 |

## Anti-patrones

Gráficos decorativos (3D, tartas con muchas porciones), métricas de vanidad, paneles que
obligan a comparar entre pestañas, ejes truncados engañosos.

## Métricas

Tiempo para responder preguntas clave, exactitud de interpretación (test), frecuencia de
uso, exportaciones (señal de que el dashboard no basta).
