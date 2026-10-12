---
id: SIS-05
nombre: Principio de Pareto
nombre_en: Pareto Principle
alias: [regla del 80/20, pocos vitales y muchos útiles, vital few, principio de escasez de factores]
familia: SIS
evidencia: H
etiquetas: [priorizacion, distribuciones, top-tasks, roadmap, investigacion, inclusion]
refuerza: [SIS-04, DEC-01, DEC-02, MEM-05, PER-07, MOT-02, MOT-04]
tensiona: [SIS-03, ACC-03, SIS-01, DEC-03]
tensiones: [T9]
fuente_laws_of_ux: https://lawsofux.com/pareto-principle/
---

# SIS-05 · Principio de Pareto (*Pareto Principle*)

> En muchos sistemas los efectos se reparten de forma muy desigual entre las causas: una minoría de causas explica la mayoría de los resultados. «80/20» es una etiqueta mnemotécnica, no una proporción fija; lo útil es medir el grado real de concentración y actuar en consecuencia.

**Idea clave para quien diseña:** usa Pareto para decidir el **orden** del trabajo, nunca para decidir a quién dejar fuera.

## Resumen operativo
- **Qué dice:** en muchos sistemas una minoría de causas explica la mayoría de los efectos; «80/20» es un recordatorio, no una proporción fija.
- **Evidencia:** H — regularidad descriptiva muy común, nula como ratio fijo (MeasuringU: 16 % de tareas = 41 % de votos; 27 % de problemas = 72 % de fallos); el matiz olvidado: el principio como universal es de Juran, y frecuencia no es severidad.
- **Haz:** 1) construye diagramas de Pareto con datos reales (tickets, problemas, abandono por paso); 2) ordena por frecuencia × severidad × alcance; 3) reserva capacidad fija para la cola larga y la accesibilidad.
- **Evita:** eliminar funciones «poco usadas» que sirven a minorías críticas (exportación, cancelación, privacidad, tecnologías de apoyo).
- **Sospecha de esta ley cuando…:** el esfuerzo se reparte por igual sin mirar la distribución, o se cita «80/20» sin datos.
- **Mide con:** diagrama de Pareto con porcentaje acumulado por categoría; éxito de tarea desagregado por grupo.
- **Vecinas:** SIS-04 Navaja de Occam (refuerza) · DEC-02 Sobrecarga de opciones (refuerza) · SIS-03 Ley de Tesler (tensiona, T9) · ACC-03 Ley de Postel (tensiona)

## Origen

- **Vilfredo Pareto**, economista. En *Cours d'économie politique* (Lausana, 1896–1897) documenta distribuciones de renta muy desiguales y propone modelos matemáticos para cuantificarlas (lo confirma Juran, 1974; obra de Pareto no leída). El dato de que el 20 % de la población poseía el 80 % de la tierra italiana se repite en todas partes, pero las fuentes lo sitúan en obras y fechas distintas (Wikipedia lo cita del *Manuale di economia politica*, 1906; Sauro 2012 lo fecha en 1906) [?: no localizado en el texto de Pareto]. La anécdota de las vainas de guisantes de su huerto no aparece en ninguna fuente primaria consultada [?: probable embellecimiento posterior].
- **Joseph M. Juran** observó la concentración de defectos desde mediados de los años 20; a finales de los 40 la consideró un «universal» y, al preparar la 1.ª edición del *Quality Control Handbook* (1951, pp. 37–41), la bautizó «principio de Pareto»; acuñó «los pocos vitales y los muchos triviales» (primer uso publicado probable en 1954). En **«The Non-Pareto Principle; Mea Culpa»** (texto del archivo del Juran Institute, fechado en 1974; suele citarse en *Quality Progress*, mayo de 1975, dato no verificado) reconoce que se equivocó al atribuirlo a Pareto, cuyo trabajo se limitaba a la economía, y que las curvas acumuladas debían atribuirse a Lorenz. El resumen del Juran Institute añade que más tarde cambió «muchos triviales» por **«muchos útiles»** (*useful many*). Es decir: el principio como universal es de Juran, no de Pareto, como el propio Juran admitió.
- **Base matemática:** distribuciones potenciales (de Pareto); con un índice α = log₄5 ≈ 1,16 sale exactamente un 80/20 (comprobado: 0,2^(1−1/α) = 0,8).
- La fuente que declara lawsofux (Bhowmick, «The 80/20 Rule in User Experience», IBM Design / Medium) no ha podido consultarse.

## Mecanismo

Muchos fenómenos de uso son **acumulativos**: lo más visible recibe más uso, y el uso lo hace más visible (ventaja acumulada), lo que genera distribuciones de cola larga. En UX aparece en la frecuencia de tareas, el uso de funciones, la distribución de problemas de usabilidad, los comentarios de mejora, los tickets de soporte y los ingresos por cliente.

La herramienta canónica es el **diagrama de Pareto**: barras ordenadas de mayor a menor con una línea de porcentaje acumulado (Sunwall, NN/g 2021). El principio describe la concentración; **no explica por qué** ocurre en cada caso (Sunwall 2021), así que no sustituye a la investigación cualitativa.

## Evidencia y límites

- **Nivel: H** — alta solidez como **regularidad descriptiva** (las distribuciones sesgadas son ubicuas), nula como **ratio fijo**. Es una regla práctica, no una ley natural.
- **Datos UX — concentración, pero no 80/20** (Sauro, MeasuringU, 12-09-2012):
  - Tareas principales: 222 personas eligieron sus 5 tareas más importantes entre 94 posibles; las 15 primeras (16 %) reunieron el 41 % de los votos.
  - Comentarios de mejora en tests: 2 temas = 50 % de los comentarios; 5 temas = 75 %.
  - Problemas de usabilidad en una web de alquiler de coches (50 participantes): 33 problemas únicos, 181 ocurrencias; 9 problemas (27 %) explican el 72 % de las interacciones fallidas.
  - Conclusión de Sauro: la concentración es habitual pero el cociente varía, y las dos cifras **no tienen por qué sumar 100** (miden cosas distintas).
- **Límites:**
  - **Severidad ≠ frecuencia:** un problema raro puede ser grave (pérdida de datos, exclusión). En calidad se complementa con análisis de modos de fallo (FMEA) o árbol de fallos.
  - Problemas pequeños que crecen quedan fuera del radar.
  - **Tamaño muestral:** con cinco tickets no hay distribución (IxDF).
  - **Ponderación:** un problema raro de clientes de alto valor o de un grupo vulnerable puede tener prioridad.
  - Optimizar solo «lo vital» puede producir estancamiento y sobreoptimización de pocas métricas (Sunwall 2021).
- **Malentendidos frecuentes:**
  - *80/20 como proporción fija u objetivo* («recorta el 80 % de funciones»).
  - *«El 80 % de la gente usa el 20 % de las funciones; elimina el resto.»* Cada persona usa un 20 % *distinto*; la unión puede cubrir casi todo el producto. La cifra muy repetida de que la mayoría de funciones «nunca se usan», atribuida a un informe de Standish Group de 2002, tiene metodología poco documentada: no la uses como evidencia.
  - Confundir frecuencia con importancia: exportar la nómina una vez al mes es raro y crítico.
  - Atribuir el principio a Pareto en lugar de a Juran.

## Aplicación práctica

### Reglas

1. [E] Construye diagramas de Pareto con datos reales: tickets por causa, problemas de usabilidad por frecuencia, abandono por paso del embudo (Sunwall 2021; Sauro 2012).
2. [H] Ordena por **frecuencia × severidad × alcance**, no solo por frecuencia.
3. [H] Ataca primero las categorías hasta ~70–80 % del acumulado, **reservando capacidad explícita** (p. ej. una fracción fija de cada ciclo) para la cola larga y la accesibilidad.
4. [H] Identifica las tareas principales (votación de tareas al estilo de Gerry McGovern) y dales la máxima visibilidad en inicio y navegación principal; el resto, accesible por búsqueda y navegación secundaria.
5. [H] Optimiza el default para el comportamiento mayoritario observado y mueve los ajustes de minoría a «avanzado» — **sin eliminarlos** si esa minoría los necesita.
6. [H] Sistemas de diseño: invierte primero calidad (accesibilidad, rendimiento, documentación) en los componentes que cubren la mayor parte de las pantallas.
7. [H] No presentes «80/20» a stakeholders sin la distribución real.

### Por contexto

| Contexto | Aplicación |
|---|---|
| Navegación | Tareas principales visibles; cola larga vía búsqueda. |
| Dashboards/datos | Diagrama de Pareto para priorizar; mostrar la distribución real, no el eslogan. |
| E-commerce | Optimizar los embudos de más tráfico, sin degradar devoluciones, cancelaciones o reclamaciones. |
| Onboarding | Enseñar las pocas acciones que generan más valor inicial; no diseñarlo solo para los usuarios intensivos. |
| Interfaces conversacionales/IA | Analizar logs de intenciones: las pocas más frecuentes merecen respuestas excelentes y atajos (sugerencias, plantillas); para la cola larga, buena degradación (pedir aclaración, derivar a una persona). Evaluar el modelo también en casos raros y de alto riesgo (salud, finanzas) que nunca aparecerían en el top. |
| Sistemas de diseño | Inventario de uso de componentes para priorizar inversión. |
| Investigación | Síntesis de hallazgos ordenada por frecuencia × severidad; Pareto recorta alcance, no sustituye el «porqué». |

### Ejemplos

- **Bueno:** un equipo agrupa los tickets del trimestre por causa; tres causas explican la mayoría y se priorizan, mientras una fracción fija del ciclo se dedica a problemas de accesibilidad aunque generen pocos tickets.
- **Incumple:** se elimina la exportación de datos «porque la usa el 2 %»; ese 2 % eran contables que la necesitaban cada cierre de mes.
- **Incumple:** un asistente de IA se evalúa solo con las 50 preguntas más frecuentes y falla en consultas médicas poco comunes pero de alto riesgo.

## Anti-patrones

- «El resto no importa»: tratar la cola como desechable.
- Recortar funciones que sirven a minorías críticas (exportación, cancelación, privacidad) por «poco uso».
- Confundir la métrica con el valor: optimizar lo que mueve más tráfico a costa del bienestar.
- Falsa precisión: «80/20» sin datos.
- Repartir el esfuerzo de forma uniforme sin mirar la distribución (el error opuesto).

## Ética y accesibilidad

- **Línea roja:** usar el volumen para excluir. Las personas que usan lector de pantalla, con baja conectividad o de idiomas minoritarios son, estadísticamente, la «cola»; si solo cuenta el volumen, la accesibilidad nunca entra en el roadmap. **La accesibilidad es un requisito, no una apuesta de retorno.** Los principios «Resilient» e «Inclusive» de *Humane by Design* (diseñar para los casos límite y la diversidad) son el contrapeso explícito.
- **WCAG 2.2:** ningún criterio de nivel A/AA es «priorizable fuera»; en especial 2.1.1 Teclado; 1.4.4 Cambio de tamaño del texto; 1.4.10 Reajuste (reflow); 3.3.1 Identificación de errores; 4.1.2 Nombre, función, valor.

## Cómo auditarla

### Señales observables
- Roadmap sin datos de frecuencia ni severidad.
- Esfuerzo repartido uniformemente; páginas top con problemas conocidos sin resolver.
- O al revés: ninguna capacidad reservada para la cola ni para accesibilidad.

### Preguntas
- ¿Cuál es la distribución real (no supuesta) de tareas, problemas y tickets?
- ¿Cómo ponderamos severidad e impacto en grupos vulnerables?
- ¿Qué parte del esfuerzo va a los «muchos útiles»?
- ¿El tamaño de la muestra justifica la conclusión?

### Métricas
- Diagrama de Pareto con porcentaje acumulado por categoría.
- Evolución trimestral del volumen de las categorías top.
- Porcentaje de capacidad dedicado a cola y accesibilidad.
- Éxito de tarea desagregado por grupo (tecnologías de apoyo, idioma, dispositivo).

## Relaciones

- Refuerza / se apoya en: SIS-04 Navaja de Occam — ayuda a decidir qué conservar.
- Refuerza: DEC-01 Ley de Hick y DEC-02 Sobrecarga de opciones — destacar pocas opciones frecuentes.
- Refuerza: MEM-05 Posición serial y PER-07 Efecto Von Restorff — colocar y resaltar las tareas principales.
- Refuerza: MOT-02 Gradiente de meta — acortar los embudos de más tráfico.
- Refuerza: MOT-04 Ley de Parkinson — acotar el esfuerzo a lo vital.
- Tensiona con: SIS-03 Ley de Tesler — optimizar para la mayoría puede descargar complejidad sobre la minoría (T9): prioriza el orden, no excluyas.
- Tensiona con: ACC-03 Ley de Postel — la robustez ante entradas atípicas exige atender la cola.
- Tensiona con: SIS-01 Ley de Jakob — las convenciones mayoritarias pueden no servir a grupos específicos.
- Tensiona con: DEC-03 Sesgo cognitivo — el sesgo de disponibilidad distorsiona qué parece «vital».
- Se confunde a menudo con: una proporción fija o una ley natural — es una regularidad descriptiva de concentración.

## Fuentes

- Laws of UX (Jon Yablonski): https://lawsofux.com/pareto-principle/ — síntesis divulgativa.
- Primarias:
  - Pareto, V. (1896–1897). *Cours d'économie politique*. Lausana: F. Rouge. (obra no leída; vía Wikipedia y Juran)
  - Juran, J. M. (1974). The Non-Pareto Principle; Mea Culpa. Archivo del Juran Institute: https://www.juran.com/wp-content/uploads/2021/03/The-Non-Pareto-Principle-1974.pdf (texto leído; publicación en *Quality Progress*, mayo de 1975, no verificada)
  - Juran, J. M. (Ed.) (1951). *Quality Control Handbook* (1.ª ed., pp. 37–41). McGraw-Hill. (citado por Juran 1974; no leído)
  - Sauro, J. (2012). Applying the Pareto Principle to the User Experience. MeasuringU. https://measuringu.com/pareto-ux/
- Secundarias consultadas:
  - Sunwall, E. (2021). Prioritize Quantitative Data with the Pareto Principle. NN/g. https://www.nngroup.com/articles/pareto-principle/
  - IxDF. The Pareto Principle and Your User Experience Work. https://ixdf.org/literature/article/the-pareto-principle-and-your-user-experience-work
  - https://en.wikipedia.org/wiki/Pareto_principle
  - No accesibles: Bhowmick, The 80/20 Rule in User Experience (Medium, 403); Siegel, Good UX is not just about minimizing clicks (UX Collective, 403).
