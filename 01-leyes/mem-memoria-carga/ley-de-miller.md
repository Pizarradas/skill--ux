---
id: MEM-03
nombre: Ley de Miller
nombre_en: Miller's Law
alias: [el número mágico siete, 7±2, span de memoria inmediata, magical number seven]
familia: MEM
evidencia: E2
etiquetas: [memoria, capacidad, chunks, mito-7, reconocimiento-vs-recuerdo]
refuerza: [MEM-02, MEM-04, MEM-01, DEC-01, DEC-02, SIS-03]
tensiona: [ACC-04, SIS-01]
tensiones: [T1, T11]
fuente_laws_of_ux: https://lawsofux.com/millers-law/
---

# MEM-03 · Ley de Miller (*Miller's Law*)

> La memoria inmediata está limitada por el número de unidades significativas (chunks) que puede mantener, no por la cantidad de información que contienen. Miller situó ese límite "en torno a siete" para ciertos materiales; con el ensayo controlado, la investigación posterior lo sitúa en unos cuatro chunks (3–5).

**Idea clave para quien diseña:** minimiza lo que la persona tiene que *retener sin verlo*; no uses el "7±2" para decidir cuántas cosas caben en un menú.

## Resumen operativo
- **Qué dice:** la memoria inmediata se limita en unidades significativas (chunks), no en bits; con el ensayo controlado son unas 4 (3–5), no 7.
- **Evidencia:** E2 — el límite es robusto, pero la cifra depende del material, el ensayo y la persona. Se olvida que Miller habló de dos fenómenos distintos y desconfiaba de su propio "siete".
- **Haz:** 1) cuenta los datos que la persona debe retener sin verlos; si pasan de 3–4, muéstralos o persístelos 2) agrupa y formatea automáticamente las cadenas largas 3) decide el tamaño de los menús con arquitectura de la información y pruebas de árbol.
- **Evita:** limitar menús visibles a "7±2": un menú visible se reconoce, no se recuerda.
- **Sospecha de esta ley cuando…:** la gente apunta datos en papel o vuelve atrás para consultarlos; hay menús de voz largos.
- **Mide con:** datos que hay que retener sin verlos por paso; tasa de error al transcribir códigos.
- **Vecinas:** MEM-04 Fragmentación (refuerza) · DEC-01 Ley de Hick (refuerza) · ACC-04 Paradoja del usuario activo (tensiona, T1)

## Origen
**Miller, G. A. (1956).** "The magical number seven, plus or minus two: Some limits on our capacity for processing information." *Psychological Review*, 63(2), 81–97. DOI: 10.1037/h0043158. (Reimpreso en 1994: *Psychological Review*, 101(2), 343–352.)

El artículo trata **dos fenómenos distintos** que a menudo se mezclan:
1. **Juicio absoluto:** identificar estímulos que varían en una sola dimensión (tonos, intensidades). La capacidad de canal media ronda los 2,6 bits (desviación típica 0,6), es decir, unas 6,5 categorías distinguibles (rango de 3 a 15 según la dimensión).
2. **Span de memoria inmediata:** cuántos elementos se repiten tras oírlos una vez. Aquí el límite **no es constante en bits sino en chunks**: según los datos de Hayes que Miller cita, el span ronda 9 dígitos binarios y 5 palabras monosilábicas, mucho menos de lo que predeciría un límite fijo de información.

Miller introdujo además la **recodificación**: Sidney Smith, que se entrenó a sí mismo en agrupar dígitos binarios y renombrar cada grupo, con un span de 12 dígitos octales, llegó a retener 36 dígitos binarios con grupos de 3 (recodificación octal) y unos 40 con grupos de 4 y 5. Y cerró el texto sospechando que la coincidencia de tantos "sietes" era probablemente una coincidencia "pitagórica" y perniciosa. **Miller nunca propuso el 7 como ley universal.**

Revisiones clave:
- **Cowan (2001)**, *Behavioral and Brain Sciences*, 24(1), 87–114, y **Cowan (2010)**, *Current Directions in Psychological Science*, 19(1), 51–57: cuando se impide el ensayo y la recodificación, el almacén central se limita a unos **3–5 elementos significativos** en adultos jóvenes (≈4).
- **Mathy & Feldman (2012)**, *Cognition*, 122(3), 346–362: el span de "7" puede explicarse por compresión, equivalente a unos 4 chunks de información comprimida.
- Debate abierto sobre la naturaleza del límite: "huecos" discretos (**Luck & Vogel 1997**, *Nature*: unos 4 objetos visuales) frente a un recurso continuo (**Ma, Husain & Bays 2014**, *Nature Neuroscience*).

## Mecanismo
La memoria de trabajo (MEM-02) mantiene activas pocas representaciones a la vez con ayuda de la atención. Lo que cuenta es la unidad **significativa para esa persona**: "FBI-CIA-NASA" son 3 chunks para quien conoce las siglas y 11 letras para quien no. Por eso la capacidad efectiva depende del conocimiento previo, del idioma, de la edad y de si se puede ensayar en voz baja (bucle fonológico). La fragmentación (MEM-04) es la estrategia que aprovecha este mecanismo.

## Evidencia y límites
- **Nivel: E2** — que la memoria inmediata es muy limitada y se mide en unidades significativas es un hallazgo robusto; la cifra concreta depende del material, del ensayo y de la persona, y el número "7" está superado.
- **Revisión del número:** 7±2 refleja spans con ensayo y recodificación posibles; el límite central con ensayo controlado es ~4 (Cowan). IxDF propone usar "4±1" como referencia de diseño, aunque el valor exacto sigue en debate.
- **Mito principal: "los menús deben tener 7±2 opciones".** Es falso por dos razones:
  1. Un menú visible apela al **reconocimiento**, no al recuerdo: la persona no tiene que retener las opciones porque las está viendo (NN/g, Moran 2016).
  2. El límite de Miller se refiere a la **retención sin apoyo externo**, no a la cantidad de elementos que pueden mostrarse.
  Algunos autores han llamado a este mal uso "superstición" o "leyenda urbana" (Bailey 2000, "Reducing Reliance on Superstition (Let's Start with Miller's 'Magic 7')", Human Factors International; Jones 2002, "The 7±2 Urban Legend", MISRA C Conference).
- **Mito secundario: "el juicio absoluto y el span son lo mismo".** Corrección: son dos fenómenos; solo el primero se comporta como un canal de bits.
- La propia síntesis de Laws of UX advierte que no debe usarse el "número mágico" para justificar limitaciones de diseño innecesarias, y que la capacidad varía entre personas y contextos.

## Aplicación práctica
### Reglas
1. [E en su base, H en el umbral] Cuenta cuántos datos debe *recordar* la persona sin tenerlos a la vista para completar un paso; si son más de 3–4, rediseña: muéstralos, persístelos o agrúpalos.
2. [E] Formatea las cadenas largas en grupos (tarjeta 4-4-4-4, IBAN en bloques de 4, teléfono según la convención local) y aplica el formato automáticamente al escribir (NN/g, Moran 2016).
3. [H] Decide el número de ítems de un menú por arquitectura de la información, escaneo y DEC-01 Hick, **nunca** por 7±2.
4. [H] No recortes contenido útil ni escondas opciones necesarias apelando a Miller.
5. [H] En canales donde nada permanece visible (voz, audio), limita las opciones por turno; un tope de 3–5 es heurístico.
6. [H] Diseña para la capacidad de tu público, no la del equipo: los equipos suelen tener más capacidad disponible y más familiaridad (NN/g, Budiu 2018).

### Por contexto
| Contexto | Aplicación |
|---|---|
| Formularios | No pedir recordar códigos entre pantallas; mostrar número de pedido o referencia donde se necesite; agrupar cadenas largas. |
| Navegación | El tamaño del menú lo decide la arquitectura de la información y las pruebas de árbol, no un número mágico. |
| Móvil/táctil | Lo que queda fuera de pantalla hay que recordarlo: resúmenes persistentes en procesos largos. |
| Voz | Pocas opciones por turno, la más probable primero, opción de repetir y de hablar con una persona (W3C COGA 4.7.4). |
| Interfaces conversacionales/IA | Si el asistente ofrece opciones, preséntalas como botones o *chips*, no como texto que haya que recordar y teclear. |
| Dashboards/datos | Evitar que la persona tenga que memorizar valores de una vista para compararlos en otra. |
| Sistemas de diseño | Documentar el mito: no fijar topes de ítems "por Miller" en componentes de menú o pestañas. |

### Ejemplos
- **Bueno:** un campo de IBAN que inserta espacios cada 4 caracteres mientras se escribe y muestra el valor agrupado en la pantalla de confirmación.
- **Incumple (mal uso de la ley):** un equipo reduce la navegación principal a 7 entradas "por la ley de Miller" y esconde secciones muy usadas en un menú "Más". La gente ya no encuentra lo que veía; el límite no se aplicaba porque el menú era visible.
- **Incumple (la ley sí aplica):** un menú telefónico que enumera nueve opciones seguidas antes de dejar elegir.

## Anti-patrones
- Recortar contenido o funciones "porque no caben más de 7".
- Citar "7±2" como justificación en revisiones de diseño.
- Cadenas largas sin agrupar (referencias, claves de licencia, números de cuenta).
- Obligar a recordar un dato de una pantalla para usarlo en otra.
- Menús de voz largos sin opción de repetir.

## Ética y accesibilidad
- **Línea roja:** usar el "límite de memoria" como pretexto para ocultar opciones que perjudican al negocio (cancelar, rechazar) detrás de "Más opciones".
- Las personas con discapacidades cognitivas o de aprendizaje, las personas mayores y quien está con estrés o fatiga tienen spans menores.
- WCAG 2.2: **3.3.7 Entrada redundante** (A); **3.3.8 Autenticación accesible (mínima)** (AA).
- W3C COGA (nota no normativa): objetivo 6 "Ensure processes do not rely on memory".

## Cómo auditarla
### Señales observables
Usuarios que apuntan datos en papel, hacen capturas, abren otra pestaña para consultar algo o vuelven atrás para releer.
### Preguntas
- ¿Qué tiene que recordar el usuario entre el paso N y el N+1?
- ¿Algún límite numérico del diseño se justifica con "7±2"?
- ¿Hay cadenas largas sin agrupar?
- En voz o audio, ¿cuántas opciones se ofrecen por turno?
### Métricas
- Recuento de "datos a retener sin verlos" por paso (objetivo ≤ 3–4, mejor 0) [H].
- Tasa de error en transcripción de códigos y referencias.
- Pruebas de árbol (*tree testing*) para decidir el tamaño y la estructura de los menús en lugar de un número fijo.
- En menús de voz: tasa de "repetir opciones" y de transferencia a persona.

## Relaciones
- Refuerza / se apoya en: MEM-02 Memoria de trabajo — Miller es una estimación (histórica) de su capacidad.
- Refuerza / se apoya en: MEM-04 Fragmentación — el concepto de chunk nace en este artículo; agrupar es la forma de sortear el límite.
- Refuerza / se apoya en: MEM-01 Carga cognitiva — superar el límite es una forma de sobrecarga.
- Refuerza / se apoya en: DEC-01 Ley de Hick y DEC-02 Sobrecarga de opciones — son las leyes pertinentes para el tamaño de un menú visible, no Miller.
- Refuerza / se apoya en: SIS-03 Ley de Tesler — trasladar al sistema la carga de recordar.
- Tensiona con: ACC-04 Paradoja del usuario activo — un tope rígido esconde opciones que los usuarios necesitan encontrar.
- Tensiona con: SIS-01 Ley de Jakob — hay menús largos convencionales y familiares que funcionan bien.
- Se confunde a menudo con: DEC-01 Ley de Hick — Hick trata del tiempo de decisión entre opciones visibles; Miller, de lo que se retiene sin verlo.
- Se confunde a menudo con: el juicio absoluto (también en Miller 1956) — es otro fenómeno, limitado en bits.

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/millers-law/ — síntesis divulgativa.
- Primarias:
  - Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review*, 63(2), 81–97. https://doi.org/10.1037/h0043158 (texto: https://psychclassics.yorku.ca/Miller/)
  - Miller, G. A. (1994). Reimpresión. *Psychological Review*, 101(2), 343–352. https://doi.org/10.1037/0033-295X.101.2.343
  - Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, 24(1), 87–114. https://doi.org/10.1017/S0140525X01003922
  - Cowan, N. (2010). The magical mystery four: How is working memory capacity limited, and why? *Current Directions in Psychological Science*, 19(1), 51–57. https://doi.org/10.1177/0963721409359277
  - Mathy, F. & Feldman, J. (2012). What's magic about magic numbers? Chunking and data compression in short-term memory. *Cognition*, 122(3), 346–362. https://doi.org/10.1016/j.cognition.2011.11.003
  - Luck, S. J. & Vogel, E. K. (1997). *Nature*, 390, 279–281. https://doi.org/10.1038/36846
  - Ma, W. J., Husain, M. & Bays, P. M. (2014). *Nature Neuroscience*, 17(3), 347–356. https://doi.org/10.1038/nn.3655
- Secundarias consultadas:
  - Bailey, B. (2000). Reducing Reliance on Superstition (Let's Start with Miller's "Magic 7"). Human Factors International. http://www.humanfactors.com/downloads/sep00.asp (título y contenido verificados a través de la cita de Jerz 2002: https://jerz.setonhill.edu/blog/2002/11/12/702/)
  - Jones, D. M. (2002). The 7±2 Urban Legend. MISRA C Conference. https://www.shape-of-code.com/cbook/misart.pdf
  - Moran, K. (2016). How Chunking Helps Content Processing. NN/g. https://www.nngroup.com/articles/chunking/
  - Budiu, R. (2018). Working Memory and External Memory. NN/g. https://www.nngroup.com/articles/working-memory-external-memory/
  - IxDF, Chunking (glosario). https://ixdf.org/literature/book/the-glossary-of-human-computer-interaction/chunking
  - W3C COGA, Making Content Usable. https://www.w3.org/TR/coga-usable/
  - Wikipedia, Miller's law. https://en.wikipedia.org/wiki/Miller%27s_law
