---
id: DEC-03
nombre: Sesgo cognitivo
nombre_en: Cognitive Bias
alias: [sesgos cognitivos, heurísticas y sesgos, heuristics and biases]
familia: DEC
evidencia: C
etiquetas: [decision, juicio, heuristicas, arquitectura-de-la-eleccion, defaults, etica, patrones-oscuros, investigacion]
refuerza: [MOT-05, MEM-05, PER-07, DEC-04, DEC-02, MOT-02, MOT-03, MEM-01, MEM-02, PER-06]
tensiona: [ACC-04, SIS-01]
tensiones: [T12, T7, T4]
fuente_laws_of_ux: https://lawsofux.com/cognitive-bias/
---

# DEC-03 · Sesgo cognitivo (*Cognitive Bias*)

> Un sesgo cognitivo es una desviación sistemática y predecible respecto a una norma de racionalidad (lógica, probabilidad, utilidad esperada) en el juicio o la decisión, producida casi siempre por heurísticas: atajos que ahorran esfuerzo y aciertan en muchos entornos, pero fallan de forma previsible en otros.

**Idea clave para quien diseña:** no existe una interfaz neutral; siempre estás haciendo arquitectura de la elección, así que decide a favor de quién inclinas la balanza y si funcionaría igual si la persona lo supiera.

## Origen
- Kahneman, D., & Tversky, A. (1972). Subjective probability: A judgment of representativeness. *Cognitive Psychology*, 3(3), 430–454. doi:10.1016/0010-0285(72)90016-3.
- **Tversky, A., & Kahneman, D. (1974).** Judgment under uncertainty: Heuristics and biases. *Science*, 185(4157), 1124–1131. doi:10.1126/science.185.4157.1124. Describe tres heurísticas: representatividad, disponibilidad, y anclaje y ajuste.
- Kahneman & Tversky (1979), teoría prospectiva, *Econometrica* 47(2), 263–291, doi:10.2307/1914185: aversión a la pérdida y punto de referencia.
- Tversky & Kahneman (1981), efecto de encuadre, *Science* 211(4481), 453–458, doi:10.1126/science.7455683.
- Kahneman, D. (2011). *Thinking, Fast and Slow*. Divulgación del marco Sistema 1 / Sistema 2.
- Aplicación a diseño: Thomas, D. D. (2020). *Design for Cognitive Bias*. A Book Apart (no leído).

## Mecanismo
El **Sistema 1** es rápido, automático y asociativo; el **Sistema 2**, lento, deliberado y costoso. La mayoría de microdecisiones de interfaz (pulsar, aceptar, seguir) las toma el Sistema 1, con poca atención y a menudo bajo carga. Los sesgos nacen de restricciones conocidas: atención limitada (PER-06), memoria de trabajo limitada (MEM-02), recuperación desigual de recuerdos (disponibilidad), dependencia del punto de referencia (anclaje, encuadre, aversión a la pérdida), señales sociales (prueba social) y motivación (confirmación, optimismo). Por eso los sesgos crecen bajo carga y prisa.

Que sea **sistemático** importa: no es ruido aleatorio, así que promediar a muchas personas no lo cancela. Hay debate sobre su naturaleza: la escuela de la racionalidad ecológica (Gigerenzer) sostiene que muchas heurísticas son adaptativas en su entorno y que algunos "sesgos" reflejan diseños experimentales artificiales; Haselton & Buss (2000, *JPSP*, teoría de la gestión del error) proponen que la evolución favorece sesgar hacia el error menos costoso. Para diseño, la consecuencia es la misma: **la interfaz forma parte del entorno de decisión**.

## Evidencia y límites
- **Nivel: C** — es un constructo paraguas, no un efecto único; la evidencia hay que juzgarla **sesgo a sesgo** (véase la columna "Ev." de la tabla). Los más robustos: anclaje, encuadre, efecto por defecto, disponibilidad, statu quo, confirmación y aversión a la pérdida (esta última con debate sobre su magnitud).
- **Más frágiles o polémicos:** buena parte del *priming* social y el agotamiento del ego, afectados por la crisis de replicación (una réplica preregistrada en 23 laboratorios, N = 2 141, halló un efecto de agotamiento pequeño con un intervalo de confianza que incluía el cero: Hagger et al. 2016); el efecto señuelo en contextos no numéricos; y el tamaño real de los *nudges* en general: el metaanálisis de Mertens et al. (2022, *PNAS*; más de 200 estudios) estimó d = 0,45, pero con sesgo de publicación, y Maier et al. (2022, *PNAS*) sostienen que, al corregirlo, no queda evidencia de un efecto medio.
- **Efecto por defecto, con matiz:** Johnson & Goldstein (2003), "Do defaults save lives?", *Science* 302(5649), 1338–1339: el consentimiento efectivo para donar órganos es muy superior en países con modelo de exclusión voluntaria (*opt-out*), con casi 60 puntos de diferencia entre grupos. Pero eso es **consentimiento registrado**, no donaciones efectivas: en el mismo artículo, el aumento estimado de donaciones con el *opt-out* es del 16,3 % (de 14,1 a 16,4 donantes por millón). La revisión de Steffel et al. (2019) concluye que el consentimiento presunto es un factor entre muchos y que la infraestructura sanitaria pesa tanto o más.
- **Malentendidos frecuentes:**
  - Llamar "sesgo" a cualquier conducta que no gusta al equipo.
  - Creer que conocer un sesgo inmuniza; ayuda a detectarlo, no lo elimina.
  - Aplicar listas de "180 sesgos" sin mirar la evidencia de cada uno.
  - Extrapolar efectos de laboratorio con dinero hipotético a productos reales sin test.

## Aplicación práctica
### Tabla de sesgos más relevantes para UX
Ev. (subescala de esta tabla, equivalente a la escala general de `00-indice/niveles-de-evidencia.md`): **A** robusto y muy replicado (≈ E2) · **B** sólido con moderadores importantes (≈ E2 con moderadores) · **C** mixto o polémico (≈ E3). Al citar un sesgo, usa la escala general: p. ej. "efecto por defecto — E2". Todos los orígenes de la tabla se han comprobado en sus metadatos bibliográficos (autor, año, revista); las referencias completas están en "Fuentes".

| # | Sesgo (ES / EN) | Origen | Ev. | Uso de diseño legítimo | Línea roja |
|---|---|---|---|---|---|
| 1 | Anclaje / *Anchoring* | Tversky & Kahneman 1974 | A | Mostrar una referencia **real** (precio habitual verificable, consumo medio); importes sugeridos coherentes | Precios "antes" inventados o inflados; anclas irrelevantes para justificar un precio |
| 2 | Encuadre / *Framing* | Tversky & Kahneman 1981 | A | Riesgos en frecuencias naturales ("3 de cada 100"); mostrar ambos marcos en decisiones serias | Encuadrar para ocultar costes ("solo 0,99 € al día" que esconde un compromiso anual) |
| 3 | Efecto por defecto / *Default effect* | Johnson & Goldstein 2003; Samuelson & Zeckhauser 1988 | A | Valores por defecto al servicio de la persona: privacidad máxima, notificaciones mínimas, envío más común | Casillas premarcadas de marketing, seguros o donaciones; "aceptar todo" preactivado en cookies (en la UE, además, choca con el RGPD) |
| 4 | Aversión a la pérdida / *Loss aversion* | Kahneman & Tversky 1979 | A/B | Avisar de pérdidas reales ("perderás los cambios no guardados"); mostrar qué se conserva al bajar de plan | *Confirmshaming*; amenazas de pérdida exageradas para retener |
| 5 | Prueba social / *Social proof* | Cialdini 1984; Asch 1956 (conformidad) | B | Reseñas verificadas, número real de usuarios, valoraciones con su distribución | Actividad falsa ("12 personas viendo esto"), reseñas inventadas (categoría de Mathur et al. 2019) |
| 6 | Escasez y urgencia / *Scarcity* | Cialdini 1984 | B | Stock o plazos **reales** (cierre de inscripción, últimas plazas confirmadas) | Contadores que se reinician; "solo quedan 2" falso (categorías de Mathur et al. 2019) |
| 7 | Confirmación / *Confirmation bias* | Wason 1960; Nickerson 1998 | A | En investigación: hipótesis explícitas y búsqueda de evidencia contraria. En producto: perspectivas diversas en recomendadores e IA | Feeds que solo refuerzan creencias para maximizar *engagement*; IA complaciente (*sycophancy*) |
| 8 | Disponibilidad / *Availability* | Tversky & Kahneman 1973/1974 | A | Ejemplos concretos para ayudar a estimar; recordatorios de casos de uso | Inflar riesgos con anécdotas llamativas para vender protección |
| 9 | Señuelo / *Decoy (asymmetric dominance)* | Huber, Payne & Puto 1982 | B/C | Estructurar planes para que la comparación sea clara (con cautela) | Planes sin sentido que existen solo para empujar al caro |
| 10 | Precio cero / *Zero-price effect* | Shampanier, Mazar & Ariely 2007 | B | Prueba gratuita realmente gratuita y fácil de cancelar | "Gratis" con renovación de pago oculta (*sneaking*, suscripción escondida) |
| 11 | Coste hundido / *Sunk cost* | Arkes & Blumer 1985 | B | Guardar el progreso para que abandonar no desperdicie lo hecho | Retener con "has invertido tanto…"; encarecer la salida |
| 12 | Efecto halo / *Halo effect* | Thorndike 1920 | A | Cuidar la primera impresión y la calidad visual (DEC-04) | Usar la estética para tapar defectos o términos abusivos |
| 13 | Statu quo / inercia | Samuelson & Zeckhauser 1988 | A | Migraciones que conservan la configuración; cambios graduales | Renovaciones silenciosas; dificultar el cambio de proveedor (*obstruction*) |
| 14 | Efecto IKEA / *IKEA effect* | Norton, Mochon & Ariely 2012 | B | Personalización y configuración inicial que crean apego | Obligar a invertir esfuerzo para generar dependencia (*lock-in*) |
| 15 | Sesgo de automatización / *Automation bias* | Parasuraman & Riley 1997; Mosier et al. 1998; Skitka et al. 1999 | B | En IA: mostrar incertidumbre, fuentes y puntos de verificación; confirmar acciones críticas | Presentar la salida de la IA como infalible; ocultar que es generada |
| 16 | Posición serial / *Serial position* | Ebbinghaus 1885; Murdock 1962 | A | Lo importante al principio y al final de las listas (MEM-05) | Esconder condiciones en el centro de textos largos |
| 17 | Pico-final / *Peak-end* | Kahneman et al. 1993 | A | Cerrar bien los episodios (MOT-05) | Final agradable para tapar un cobro o abuso (MOT-05) |

### Reglas
1. [E] Trata cada valor por defecto como una decisión de diseño con consecuencias: elige el que serviría a la persona informada y hazlo visible y fácil de cambiar (Johnson & Goldstein 2003; T12).
2. [E] Toda cifra de referencia, escasez o prueba social debe ser real y auditable; sus versiones falsas son patrones oscuros documentados (Mathur et al. 2019).
3. [H] **Prueba de transparencia:** si el diseño dejaría de funcionar cuando la persona supiera qué técnica se usa y por qué, es manipulación (criterio próximo al de Thaler & Sunstein, *Nudge*, 2008).
4. [H] **Prueba de interés:** el empujón debe llevar a lo que la persona elegiría con información completa y sin prisa.
5. [H] **Simetría:** darse de baja debe costar lo mismo que darse de alta. El art. 25.3.c de la Ley de Servicios Digitales de la UE (Reglamento 2022/2065) cita expresamente "hacer que el procedimiento para poner fin a un servicio sea más difícil que suscribirse" entre las prácticas sobre las que la Comisión puede dar directrices. En EE. UU., la regla *click-to-cancel* de la FTC (2024) fue anulada por el Tribunal de Apelaciones del Octavo Circuito en julio de 2025, y la FTC restableció el texto anterior en febrero de 2026.
6. [H] En decisiones serias (salud, dinero, privacidad), presenta los riesgos en frecuencias y en los dos encuadres.
7. [H] En IA conversacional, diseña contra la complacencia y el sesgo de automatización: incertidumbre visible, fuentes, confirmación antes de acciones irreversibles y sin antropomorfismo que exagere la competencia.
8. [H] No uses un sesgo concreto sin comprobar su nivel de evidencia y sin test en tu contexto.

### Por contexto
| Contexto | Aplicación |
|---|---|
| Formularios | Sin casillas premarcadas que beneficien al negocio; consentimientos separados y en blanco. |
| E-commerce | Precios de referencia verificables; reseñas con verificación y distribución; stock real. |
| Onboarding | Defaults de privacidad máxima; personalización que aporte valor (efecto IKEA legítimo). |
| Suscripciones | Baja simétrica al alta; avisos de renovación previos; "gratis" que sea gratis. |
| Dashboards/datos | Ejes y referencias que no anclen artificialmente; comparar con bases honestas. |
| Conversacional/IA | Señal de incertidumbre, fuentes, desacuerdo cuando procede (anti-*sycophancy*). |
| Sistemas de diseño | Botones de aceptar y rechazar con peso visual equivalente en consentimientos; patrones de confirmación estándar. |

### Ejemplos
- **Bueno:** un gestor de pensiones que, al darse de alta, preselecciona una aportación prudente y diversificada, explica por qué y permite cambiarla en un clic.
- **Bueno:** una calculadora de consumo eléctrico que compara tu gasto con la media real de hogares similares (anclaje honesto).
- **Lo incumple:** una reserva de hotel con "¡Solo queda 1 habitación!" y "8 personas mirando ahora" que se repiten idénticos al recargar, más una casilla de seguro de cancelación premarcada.

## Sesgos del propio equipo de UX
Los sesgos no afectan solo a las personas usuarias. Whitenton (NN/g) mostró a unos 1 000 profesionales de UX el mismo resultado de un test con 20 usuarios en dos encuadres: con "4 de 20 no encontraron la búsqueda", el 51 % recomendó rediseñar; con "16 de 20 la encontraron", el 39 % (p < 0,0001). Mismo dato, distinta decisión.
- **Encuadre de hallazgos:** reporta éxito y fracaso a la vez ("16 de 20 la encontraron; 4 no").
- **Confirmación:** escribe hipótesis antes de investigar, busca activamente evidencia contraria y triangula métodos.
- **Precisión ilusoria con n pequeños:** con n = 20, un 80 % de éxito es compatible con valores aproximados entre 58 % y 93 % (NN/g); da intervalos, no solo porcentajes.
- **Halo en los tests:** un prototipo pulido infla las valoraciones (DEC-04, T4).
- **Disponibilidad:** la última sesión o el cliente más ruidoso pesa más de lo que debe; contrasta con datos agregados.
- **Coste hundido:** "ya hemos invertido mucho en este diseño" no es un argumento de usabilidad.

## Anti-patrones
- Patrones oscuros: Mathur et al. (2019) analizaron ~53 000 páginas de producto de ~11 000 tiendas y hallaron 1 818 instancias de 15 tipos en 7 categorías (*sneaking*, *urgency*, *misdirection*, *social proof*, *scarcity*, *obstruction*, *forced action*); 183 sitios usaban prácticas claramente engañosas y 22 terceros las vendían listas para usar. Casi todos explotan sesgos de la tabla.
- Botones asimétricos (aceptar destacado, rechazar como enlace gris).
- *Confirmshaming* y dobles negaciones.
- Invertir la posición convencional de los botones para inducir errores (abuso de SIS-01).

## Ética y accesibilidad
- **Línea roja general:** veracidad (datos reales), simetría (salir tan fácil como entrar), transparencia (funcionaría si se supiera) e interés de la persona. Aplica la prueba de cuatro preguntas de `06-etica-accesibilidad/etica-y-patrones-oscuros.md`.
- Las personas con discapacidad cognitiva, mayores, bajo estrés o con lector de pantalla son más vulnerables a encuadres engañosos, urgencia falsa y casillas premarcadas [H].
- WCAG 2.2: **2.2.1** Tiempo ajustable (temporizadores de urgencia); **3.3.4** Prevención de errores (legales, financieros, datos): revisar, confirmar o deshacer; **3.3.2** Etiquetas o instrucciones (opciones sin dobles negaciones); **1.3.1** Información y relaciones; **4.1.2** Nombre, función, valor (estado real de casillas anunciado).

## Cómo auditarla
### Señales observables
- Casillas premarcadas; botones asimétricos en consentimientos.
- Contadores o mensajes de stock que se reinician al recargar.
- Textos de *confirmshaming*; precios tachados sin referencia verificable.
- Flujo de baja más largo que el de alta; reseñas sin verificación.
- Respuestas de IA sin señal de incertidumbre.
### Preguntas
- ¿Qué valor por defecto ve la persona y a quién beneficia?
- ¿El encuadre del precio o del riesgo es completo?
- ¿Los datos sociales y de escasez son reales y auditables?
- ¿Cuántos pasos hay para darse de baja frente a darse de alta?
- En investigación: ¿cómo se encuadraron los hallazgos?, ¿se buscó evidencia contraria?, ¿se reportan porcentajes de n pequeños como si fueran precisos?
### Métricas
- Pasos y tiempo de baja frente a alta.
- Tasa de cambio del valor por defecto (si casi nadie lo cambia y luego se queja, revisa a quién sirve).
- Métricas de contrapeso: devoluciones, reclamaciones, bajas, arrepentimiento, cancelaciones tempranas.
- Prueba de recarga: los indicadores de escasez/actividad no deben variar sin cambio real.

## Relaciones
- Refuerza / se apoya en (es categoría paraguas de):
  - MOT-05 Regla pico-final — caso concreto de sesgo de memoria.
  - MEM-05 Efecto de posición serial — sesgo de recuerdo por orden.
  - PER-07 Efecto Von Restorff — sesgo de saliencia.
  - DEC-04 Efecto estética-usabilidad — forma del efecto halo.
  - DEC-02 Sobrecarga de opciones — defaults, statu quo y señuelo actúan en la elección.
  - MOT-02 Gradiente de meta y MOT-03 Zeigarnik — palancas motivacionales con el mismo riesgo ético (T7).
  - MEM-01, MEM-02, PER-06 — la carga y la atención limitada aumentan los sesgos.
- Tensiona con:
  - ACC-04 Paradoja del usuario activo — quien no lee queda más expuesto a encuadres.
  - SIS-01 Ley de Jakob — las convenciones pueden usarse para engañar.
  - T12 — el default es la herramienta más potente y la más peligrosa; T4 — sesgo de halo en la evaluación.
- Se confunde a menudo con: "error humano" o "falta de atención" — el sesgo es sistemático y previsible, por tanto diseñable; también con "manipulación", que es un uso posible, no el concepto.

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/cognitive-bias/ — síntesis divulgativa.
- Primarias:
  - Kahneman, D., & Tversky, A. (1972). Subjective probability: A judgment of representativeness. *Cognitive Psychology*, 3(3), 430–454. https://doi.org/10.1016/0010-0285(72)90016-3
  - Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science*, 185(4157), 1124–1131. https://doi.org/10.1126/science.185.4157.1124
  - Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*, 47(2), 263–291. https://doi.org/10.2307/1914185
  - Tversky, A., & Kahneman, D. (1981). The framing of decisions and the psychology of choice. *Science*, 211(4481), 453–458. https://doi.org/10.1126/science.7455683
  - Johnson, E. J., & Goldstein, D. (2003). Do defaults save lives? *Science*, 302(5649), 1338–1339. https://doi.org/10.1126/science.1091721
  - Steffel, M., Williams, E. F., & Tannenbaum, D. (2019). Does changing defaults save lives? Effects of presumed consent organ donation policies. *Behavioral Science & Policy*, 5(1), 68–88. https://doi.org/10.1353/bsp.2019.0005 (solo resumen consultado)
  - Mathur, A., et al. (2019). Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites. *Proc. ACM HCI*, 3(CSCW), art. 81. https://doi.org/10.1145/3359183 (preprint: https://arxiv.org/abs/1907.07032)
  - Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
  - Thaler, R., & Sunstein, C. (2008). *Nudge*. Yale University Press.
  - Orígenes de la tabla (metadatos verificados en Crossref u Open Library):
    - Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. *Cognitive Psychology*, 5(2), 207–232. https://doi.org/10.1016/0010-0285(73)90033-9
    - Samuelson, W., & Zeckhauser, R. (1988). Status quo bias in decision making. *Journal of Risk and Uncertainty*, 1(1), 7–59. https://doi.org/10.1007/BF00055564
    - Cialdini, R. B. (1984). *Influence: How and Why People Agree to Things*. William Morrow.
    - Asch, S. E. (1956). Studies of independence and conformity: I. A minority of one against a unanimous majority. *Psychological Monographs*, 70(9), 1–70. https://doi.org/10.1037/h0093718
    - Wason, P. C. (1960). On the failure to eliminate hypotheses in a conceptual task. *Quarterly Journal of Experimental Psychology*, 12(3), 129–140. https://doi.org/10.1080/17470216008416717
    - Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. *Review of General Psychology*, 2(2), 175–220. https://doi.org/10.1037/1089-2680.2.2.175
    - Huber, J., Payne, J. W., & Puto, C. (1982). Adding asymmetrically dominated alternatives. *Journal of Consumer Research*, 9(1), 90–98. https://doi.org/10.1086/208899
    - Shampanier, K., Mazar, N., & Ariely, D. (2007). Zero as a special price: The true value of free products. *Marketing Science*, 26(6), 742–757. https://doi.org/10.1287/mksc.1060.0254
    - Arkes, H. R., & Blumer, C. (1985). The psychology of sunk cost. *Organizational Behavior and Human Decision Processes*, 35(1), 124–140. https://doi.org/10.1016/0749-5978(85)90049-4
    - Thorndike, E. L. (1920). A constant error in psychological ratings. *Journal of Applied Psychology*, 4(1), 25–29. https://doi.org/10.1037/h0071663
    - Norton, M. I., Mochon, D., & Ariely, D. (2012). The IKEA effect: When labor leads to love. *Journal of Consumer Psychology*, 22(3), 453–460. https://doi.org/10.1016/j.jcps.2011.08.002
    - Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse, abuse. *Human Factors*, 39(2), 230–253. https://doi.org/10.1518/001872097778543886
    - Mosier, K. L., Skitka, L. J., Heers, S., & Burdick, M. (1998). Automation bias: Decision making and performance in high-tech cockpits. *International Journal of Aviation Psychology*, 8(1), 47–63. https://doi.org/10.1207/s15327108ijap0801_3
    - Skitka, L. J., Mosier, K. L., & Burdick, M. (1999). Does automation bias decision-making? *International Journal of Human-Computer Studies*, 51(5), 991–1006. https://doi.org/10.1006/ijhc.1999.0252
    - Ebbinghaus, H. (1885). *Über das Gedächtnis*. Duncker & Humblot.
    - Murdock, B. B. (1962). The serial position effect of free recall. *Journal of Experimental Psychology*, 64(5), 482–488. https://doi.org/10.1037/h0045106
    - Kahneman, D., Fredrickson, B. L., Schreiber, C. A., & Redelmeier, D. A. (1993). When more pain is preferred to less: Adding a better end. *Psychological Science*, 4(6), 401–405. https://doi.org/10.1111/j.1467-9280.1993.tb00589.x
  - Evidencia y límites:
    - Haselton, M. G., & Buss, D. M. (2000). Error management theory: A new perspective on biases in cross-sex mind reading. *JPSP*, 78(1), 81–91. https://doi.org/10.1037/0022-3514.78.1.81
    - Hagger, M. S., Chatzisarantis, N. L. D., et al. (2016). A multilab preregistered replication of the ego-depletion effect. *Perspectives on Psychological Science*, 11(4), 546–573. https://doi.org/10.1177/1745691616652873
    - Mertens, S., Herberz, M., Hahnel, U. J. J., & Brosch, T. (2022). The effectiveness of nudging: A meta-analysis of choice architecture interventions across behavioral domains. *PNAS*, 119(1), e2107346118. https://doi.org/10.1073/pnas.2107346118
    - Maier, M., Bartoš, F., Stanley, T. D., Shanks, D. R., Harris, A. J. L., & Wagenmakers, E.-J. (2022). No evidence for nudging after adjusting for publication bias. *PNAS*, 119(31), e2200300119. https://doi.org/10.1073/pnas.2200300119
  - Normativa:
    - Reglamento (UE) 2022/2065 (Ley de Servicios Digitales), art. 25. https://eur-lex.europa.eu/eli/reg/2022/2065/oj
    - FTC, Negative Option Rule (Federal Register, 15-11-2024); *Custom Communications, Inc. v. FTC* (8th Cir., 8-7-2025); FTC, revisión de la regla para ajustarla a la sentencia (Federal Register, 12-2-2026). https://www.federalregister.gov/documents/2026/02/12/2026-02866/revision-of-the-negative-option-rule-withdrawal-of-the-cars-rule-removal-of-the-non-compete-rule-to
- Secundarias consultadas:
  - https://en.wikipedia.org/wiki/Cognitive_bias
  - https://www.nngroup.com/articles/decision-framing-cognitive-bias-ux-pros/ (Whitenton, NN/g)
  - https://bunny.deceptive.design/book/contents/chapter-13
  - https://thedecisionlab.com/insights/health/can-defaults-save-lives-the-power-of-default-options-on-life-saving-decisions
  - https://marginalrevolution.com/marginalrevolution/2018/08/presumed-consent-wales-falls-short.html
