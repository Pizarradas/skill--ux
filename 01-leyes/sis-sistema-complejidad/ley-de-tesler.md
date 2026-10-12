---
id: SIS-03
nombre: Ley de Tesler (conservación de la complejidad)
nombre_en: Tesler's Law
alias: [Law of Conservation of Complexity, ley de conservación de la complejidad, teoría del colchón de agua, waterbed theory]
familia: SIS
evidencia: H
etiquetas: [complejidad, defaults, automatizacion, divulgacion-progresiva, sistemas-de-diseno, ia]
refuerza: [ACC-04, MEM-01, DEC-01, DEC-02, ACC-03, ACC-02]
tensiona: [SIS-04, SIS-02, SIS-05]
tensiones: [T1, T9]
fuente_laws_of_ux: https://lawsofux.com/teslers-law/
---

# SIS-03 · Ley de Tesler (*Tesler's Law*)

> Toda aplicación o proceso contiene un núcleo de complejidad que no puede eliminarse; el diseño solo decide quién lo carga: la persona usuaria, quien desarrolla la aplicación o quien construye la plataforma. Siempre que sea posible, debe cargarlo el equipo, porque el coste se multiplica por cada persona usuaria.

**Idea clave para quien diseña:** antes de quitar algo, pregunta «¿quién hará esto ahora?»; si la respuesta es «la persona», no has simplificado, has trasladado.

## Resumen operativo
- **Qué dice:** toda tarea tiene una complejidad esencial que no desaparece; el diseño decide si la carga la persona usuaria, el producto o la plataforma.
- **Evidencia:** H — marco de decisión argumentado, no ley medible; el matiz olvidado: solo la complejidad **esencial** es irreducible, la accidental sí se elimina.
- **Haz:** 1) infiere lo inferible y no pidas dos veces el mismo dato; 2) usa defaults seguros, visibles y modificables; 3) toda automatización muestra qué decidió y ofrece corrección o deshacer.
- **Evita:** usar «el dominio es complejo» para justificar una interfaz complicada, o absorber complejidad de forma opaca.
- **Sospecha de esta ley cuando…:** se piden datos que el sistema ya tiene; la gente usa hojas de cálculo o notas externas para completar la tarea.
- **Mide con:** número de campos deducibles que se piden (objetivo 0); porcentaje de cambio de cada default; en IA, reformulaciones por objetivo y tiempo de verificación.
- **Vecinas:** ACC-03 Ley de Postel (refuerza) · DEC-01 Ley de Hick (refuerza) · SIS-04 Navaja de Occam (tensiona, T1) · SIS-05 Principio de Pareto (tensiona, T9)

## Origen

- **Larry Tesler, hacia 1984.** Su web personal (nomodes.com, página «Complexity Law») titula la cita «Original Formulation (ca. 1984)» y la enuncia así, en esencia: cada aplicación tiene una complejidad inherente e irreducible; la única cuestión es quién debe ocuparse de ella: la persona usuaria, quien desarrolla la aplicación o quien desarrolla la plataforma.
- **Lugar: Apple, no Xerox PARC.** lawsofux y Wikipedia sitúan el origen en Xerox PARC a mediados de los años 80, pero el propio Tesler, en la entrevista con Dan Saffer, cuenta que en PARC surgió el argumento económico a favor de la consistencia y que formuló la ley **en Apple, entre 1983 y 1985**, mientras desarrollaba el framework MacApp, para convencer a la dirección y a desarrolladores externos de adoptar una capa de «aplicación genérica» compartida. La versión «PARC» es una lectura errónea de esa entrevista.
- **Dan Saffer, *Designing for Interaction*** (New Riders, 1.ª ed. 2006, subtítulo *Creating Smart Applications and Clever Devices*; 2.ª ed. 2010, *Creating Innovative Applications and Devices*): incluye la entrevista con Tesler donde aparece el argumento económico — si un millón de personas pierden un minuto al día por una complejidad que un ingeniero podría eliminar en una semana, se penaliza a la persona usuaria para facilitar el trabajo del ingeniero. Texto de la entrevista leído en la web del libro (archivada en 2009); capítulo y página en el libro no verificados (Wikipedia indica 2.ª ed., cap. 7, p. 136; el libro no es accesible en abierto).
- **Contrapunto: Bruce Tognazzini (septiembre de 1998), «The Complexity Paradox»**, AskTog (https://asktog.com/columns/011complexity.html): combinando la ley de Tesler con su «ley del desplazamiento» (*Tog's Law of Commuting*, 1996), sostiene que, cuando se reduce la complejidad de una tarea, la gente emprende tareas más exigentes, de modo que la complejidad *experimentada* tiende a mantenerse.
- En el libro de Yablonski *Laws of UX* (2020) es el capítulo 9.

## Mecanismo

Conviene separar **complejidad esencial** (inherente al dominio: un pago exige importe, destinatario, método y autorización) y **complejidad accidental** (introducida por la implementación). La distinción procede de Fred Brooks, «No Silver Bullet» (1986; versión en *Computer*, 1987), no de Tesler. La ley de Tesler habla de la esencial; la accidental sí puede eliminarse, y ese es el terreno de SIS-04 Occam.

La complejidad esencial se **desplaza**, no desaparece. Autocompletar destinatarios, heredar la dirección de facturación como dirección de envío, pagar con cartera digital o interpretar consultas en lenguaje natural trasladan trabajo de la persona al sistema (ejemplos del artículo de Yablonski 2024). Farnam Street («Why Life Can't Be Simpler», 2020) añade dos matices: quitar controles visibles puede hacer la tarea *más* difícil, y la automatización total deja a la gente mal preparada cuando falla (pilotos, conducción automatizada).

## Evidencia y límites

- **Nivel: H** — principio de ingeniería y diseño argumentado, no ley empírica. No existe forma de medir la complejidad total «conservada»; úsese como **marco de decisión** («¿quién paga este coste y cuántas veces?»), no como ley física.
- **No toda complejidad es irreducible.** Invocar Tesler para justificar una interfaz complicada («el dominio es complejo») es un abuso frecuente: buena parte suele ser accidental.
- **Paradoja de Tognazzini:** simplificar no reduce la complejidad vivida porque la gente sube el listón; el argumento económico sigue en pie, pero «producto simple» es un objetivo móvil.
- **Absorber toda la complejidad tiene costes:** opacidad, pérdida de control, fallos graves cuando la automatización se equivoca y personas que no pueden corregir al sistema. Mantener cierta participación preserva la sensación de control (Farnam Street).
- **Simplificar hasta la abstracción:** Yablonski (2024) advierte contra interfaces tan reducidas que pierden significado.
- **Malentendidos frecuentes:**
  - *«Tesler = minimalismo.»* No: absorber complejidad puede exigir *más* trabajo y a veces más UI (previsualizaciones, validación en línea).
  - *«Trasladar la complejidad al experto está bien.»* Solo si es elección suya, mediante divulgación progresiva.

## Aplicación práctica

### Reglas

1. [H] Infiere todo lo inferible: ciudad a partir del código postal, tipo de tarjeta por sus dígitos, país sugerido (nunca impuesto) por la ubicación. Objetivo: cero campos obligatorios que el sistema pueda deducir.
2. [H] No pidas nunca dos veces el mismo dato en un flujo (alineado con WCAG 3.3.7).
3. [H] El valor por defecto es el equipo absorbiendo una decisión: elige defaults seguros y útiles para la mayoría, siempre visibles y modificables. Si más de la mitad de las personas cambia un ajuste, el default probablemente es erróneo (umbral orientativo).
4. [E] En aplicaciones complejas, reduce el desorden **sin reducir capacidad**: divulgación progresiva, aprender haciendo sin riesgo (deshacer, borradores), sugerencias de métodos más eficientes en contexto, ayuda para seguir el hilo (historial, notas) (Kaplan, NN/g 2020, «8 Design Guidelines for Complex Applications»). En dominios críticos, aprender haciendo no basta: hace falta formación.
5. [H] Los componentes del sistema de diseño encapsulan la complejidad recurrente (validación, estados de carga/error/vacío, accesibilidad) — exactamente el argumento original de Tesler a favor de librerías compartidas.
6. [H] Toda automatización muestra qué decidió y ofrece vía de corrección o deshacer.
7. [H] En el roadmap, registra por épica *dónde* queda la complejidad (persona / producto / plataforma / soporte) y su coste.

### Por contexto

| Contexto | Aplicación |
|---|---|
| Formularios | Autocompletado, formatos flexibles (con ACC-03), validación en línea, datos arrastrados entre pasos. |
| E-commerce | Facturación = envío por defecto, carteras de pago, direcciones guardadas. |
| Onboarding | Plantillas iniciales y configuración por defecto en lugar de cuestionarios largos. |
| Dashboards/datos | Vistas predefinidas útiles; filtros avanzados accesibles pero plegados. |
| Sistemas de diseño | Componentes con estados y accesibilidad resueltos de serie. |
| Interfaces conversacionales/IA | La interfaz por intención («dime qué quieres») traslada la complejidad de navegar al sistema, pero crea un coste nuevo: **articular la intención** por escrito, la llamada «barrera de articulación» descrita por Jakob Nielsen («The Articulation Barrier: Prompt-Driven AI UX Hurts Usability», UX Tigers, 25-05-2023; reproducido en su boletín de Substack), que estima que cerca de la mitad de la población de los países ricos no escribe con la soltura necesaria para obtener buenos resultados de un chatbot. Mitígalo con sugerencias de prompt, plantillas, preguntas de aclaración y resultados editables. Además, la complejidad reaparece como **verificación**: la persona debe comprobar la respuesta. Diseña para verificar barato: citas, diffs, previsualización, deshacer. Y que el sistema mantenga el contexto en lugar de obligar a repetirlo. |
| Voz | Sin pantalla, el sistema debe absorber más: confirmar interpretaciones, resumir opciones. |

### Ejemplos

- **Bueno:** un checkout detecta el tipo de tarjeta al teclear, rellena la ciudad desde el código postal y propone la dirección de facturación como de envío; la persona revisa en lugar de teclear.
- **Incumple:** un formulario exige la fecha «DD/MM/AAAA sin espacios» y rechaza «3-4-2026»; la complejidad de normalizar se la queda la persona.
- **Incumple (exceso):** un agente de IA ejecuta cambios en varios documentos sin mostrar lo que hizo; la complejidad no desapareció, se convirtió en una auditoría posterior imposible.

## Anti-patrones

- Trasladar complejidad a la persona por comodidad del equipo: formatos rígidos, errores con códigos internos.
- Trasladarla al soporte o a terceros invisibles (centros de llamadas, moderación) sin contabilizarla.
- Eliminar funciones avanzadas en vez de escalonarlas.
- Automatización opaca sin explicación ni deshacer.
- «Simplificar» quitando opciones de privacidad o de baja: trasladar complejidad *en contra* de la persona.

## Ética y accesibilidad

- **Línea roja:** automatizar decisiones que afectan a personas (crédito, salud, empleo) sin explicación ni vía de corrección; el principio «Empowering» de *Humane by Design* pide una persona en el circuito (*human in the loop*) para entender y revisar decisiones de IA.
- Si la complejidad se desplaza a interacciones finas (gestos ocultos, hover, arrastre), se excluye a quienes usan teclado, lector de pantalla o tienen temblor. La divulgación progresiva debe anunciar su estado expandido/plegado.
- **WCAG 2.2:** 3.3.7 Entrada redundante; 3.3.8 Autenticación accesible (mínima); 2.5.7 Movimientos de arrastre; 2.5.1 Gestos del puntero; 3.3.4 Prevención de errores (legales, financieros, datos); 4.1.2 Nombre, función, valor (estado de controles desplegables).

## Cómo auditarla

### Señales observables
- Campos que piden datos que el sistema ya tiene.
- Instrucciones largas junto a los campos.
- Personas con hojas de cálculo o notas externas para completar la tarea.
- Muchos tickets sobre la misma tarea.
- Automatizaciones sin explicación ni deshacer.

### Preguntas
- ¿Cuál es la complejidad esencial de esta tarea y cuál la accidental?
- ¿Quién la carga hoy? ¿Cuántas personas × cuántas veces?
- ¿Qué pasa cuando la automatización falla? ¿La persona puede ver y corregir lo que se decidió?
- En IA: ¿cuánto cuesta formular la petición y cuánto verificar la respuesta?

### Métricas
- Número de campos deducibles que se piden (objetivo 0).
- Porcentaje de cambio de cada default.
- Tiempo y errores por tarea; volumen de soporte por tarea.
- En IA: reformulaciones por objetivo, tiempo de verificación, correcciones y deshacer tras acciones automáticas.

## Relaciones

- Refuerza / se apoya en: ACC-04 Paradoja del usuario activo — la guía contextual absorbe complejidad que nadie leería en un manual.
- Refuerza: MEM-01 Carga cognitiva — lo que absorbe el sistema no ocupa a la persona.
- Refuerza: DEC-01 Ley de Hick y DEC-02 Sobrecarga de opciones — buenos defaults reducen decisiones.
- Refuerza: ACC-03 Ley de Postel — aceptar entradas flexibles es absorber variabilidad.
- Refuerza: ACC-02 Umbral de Doherty — la latencia es complejidad trasladada a la persona en forma de espera.
- Tensiona con: SIS-04 Navaja de Occam — quitar frente a absorber (T1): elimina lo innecesario, absorbe lo necesario, difiere lo avanzado.
- Tensiona con: SIS-02 Modelo mental — la absorción opaca deja modelos erróneos; absorber con visibilidad.
- Tensiona con: SIS-05 Principio de Pareto — optimizar para la mayoría puede descargar la complejidad sobre la minoría (T9).
- Se confunde a menudo con: minimalismo — Tesler trata de reubicar complejidad, no de reducir elementos visibles.

## Fuentes

- Laws of UX (Jon Yablonski): https://lawsofux.com/teslers-law/ — síntesis divulgativa.
- Primarias:
  - Tesler, L. The Law of Conservation of Complexity (web personal, «Complexity Law»). https://www.nomodes.com/computing-history
  - Tesler, L., entrevistado por D. Saffer (c. 2006). Larry Tesler Interview. designingforinteraction.com, archivada: https://web.archive.org/web/20090216232522/http://www.designingforinteraction.com/tesler.html
  - Saffer, D. (2006; 2.ª ed. 2010). *Designing for Interaction*. New Riders. (libro no consultado; capítulo y página de la entrevista no verificados)
  - Tognazzini, B. (1998, septiembre). The Complexity Paradox. AskTog. https://asktog.com/columns/011complexity.html
  - Nielsen, J. (2023, 25 de mayo). The Articulation Barrier: Prompt-Driven AI UX Hurts Usability. UX Tigers. https://www.uxtigers.com/post/ai-articulation-barrier
  - Brooks, F. P. (1987). No Silver Bullet: Essence and Accidents of Software Engineering. *Computer*, 20(4), 10–19. DOI 10.1109/MC.1987.1663532 (metadatos verificados en Crossref; texto no leído; la versión de 1986 no se ha verificado)
- Secundarias consultadas:
  - Yablonski, J. (2024). Tesler's Law. https://lawsofux.com/articles/2024/teslers-law/
  - https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity
  - Farnam Street (2020). Why Life Can't Be Simpler. https://fs.blog/2020/10/why-life-cant-be-simpler/
  - Kaplan, K. (2020). 8 Design Guidelines for Complex Applications. NN/g. https://www.nngroup.com/articles/complex-application-design/
  - NN/g, vídeo «Tesler's Law». https://www.nngroup.com/videos/teslers-law/
  - Nielsen, J. (2023, 18 de junio). AI: First New UI Paradigm in 60 Years. NN/g. https://www.nngroup.com/articles/ai-paradigm/
