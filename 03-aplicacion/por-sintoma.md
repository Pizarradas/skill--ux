# Router: síntoma → leyes → acciones

Usa esta tabla cuando te describan un **problema** y no una ley. Para cada síntoma:
leyes candidatas (en orden de probabilidad), preguntas que discriminan y primeras acciones.
Después, abre las fichas de las leyes elegidas.

---

## Encontrar y ver

| Síntoma | Leyes candidatas | Preguntas discriminantes | Primeras acciones |
|---|---|---|---|
| "No ven el botón / el aviso" | PER-06, PER-07, PER-02, ACC-01 | ¿Parece un anuncio? ¿Compite con otros énfasis? ¿Se parece a texto no interactivo? ¿Está fuera de la zona de atención de la tarea? | Un solo énfasis; colocarlo en el camino de la tarea; aspecto de control interactivo convencional |
| "Hacen clic en cosas que no son clicables" | PER-02, SIS-01, PER-05 | ¿Qué elementos estáticos parecen botones/enlaces? | Diferenciar estilos interactivo/estático; reservar color de enlace para enlaces |
| "No notan que algo cambió" (error, carrito, estado) | PER-06 (ceguera al cambio), ACC-02 | ¿El cambio ocurre lejos del foco? ¿A la vez que otros cambios? | Feedback junto al punto de acción; animación breve y respetuosa; mensaje de estado accesible |
| "La página parece desordenada / no se entiende la estructura" | PER-01, PER-03, PER-04, PER-05, MEM-04 | ¿El espacio interno de los grupos es menor que el externo? ¿Hay contenedores coherentes? | Escala de espaciado; agrupar con espacio y contenedores; encabezados |
| "Usan la búsqueda para cosas que están en la página" | PER-06, MEM-04, SIS-02 | ¿Las etiquetas usan el vocabulario de la persona? ¿Está bajo el pliegue o en zona de anuncios? | Etiquetas en lenguaje de la persona; reubicar; tree testing |

## Entender y recordar

| Síntoma | Leyes candidatas | Preguntas discriminantes | Primeras acciones |
|---|---|---|---|
| "Se pierden; no saben dónde están ni cómo seguir" | SIS-02, SIS-01, MEM-02, MOT-02 | ¿Hay indicadores de ubicación? ¿La estructura refleja el modelo de la persona o el organigrama? | Migas, estado activo de navegación, pasos visibles; reorganizar IA con card sorting |
| "Vuelven atrás para consultar datos" | MEM-02, MEM-01 | ¿Qué dato necesitan de la pantalla anterior? | Arrastrar el dato (resumen persistente, comparador) |
| "Contenido denso que no leen" | MEM-04, PER-06, MEM-01 | ¿Hay jerarquía de encabezados? ¿Párrafos largos? | Fragmentar, encabezados descriptivos, listas, resumen al inicio |
| "Olvidan lo que vieron en la lista" | MEM-05, MEM-03 | ¿Lo importante está en medio? | Lo importante al principio/final; favoritos/comparar |
| "Errores al introducir códigos, contraseñas, IDs" | MEM-02, ACC-03 | ¿Hay que copiar o recordar? | Pegar permitido, mostrar contraseña, autocompletar, agrupar dígitos (chunking) |

## Decidir

| Síntoma | Leyes candidatas | Preguntas discriminantes | Primeras acciones |
|---|---|---|---|
| "Tardan en elegir; abandonan en la elección (planes, productos)" | DEC-02, DEC-01, DEC-03, PER-07 | ¿Cuántas opciones? ¿Son comparables? ¿Hay recomendación? ¿Expertise en la categoría? | Reducir/estructurar opciones; comparación lado a lado; opción recomendada honesta; filtros |
| "Menú/ajustes inmanejables" | DEC-01, SIS-05, SIS-03, MEM-04 | ¿Qué se usa de verdad (datos)? | Agrupar, priorizar lo frecuente, buscador de ajustes, avanzados a un nivel |
| "Eligen la opción equivocada" | DEC-03 (encuadre, default), PER-02, MEM-05 | ¿El default es el adecuado? ¿Las etiquetas son ambiguas? | Revisar default y textos; describir consecuencias |
| "Desconfían del producto / parece poco serio" | DEC-04, SIS-01, PER-05 | ¿Calidad visual? ¿Inconsistencias? ¿Patrones raros? | Coherencia visual, convenciones, pulido |

## Actuar

| Síntoma | Leyes candidatas | Preguntas discriminantes | Primeras acciones |
|---|---|---|---|
| "Toques erróneos, sobre todo en móvil" | ACC-01, PER-01 | ¿Tamaño y separación de objetivos? ¿Zona alcanzable? | ≥ 44–48 px táctil (mín. 24 px WCAG), separación, acciones en zona del pulgar |
| "Se siente lento" | ACC-02, MOT-01 | ¿Latencia real (INP, TTFB) o falta de feedback? | Feedback < 100 ms, UI optimista, skeletons, progreso real > 1 s, optimizar rendimiento |
| "Rechazos de formulario, validaciones frustrantes" | ACC-03, MEM-02 | ¿Formatos rígidos? ¿Mensajes inútiles? ¿Errores al final? | Aceptar formatos variados, normalizar, validación en línea, mensajes con solución |
| "No usan funciones clave / no descubren" | ACC-04, PER-06, SIS-02 | ¿Requieren leer instrucciones? ¿Están visibles cuando hacen falta? | Ayuda contextual just-in-time, estados vacíos que enseñan, valores de ejemplo |
| "Doble envío / pulsan varias veces" | ACC-02 | ¿Hay estado de "enviando"? | Desactivar + indicador inmediato; idempotencia en servidor |

## Continuar y recordar la experiencia

| Síntoma | Leyes candidatas | Preguntas discriminantes | Primeras acciones |
|---|---|---|---|
| "Abandonan a mitad del onboarding/formulario largo" | MOT-02, MOT-03, MEM-01, MOT-04 | ¿Se ve el progreso? ¿Duración esperada? ¿Se puede retomar? | Progreso visible honesto, estimación de tiempo, guardado y retorno, quitar campos |
| "Terminan, pero la valoración es mala" | MOT-05, DEC-04 | ¿Hubo un pico negativo (error, sorpresa de precio, espera)? ¿Cómo es el final? | Eliminar picos negativos, cuidar la confirmación final y la recuperación de errores |
| "No vuelven / baja retención" | MOT-05, MOT-01, MOT-03, SIS-05 | ¿Llegan al valor central rápido? ¿Hay razones para volver? | Acortar tiempo hasta el valor, recordatorios útiles (no compulsivos) |
| "Tareas sencillas se alargan" | MOT-04, SIS-03 | ¿Hay campos/pasos que el sistema podría completar? | Autocompletar, defaults, plazos y expectativas claras |
| "Se quejan tras un rediseño" | SIS-01, SIS-02 | ¿Cambió la ubicación o el comportamiento de cosas aprendidas? | Transición gradual, opción temporal de volver, explicar cambios en contexto |

## Complejidad y estrategia

| Síntoma | Leyes candidatas | Primeras acciones |
|---|---|---|
| "El producto tiene demasiadas funciones" | SIS-05, SIS-04, SIS-03, DEC-01 | Datos de uso; jerarquía por frecuencia; eliminar lo no usado; divulgación progresiva |
| "Usuarios expertos se quejan de lentitud, novatos de complejidad" | SIS-03, MOT-01, DEC-01 | Capas: atajos/acciones masivas para expertos, guiado para novatos |
| "Interfaz de IA / chat: no saben qué pedir o confían demasiado" | SIS-02, ACC-04, DEC-03 | Ver `03-aplicacion/interfaces-ia-conversacionales.md` |
