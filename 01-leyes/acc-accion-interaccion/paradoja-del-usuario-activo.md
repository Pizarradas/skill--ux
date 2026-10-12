---
id: ACC-04
nombre: Paradoja del usuario activo
nombre_en: Paradox of the Active User
alias: [paradoja de producción, paradoja de asimilación, usuarios que no leen manuales]
familia: ACC
evidencia: E2
etiquetas: [onboarding, ayuda-contextual, aprendizaje, tutoriales, estados-vacios, descubrimiento, expertos]
refuerza: [SIS-01, SIS-02, MEM-01, MEM-02, SIS-04, SIS-03, ACC-03]
tensiona: [MOT-01, DEC-01, SIS-05, PER-06]
tensiones: [T14, T9, T2]
fuente_laws_of_ux: https://lawsofux.com/paradox-of-the-active-user/
---

# ACC-04 · Paradoja del usuario activo (*Paradox of the Active User*)

> Las personas se ponen a usar un sistema para lograr su objetivo inmediato sin leer antes manuales ni tutoriales, aunque dedicar un poco de tiempo a aprender les ahorraría tiempo a la larga; y una vez que un procedimiento "funciona", tienden a quedarse con él aunque sea ineficiente.

**Idea clave para quien diseña:** diseña para quien empieza a tocar sin leer: que la interfaz se entienda sola y que la ayuda aparezca en el momento y lugar en que se necesita.

## Resumen operativo
- **Qué dice:** la gente se pone a usar el sistema sin aprender antes y se queda con procedimientos que "funcionan" aunque sean ineficientes.
- **Evidencia:** E2 — observaciones de IBM y estudios posteriores (Fu y Gray, 2004); se olvida que sí se busca ayuda cuando hay un atasco, en contexto.
- **Haz:** 1) que la tarea principal funcione sin instrucciones previas 2) ayuda justo a tiempo, en el punto de uso 3) exploración segura: deshacer, vista previa, *training wheels*.
- **Evita:** tutoriales iniciales tipo baraja de tarjetas o *coach marks* obligatorios: NN/g no halló mejora del rendimiento.
- **Sospecha de esta ley cuando…:** alta tasa de "Saltar" en el onboarding; veteranos que nunca usan atajos.
- **Mide con:** test de primer uso sin instrucciones (éxito, tiempo); éxito posterior con y sin tutorial; adopción de atajos.
- **Vecinas:** SIS-01 Ley de Jakob (refuerza) · ACC-03 Ley de Postel (refuerza) · PER-06 Atención selectiva (tensiona, T14) · SIS-05 Principio de Pareto (tensiona, T9)

## Origen
- **Carroll, J. M. y Rosson, M. B. (1987). "Paradox of the active user".** En J. M. Carroll (ed.), *Interfacing Thought: Cognitive Aspects of Human-Computer Interaction*, MIT Press, pp. 80–111 (páginas según registros bibliográficos; capítulo no consultado). Resultado de observaciones en el IBM User Interface Institute a principios de los años 80: los usuarios nuevos no leían los manuales, se lanzaban a usar el sistema y tropezaban con errores y bloqueos.
- Carroll y Rosson la descomponen en dos paradojas:
  - **Paradoja de producción:** la motivación por terminar la tarea impide aprender; la persona se instala en procedimientos subóptimos pero "suficientes".
  - **Paradoja de asimilación:** el conocimiento previo ayuda a entender lo nuevo, pero también provoca errores cuando la analogía no se sostiene.
- Trabajos asociados de Carroll:
  - **Carroll y Carrithers (1984), "Training wheels in a user interface"**, *Communications of the ACM*, 27(8), 800–806, doi:10.1145/358198.358218: hacer inalcanzables los estados de error típicos produjo un aprendizaje sustancialmente más rápido y mejor comprensión posterior; el grupo de control pasó casi una cuarta parte de su tiempo recuperándose de esos errores. Versión ampliada: Carroll y Carrithers (1984), *Human Factors*, 26(4), 377–389.
  - Catrambone y Carroll (1987), "Learning a word processing system with training wheels and guided exploration", *CHI+GI '87*, 169–174.
  - Carroll (1990), *The Nurnberg Funnel: Designing Minimalist Instruction for Practical Computer Skill*, MIT Press: base de la **instrucción minimalista**.
- **Fu y Gray (2004)**, "Resolving the paradox of the active user: stable suboptimal performance in interactive tasks", *Cognitive Science*, 28(6), 901–935: explican por qué incluso expertos persisten en procedimientos ineficientes (preferencia por procedimientos genéricos y bien practicados, hechos de acciones interactivas con retroalimentación inmediata).
- Nielsen (1998), "Paradox of the Active User", NN/g.

## Mecanismo
La motivación está anclada a la tarea inmediata, no al aprendizaje. Leer documentación tiene un coste seguro y presente y un beneficio incierto y futuro, así que se descarta (descuento temporal). Cuando un procedimiento consigue el resultado, queda reforzado aunque sea lento: según Fu y Gray, se prefieren procedimientos generales hechos de acciones interactivas, porque cada acción cambia la pantalla y sugiere la siguiente (poco esfuerzo cognitivo inmediato), aunque a la larga exijan más esfuerzo; la elección se repite en cada paso y desemboca en un rendimiento subóptimo estable.

Ante algo nuevo, la persona razona por analogía con sistemas que ya conoce (asimilación). Si la analogía es válida, aprende deprisa; si no, comete errores sistemáticos difíciles de diagnosticar. Por eso la paradoja es a la vez un problema de aprendizaje y de modelo mental (SIS-02).

## Evidencia y límites
- **Nivel: E2** — patrón observado y reproducido en múltiples estudios observacionales desde los años 80 (IBM; Nielsen señala que muchos estudios posteriores lo confirman). Las soluciones de Carroll (*training wheels*, manual mínimo, exploración guiada) tienen apoyo experimental de la época. La magnitud depende del dominio y del perfil.
- **Evidencia sobre tutoriales:** NN/g (Kendrick, 2020) encontró que los **tutoriales tipo "baraja de tarjetas" al abrir una app no mejoraron el rendimiento** en las tareas.
- **Límites:**
  - En dominios de alto riesgo (sanidad, aviación) y en software profesional con formación obligatoria la gente sí se forma.
  - Personas con baja autoeficacia pueden preferir guía previa.
  - "Nadie lee nada" es exagerado: se consulta la ayuda **cuando hay un atasco**, en contexto, en buscadores o en vídeos.
- **Malentendidos frecuentes:**
  - "La ayuda no sirve" → la ayuda sirve si está en el momento y lugar de la necesidad.
  - "Solución: más *coach marks* al inicio" → es exactamente lo que la paradoja predice que se ignorará.
  - "Es pereza" → es una decisión racional a corto plazo dado el coste de aprender.

## Aplicación práctica
### Reglas
1. [E/H] Diseña y prueba primero sin onboarding; añádelo solo si un prototipo demuestra una mejora medible del éxito — NN/g (Kendrick, 2020).
2. [E] Evita la baraja de tarjetas inicial; si se usa, breve, un concepto por tarjeta y "Saltar" muy visible — NN/g.
3. [H] Reserva el onboarding para cuando hace falta información para empezar, hay alta personalización o funciones genuinamente nuevas; limita la configuración inicial a lo imprescindible.
4. [H] Ayuda justo a tiempo: *tooltips* bajo demanda para iconos o términos poco claros; destaca una función cuando se vuelve útil (p. ej. estadísticas cuando ya hay datos) — T14.
5. [H] Convierte los mensajes de error en momentos de aprendizaje: qué pasó y cómo resolverlo (3.3.3).
6. [H] Estados vacíos que enseñan haciendo: acción primaria clara o datos de ejemplo.
7. [E] *Training wheels* actuales: modos simplificados para principiantes y bloqueo de acciones peligrosas hasta que se entiendan — Carroll y Carrithers (1984); Catrambone y Carroll (1987).
8. [H] Facilita la exploración segura: deshacer generoso, vista previa, entornos de prueba y confirmación solo en lo irreversible.
9. [H] Asimilación: aprovecha convenciones conocidas (SIS-01) y avisa explícitamente donde el sistema rompe la analogía.
10. [H] Rompe el estancamiento de producción: sugiere el atajo cuando detectes un procedimiento lento repetido ("Puedes hacerlo con ⌘K"), descartable y sin insistir.

### Por contexto
| Contexto | Aplicación |
|---|---|
| Onboarding | Sin muros obligatorios; empezar por la tarea real; configuración mínima y diferida. |
| Web/escritorio | Ayuda en el punto de uso; mecanismo de ayuda en ubicación consistente (3.2.6); descubrimiento progresivo de atajos. |
| Móvil/táctil | Nada de tutoriales iniciales largos; pistas en contexto que no tapen controles ni desaparezcan para siempre con un toque accidental. |
| Formularios | Instrucciones de formato en la etiqueta; tolerancia de entrada (ACC-03) para quien no las lee. |
| Dashboards/datos | Estados vacíos con datos de ejemplo; explicación de métricas en *tooltip* accesible. |
| Interfaces conversacionales/IA | Ejemplos de *prompts* o *chips* en el estado vacío; límites explicados en contexto ("No tengo acceso a tu calendario; conéctalo aquí"); responder bien a "¿qué puedes hacer?". |
| Voz | Aceptar formulaciones libres; ofrecer sugerencias tras un fallo, no una lista larga de comandos al inicio. |
| Sistemas de diseño | Componentes de ayuda contextual, estado vacío y *tooltip* con reglas de cuándo usarlos y cuándo no. |

### Ejemplos
- **Bueno:** un editor que, al abrir un documento vacío, muestra tres acciones de inicio y, la primera vez que la persona selecciona texto, una pista breve sobre el menú de formato que no vuelve a aparecer.
- **Incumple:** una app que obliga a pasar seis pantallas de tutorial antes de poder hacer nada, sin opción de saltar.
- **Incumple:** documentación disponible solo como PDF externo, sin ayuda dentro del producto.

## Anti-patrones
- Muros de onboarding obligatorios y no saltables.
- *Coach marks* que tapan la interfaz y se pierden para siempre tras un toque accidental.
- Ayuda solo en un portal o PDF externo.
- Funciones avanzadas sin ningún camino de descubrimiento.
- Insistir con el mismo consejo una y otra vez.

## Ética y accesibilidad
- **Línea roja:** aprovechar que "no leen" para esconder condiciones importantes (suscripciones, renovaciones, permisos de datos) en textos largos que se sabe que no se leerán.
- WCAG 2.2: **1.4.13 Content on Hover or Focus** (AA: *tooltips* descartables, persistentes y sobrevolables; accesibles por teclado); **3.3.2 Labels or Instructions** (A: las instrucciones necesarias deben estar presentes en el punto de uso, no solo en un tutorial previo); **3.3.3 Error Suggestion** (AA); **3.3.5 Help** (AAA); **3.2.6 Consistent Help** (A, nuevo en 2.2); **2.1.2 No Keyboard Trap** (A: superposiciones de tutorial con gestión de foco y cierre con Esc).

## Cómo auditarla
### Señales observables
- Alta tasa de "Saltar" en el onboarding; tutoriales completados sin efecto en el éxito posterior.
- Errores repetidos en el primer uso; errores por analogía equivocada.
- Veteranos que siguen usando menús en lugar de atajos.
### Preguntas
- ¿Se puede completar la tarea principal sin instrucciones previas?
- ¿Hay ayuda en el punto de uso y en una ubicación consistente?
- ¿Los estados vacíos y los errores enseñan qué hacer?
- ¿Dónde rompe el sistema las convenciones conocidas y se avisa de ello?
### Métricas
- Test de primer uso sin instrucciones: éxito, tiempo, si se abre la ayuda y si se encuentra lo buscado.
- Finalización del tutorial frente a retención y éxito posterior (comparar con y sin tutorial).
- Visitas al centro de ayuda y términos buscados.
- Adopción de funciones avanzadas y uso de atajos en usuarios veteranos.

## Relaciones
- Refuerza / se apoya en: SIS-01 Ley de Jakob — las convenciones conocidas facilitan la asimilación.
- Refuerza / se apoya en: SIS-02 Modelo mental — la asimilación es razonar con el modelo previo.
- Refuerza / se apoya en: MEM-01 Carga cognitiva / MEM-02 Memoria de trabajo — un tutorial previo no se recuerda al llegar a la tarea.
- Refuerza / se apoya en: SIS-04 Navaja de Occam — menos que aprender, menos que enseñar.
- Refuerza / se apoya en: SIS-03 Ley de Tesler — la complejidad que la persona no quiere aprender debe absorberla el sistema.
- Refuerza / se apoya en: ACC-03 Ley de Postel — tolerar entradas de quien no leyó las instrucciones.
- Tensiona con: PER-06 Atención selectiva — tooltips y tours compiten por la atención; ayuda bajo demanda y en el momento de necesidad (T14).
- Tensiona con: MOT-01 Flujo — el flujo exige habilidad, y la persona activa evita el aprendizaje que la daría; escalar habilidad dentro de la tarea.
- Tensiona con: DEC-01 Ley de Hick — mostrar todo para que se descubra alarga la decisión; divulgación progresiva.
- Tensiona con: SIS-05 Principio de Pareto — centrarse en el 20 % de funciones deja sin descubrir las avanzadas (T9).
- Se confunde a menudo con: "los usuarios son perezosos" — es una elección racional a corto plazo; y con la Ley de Jakob — Jakob habla de expectativas por otros sitios, la paradoja de no invertir en aprender.

## Fuentes
- Laws of UX (Jon Yablonski): https://lawsofux.com/paradox-of-the-active-user/ — síntesis divulgativa.
- Primarias:
  - Carroll, J. M. y Rosson, M. B. (1987). Paradox of the active user. En J. M. Carroll (ed.), *Interfacing Thought: Cognitive Aspects of Human-Computer Interaction* (pp. 80–111). MIT Press (capítulo no consultado).
  - Carroll, J. M. y Carrithers, C. (1984). Training wheels in a user interface. *Communications of the ACM*, 27(8), 800–806. doi:10.1145/358198.358218
  - Carroll, J. M. y Carrithers, C. (1984). Blocking learner error states in a training-wheels system. *Human Factors*, 26(4), 377–389. doi:10.1177/001872088402600402
  - Catrambone, R. y Carroll, J. M. (1987). Learning a word processing system with training wheels and guided exploration. *CHI+GI '87*, 169–174. doi:10.1145/29933.275625
  - Carroll, J. M. (1990). *The Nurnberg Funnel: Designing Minimalist Instruction for Practical Computer Skill*. MIT Press.
  - Fu, W.-T. y Gray, W. D. (2004). Resolving the paradox of the active user: stable suboptimal performance in interactive tasks. *Cognitive Science*, 28(6), 901–935. doi:10.1207/s15516709cog2806_2
- Secundarias consultadas:
  - Nielsen, J. (1998). Paradox of the Active User. NN/g: https://www.nngroup.com/articles/paradox-of-the-active-user/
  - Kendrick, A. (2020). Mobile-App Onboarding: An Analysis of Components and Techniques. NN/g: https://www.nngroup.com/articles/mobile-app-onboarding/
  - Apuntes de curso (Middlesex University) sobre Carroll: https://cwa.mdx.ac.uk/bis4407/lec12Examples/carroll.html
  - No accedidos: PDF de Carroll y Rosson en ResearchGate; "Onboarding for Active Users" de Laws of UX.
