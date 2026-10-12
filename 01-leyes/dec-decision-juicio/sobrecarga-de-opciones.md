---
id: DEC-02
nombre: Sobrecarga de opciones
nombre_en: Choice Overload
alias: [sobrecarga de elección, exceso de opciones, paradoja de la elección, overchoice, paradox of choice]
familia: DEC
evidencia: E3
etiquetas: [decision, surtido, ecommerce, precios, filtros, comparacion, satisfaccion]
refuerza: [DEC-01, MEM-01, MEM-02, MEM-04, DEC-03, PER-07, SIS-05]
tensiona: [SIS-03, ACC-03, SIS-02]
tensiones: [T1, T11, T12]
fuente_laws_of_ux: https://lawsofux.com/choice-overload/
---

# DEC-02 · Sobrecarga de opciones (*Choice Overload*)

> En ciertas condiciones, ampliar el surtido reduce la probabilidad de elegir, la satisfacción o la confianza en lo elegido, y aumenta el arrepentimiento y el aplazamiento. No es un efecto universal: aparece cuando se dan moderadores concretos.

**Idea clave para quien diseña:** no recortes el catálogo; reduce el surtido *efectivo* en cada momento (filtros, recomendación, comparación alineada) y compruébalo con un test.

## Origen
- Toffler, A. (1970). *Future Shock*. Acuña *overchoice*; es un ensayo, no un estudio.
- **Iyengar, S. S., & Lepper, M. R. (2000).** When choice is demotivating: Can one desire too much of a good thing? *Journal of Personality and Social Psychology*, 79(6), 995–1006. doi:10.1037/0022-3514.79.6.995. En un supermercado, una mesa de degustación con 24 mermeladas atrajo a más gente que una con 6 (se detuvo el 60 % de quienes pasaban, 145 de 242, frente al 40 %, 104 de 260), pero después compró con el cupón el 3 % de quienes se habían detenido en la mesa grande (4 personas) frente a casi el 30 % en la pequeña (31). El artículo incluye otros dos estudios (redacciones opcionales, bombones) con resultados en la misma línea.
- Schwartz, B. (2004). *The Paradox of Choice*. Ecco. Divulgación; populariza la distinción *maximizers* / *satisficers*.
- Iyengar, Huberman & Jiang (2004), "How much choice is too much? Contributions to 401(k) retirement plans", en Mitchell & Utkus (eds.), *Pension Design and Structure*, Oxford University Press, 83–96, doi:10.1093/0199273391.003.0005. Con registros de casi 800 000 empleados, cada diez fondos más se asociaron con 1,5–2 puntos menos de participación; en la curva ajustada (resto de variables en su media), la participación era del 75 % con 2 fondos y de aproximadamente el 60 % con 59. Es un estudio correlacional, no un experimento.

## Mecanismo
1. **Coste de comparación:** las comparaciones posibles crecen más deprisa que las opciones y saturan la memoria de trabajo (MEM-02).
2. **Coste de oportunidad y arrepentimiento anticipado:** cuantas más alternativas buenas se descartan, más pesa lo perdido.
3. **Expectativas elevadas:** un surtido grande promete el ajuste perfecto, y lo elegido decepciona más.
4. **Responsabilidad percibida:** si sale mal, la culpa es de quien eligió.
5. **Aplazar como salida:** no elegir evita el conflicto (statu quo, DEC-03).

Quienes buscan "lo mejor" (*maximizers*) lo sufren más que quienes buscan "lo suficiente" (*satisficers*).

## Evidencia y límites
- **Nivel: E3** — los dos metaanálisis de referencia dan lecturas distintas, y la diferencia la explican los moderadores:
  - **Scheibehenne, Greifeneder & Todd (2010)**, *Journal of Consumer Research*, 37(3), 409–425, doi:10.1086/651235. 63 condiciones de 50 experimentos (N = 5 036). **El efecto medio es prácticamente nulo** y la variabilidad entre estudios es grande; identifica precondiciones posibles, pero ninguna suficiente. El tamaño de efecto medio es D = 0,02 (IC 95 %: −0,09 a 0,12). Varias réplicas no hallaron el efecto, entre ellas una con mermeladas en un supermercado alemán (Scheibehenne 2008).
  - **Chernev, Böckenholt & Goodman (2015)**, *Journal of Consumer Psychology*, 25(2), 333–358, doi:10.1016/j.jcps.2014.08.002. 99 observaciones (N = 7 202). Al modelar moderadores, el efecto del tamaño del surtido **sí es significativo**. Cuatro factores lo facilitan:
    1. **Dificultad de la tarea:** presión de tiempo, responsabilidad, formato de presentación.
    2. **Complejidad del surtido:** sin opción dominante, atributos difíciles de alinear, opciones de atractivo parecido.
    3. **Incertidumbre de preferencias:** poca pericia, sin un ideal previo.
    4. **Meta de minimizar esfuerzo:** se quiere decidir rápido, no explorar.
    Satisfacción, arrepentimiento, aplazamiento y cambio de opción funcionan como medidas equivalentes.
- **Otros matices:** relación en **U invertida** entre número de opciones (de 2 a 20 bolígrafos) y compras (Shah & Wolford 2007, *Psychological Science*; hipótesis y diseño comprobados en el resumen, resultado no verificado en el texto); al elegir **para otros**, la sobrecarga se invierte y más opciones dan más satisfacción (Polman 2012, *JPSP*, 6 estudios); la presentación **visual** del surtido se percibe más variada y fácil, pero en surtidos grandes y con preferencias inciertas aumenta la complejidad percibida y la sobrecarga frente al texto (Townsend & Kahn 2014, *JCR*).
- **Límites:** con pericia, preferencias claras, una opción dominante o buenas herramientas de filtrado, los surtidos grandes suelen preferirse. Atraer y convertir pueden ir en direcciones opuestas: más visitas, menos compras.
- **Malentendidos frecuentes:**
  - *"La variedad vende diez veces menos".* El estudio de las mermeladas es un experimento de campo único que no se generaliza.
  - *"Nunca más de X opciones".* Ninguna fuente respalda un número mágico.
  - *Confundirla con la Ley de Hick (DEC-01).* Hick son milisegundos de reacción; esto es satisfacción y aplazamiento.
  - *Recortar catálogo sin test.* No hay garantía de que suba la conversión.

## Aplicación práctica
### Reglas
1. [E] Antes de recortar, diagnostica los cuatro moderadores de Chernev et al. (2015): si ninguno está presente, el surtido amplio probablemente no es el problema.
2. [E] Facilita la alineación de atributos: compara lado a lado con los mismos atributos en el mismo orden (Chernev et al. 2015, complejidad del surtido).
3. [H, derivada de Chernev 2015] Conserva el catálogo y reduce el surtido efectivo con filtros, facetas, ordenación útil y "recomendado".
4. [H] Si las preferencias son inciertas, haz primero pocas preguntas que filtren ("¿para qué lo usarás?") y muestra después las opciones.
5. [H] En precios, pocos planes con uno recomendado y diferencias expresadas en atributos comparables; no hay estudio que fije el número.
6. [H] En el paso de pago la meta es minimizar esfuerzo: no añadas ventas cruzadas con muchas opciones.
7. [E] Evita también el extremo contrario: ante una única opción, la gente quiere seguir buscando y aplaza la decisión (aversión a la opción única); añadir alternativas puede hacer que esa misma opción se elija más (Mochon 2013, *JCR*).
8. [H] Mide con A/B: tasa de elección y aplazamiento, pero también satisfacción, devoluciones y cambios de opción.

### Por contexto
| Contexto | Aplicación |
|---|---|
| E-commerce | Filtros y facetas visibles, orden por defecto útil, comparador de hasta unos pocos productos. |
| Precios | Tabla de planes con atributos alineados y plan recomendado; nada de matrices de 20 funciones con marcas sueltas. |
| Formularios | Desplegables largos con búsqueda; valores por defecto sensatos. |
| Onboarding/configuración | Plantillas y valores por defecto antes que un lienzo en blanco con todas las opciones. |
| Dashboards/datos | Vistas predefinidas por rol antes que un constructor de widgets vacío. |
| Conversacional/IA | Una recomendación justificada y 1–2 alternativas; si la preferencia no está clara, preguntar antes de enumerar [H]. |
| Sistemas de diseño | Componentes de comparación (tabla semántica) y de filtrado con anuncio de resultados como piezas estándar. |

### Ejemplos
- **Bueno:** una tienda de portátiles con cientos de modelos que pregunta primero el uso principal y el presupuesto, muestra tres resultados destacados y permite comparar los mismos atributos en columnas.
- **Bueno:** un asistente de IA que, ante "¿qué cámara compro?", da una recomendación razonada y dos alternativas con el motivo de cada una.
- **Lo incumple:** una operadora con catorce tarifas casi idénticas, cada una con condiciones en un formato distinto. Comparar es imposible y la mayoría acaba en la opción por defecto, que es la cara.

## Anti-patrones
- Multiplicar tarifas casi iguales para impedir la comparación (*confusopoly*).
- Planes señuelo que usan la complejidad para dirigir la elección (véase DEC-03).
- Recorte paternalista que elimina alternativas legítimas (plan barato, opción de no contratar).
- Venta cruzada con muchas opciones en el checkout.
- Citar el estudio de las mermeladas como ley universal.

## Ética y accesibilidad
- **Línea roja:** crear complejidad deliberada para que la persona no pueda comparar y caiga en el valor por defecto o en la opción cara; o quitar opciones legítimas para forzar una. El valor por defecto debe ser el que elegiría la persona informada (T12).
- Las personas con baja visión o discapacidad cognitiva sufren más los surtidos densos [H].
- WCAG 2.2: **1.3.1** Información y relaciones (tablas de comparación con `th` y `scope`); **4.1.3** Mensajes de estado (anunciar el número de resultados al filtrar, p. ej. con `aria-live`); **3.3.2** Etiquetas o instrucciones en filtros; **2.4.6** Encabezados y etiquetas.

## Cómo auditarla
### Señales observables
- Muchas visitas a listados o fichas con baja conversión.
- Entradas y salidas repetidas de la tabla de planes; muchas pestañas abiertas para comparar.
- Abandono en el paso de elegir variante.
- Tickets del tipo "¿cuál me conviene?" y devoluciones por "no era lo que esperaba".
### Preguntas
- ¿Hay una opción dominante o recomendada?
- ¿Los atributos se pueden comparar lado a lado?
- ¿El usuario típico es experto o novato? ¿Quiere explorar o terminar rápido?
- ¿Existen filtros y un orden por defecto razonable?
- ¿Quitar opciones obligaría a la persona a resolver por su cuenta lo que hoy resuelve el sistema (T1)?
### Métricas
- Tasa de elección frente a aplazamiento (abandono, "guardar para después").
- Satisfacción posterior, arrepentimiento, devoluciones y tasa de cambio de opción.
- Uso de filtros y comparador; tiempo hasta añadir al carrito.
- A/B de surtido efectivo (no del catálogo) con métricas de contrapeso.

## Relaciones
- Refuerza / se apoya en:
  - DEC-01 Ley de Hick — pariente cercano, pero mide otra cosa.
  - MEM-01 Carga cognitiva y MEM-02 Memoria de trabajo — comparar satura la capacidad.
  - MEM-04 Fragmentación — agrupar y filtrar reduce el surtido efectivo.
  - DEC-03 Sesgo cognitivo — efecto por defecto, statu quo y señuelo actúan aquí.
  - PER-07 Efecto Von Restorff — destacar el plan recomendado.
  - SIS-05 Principio de Pareto — priorizar las pocas opciones que elige la mayoría.
- Tensiona con:
  - SIS-03 Ley de Tesler — eliminar opciones puede trasladar complejidad a la persona (T1).
  - ACC-03 Ley de Postel — aceptar la diversidad real de necesidades.
  - SIS-02 Modelo mental — los expertos esperan surtidos completos.
  - T11 — fragmentar el surtido ayuda, pero lo que se compara debe verse junto.
- Se confunde a menudo con: DEC-01 Ley de Hick — tiempo de reacción frente a satisfacción y aplazamiento.

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/choice-overload/ — síntesis divulgativa.
- Primarias:
  - Iyengar, S. S., & Lepper, M. R. (2000). When choice is demotivating: Can one desire too much of a good thing? *JPSP*, 79(6), 995–1006. https://doi.org/10.1037/0022-3514.79.6.995
  - Iyengar, S. S., Huberman, G., & Jiang, W. (2004). How much choice is too much? Contributions to 401(k) retirement plans. En O. S. Mitchell & S. P. Utkus (eds.), *Pension Design and Structure* (pp. 83–96). Oxford University Press. https://doi.org/10.1093/0199273391.003.0005
  - Scheibehenne, B., Greifeneder, R., & Todd, P. M. (2010). Can there ever be too many options? A meta-analytic review of choice overload. *JCR*, 37(3), 409–425. https://doi.org/10.1086/651235
  - Chernev, A., Böckenholt, U., & Goodman, J. (2015). Choice overload: A conceptual review and meta-analysis. *JCP*, 25(2), 333–358. https://doi.org/10.1016/j.jcps.2014.08.002 (verificado en resumen; texto tras muro de pago)
  - Shah, A. M., & Wolford, G. (2007). Buying behavior as a function of parametric variation of number of choices. *Psychological Science*, 18(5), 369–370. https://doi.org/10.1111/j.1467-9280.2007.01906.x
  - Polman, E. (2012). Effects of self–other decision making on regulatory focus and choice overload. *JPSP*, 102(5), 980–993. https://doi.org/10.1037/a0026966
  - Townsend, C., & Kahn, B. E. (2014). The "visual preference heuristic". *JCR*, 40(5), 993–1015. https://doi.org/10.1086/673521
  - Mochon, D. (2013). Single-option aversion. *JCR*, 40(3), 555–566. https://doi.org/10.1086/671343
  - Toffler, A. (1970). *Future Shock*. Random House.
  - Schwartz, B. (2004). *The Paradox of Choice: Why More Is Less*. Ecco.
- Secundarias consultadas:
  - https://en.wikipedia.org/wiki/Overchoice
  - https://www.nngroup.com/articles/simplicity-vs-choice/
  - https://thedecisionlab.com/reference-guide/economics/the-paradox-of-choice
  - https://www.kellogg.northwestern.edu/faculty/research/detail/2015/when-product-assortment-leads-to-choice-overload-a-conceptual
  - https://www.jasoncollins.blog/posts/not-the-jam-study-again
