---
id: PER-05
nombre: Ley de Prägnanz
nombre_en: Law of Prägnanz
alias: [ley de la buena forma, ley de la simplicidad, ley de pregnancia, Law of Simplicity, Law of Good Gestalt, Good Figure]
familia: PER
evidencia: C
etiquetas: [gestalt, simplicidad, forma, iconografia, layout, complejidad]
refuerza: [SIS-04, DEC-04, MEM-01, MEM-04, PER-03, PER-04]
tensiona: [SIS-03, PER-07, SIS-02, PER-02]
tensiones: [T1, T3]
fuente_laws_of_ux: https://lawsofux.com/law-of-pr%C3%A4gnanz/
---

# PER-05 · Ley de Prägnanz (*Law of Prägnanz*)

> Cuando un estímulo admite varias lecturas, el sistema visual se queda con la organización más simple, regular, simétrica y estable que sea compatible con lo que ve. Es la tendencia general de la que los demás principios Gestalt son casos particulares.

**Idea clave para quien diseña:** la pantalla se va a "leer" como unas pocas formas simples quieras o no; decide tú cuáles son, porque si no, el ojo las inventará.

## Resumen operativo
- **Qué dice:** ante un estímulo ambiguo, se percibe la organización más simple, regular y estable compatible con él; es el principio general del que derivan los demás Gestalt.
- **Evidencia:** C — descripción robusta del fenómeno, pero sin predicciones numéricas para una pantalla; se olvida que describe cómo percibimos, no prescribe minimalismo.
- **Haz:** 1) que cada pantalla, desenfocada, se resuelva en pocas masas 2) limita el inventario de formas (radios, sombras, alineaciones) 3) lo que debe verse igual, idéntico; lo distinto, claramente distinto.
- **Evita:** simplificar la forma escondiendo información necesaria (costes, condiciones, opción de rechazo).
- **Sospecha de esta ley cuando…:** la pantalla se percibe "desordenada" o "rota" sin un error concreto; iconos casi iguales se confunden.
- **Mide con:** prueba de desenfoque (masas percibidas frente a grupos previstos); test de 5 segundos sobre la estructura.
- **Vecinas:** SIS-04 Navaja de Occam (refuerza) · PER-03 Región común (refuerza) · SIS-03 Ley de Tesler (tensiona, T1) · PER-07 Efecto Von Restorff (tensiona, T3)

## Origen

- **Max Wertheimer (1912)**, trabajo sobre el movimiento aparente (fenómeno phi): se toma como punto de partida de la psicología de la Gestalt, y Wagemans et al. (2012) lo usan como hito del centenario. La anécdota de las luces de un paso a nivel en 1910 que difunde Laws of UX (vía Smashing Magazine) es un relato divulgativo **(no verificado: no aparece en las fuentes primarias consultadas ni en Wagemans et al. 2012, parte I)**.
- **Wertheimer (1923)**, *Untersuchungen zur Lehre von der Gestalt II*, *Psychologische Forschung*, 4, 301–350 **[verificada]**. Describe la tendencia hacia formas "buenas" y estables: un ángulo de 93° se sigue viendo como recto y las formas intermedias se perciben como la forma estable más próxima. Traducción inglesa en W. D. Ellis (ed.), *A Source Book of Gestalt Psychology* (1938).
- **Koffka (1935)**, *Principles of Gestalt Psychology* (Nueva York: Harcourt, Brace), p. 110: atribuye el nombre "ley de Prägnanz" a Wertheimer y la formula como que la organización psicológica será siempre tan "buena" como lo permitan las condiciones; "buena" abarca regularidad, simetría y simplicidad, y él mismo reconoce que es un principio "algo vago".
- **Debate moderno simplicidad ↔ probabilidad:** la Gestalt defendía un principio de mínimo frente al principio de probabilidad de Helmholtz (se percibe la causa distal más probable). Chater (1996, *Psychological Review*, 103(3), 566–581) sostiene, apoyándose en la complejidad de Kolmogorov, que ambos principios no compiten sino que son equivalentes; Feldman (2009, *Psychological Review*, 116(4), 875–887) muestra que una regla de simplicidad en espacios de interpretación jerárquicos maximiza la probabilidad posterior bayesiana bajo ciertos supuestos; van der Helm (*Simplicity in Vision*, Cambridge University Press, 2014) defiende la versión informacional de la teoría de la información estructural (SIT). Verificado en resúmenes y en Wagemans et al. (2012, parte II); libros y artículos completos no leídos.
- **Revisión de referencia:** Wagemans, J. et al. (2012). "A century of Gestalt psychology in visual perception" (partes I y II), *Psychological Bulletin*, 138(6). doi:10.1037/a0029333 (parte I) **[verificada]**.

## Mecanismo

El sistema visual recibe imágenes ambiguas: la misma retina es compatible con infinitas escenas. Para resolverlas elige la interpretación de descripción más económica: completa contornos interrumpidos (cierre), prefiere la simetría y la continuidad, y "regulariza" lo casi regular. En entornos naturales esa lectura suele coincidir además con la más probable, de ahí que las teorías de simplicidad y de probabilidad converjan.

Para quien usa una interfaz, esto significa que la pantalla se reduce a pocas masas y formas antes de leer nada. Laws of UX añade que procesamos y recordamos mejor las figuras simples; es coherente con la literatura de simplicidad y memoria visual, pero la página no da la cita concreta, así que debe tratarse como afirmación general.

## Evidencia y límites

- **Nivel: C (constructo teórico).** Como *descripción* del fenómeno es robusta; como *ley explicativa* fue criticada por vaga y no cuantificable hasta la llegada de los modelos informacionales y bayesianos (Wagemans et al. 2012). No ofrece predicciones numéricas aplicables a una pantalla.
- **Condiciones:** actúa sobre todo ante ambigüedad o complejidad; cuando la estructura es clara, la "buena forma" es simplemente la forma dada. Compite con la experiencia previa y con la tarea.
- **Simple perceptivo ≠ simple funcional.** Pocas formas regulares no implican una tarea sencilla. Esconder funciones para que la pantalla "parezca" limpia traslada la complejidad (SIS-03, T1).
- **Regularización con coste:** desalineaciones pequeñas se leen como error o como intención extraña, y diferencias sutiles que sí importan (estados, iconos casi iguales) se pasan por alto.
- **Malentendido frecuente:** "Prägnanz = menos es más". Corrección: el principio describe cómo percibimos, no prescribe minimalismo. Una interfaz densa pero bien estructurada cumple Prägnanz; una minimalista ambigua no.

## Aplicación práctica

### Reglas

1. [H] Estructura cada pantalla para que, desenfocada (*squint/blur test*), se resuelva en pocas masas principales (orientativo: 3–5). La cifra es convención, no experimento.
2. [H] Limita el inventario de formas: pocos radios de borde, pocas sombras, una rejilla y alineaciones consistentes. Cada variante extra es una forma que el ojo debe explicar.
3. [H] Diseña iconos con siluetas geométricas simples, reconocibles por su contorno; reduce detalle a tamaños pequeños.
4. [H] Si dos elementos deben verse distintos, que la diferencia sea clara; si deben verse iguales, que sean idénticos. Evita el "casi igual", que el ojo regulariza o lee como error.
5. [H] En visualización de datos, elimina tinta no informativa y prefiere codificaciones fáciles de comparar (barras alineadas a una base común) frente a 3D o tartas con muchas porciones. Base relacionada: Cleveland & McGill (1984), *Graphical perception*, *JASA*, sobre la precisión de las codificaciones gráficas.
6. [H] En formularios y móvil, una columna y un flujo lineal; los saltos de forma y de dirección añaden figuras que interpretar.
7. [H] Simplifica la forma, nunca la información necesaria: costes, condiciones y la opción de rechazo deben seguir visibles.
8. [H] En revisiones de diseño, compara un *wireframe* simplificado con la pantalla real para discutir estructura sin distracción de contenido (práctica que propone IxDF).

### Por contexto

| Contexto | Aplicación |
|---|---|
| Web/escritorio | Rejilla consistente, pocas masas por vista, alineación estricta de bordes de bloques. |
| Móvil/táctil | Una columna; tarjetas de forma única; iconos reconocibles por su contorno al tamaño real de uso. |
| Formularios | Flujo lineal, campos de ancho proporcional al dato, un único estilo de campo. |
| Navegación | Un solo patrón de menú por nivel; iconos de pestaña distinguibles por silueta. |
| Dashboards/datos | Pocos tipos de gráfico, base común, sin efectos 3D ni degradados decorativos. |
| Onboarding | Ilustraciones simples que se reconozcan en un vistazo; un mensaje por pantalla. |
| Interfaces conversacionales/IA | Respuestas con estructura regular (encabezados, listas) en vez de muros de texto; indicadores de estado y avatares de forma simple y distinta; estados de carga con una forma sencilla en lugar de animaciones "orgánicas" complejas. |
| Sistemas de diseño | Tokens que limitan radios, sombras y espaciados; biblioteca de iconos con una gramática geométrica común. |

### Ejemplos

- **Bueno:** un logotipo como el panda de WWF (ejemplo de IxDF) se reconoce a tamaño de favicon porque el ojo completa las formas con muy poca información.
- **Bueno:** un panel que, desenfocado, muestra cabecera, una franja de KPIs y un área de detalle; la estructura se entiende antes de leer cifras.
- **Lo incumple:** una página de producto con cinco radios de borde, tres estilos de sombra y bloques ligeramente desalineados: el ojo no logra resolverla en pocas formas y la percibe como desordenada o "rota".

## Anti-patrones

- Simplificación engañosa: ocultar costes, condiciones o el "no, gracias" bajo una interfaz "limpia".
- Iconos tan reducidos que pierden la distinción (dos glifos casi iguales con funciones distintas), choque con PER-02.
- Iconos sin etiqueta confiando en que "la forma simple se entiende sola".
- Gráficos decorativos (3D, perspectiva, degradados) que deforman la lectura de valores.
- Minimalismo que elimina pistas de interacción (bordes de campo, subrayado de enlaces).
- Multiplicar variantes visuales "casi iguales" en el sistema de diseño.

## Ética y accesibilidad

- **Línea roja:** usar la apariencia de simplicidad para esconder información que la persona necesita para decidir (precio total, renovación automática, alternativa de rechazo).
- **WCAG 1.1.1 Contenido no textual (A)** y **4.1.2 Nombre, función, valor (A):** un icono simple sigue necesitando nombre accesible; conviene además etiqueta visible.
- **WCAG 1.4.11 Contraste no textual (AA):** iconos y límites que transmiten información, ≥ 3:1.
- **WCAG 1.4.1 Uso del color (A):** simplificar a "solo color" para distinguir estados no es aceptable.

## Cómo auditarla

### Señales observables
- Muchas formas, radios, sombras o alineaciones distintas en la misma vista.
- Iconos que no se reconocen sin su etiqueta.
- Pantallas que, desenfocadas, no muestran una estructura clara.
- Gráficos decorativos que dificultan leer valores.
- Funciones o información que "desaparecieron" en un rediseño minimalista.

### Preguntas
- ¿Cuántas formas o patrones visuales distintos hay y son todos necesarios?
- ¿La estructura se entiende en 5 segundos?
- ¿Simplificar ha escondido algo que el usuario necesita?
- ¿Hay elementos "casi iguales" que deberían ser idénticos o claramente distintos?

### Métricas
- *Blur/squint test*: número de masas percibidas frente a grupos lógicos previstos.
- Test de 5 segundos: proporción de participantes que describe correctamente la estructura de la página.
- Test de reconocimiento de iconos sin etiqueta (tasa de acierto por icono).
- Inventario del sistema: recuento de radios, sombras, tamaños de icono y estilos de contenedor en uso.
- Tras simplificar: tasa de éxito y tiempo en tareas que usaban lo ocultado (para detectar complejidad desplazada).

## Relaciones

- Refuerza / se apoya en: SIS-04 Navaja de Occam — eliminar lo innecesario produce formas más simples.
- Refuerza / se apoya en: DEC-04 Efecto estética-usabilidad — el orden visual se percibe como calidad.
- Refuerza / se apoya en: MEM-01 Carga cognitiva — menos formas que interpretar, menos carga.
- Refuerza / se apoya en: MEM-04 Fragmentación — pocas masas equivalen a pocos fragmentos.
- Refuerza / se apoya en: PER-03 Región común y PER-04 Conectividad uniforme — formas cerradas y conectadas son "buenas formas".
- Tensiona con: SIS-03 Ley de Tesler — la complejidad no desaparece, se desplaza; resolución T1.
- Tensiona con: PER-07 Efecto Von Restorff — la regularidad total deja la pantalla sin foco; se necesita una excepción controlada (T3).
- Tensiona con: SIS-02 Modelo mental — lo "simple" para quien diseña puede no coincidir con lo que la persona espera.
- Tensiona con: PER-02 Ley de semejanza — simplificar iconos hasta hacerlos casi iguales borra diferencias funcionales.
- Se confunde a menudo con: minimalismo — estilo estético; Prägnanz es un fenómeno perceptivo que también se cumple en interfaces densas.
- Se confunde a menudo con: Navaja de Occam — Occam elige entre soluciones; Prägnanz describe cómo se percibe la que elijas.

## Fuentes

- Laws of UX (Jon Yablonski): https://lawsofux.com/law-of-pr%C3%A4gnanz/ — síntesis divulgativa.
- Primarias:
  - Wertheimer, M. (1923). Untersuchungen zur Lehre von der Gestalt II. *Psychologische Forschung*, 4, 301–350. Traducción: "Laws of organization in perceptual forms", en Ellis (ed., 1938). https://www.yorku.ca/pclassic/Wertheimer/Forms/forms.htm
  - Wagemans, J., Elder, J. H., Kubovy, M., Palmer, S. E., Peterson, M. A., Singh, M., & von der Heydt, R. (2012). A century of Gestalt psychology in visual perception: I. *Psychological Bulletin*, 138(6), 1172–1217. doi:10.1037/a0029333 — y parte II (Wagemans, Feldman, Gepshtein, Kimchi et al., 2012), *Psychological Bulletin*, 138(6), 1218–1252. doi:10.1037/a0029334
  - Koffka, K. (1935). *Principles of Gestalt Psychology*. Nueva York: Harcourt, Brace (p. 110). Texto en https://archive.org/details/in.ernet.dli.2015.7888
  - Chater, N. (1996). Reconciling simplicity and likelihood principles in perceptual organization. *Psychological Review*, 103(3), 566–581. doi:10.1037/0033-295X.103.3.566 (resumen).
  - Feldman, J. (2009). Bayes and the simplicity principle in perception. *Psychological Review*, 116(4), 875–887. doi:10.1037/a0017144 (resumen).
  - van der Helm, P. A. (2014). *Simplicity in Vision: A Multidisciplinary Account of Perceptual Organization*. Cambridge University Press. doi:10.1017/CBO9781139538268 (metadatos).
  - Cleveland, W. S., & McGill, R. (1984). Graphical perception: Theory, experimentation, and application to the development of graphical methods. *Journal of the American Statistical Association*, 79(387), 531–554. doi:10.1080/01621459.1984.10478080 (metadatos).
- Secundarias consultadas:
  - https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/ (Bradley, 2014)
  - https://ixdf.org/literature/article/the-laws-of-figure-ground-praegnanz-closure-and-common-fate-gestalt-principles-3
  - https://pubmed.ncbi.nlm.nih.gov/22845751/ (metadatos de Wagemans et al. 2012)
