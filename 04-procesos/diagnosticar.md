# H5 · Diagnosticar un problema a partir de síntomas o datos

**Objetivo:** ir del síntoma (métrica, queja, observación) a hipótesis causales
fundamentadas en las leyes, y de ahí a experimentos.

## Proceso

1. **Describe el síntoma con precisión**: dónde (pantalla/paso), quién (segmento,
   dispositivo), cuándo (desde qué cambio), cuánto (magnitud).
2. **Consulta el router** `03-aplicacion/por-sintoma.md` para obtener leyes candidatas.
3. **Genera 3–5 hipótesis** del tipo: *"Las personas [comportamiento] porque [mecanismo
   de la ley X] provocado por [elemento concreto]"*.
4. **Discrimina**: para cada hipótesis, ¿qué otro dato la confirmaría o descartaría?
   (mapas de clics, grabaciones, embudos por dispositivo, tiempos por paso, búsquedas
   internas, tickets de soporte, test rápido).
5. **Prioriza** por probabilidad × impacto × coste de comprobar.
6. **Propón el cambio mínimo** que pondría a prueba la hipótesis principal y su métrica.

## Señales → familias (atajo)

| Señal en datos | Familia probable |
|---|---|
| Clics en elementos no interactivos; nadie pulsa lo interactivo | PER (semejanza, Von Restorff, atención selectiva) |
| Mucho tiempo en una pantalla de elección, luego abandono | DEC (Hick, sobrecarga) |
| Errores de entrada, validaciones fallidas repetidas | ACC-03 Postel, MEM-02 |
| Taps erróneos, zoom, "rage clicks" en móvil | ACC-01 Fitts, ACC-02 Doherty |
| Abandono a mitad de proceso largo | MOT-02, MOT-03, MEM-01 |
| Valoración final baja pese a buen éxito de tarea | MOT-05 pico-final |
| Usuarios veteranos se quejan tras un rediseño | SIS-01 Jakob, SIS-02 |
| Uso concentrado en pocas funciones; menús saturados | SIS-05 Pareto, SIS-04 Occam |
| Búsqueda interna de cosas que están en la página | PER-06 atención selectiva, PER-01…04 |

## Advertencia

Correlación no es causa: una ley **explica plausiblemente**; el experimento **confirma**.
