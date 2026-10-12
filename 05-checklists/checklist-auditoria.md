# Checklist de auditoría completa

Red de seguridad **después** del recorrido por el ciclo de interacción
(`04-procesos/auditar.md`). Cada punto es comprobable; anota ✔ / ✘ / N/A y, si es ✘,
abre un hallazgo con severidad. Los ids `C-xx` permiten referenciar puntos en informes.

## SIS · Expectativas y complejidad

| Id | Comprobación | Ley |
|---|---|---|
| C-01 | Los patrones globales (logo, navegación, búsqueda, carrito/cuenta, gestos) están donde la plataforma y la categoría lo esperan. | SIS-01 |
| C-02 | El vocabulario es el de la persona usuaria, no el interno de la organización o del sistema. | SIS-02 |
| C-03 | La estructura de navegación refleja cómo las personas agrupan el contenido (validado o razonado). | SIS-02 |
| C-04 | Se puede completar la tarea principal sin leer instrucciones previas. | ACC-04 |
| C-05 | Ningún dato o decisión que el sistema podría resolver (defaults, inferencia, autocompletado) recae en la persona. | SIS-03 |
| C-06 | No hay elementos que no contribuyan a la tarea (decoración que compite, funciones sin uso). | SIS-04 |
| C-07 | Las funciones y contenidos más usados son los más accesibles. | SIS-05 |
| C-08 | Los cambios respecto a versiones anteriores tienen transición (aviso, convivencia, ayuda). | SIS-01 |

## PER · Percepción y atención

| Id | Comprobación | Ley |
|---|---|---|
| C-10 | El espacio dentro de cada grupo es claramente menor que entre grupos; etiquetas pegadas a su campo/objeto. | PER-01 |
| C-11 | Los elementos con la misma función se ven iguales y los de funciones distintas se distinguen; los enlaces se distinguen del texto sin depender sólo del color. | PER-02 |
| C-12 | Los contenedores (tarjetas, fondos, bordes) agrupan sólo lo que está relacionado. | PER-03 |
| C-13 | Las conexiones visuales (líneas, flechas, pasos) reflejan relaciones reales. | PER-04 |
| C-14 | Formas, iconos y composición son simples y se interpretan sin ambigüedad. | PER-05 |
| C-15 | Lo importante no parece publicidad ni está en zonas típicas de anuncios. | PER-06 |
| C-16 | Los cambios de estado (errores, añadido al carrito, guardado) ocurren cerca del foco o se señalan. | PER-06 |
| C-17 | Hay como máximo un énfasis principal por zona; coincide con la acción más probable. | PER-07 |
| C-18 | El énfasis no depende sólo del color ni del movimiento. | PER-07 |

## MEM · Memoria y carga

| Id | Comprobación | Ley |
|---|---|---|
| C-20 | No se exige recordar información de una pantalla a otra (se arrastra o se resume). | MEM-02 |
| C-21 | Se favorece reconocer sobre recordar: opciones visibles, sugerencias, historial, estados visitados. | MEM-02 |
| C-22 | El contenido y los datos largos están fragmentados en unidades con sentido (encabezados, grupos, formatos de números). | MEM-04 |
| C-23 | No hay elementos que consuman atención sin ayudar a la tarea (carga extrínseca). | MEM-01 |
| C-24 | La complejidad visible se adapta a la experiencia (progresiva para novatos, densa y eficiente para expertos). | MEM-01 |
| C-25 | Lo más importante de listas y secuencias está al principio (y, si procede, al final). | MEM-05 |
| C-26 | No se usa "7±2" como límite arbitrario de elementos. | MEM-03 |

## DEC · Decisión y juicio

| Id | Comprobación | Ley |
|---|---|---|
| C-30 | El número de opciones simultáneas es el necesario para este momento; lo demás está agrupado o diferido. | DEC-01 |
| C-31 | Las listas largas tienen búsqueda, filtros, orden o agrupación que permita subdividir la decisión. | DEC-01, DEC-02 |
| C-32 | Cuando hay que comparar, la comparación es lado a lado con atributos homogéneos. | DEC-02 |
| C-33 | Hay valores por defecto o recomendaciones, y son honestos y fáciles de cambiar. | DEC-03 |
| C-34 | No se explotan sesgos contra el interés de la persona (urgencia/escasez falsas, anclas inventadas, confirmshaming, preselecciones de pago). | DEC-03 · Ética |
| C-35 | La calidad visual es coherente y transmite confianza, sin ocultar problemas de uso. | DEC-04 |

## ACC · Acción e interacción

| Id | Comprobación | Ley |
|---|---|---|
| C-40 | Objetivos interactivos ≥ 24×24 px CSS (WCAG 2.5.8) y, en táctil, ≈ 44–48 px para acciones frecuentes, con separación. | ACC-01 |
| C-41 | La acción principal está cerca del foco de la tarea; las destructivas, separadas de las frecuentes. | ACC-01 |
| C-42 | Toda acción produce feedback inmediato (≈ ≤ 100 ms) y las respuestas habituales son subsegundo. | ACC-02 |
| C-43 | Las esperas > 1 s tienen indicador; > 10 s, progreso y posibilidad de seguir. | ACC-02 |
| C-44 | La entrada acepta formatos variados, normaliza y muestra su interpretación cuando hay ambigüedad. | ACC-03 |
| C-45 | Los errores se explican junto al campo, con cómo corregirlos, sin borrar lo introducido. | ACC-03 |
| C-46 | La ayuda aparece en contexto y en el momento de necesidad; es descartable y recuperable. | ACC-04 |

## MOT · Motivación y experiencia en el tiempo

| Id | Comprobación | Ley |
|---|---|---|
| C-50 | En procesos de varios pasos, el progreso es visible y real. | MOT-02 |
| C-51 | Se puede pausar y retomar sin perder trabajo; lo pendiente se recuerda de forma útil (no compulsiva). | MOT-03 |
| C-52 | La duración esperada se comunica y se cumple; el sistema evita que las tareas se alarguen (autocompletar, defaults). | MOT-04 |
| C-53 | Se han identificado y suavizado los picos negativos (errores, esperas, sorpresas de coste). | MOT-05 |
| C-54 | El final de cada flujo (confirmación, éxito, salida) está diseñado: claro, tranquilizador, con siguiente paso. | MOT-05 |
| C-55 | La tarea principal no se interrumpe sin necesidad; las interrupciones son proporcionales al riesgo. | MOT-01 |

## Transversal · Ética y accesibilidad

| Id | Comprobación | Referencia |
|---|---|---|
| C-60 | Todas las recomendaciones persuasivas pasan la prueba de cuatro preguntas. | `06-etica-accesibilidad/etica-y-patrones-oscuros.md` |
| C-61 | Cancelar, darse de baja o rechazar cuesta lo mismo que aceptar o darse de alta. | Ética |
| C-62 | La agrupación visual está también en la estructura semántica (encabezados, listas, `fieldset`, regiones). | WCAG 1.3.1 |
| C-63 | Contraste suficiente de texto (4.5:1) y de componentes (3:1); foco visible. | WCAG 1.4.3, 1.4.11, 2.4.7 |
| C-64 | Todo funciona con teclado y los estados se anuncian a tecnologías de apoyo. | WCAG 2.1.1, 4.1.2, 4.1.3 |
| C-65 | Hay alternativa a gestos complejos y arrastres; el movimiento respeta `prefers-reduced-motion`. | WCAG 2.5.1, 2.5.7, 2.3.3 |
| C-66 | Los límites de tiempo se pueden ampliar o desactivar. | WCAG 2.2.1 |
