---
id: DEC-01
nombre: Ley de Hick (Hick-Hyman)
nombre_en: Hick's Law
alias: [ley de Hick-Hyman, Hick-Hyman Law]
familia: DEC
evidencia: E1
etiquetas: [decision, tiempo-de-reaccion, menus, navegacion, opciones, teoria-de-la-informacion]
refuerza: [MEM-01, MEM-04, PER-07, SIS-05, SIS-01, ACC-01, ACC-02]
tensiona: [SIS-03, SIS-04, ACC-04]
tensiones: [T1]
fuente_laws_of_ux: https://lawsofux.com/hicks-law/
---

# DEC-01 · Ley de Hick (*Hick's Law*)

> Cuando alguien elige entre alternativas que ya conoce y cuyo mapeo con la respuesta ha aprendido, el tiempo medio de decisión crece con el logaritmo del número de alternativas (más exactamente, con la información en bits que contiene la elección), no de forma lineal.

**Idea clave para quien diseña:** Hick sólo predice el tiempo de *decidir* cuando la persona ya sabe qué busca y la lista se puede subdividir; si tiene que *leer* para encontrar su opción, cada ítem que examina suma coste y lo que manda es la búsqueda visual.

## Origen
- Hick, W. E. (1952). On the rate of gain of information. *Quarterly Journal of Experimental Psychology*, 4(1), 11–26. doi:10.1080/17470215208416600. Lámparas emparejadas con teclas, hasta diez alternativas: el tiempo de reacción crecía con el número de lámparas posibles y la tasa de ganancia de información resultó aproximadamente constante (del orden de cinco bits por segundo).
- Hyman, R. (1953). Stimulus information as a determinant of reaction time. *Journal of Experimental Psychology*, 45(3), 188–196. doi:10.1037/h0056940. Mostró que el tiempo es lineal respecto a la información transmitida, también con alternativas no equiprobables.
- (Ambos verificados por metadatos y resumen, no en texto completo.)

**Fórmula.** Forma habitual: **RT = a + b · log₂(n + 1)**, donde el +1 recoge la incertidumbre de si hay que responder o no. Con probabilidades desiguales: **RT = a + b · H**, siendo H la entropía del conjunto. Algunas fuentes (IxDF) la escriben sin el +1. Las constantes *a* y *b* son empíricas y dependen de la tarea: **no existen valores universales**, así que no tiene sentido "calcular" milisegundos para un menú web sin medirlos.

## Mecanismo
La explicación clásica es de teoría de la información: cada elección reduce incertidumbre y el sistema cognitivo procesa una cantidad aproximadamente constante de bits por unidad de tiempo. Una lectura complementaria es que la persona va subdividiendo el conjunto (descarta más o menos la mitad en cada paso, como en una búsqueda binaria), de ahí la curva logarítmica: duplicar las opciones no duplica el tiempo, le suma un incremento constante.

Influye también la **compatibilidad estímulo-respuesta**: los mapeos "naturales" (girar hacia donde se quiere ir, una tecla bajo cada lámpara) responden más rápido. Con práctica intensa la pendiente *b* disminuye.

## Evidencia y límites
- **Nivel: E1** — modelo formal predictivo y uno de los resultados más replicados de la psicología experimental, **dentro de su dominio**: tareas de tiempo de reacción de elección con alternativas conocidas y mapeo aprendido.
- **Cuándo NO aplica (crítico en UX):**
  1. **Búsqueda visual en listas desconocidas o sin orden.** Si hay que leer las opciones, el tiempo lo dicta la búsqueda visual, que crece con cada ítem que hay que examinar, no la decisión de Hick. Es el caso típico de la primera visita a un menú web. El modelo de **Cockburn, Gutwin & Greenberg (2007, CHI, 627–636, doi:10.1145/1240624.1240723)** usa por eso componentes distintos: búsqueda visual para quien es novato, decisión de Hick-Hyman para quien es experto, y una transición entre ambas a medida que se aprende el menú.
  2. El tramo logarítmico aparece cuando el usuario **ya sabe** lo que busca y la lista tiene un orden predecible. **Landauer & Nachbar (1985, CHI'85, 73–78, doi:10.1145/317456.317470)**, con menús de números y palabras en orden alfabético en pantalla táctil, hallaron que el tiempo por pantalla seguía T = k + c·log b (Hick-Hyman para decidir y Fitts para moverse, en serie), lo que favorece menús anchos frente a profundos.
  3. Respuestas verbales a estímulos muy familiares y movimientos sacádicos muestran poco o ningún efecto (en sacadas incluso un efecto "anti-Hick").
- **Malentendidos frecuentes:**
  - *"Menús de 7 ítems como máximo" / "menos opciones siempre".* La investigación sobre amplitud y profundidad apunta en sentido contrario para la navegación: Larson & Czerwinski (1998, CHI) compararon tres jerarquías web de 512 nodos: las dos de dos niveles (16×32, media 36 s por búsqueda; 32×16, 46 s) fueron más rápidas que la de tres niveles (8×8×8, 58 s), y esta fue significativamente más lenta que ambas; además, en la de tres niveles los participantes se perdieron significativamente más. Cada nivel extra añade una decisión, una navegación y riesgo de perderse.
  - *Confundirla con la sobrecarga de opciones (DEC-02).* Hick mide milisegundos de reacción; la sobrecarga mide satisfacción, abandono y aplazamiento en decisiones de preferencia.
  - *"Número y complejidad".* La versión divulgativa de Laws of UX añade "complejidad"; la ley original habla de número y probabilidad de las alternativas.

## Aplicación práctica
### Reglas
1. [E] En tareas críticas en tiempo (alarmas, controles de vehículo, atajos de experto) reduce las alternativas presentes en el momento de decidir, haz predecible su probabilidad y usa mapeos estímulo-respuesta compatibles (Hick 1952; Hyman 1953).
2. [E] En navegación, prefiere pocos niveles con más ítems por nivel, bien agrupados y etiquetados, antes que árboles profundos (Larson & Czerwinski 1998).
3. [E] Ordena alfabéticamente, o con búsqueda/autocompletado, las listas largas que se recorren sabiendo lo que se busca (países, idiomas): convierte una búsqueda ítem a ítem en una subdivisible (Landauer & Nachbar 1985).
4. [E] Para expertos, ofrece atajos y paletas de comandos con búsqueda: quien ya sabe lo que quiere apenas paga por el tamaño del repertorio (Cockburn et al. 2007).
5. [H] Destaca una opción recomendada y usa valores por defecto para resolver decisiones que no necesitan a la persona.
6. [H] Aplica divulgación progresiva en onboarding: primero la acción principal, después lo secundario.
7. [H] Cuando el usuario explora sin objetivo, no razones con Hick: razona con búsqueda visual y agrupación (PER-01, PER-03).

### Por contexto
| Contexto | Aplicación |
|---|---|
| Web/escritorio | Megamenús amplios y agrupados con encabezados mejor que cascadas de 4 niveles. |
| Móvil/táctil | Pocas acciones primarias visibles; el resto en hojas de acción agrupadas, no en submenús anidados. |
| Formularios | Desplegables largos con búsqueda; valores por defecto razonables; pocas decisiones por paso. |
| Navegación | Etiquetas predecibles y orden estable para que la posición se aprenda (paso de búsqueda visual a decisión; Cockburn et al. 2007). |
| Dashboards/datos | Separar acciones frecuentes de raras (SIS-05) y destacar la recomendada (PER-07). |
| E-commerce | Preseleccionar el envío más común sin ocultar las alternativas. |
| Onboarding | Revelar funciones por etapas, empezando por la tarea núcleo. |
| Conversacional/IA | 2–4 respuestas sugeridas en vez de listas largas [H]. |
| Voz | Muy pocas opciones leídas en voz alta: no se pueden escanear y todo pasa por la memoria de trabajo [H]. |

### Ejemplos
- **Bueno:** un selector de país con campo de búsqueda y lista alfabética. Quien sabe que busca "Perú" teclea dos letras; la longitud de la lista deja de importar.
- **Bueno:** un mando a distancia con muy pocos botones físicos que traslada la complejidad a menús en pantalla organizados y revelados por etapas.
- **Lo incumple:** un sitio institucional que, "para aplicar Hick", parte un menú de 40 enlaces en cinco niveles de 8. Cada nivel obliga a adivinar dónde está algo, se multiplican los retrocesos y el tiempo total empeora.

## Anti-patrones
- Recortar opciones necesarias tras "Más…" o crear embudos profundos (simplificar hasta la abstracción).
- Aplicar números mágicos (7, 5, 3) a menús de navegación.
- Varias CTA con el mismo peso visual en la misma zona.
- Listas largas sin orden ni búsqueda.
- Calcular tiempos con constantes "estándar" que no existen.

## Ética y accesibilidad
- **Línea roja:** reducir las opciones visibles para empujar hacia la más rentable (ocultar el plan gratuito o la opción de no contratar). Mathur et al. (2019) clasifican estas prácticas como *misdirection* u *obstruction*.
- Para quien usa lector de pantalla las opciones se recorren en secuencia: el coste crece de forma lineal. Agrupa con encabezados y *landmarks* y ofrece búsqueda.
- En discapacidad cognitiva, reducir decisiones simultáneas tiene especial valor [H].
- WCAG 2.2: **1.3.1** Información y relaciones; **2.4.1** Evitar bloques; **2.4.5** Múltiples vías; **2.4.6** Encabezados y etiquetas; **3.2.3** Navegación coherente (orden estable que se pueda aprender); **2.2.1** Tiempo ajustable si la elección tiene límite de tiempo.

## Cómo auditarla
### Señales observables
- Menús de más de 10–15 ítems sin agrupar ni ordenar; jerarquías de 4 niveles o más.
- Varias CTA equivalentes compitiendo en la misma pantalla.
- Cursor que sobrevuela opciones sin hacer clic; clics en la opción equivocada.
### Preguntas
- ¿La persona sabe lo que busca o tiene que explorar? (Decide si aplica Hick o búsqueda visual.)
- ¿La lista tiene un orden que se pueda predecir? ¿Se puede buscar?
- ¿Hay una opción recomendada? ¿Cuántas decisiones del paso podría resolver un valor por defecto?
- ¿Quitar opciones traslada trabajo a la persona (T1)?
### Métricas
- Tiempo hasta el primer clic y tasa de primer clic correcto (tree testing).
- Tasa de retroceso en la navegación.
- Comparación de tiempos entre usuarios nuevos y recurrentes (debería caer al aprenderse el menú).

## Relaciones
- Refuerza / se apoya en:
  - MEM-01 Carga cognitiva — menos incertidumbre por decisión, menos carga.
  - MEM-04 Fragmentación — agrupar reduce la incertidumbre efectiva.
  - PER-07 Efecto Von Restorff — destacar la opción recomendada acorta la decisión.
  - SIS-05 Principio de Pareto — priorizar lo frecuente.
  - SIS-01 Ley de Jakob — las convenciones convierten búsqueda en reconocimiento.
  - ACC-01 Ley de Fitts — Hick modela el decidir, Fitts el moverse; se suman en el tiempo total.
  - ACC-02 Umbral de Doherty — decisiones rápidas necesitan respuestas rápidas.
- Tensiona con:
  - SIS-03 Ley de Tesler — quitar opciones puede trasladar la complejidad a la persona (T1: elimina lo innecesario, absorbe lo necesario, difiere lo avanzado).
  - SIS-04 Navaja de Occam — bien aplicada converge con Hick; mal aplicada lleva a la sobresimplificación (T1).
  - ACC-04 Paradoja del usuario activo — lo escondido en submenús no se explora.
- Se confunde a menudo con: DEC-02 Sobrecarga de opciones — Hick es tiempo de reacción con alternativas conocidas; la sobrecarga trata de satisfacción y aplazamiento en decisiones de preferencia.

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/hicks-law/ — síntesis divulgativa.
- Primarias:
  - Hick, W. E. (1952). On the rate of gain of information. *QJEP*, 4(1), 11–26. https://doi.org/10.1080/17470215208416600
  - Hyman, R. (1953). Stimulus information as a determinant of reaction time. *J. Exp. Psychol.*, 45(3), 188–196. https://doi.org/10.1037/h0056940
  - Card, S. K., Moran, T. P., & Newell, A. (1983). *The Psychology of Human-Computer Interaction*. Erlbaum.
  - Landauer, T. K., & Nachbar, D. W. (1985). Selection from alphabetic and numeric menu trees using a touch screen: Breadth, depth, and width. *CHI '85*, 73–78. https://doi.org/10.1145/317456.317470
  - Larson, K., & Czerwinski, M. (1998). Web page design: Implications of memory, structure and scent for information retrieval. *CHI '98*, 25–32. https://doi.org/10.1145/274644.274649
  - Seow, S. C. (2005). Information theoretic models of HCI: A comparison of the Hick-Hyman law and Fitts' law. *Human-Computer Interaction*, 20(3), 315–352. https://doi.org/10.1207/s15327051hci2003_3
  - Cockburn, A., Gutwin, C., & Greenberg, S. (2007). A predictive model of menu performance. *CHI '07*, 627–636. https://doi.org/10.1145/1240624.1240723
  - Mathur, A. et al. (2019). Dark Patterns at Scale. *Proc. ACM HCI*, 3(CSCW), art. 81. https://doi.org/10.1145/3359183
- Secundarias consultadas:
  - https://en.wikipedia.org/wiki/Hick%27s_law
  - https://ixdf.org/literature/article/hick-s-law-making-the-choice-easier-for-users
  - https://www.microsoft.com/en-us/research/publication/web-page-design-implications-memory-structure-scent-information-retrieval/
  - https://hcibook.com/e3/online/menu-breadth
