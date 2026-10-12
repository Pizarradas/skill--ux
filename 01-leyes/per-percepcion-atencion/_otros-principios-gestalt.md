---
id: PER-ANEXO
nombre: Otros principios Gestalt (no incluidos en Laws of UX)
nombre_en: Other Gestalt principles
familia: PER
evidencia: C
etiquetas: [gestalt, figura-fondo, cierre, continuidad, destino-comun, simetria, paralelismo, punto-focal, experiencia-pasada]
refuerza: [PER-01, PER-02, PER-03, PER-04, PER-05, PER-07, SIS-01]
---

# PER-ANEXO · Otros principios Gestalt (*Other Gestalt principles*)

> Laws of UX recoge cinco principios de agrupación (PER-01 a PER-05). La tradición Gestalt y la investigación posterior describen otros que también organizan una interfaz. Esta ficha complementaria los resume con su mecanismo, reglas de uso y fuentes.

**Cómo leerla.** Igual que en las demás fichas PER: son tendencias *a igualdad de lo demás*, no reglas deterministas. Compiten entre sí y con la tarea, y su fuerza relativa depende del contexto (Wagemans et al. 2012). Las reglas son **[H]** (heurísticas) salvo indicación. Salvo que se diga otra cosa, todos aparecen en Wertheimer (1923) y se tratan en Wagemans et al. (2012), Bradley (2014, Smashing Magazine) e IxDF.

---

## 1. Figura-fondo (*Figure/Ground*)

- **Origen:** Rubin (1915), *Synsoplevede Figurer* (Copenhague: Gyldendal), con la conocida figura jarrón-caras (referencia y atribución verificadas en Wagemans et al. 2012; original en danés no consultado).
- **Mecanismo:** separamos la escena en una figura (con forma, "delante") y un fondo (sin forma, "detrás"). Las regiones más pequeñas, convexas, simétricas y rodeadas tienden a verse como figura: los principios configuracionales clásicos (Rubin 1915; Harrower 1936, según Wagemans et al. 2012; también Bradley 2014 e IxDF).
- **Reglas en UI:**
  1. Para capas superpuestas (modal, menú, *popover*), separa la figura con *scrim* que atenúe el fondo y con elevación (sombra), no solo con un borde fino.
  2. Texto sobre imagen solo con capa, degradado o zona de color que garantice contraste: **WCAG 1.4.3 Contraste mínimo (AA)** — 4,5:1 texto normal, 3:1 texto grande — y **1.4.11 Contraste no textual (AA)**, 3:1 para componentes.
  3. Evita fondos fotográficos o texturas detrás de controles; la figura (el control) debe ganar siempre.
- **Riesgo:** figura-fondo ambiguo en logotipos o ilustraciones que se usan como icono funcional.
- **Fuentes:** Bradley (2014); IxDF, "The Laws of Figure/Ground, Prägnanz, Closure, and Common Fate"; Wagemans et al. (2012) (la parte I trata expresamente la organización figura-fondo).

## 2. Cierre (*Closure*)

- **Mecanismo:** completamos figuras incompletas si hay información suficiente; si el hueco es excesivo, la forma se rompe (Bradley 2014). Es un caso de la tendencia a la buena forma (PER-05).
- **Reglas en UI:**
  1. Iconos de contorno y logotipos pueden omitir trazos, pero comprueba el reconocimiento a tamaño real; el panda de WWF es el ejemplo clásico (IxDF).
  2. En carruseles horizontales, deja la última tarjeta visible cortada por el borde para indicar que hay más contenido (pista de desplazamiento).
  3. No confíes en el cierre para controles críticos: un campo sin borde completo o un botón "fantasma" puede no leerse como objeto. Si el límite identifica el control, **WCAG 1.4.11** (3:1).
- **Fuentes:** Bradley (2014); IxDF (misma pieza).

## 3. Buena continuidad (*Good Continuation*)

- **Origen:** Wertheimer (1923) lo describe como "factor de dirección" **[verificada]**.
- **Mecanismo:** seguimos líneas y curvas en la dirección que llevan; un elemento fuera de la trayectoria parece desconectado (IxDF).
- **Reglas en UI:**
  1. Alinea los elementos de una secuencia (pasos, filas, etiquetas) sobre un eje común; romper la línea comunica "esto es otra cosa".
  2. En *steppers*, líneas de tiempo y flujos, mantén una dirección única (izquierda→derecha o arriba→abajo) sin quiebros innecesarios.
  3. En gráficos, ejes y series continuas sin cortes que sugieran discontinuidad de datos inexistente; en listas horizontales, deja que el contenido continúe fuera de pantalla para invitar a desplazarse.
- **Fuentes:** Wertheimer (1923); IxDF, "Laws of Proximity, Uniform Connectedness, and Continuation".

## 4. Destino común (*Common Fate*)

- **Origen:** Wertheimer (1923) **[verificada]**. Variantes modernas: **sincronía** y **destino común generalizado** (cambios de luminancia simultáneos), descritas en Wagemans et al. (2012) como nuevos principios de agrupación: lo que cambia a la vez (luminancia, no sólo posición) se agrupa, aunque los cambios no vayan en la misma dirección en el caso de la sincronía.
- **Mecanismo:** lo que se mueve o cambia a la vez, en la misma dirección y velocidad, se percibe como un grupo.
- **Reglas en UI:**
  1. Anima juntos los elementos de un mismo grupo (submenú que se despliega como bloque — ejemplo de LinkedIn en IxDF —, selección múltiple, arrastrar un grupo).
  2. No animes a la vez elementos no relacionados: crean agrupaciones falsas y favorecen la ceguera al cambio (PER-06).
  3. Respeta `prefers-reduced-motion` y ofrece una señal estática equivalente (agrupación por región o semejanza). **WCAG 2.2.2 Pausar, detener, ocultar (A)** y **2.3.3 Animación por interacciones (AAA)**.
- **Fuentes:** Wertheimer (1923); Wagemans et al. (2012); IxDF (pieza sobre figure/ground y common fate).

## 5. Simetría y paralelismo (*Symmetry*, *Parallelism*)

- **Mecanismo:** las formas simétricas se perciben como una unidad organizada alrededor de un centro; Bradley (2014) muestra un caso en que la simetría se impone a la proximidad. Los elementos paralelos se perciben como relacionados (Bradley 2014).
- **Reglas en UI:**
  1. Usa composiciones simétricas para transmitir estabilidad (pantallas de confirmación, páginas de inicio de sesión) y asimetría intencional para dirigir la mirada hacia un punto.
  2. Cuando dos opciones deban percibirse como un par de alternativas equivalentes, dales disposición simétrica; si no lo son, no fuerces la simetría.
  3. Mantén paralelas (misma orientación, mismo eje) las líneas, columnas y elementos que pertenecen al mismo sistema; un elemento girado o desalineado se lee como ajeno.
- **Fuentes:** Bradley (2014); Wagemans et al. (2012).

## 6. Punto focal (*Focal Point*)

- **Mecanismo:** un elemento que contrasta con su entorno captura y retiene la atención (Bradley 2014). Es la cara perceptiva del **PER-07 Efecto Von Restorff** y del *pop-out* de la teoría de integración de rasgos (Treisman & Gelade 1980).
- **Reglas en UI:**
  1. Un punto focal por zona de atención; varios se anulan entre sí (T3).
  2. Crea el foco con más de un canal (tamaño, color, peso, posición, espacio a su alrededor), no solo con color (**WCAG 1.4.1 Uso del color (A)**).
  3. Comprueba que el foco no adopta rasgos de anuncio (fondo de color en rectángulo, animación), que se filtrarían (PER-06).
- **Fuentes:** Bradley (2014); véase PER-07 para las fuentes primarias del efecto de aislamiento.

## 7. Experiencia pasada (*Past Experience*)

- **Origen:** considerada en Wertheimer (1923) **[verificada]**.
- **Mecanismo:** la percepción se apoya en la experiencia individual y cultural: un rojo/verde se lee como parar/avanzar por el semáforo. Bradley (2014) lo califica como el principio más débil, porque cede ante los demás (afirmación divulgativa, no experimental).
- **Reglas en UI:**
  1. Usa formas y ubicaciones convencionales para lo estructural (lupa para buscar, carrito arriba a la derecha) — **SIS-01 Ley de Jakob**.
  2. Revisa los significados culturales del color y de los iconos antes de localizar un producto; no los uses como única señal.
  3. No esperes que la experiencia pasada compense una mala agrupación: al ser débil, la proximidad o la región común la anulan.
- **Fuentes:** Wertheimer (1923); Bradley (2014).

## 8. "Set" objetivo (*Einstellung*)

- **Origen:** Wertheimer (1923) **[verificada]**.
- **Mecanismo:** la agrupación percibida en los elementos anteriores persiste al leer los siguientes; se crea una expectativa de patrón.
- **Reglas en UI:**
  1. Mantén el mismo patrón en todos los ítems de una lista, tabla o rejilla (mismo orden de campos, misma posición de la acción).
  2. Si un ítem debe romper el patrón (anuncio, aviso), márcalo explícitamente; un cambio silencioso a mitad de lista provoca errores.
- **Fuentes:** Wertheimer (1923).

---

## Fuentes

- Primarias:
  - Wertheimer, M. (1923). Untersuchungen zur Lehre von der Gestalt II. *Psychologische Forschung*, 4, 301–350. Traducción inglesa "Laws of organization in perceptual forms", en W. D. Ellis (ed., 1938), *A Source Book of Gestalt Psychology*, pp. 71–88. https://www.yorku.ca/pclassic/Wertheimer/Forms/forms.htm
  - Wagemans, J., Elder, J. H., Kubovy, M., Palmer, S. E., Peterson, M. A., Singh, M., & von der Heydt, R. (2012). A century of Gestalt psychology in visual perception: I. Perceptual grouping and figure-ground organization. *Psychological Bulletin*, 138(6), 1172–1217. doi:10.1037/a0029333
  - Rubin, E. (1915). *Synsoplevede Figurer: Studier i psykologisk Analyse*. Copenhague: Gyldendal (referencia tomada de Wagemans et al. 2012; original no consultado).
- Secundarias consultadas:
  - https://www.smashingmagazine.com/2014/03/design-principles-visual-perception-and-the-principles-of-gestalt/ (Bradley, 2014)
  - https://ixdf.org/literature/article/the-laws-of-figure-ground-praegnanz-closure-and-common-fate-gestalt-principles-3
  - https://ixdf.org/literature/article/laws-of-proximity-uniform-connectedness-and-continuation-gestalt-principles-2
  - https://en.wikipedia.org/wiki/Principles_of_grouping
