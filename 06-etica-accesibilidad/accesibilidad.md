# Accesibilidad: cruce entre leyes de UX y WCAG 2.2

Las leyes describen a una persona "promedio"; la accesibilidad recuerda que la variación
humana es la norma (visión, audición, motricidad, cognición, contexto temporal: una mano
ocupada, sol en la pantalla, prisa). **Ninguna recomendación puede empeorar la accesibilidad.**

## Matriz ley ↔ criterios WCAG 2.2

| Ley | Riesgo de accesibilidad | Criterios WCAG 2.2 relacionados |
|---|---|---|
| ACC-01 Fitts | Objetivos pequeños o juntos excluyen a personas con temblor, baja precisión o pantallas pequeñas | 2.5.8 Tamaño del objetivo (mínimo, AA: 24×24 px CSS o espaciado equivalente); 2.5.5 Tamaño del objetivo (mejorado, AAA: 44×44); 2.5.7 Movimientos de arrastre (alternativa sin arrastrar) |
| ACC-02 Doherty | Esperas sin anuncio; contenidos que cambian sin aviso | 4.1.3 Mensajes de estado; 2.2.1 Tiempo ajustable; 2.2.2 Pausar, detener, ocultar |
| ACC-03 Postel | Formatos rígidos que bloquean; errores sin explicación | 3.3.1 Identificación de errores; 3.3.3 Sugerencias ante errores; 3.3.4 Prevención de errores; 1.3.5 Identificar el propósito de la entrada (autocomplete); 3.3.7 Entrada redundante; 3.3.8 Autenticación accesible |
| ACC-04 Usuario activo | Ayuda inaccesible o sólo en hover | 3.3.2 Etiquetas o instrucciones; 1.4.13 Contenido en hover o foco; 3.2.6 Ayuda consistente |
| PER-01…04 Gestalt | La agrupación sólo visual no llega a lectores de pantalla | 1.3.1 Información y relaciones (estructura semántica: `fieldset`, listas, encabezados, regiones); 1.3.2 Secuencia significativa |
| PER-02 Semejanza | Enlaces o estados distinguibles sólo por color | 1.4.1 Uso del color; 1.4.11 Contraste no textual |
| PER-07 Von Restorff | Destaque sólo por color o por movimiento | 1.4.1 Uso del color; 1.4.3 Contraste mínimo; 2.3.3 Animación por interacciones; `prefers-reduced-motion` |
| PER-06 Atención selectiva | Cambios de contexto inesperados; información crítica fuera del foco | 3.2.1 Al recibir el foco; 3.2.2 Al recibir entradas; 2.4.3 Orden del foco; 2.4.11 Foco no oculto |
| MEM-01/02 Carga y memoria | Exigir recordar datos entre pasos, códigos, puzles cognitivos | 3.3.7 Entrada redundante; 3.3.8 Autenticación accesible (sin pruebas de función cognitiva); 2.2.1 Tiempo ajustable |
| MEM-05 Posición serial | Orden visual distinto del orden del DOM | 1.3.2 Secuencia significativa; 2.4.3 Orden del foco |
| DEC-01/02 Hick, Sobrecarga | Listas extensas difíciles de recorrer con teclado/lector | 2.4.1 Evitar bloques; 2.4.6 Encabezados y etiquetas |
| SIS-01 Jakob | Controles personalizados con comportamiento no estándar | 4.1.2 Nombre, función, valor; 2.1.1 Teclado; 3.2.3 Navegación coherente; 3.2.4 Identificación coherente |
| MOT-04 Parkinson / urgencia | Límites de tiempo que excluyen a quien necesita más tiempo | 2.2.1 Tiempo ajustable; 2.2.6 Tiempos de espera (AAA) |
| MOT-01 Flow | Autoplay y movimiento que distraen | 2.2.2 Pausar, detener, ocultar; 1.4.2 Control del audio |
| DEC-04 Estética-usabilidad | Estética con bajo contraste, texto gris claro, tipografía fina | 1.4.3 Contraste mínimo (4.5:1 texto, 3:1 texto grande); 1.4.12 Espaciado del texto |

## Accesibilidad cognitiva

Las leyes MEM y DEC son el núcleo de la accesibilidad cognitiva. Referencia: W3C
*Making Content Usable for People with Cognitive and Learning Disabilities* (COGA, 2021):
lenguaje claro, pasos cortos, ayuda disponible, no depender de la memoria, evitar
distracciones, permitir deshacer, tiempos suficientes.

## Regla práctica

Cuando una ley sugiera usar **color, movimiento, posición o tiempo** para comunicar algo,
añade siempre un **segundo canal** (texto, icono con nombre accesible, forma, estructura
semántica) y respeta las preferencias del sistema (`prefers-reduced-motion`,
`prefers-contrast`, tamaño de texto).
