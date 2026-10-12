---
id: ACC-01
nombre: Ley de Fitts
nombre_en: Fitts's Law
alias: [modelo de Fitts, ley de apuntamiento, pointing law, Fitts' law]
familia: ACC
evidencia: E1
etiquetas: [apuntamiento, tamano-de-objetivo, distancia, tactil, puntero, accesibilidad, target-size]
refuerza: [PER-01, ACC-02, MOT-01, SIS-01]
tensiona: [DEC-01, DEC-02, SIS-04, PER-05, DEC-04, PER-07, SIS-03, MEM-04]
tensiones: [T5]
fuente_laws_of_ux: https://lawsofux.com/fittss-law/
---

# ACC-01 · Ley de Fitts (*Fitts's Law*)

> El tiempo que se tarda en llevar el dedo, la mano o el cursor hasta un objetivo crece con el logaritmo del cociente entre la distancia que hay que recorrer y el tamaño del objetivo en la dirección del movimiento; los objetivos lejanos y pequeños son más lentos y provocan más fallos.

**Idea clave para quien diseña:** acerca la acción al foco de la tarea y dale un área real de toque generosa; agrandar rinde cada vez menos, acercar casi siempre rinde.

## Resumen operativo
- **Qué dice:** el tiempo para alcanzar un objetivo crece con log2(D/W + 1): lejos y pequeño es lento y propenso a fallos.
- **Evidencia:** E1 — modelo predictivo muy replicado (base de ISO/TS 9241-411); se olvida que la ganancia por agrandar es decreciente y que al tacto los bordes no son "infinitos".
- **Haz:** 1) acción siguiente junto al foco de la tarea 2) área interactiva ≥ 24×24 px CSS (44 pt / 48 dp en táctil), toda la fila clicable 3) separa acciones destructivas de las frecuentes.
- **Evita:** iconos diminutos sin área ampliada y trasladar la lógica de esquinas del ratón al tacto.
- **Sospecha de esta ley cuando…:** hay *rage taps* o *dead clicks*; toques seguidos de "atrás" en menos de 2 s.
- **Mide con:** tasa de error y tiempo por objetivo en test; regla `target-size` de axe-core; *throughput* (bits/s) para dispositivos.
- **Vecinas:** PER-01 Ley de proximidad (refuerza) · ACC-02 Umbral de Doherty (refuerza) · DEC-01 Ley de Hick (tensiona) · MEM-04 Fragmentación (tensiona, T5)

## Origen
- **Paul M. Fitts (1954)**, "The information capacity of the human motor system in controlling the amplitude of movement", *Journal of Experimental Psychology*, 47(6), 381–391. doi:10.1037/h0055392. Tarea de golpeteo recíproco en una dimensión entre dos franjas de anchura y separación variables. Formulación original: `ID = log2(2D/W)`, `MT = a + b·ID`.
- Fitts y Peterson (1964) extendieron el modelo a movimientos discretos (*J. Exp. Psychol.*, 67(2), 103–112, doi:10.1037/h0045689).
- **MacKenzie (1992)** propuso la **formulación de Shannon**, hoy la estándar en HCI:

  **`MT = a + b · log2(D/W + 1)`**

  `MT` tiempo de movimiento; `D` distancia al centro del objetivo; `W` anchura del objetivo en el eje del movimiento; `a`, `b` constantes empíricas (dependen del dispositivo y la persona); el término logarítmico es el índice de dificultad `ID`, en bits.
- **Anchura efectiva** (Crossman, 1956; adoptada por ISO 9241-9): `We = 4,133·SDx` (desviación típica de los puntos de selección). Con ella `IDe = log2(D/We + 1)` y el rendimiento (*throughput*) `TP = IDe/MT` en bits/s. `We ≈ W` cuando la tasa de error ronda el 4 %. ISO 9241-9:2000 fue sustituida por la especificación técnica **ISO/TS 9241-411:2012** (*Evaluation methods for the design of physical input devices*), confirmada en 2026.
- Extensiones: Welford (1968) separa los términos de distancia y anchura; Accot y Zhai (CHI '97) formulan la **ley de dirección** (*steering law*) para trayectorias en túnel, `T = a + b·(A/W)`, lineal y no logarítmica; Bi, Li y Zhai (CHI 2013) proponen **FFitts** para el dedo, añadiendo la imprecisión absoluta del contacto.

## Mecanismo
Apuntar combina una fase balística inicial, rápida y gobernada por la distancia, con una fase de corrección guiada por la vista, gobernada por el tamaño del objetivo. Cada corrección reduce el error restante en una proporción aproximadamente constante, de ahí la forma logarítmica: duplicar la distancia no duplica el tiempo, y reducir el objetivo a la mitad añade aproximadamente un bit de dificultad.

Detrás está el compromiso velocidad-precisión: si se exige ir rápido a un objetivo pequeño, sube la tasa de error. Por eso medir solo tiempos sin contar errores produce resultados engañosamente buenos.

## Evidencia y límites
- **Nivel: E1** — modelo matemático predictivo, de los más replicados de la psicología aplicada y base de la norma ISO 9241-9 para evaluar dispositivos apuntadores.
- **Qué no modela:** búsqueda visual ni tiempo de decisión (ver DEC-01 Hick, PER-06); arrastres por trayectorias restringidas (ley de dirección). Es unidimensional en origen: en 2D no hay una definición única de `W`; a efectos prácticos NN/g sugiere tomar la menor dimensión del rectángulo. Escalar `D` y `W` en la misma proporción no deja el tiempo exactamente igual, aunque el modelo lo prediga.
- **Táctil:** el modelo clásico subestima la dificultad de objetivos pequeños tocados con el dedo (FFitts). Hoober (UXmatters, 2017) señala que la precisión es mayor en el centro de la pantalla que en los bordes: propone unos **7 mm en el centro y unos 12 mm en las esquinas**, tamaños que contienen ~95 % de los toques observados.
- **Hallazgo de Hoober sobre el agarre** (1.333 observaciones de campo en 2013; resumido en 2017): el mapa clásico de "zonas del pulgar" es conocido pero incorrecto, porque la gente cambia de agarre constantemente; ~75 % toca la pantalla solo con un pulgar, pero menos del 50 % sujeta el móvil con una sola mano (2013: 49 % una mano, 36 % acunado, 15 % dos manos).
- **Bordes y esquinas "infinitos" — ratón frente a tacto:** con ratón o *trackpad* el cursor se detiene en el borde de la pantalla, así que la anchura efectiva en esa dirección es ilimitada (la barra de menús de macOS es el ejemplo clásico). **Con el dedo no funciona igual:** Avrahami (CHI '15, doi:10.1145/2702123.2702439; dos experimentos controlados en tabletas) halló que la proximidad al borde puede tener un efecto negativo significativo en el tiempo de reacción al tacto (verificado en el resumen; texto completo tras muro de pago), y la literatura posterior (Avrahami, 2015; Usuba, Yamanaka y Sato, 2023) recomienda separar los objetivos al menos 4 mm del borde. Una preimpresión de 2026 (Kasahara, Yamanaka y Miyashita, arXiv:2603.23865) informa de lo contrario para la tasa de acierto con objetivos rectangulares que tocan el borde en pantallas sin bisel elevado, y atribuye la discrepancia a la forma del objetivo y del marco (Avrahami usó marcos elevados y objetivos circulares): la cuestión está abierta.
- **Malentendidos frecuentes:**
  - "Más grande siempre es mejor" → la ganancia es logarítmica y decreciente; un botón descomunal deja de leerse como botón y empuja otros objetivos más lejos.
  - "Fitts justifica llevar todo a las esquinas en móvil" → falso al tacto (ver arriba).
  - "Basta con un *padding* invisible" → NN/g señala que si la persona no sabe que el área es mayor, frena igualmente al acercarse a la parte visible. El área ampliada ayuda, pero no sustituye a un tamaño visible razonable.
  - Aplicarla a la mirada (*eye tracking*) es controvertido.

## Aplicación práctica
### Reglas
1. [E] Coloca la acción principal cerca del último punto de atención de la tarea (p. ej. botón de envío junto al último campo, en el orden de la tarea) — Fitts 1954; NN/g.
2. [E] Haz clicable toda la fila o la combinación etiqueta + icono, no solo el icono; asocia `<label>` a casillas y radios — NN/g.
3. [N] Área interactiva mínima de **24×24 px CSS** o espaciado equivalente (WCAG 2.5.8, AA); **44×44 px CSS** para acciones frecuentes, difíciles de deshacer o cercanas al borde (2.5.5, AAA).
4. [E] En móvil, más tamaño en bordes y esquinas que en el centro (~12 mm frente a ~7 mm; Hoober, datos de campo).
5. [E] Para uso con el pulgar a una mano, objetivos de ~9,2 mm en tareas discretas y ~9,6 mm en tareas en serie como teclear — Parhi, Karlson y Bederson (MobileHCI '06, doi:10.1145/1152215.1152260).
6. [H] Separa físicamente las acciones destructivas de las frecuentes (borrar/guardar, comprar/cancelar): los toques imprecisos ocurren en toda la pantalla.
7. [H] No diseñes contra un mapa fijo de zonas del pulgar; prueba en dispositivo real con varios agarres.
8. [E] En escritorio, usa los bordes y esquinas de pantalla para comandos globales solo en aplicaciones a pantalla completa o de sistema; nunca traslades esa lógica al tacto.
9. [E] Menús contextuales que se abren en el cursor y menús radiales (todos los elementos equidistantes; Callahan et al., CHI '88, doi:10.1145/57167.57182) para herramientas expertas. En ese estudio (33 participantes, menús de 8 elementos) los menús radiales redujeron el tiempo de búsqueda del objetivo y los errores; la cifra de "~15 % más rápido" procede del estudio piloto (16 participantes), y los autores hablan de selección "ligeramente más rápida" y piden más experimentos.
10. [H] En submenús en cascada evita túneles estrechos (ley de dirección): tolerancia diagonal ("triángulo de intención") o retardo de cierre.
11. [H] Evita controles que se ocultan solos (p. ej. reproductores de vídeo): obligan a relocalizar el objetivo en cada gesto.

**Tabla de tamaños de objetivo**

| Fuente | Valor | Nivel | Estado de verificación |
|---|---|---|---|
| WCAG 2.2, SC 2.5.8 Target Size (Minimum) | 24×24 px CSS (o espaciado: círculo de 24 px centrado sin solapar; excepciones: control equivalente, enlace en línea, control nativo sin modificar, esencial) | AA | Verificado (W3C, *Understanding*) |
| WCAG 2.2, SC 2.5.5 Target Size (Enhanced) | 44×44 px CSS | AAA | Verificado (W3C, *Understanding*) |
| Apple Human Interface Guidelines | iOS/iPadOS: 44×44 pt por defecto, 28×28 pt mínimo (visionOS 60×60 pt) | Guía de plataforma | Verificado (HIG, *Accessibility*) |
| Material Design (Android) | 48×48 dp (≈ 9 mm), separados ≥ 8 dp | Guía de plataforma | Verificado (Android Developers; Material Design, *Accessibility*) |
| Parhi et al. 2006 (pulgar) | 9,2 mm discreto / 9,6 mm en serie | Estudio | Verificado (resumen) |
| Hoober 2017 (campo) | ~7 mm centro / ~12 mm esquinas | Datos de campo | Verificado (artículo) |

### Por contexto
| Contexto | Aplicación |
|---|---|
| Web/escritorio | Filas y etiquetas clicables; menú contextual en el cursor; esquinas de pantalla solo en apps a pantalla completa; tolerancia diagonal en submenús. |
| Móvil/táctil | Área ≥ 44 pt / 48 dp; más grande junto a bordes; separar del borde; no ocultar controles; separar destructivas. |
| Formularios | Botón de envío junto al último campo; etiquetas clicables; casillas nativas pequeñas con área táctil ampliada. |
| Navegación | Destinos frecuentes grandes y cerca; orden de menús por frecuencia de uso. |
| Dashboards/datos | Puntos de gráfico diminutos → zona de *hover*/toque ampliada o selección por proximidad; alternativa a arrastrar para filtrar rangos (2.5.7). |
| E-commerce | "Añadir al carrito" cerca de talla y precio; controles de cantidad no pegados entre sí. |
| Interfaces conversacionales/IA | Botón de envío junto al campo y alcanzable con el pulgar; *chips* de sugerencia, "copiar", "regenerar" y "detener" con área suficiente. |
| Voz | No aplica a la entrada vocal; sí a los controles visibles asociados (micrófono, cancelar). |
| Sistemas de diseño | Token de área mínima de objetivo independiente del tamaño visual; variantes compactas que conserven 24 px CSS. |

### Ejemplos
- **Bueno:** una lista de ajustes en móvil donde toda la fila activa el interruptor, con la fila de 48 dp de alto: la persona acierta aunque toque el texto.
- **Incumple:** un formulario largo cuyo botón "Continuar" está arriba a la derecha, lejos del último campo, y es un icono de 20 px: distancia máxima y anchura mínima.
- **Incumple (al tacto):** un menú móvil con iconos de 32 px pegados al borde inferior, copiado de la lógica de "esquinas infinitas" de escritorio.

## Anti-patrones
- Iconos de 16–20 px sin área ampliada como única forma de activar una acción.
- "Aceptar" enorme junto a un "Rechazar" o una "×" diminutos (muros de *cookies*, modales de suscripción): Fitts usado contra la persona.
- Anuncios colocados donde caen los toques accidentales.
- Acciones opuestas contiguas (eliminar al lado de editar).
- Funciones que solo se ejecutan arrastrando o con trayectorias precisas en *hover*.

## Ética y accesibilidad
- **Línea roja:** manipular deliberadamente tamaño o distancia para favorecer la opción que conviene al negocio (aceptar seguimiento, suscribirse) y dificultar la contraria.
- Personas con temblor, artritis, baja visión o punteros de cabeza o boca tienen una imprecisión absoluta mucho mayor (la componente FFitts).
- WCAG 2.2: **2.5.8 Target Size (Minimum)** (AA), **2.5.5 Target Size (Enhanced)** (AAA), **2.5.7 Dragging Movements** (AA, alternativa sin arrastre: contrapartida de la ley de dirección), **2.5.1 Pointer Gestures** (A).

## Cómo auditarla
### Señales observables
- Objetivos interactivos cuya área real (*box model*, incluido `::before` de ampliación) mide menos de 24×24 px CSS.
- Acciones principales lejos del foco de la tarea; acciones opuestas pegadas.
- *Rage taps*, *dead clicks* y toques seguidos de "atrás" en menos de 2 s.
### Preguntas
- ¿Cuál es el área interactiva real frente a la visual?
- ¿La acción siguiente está donde ya mira la persona?
- ¿Algo depende de esquinas o bordes en una interfaz táctil?
- ¿Hay alternativa sin arrastre?
### Métricas
- Regla `target-size` de axe-core; aviso de *tap targets* de Lighthouse.
- Tasa de error por objetivo y tiempo hasta el primer clic en test; cálculo de `ID` para comparar variantes.
- Analítica de *rage/dead clicks* (Hotjar, Clarity, FullStory).
- Evaluación formal de dispositivos: *throughput* (bits/s) según ISO 9241-9.

## Relaciones
- Refuerza / se apoya en: PER-01 Ley de proximidad — agrupar acción y contexto acorta `D`.
- Refuerza / se apoya en: ACC-02 Umbral de Doherty — el tiempo total de interacción suma el motor y el del sistema.
- Refuerza / se apoya en: MOT-01 Flujo — menos fricción motora mantiene el ritmo.
- Refuerza / se apoya en: SIS-01 Ley de Jakob — ubicaciones convencionales reducen búsqueda y distancia.
- Tensiona con: DEC-01 Ley de Hick / DEC-02 Sobrecarga de opciones — muchas opciones grandes alargan las distancias; priorizar y agrupar.
- Tensiona con: SIS-04 Navaja de Occam / PER-05 Prägnanz / DEC-04 Estética-usabilidad — la limpieza visual empuja a iconos diminutos; conservar el área interactiva aunque el icono sea pequeño.
- Tensiona con: PER-07 Von Restorff — destacar no es agrandar; contraste y posición también sirven.
- Tensiona con: SIS-03 Ley de Tesler — la complejidad retirada del layout puede reaparecer como gestos precisos.
- Tensiona con: MEM-04 Fragmentación — más pasos, más desplazamientos y clics (T5).
- Se confunde a menudo con: DEC-01 Ley de Hick — Hick modela el tiempo de decidir; Fitts, el de alcanzar un objetivo ya elegido. Y con la ley de dirección — trayectorias en túnel, relación lineal.

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/fittss-law/ — síntesis divulgativa.
- Primarias:
  - Fitts, P. M. (1954). The information capacity of the human motor system in controlling the amplitude of movement. *J. Exp. Psychol.*, 47(6), 381–391. doi:10.1037/h0055392
  - Fitts, P. M. y Peterson, J. R. (1964). Information capacity of discrete motor responses. *J. Exp. Psychol.*, 67(2), 103–112. doi:10.1037/h0045689
  - MacKenzie, I. S. (1992). Fitts' law as a research and design tool in human–computer interaction. *Human–Computer Interaction*, 7, 91–139. doi:10.1207/s15327051hci0701_3
  - Accot, J. y Zhai, S. (1997). Beyond Fitts' law: models for trajectory-based HCI tasks. *CHI '97*, 295–302.
  - Bi, X., Li, Y. y Zhai, S. (2013). FFitts Law: Modeling Finger Touch with Fitts' Law. *CHI 2013*, 1363–1372.
  - Callahan, J., Hopkins, D., Weiser, M. y Shneiderman, B. (1988). An empirical comparison of pie vs. linear menus. *CHI '88*, 95–100. doi:10.1145/57167.57182
  - Parhi, P., Karlson, A. y Bederson, B. (2006). Target size study for one-handed thumb use on small touchscreen devices. *MobileHCI '06*, 203–210. doi:10.1145/1152215.1152260
  - Avrahami, D. (2015). The Effect of Edge Targets on Touch Performance. *CHI '15*, 1837–1846. doi:10.1145/2702123.2702439 (verificado el resumen; texto completo tras muro de pago)
  - Usuba, H., Yamanaka, S. y Sato, J. (2023). Clarifying the effect of edge targets in touch pointing through crowdsourced experiments. *Proc. ACM Hum.-Comput. Interact.*, 7(ISS). doi:10.1145/3626469
  - Kasahara, N., Yamanaka, S. y Miyashita, H. (2026). Skewed Dual Normal Distribution Model: Predicting Touch Pointing Success Rates for Targets Near Screen Edges and Corners. Preimpresión, arXiv:2603.23865
  - ISO/TS 9241-411:2012. Ergonomics of human-system interaction — Part 411: Evaluation methods for the design of physical input devices (sustituye a ISO 9241-9:2000).
  - Apple. Human Interface Guidelines — Accessibility: https://developer.apple.com/design/human-interface-guidelines/accessibility
  - Android Developers. Make apps more accessible (touch target 48dp): https://developer.android.com/guide/topics/ui/accessibility/apps · Material Design, Accessibility: https://m2.material.io/design/usability/accessibility.html
  - W3C (2023). WCAG 2.2 Understanding 2.5.8 y 2.5.5: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html · https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html
- Secundarias consultadas:
  - Budiu, R. (2022). Fitts's Law and Its Applications in UX. NN/g: https://www.nngroup.com/articles/fitts-law/
  - Hoober, S. (2017). Design for Fingers, Touch, and People, Part 1. UXmatters: https://www.uxmatters.com/mt/archives/2017/03/design-for-fingers-touch-and-people-part-1.php
  - Hoober, S. (2013). How Do Users Really Hold Mobile Devices? UXmatters: https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php
  - Hoober, S. (2022). Fitts' Law in the Touch Era. Smashing Magazine: https://www.smashingmagazine.com/2022/02/fitts-law-touch-era/
  - https://en.wikipedia.org/wiki/Fitts%27s_law
