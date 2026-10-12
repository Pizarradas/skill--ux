---
id: SIS-01
nombre: Ley de Jakob
nombre_en: Jakob's Law
alias: [Jakob's Law of Internet User Experience, ley de la experiencia de usuario en Internet, consistencia externa]
familia: SIS
evidencia: H
etiquetas: [convenciones, consistencia, expectativas, transferencia, aprendizaje, redisenos]
refuerza: [SIS-02, MEM-01, DEC-01, ACC-04, ACC-03, ACC-02]
tensiona: [PER-07, DEC-04, SIS-04, MOT-05, MEM-05]
tensiones: [T2, T13]
fuente_laws_of_ux: https://lawsofux.com/jakobs-law/
---

# SIS-01 · Ley de Jakob (*Jakob's Law*)

> Las personas acumulan casi toda su experiencia de uso en productos ajenos al tuyo y llegan con expectativas formadas allí; tu producto resultará más fácil cuanto más se comporte como esos productos en los aspectos donde existe una convención estable y compartida.

**Idea clave para quien diseña:** la novedad tiene un precio que paga la persona usuaria; sé convencional en la estructura y gasta tu originalidad donde aporte valor medible.

## Resumen operativo
- **Qué dice:** la gente llega con expectativas formadas en otros productos; cuanto más respetes las convenciones estables y compartidas, menos tendrá que aprender.
- **Evidencia:** H — heurística con respaldo indirecto (transferencia y curva de práctica); el matiz olvidado: pone un **coste** a la novedad, no la prohíbe.
- **Haz:** 1) respeta ubicación, vocabulario y comportamiento convencionales (logo a inicio, búsqueda visible, controles nativos); 2) documenta cada desviación con hipótesis de beneficio y datos; 3) en rediseños de uso diario, transición gestionada (vista previa, convivencia, vuelta atrás).
- **Evita:** clonar a un competidor concreto o confundir convención con estilo visual; lo que se transfiere es ubicación, términos y comportamiento.
- **Sospecha de esta ley cuando…:** la gente busca un elemento en «su sitio habitual» y no lo encuentra; suben los tickets tras un rediseño.
- **Mide con:** test de primer clic frente al patrón del sector; tasa de reversión y volumen de soporte durante rediseños.
- **Vecinas:** SIS-02 Modelo mental (refuerza) · MEM-01 Carga cognitiva (refuerza) · PER-07 Efecto Von Restorff (tensiona, T2) · MEM-05 Efecto de posición serial (tensiona, T13)

## Origen

- **Jakob Nielsen (2000, 23 de julio), «End of Web Design»**, columna Alertbox (useit.com; hoy en https://www.nngroup.com/articles/end-of-web-design/). Es el texto más antiguo localizado que formula la premisa y ya la bautiza como **«Jakob's Law of the Internet User Experience»**: la gente pasa la mayor parte del tiempo en *otros* sitios. Propone reducir la singularidad en diseño visual, terminología, flujos de interacción y arquitectura de información, y delegar funciones avanzadas en el navegador (atrás, marcadores). El artículo afirma que la ley «lleva varios años rigiendo la Web», refiriéndose al fenómeno; no se ha localizado una formulación escrita anterior (no verificado: búsqueda limitada al archivo de useit.com).
- **Nielsen (lista original 1996, actualizada 2011), «Top 10 Mistakes in Web Design»**, punto 8, «violar las convenciones de diseño» (https://www.nngroup.com/articles/top-10-mistakes-web-design/).
- **Nielsen (2017), vídeo «Jakob's Law of Internet User Experience»**, NN/g (https://www.nngroup.com/videos/jakobs-law-internet-ux/), que popularizó la ley con el nombre que ya tenía en 2000.
- **Base cognitiva — la curva de práctica:** Snoddy (1926, *Journal of Applied Psychology*, 10(1), 1–36) y Newell & Rosenbloom (1981, «Mechanisms of skill acquisition and the law of practice», en J. R. Anderson (Ed.), *Cognitive Skills and Their Acquisition*, pp. 1–55, Erlbaum). Aplicado a interfaces por Raluca Budiu (2016), «The Power Law of Learning: Consistency vs. Innovation in User Interfaces», NN/g (https://www.nngroup.com/articles/power-law-learning/).

## Mecanismo

**Transferencia de esquemas.** Las personas reutilizan modelos mentales (SIS-02) aprendidos en otros productos: si la interfaz encaja con el patrón conocido, el coste de aprendizaje es casi nulo y la atención queda libre para la tarea. **Curva de práctica:** el tiempo por tarea cae deprisa en las primeras repeticiones y luego se estabiliza. Un patrón convencional llega «ya practicado» (tramo plano); uno nuevo devuelve a la persona al tramo empinado, aunque al final pudiera ser más eficiente. Budiu lo ilustra con menús circulares frente a jerárquicos (Ahlström et al., CHI 2010): un diseño puede acabar siendo más rápido pero necesitar muchas más repeticiones para alcanzar su rendimiento.

Además, la previsibilidad da **sensación de control** y reduce la carga cognitiva (MEM-01); romper una convención genera duda, errores y abandono (Nielsen 2011, punto 8). Lo que más se transfiere no es el estilo visual sino la **ubicación, la terminología y el comportamiento** de los elementos.

## Evidencia y límites

- **Nivel: H** — heurística de diseño. Nielsen no aportó datos cuantitativos en 2000; la premisa («la mayor parte del tiempo se pasa fuera de tu producto») es casi aritmética para la mayoría de productos. El respaldo es indirecto: literatura de transferencia de aprendizaje, ley de la práctica y décadas de tests donde las desviaciones de convención producen errores. Solidez moderada-alta como heurística; no es una ley cuantitativa.
- **Matiz sobre la «ley potencial» de la práctica:** Heathcote, Brown & Mewhort (2000, *Psychonomic Bulletin & Review*, 7(2), 185–207) muestran que, a nivel individual, una función exponencial ajusta mejor y que la forma potencial podría ser un artefacto de promediar entre personas. La conclusión práctica no cambia: aprender cuesta y se amortiza con la repetición.
- **Cuándo pesa más:** uso infrecuente o esporádico; personas no cautivas (pueden irse a la competencia); existencia de una convención dominante real.
- **Cuándo pesa menos:** usuarios cautivos y frecuentes (herramientas internas), marcas con mucho peso o cuando el propio diseño se convierte en estándar (criterios de Budiu 2016).
- **Test para innovar (Budiu 2016):** innova solo si (1) el diseño nuevo es *claramente* mejor una vez aprendido, (2) la gente tolerará el periodo de aprendizaje y (3) puedes acelerar ese aprendizaje. Whitenton (NN/g, 2021) añade que la inconsistencia se justifica cuando el problema es realmente distinto del caso habitual.
- **Malentendidos frecuentes:**
  - *«Nunca innoves.»* Falso: la ley pone un **coste** a la novedad, no la prohíbe. Yablonski (2024, «Familiar vs Novel», lawsofux.com/articles) reconoce tres casos donde lo nuevo compensa: diferenciarse, señalar un cambio tecnológico disruptivo (cita el buscador conversacional) y experiencias de exploración o sorpresa.
  - *«Copia al líder del sector.»* La ley habla de convenciones **compartidas por muchos**, no de clonar a un competidor con patrones idiosincrásicos.
  - *«Jakob = consistencia visual.»* Importan más interacción, ubicación y vocabulario.
  - Confundir consistencia **externa** (con el ecosistema: esta ley) con consistencia **interna** (dentro del producto: también necesaria, pero distinta).

## Aplicación práctica

### Reglas

1. [H] El logotipo lleva a inicio; cuenta y carrito arriba a la derecha en interfaces LTR occidentales; la búsqueda, si es tarea principal, se muestra como campo de texto visible y no solo como icono (Nielsen 2011).
2. [E] Las etiquetas de navegación usan el vocabulario de la persona y del sector, no jerga interna; valídalo con card sorting y tree testing (fija un umbral de acierto propio por etiqueta clave).
3. [H] Los componentes base (checkbox, radio, interruptor, select, selector de fecha, botón) conservan la semántica y el comportamiento de plataforma (HTML nativo, ARIA APG, HIG, Material).
4. [H] Cada desviación de una convención se documenta en el sistema de diseño con hipótesis de beneficio y evidencia.
5. [H] Respeta los atajos y gestos del sistema: atrás, deshacer (Ctrl/Cmd+Z), gestos de borde, paleta de comandos (Ctrl/Cmd+K en herramientas de productividad).
6. [E] En rediseños de productos de uso diario, ofrece transición gestionada: vista previa opcional, convivencia temporal con la versión anterior y vía de retorno (caso del rediseño de YouTube de 2017 que recoge lawsofux; la curva de práctica justifica el coste del cambio, Budiu 2016).
7. [H] En aplicaciones empresariales, el «ecosistema» de la persona incluye hoja de cálculo y correo: imita sus convenciones (selección, copiar/pegar, filtros) para reducir formación.

### Por contexto

| Contexto | Aplicación |
|---|---|
| Web/escritorio | Cabecera, pie, migas y búsqueda donde se esperan; enlaces que parecen enlaces. |
| Móvil/táctil | Gestos y navegación de la plataforma (barra inferior, atrás del sistema); no secuestrar gestos de borde. |
| Formularios | Controles nativos; orden y nombres de campo habituales (nombre, apellidos, dirección); autocompletado estándar (`autocomplete`). |
| Navegación | Patrones dominantes del sector; un menú hamburguesa en escritorio rompe la expectativa de navegación visible. |
| E-commerce | Ficha de producto, carrito y checkout con la secuencia que la gente ya conoce. |
| Interfaces conversacionales/IA | Respeta la convención emergente (campo de entrada abajo, historial, detener/regenerar, editar, copiar). Pero la familiaridad engaña: la caja de texto evoca un **buscador** (resultados verificables) o una **persona** (memoria, intención); ninguna expectativa es correcta, así que hay que corregirlas explícitamente (véase SIS-02). |
| Sistemas de diseño | Registrar convenciones adoptadas y desviaciones; preferir componentes nativos o con semántica completa. |

### Ejemplos

- **Bueno:** un servicio de vídeo lanza un rediseño mayor permitiendo previsualizarlo, enviar comentarios y volver a la versión antigua durante un tiempo; el choque de modelo mental se amortigua.
- **Incumple:** una app social reorganiza de golpe la navegación y mezcla contenidos de amigos y medios; la gente no encuentra lo que usaba a diario y reacciona con rechazo (Yablonski menciona el rediseño de Snapchat de 2018 en «The Psychology of Design»).
- **Matiz:** una herramienta de diseño introduce un gesto nuevo para un problema que no tenía convención; supera el test de Budiu porque no existe patrón previo que romper.

## Anti-patrones

- Controles a medida que imitan los nativos sin su semántica (un `div` con aspecto de botón): fallan con teclado y lector de pantalla.
- Desplazamiento secuestrado, botón atrás que no vuelve al estado anterior.
- Terminología interna o de marca en la navegación («Espacio Nube» en vez de «Archivos»).
- Rediseño forzoso y repentino en un producto de uso diario.
- Clonar a un competidor concreto en lugar de seguir la convención general.
- Imponer convenciones occidentales (dirección LTR, formatos de fecha, colores) a públicos con otras.

## Ética y accesibilidad

- **Línea roja:** explotar la familiaridad para engañar — anuncios disfrazados de resultados, «Cancelar» con aspecto de acción primaria, casillas premarcadas en el carrito. NN/g (Chan, 2024) cita un seguro de envío añadido por defecto como violación engañosa de la expectativa «yo controlo mi carrito».
- Para quienes usan tecnologías de apoyo, la convención es aún más crítica: su modelo depende de roles y estados semánticos.
- **WCAG 2.2:** 3.2.3 Navegación coherente; 3.2.4 Identificación coherente; 3.2.6 Ayuda coherente; 4.1.2 Nombre, función, valor; 2.4.4 Propósito de los enlaces (en contexto).

## Cómo auditarla

### Señales observables
- Personas que buscan un elemento en su «sitio habitual» y no lo encuentran.
- Clics en elementos no interactivos que parecen enlaces, o enlaces que no lo parecen.
- Términos internos en menús y botones.
- Componentes con comportamiento no estándar; picos de tickets tras un rediseño.

### Preguntas
- ¿Qué productos usa más nuestro público y qué patrones comparten?
- ¿Cada desviación tiene hipótesis de beneficio y datos?
- ¿Hay plan de transición (previsualización, convivencia, retorno) para cambios grandes?
- ¿Los componentes respetan la semántica nativa?

### Métricas
- Tasa de éxito en test de primer clic frente al patrón de referencia del sector.
- Acierto por etiqueta en tree testing.
- Tiempo hasta la primera tarea completada por usuarios nuevos.
- Durante rediseños: tasa de reversión a la versión anterior y volumen de soporte.
- Evaluación heurística: «Consistencia y estándares».

## Relaciones

- Refuerza / se apoya en: SIS-02 Modelo mental — es su base teórica; Jakob es su consecuencia práctica.
- Refuerza: MEM-01 Carga cognitiva — lo conocido no ocupa recursos de aprendizaje.
- Refuerza: DEC-01 Ley de Hick — un patrón reconocido reduce decisiones.
- Refuerza: ACC-04 Paradoja del usuario activo — la gente no lee instrucciones; lo familiar no las necesita.
- Refuerza: ACC-03 Ley de Postel y ACC-02 Umbral de Doherty — tolerancia de entrada y rapidez también son expectativas aprendidas.
- Tensiona con: PER-07 Efecto Von Restorff y DEC-04 Estética-usabilidad — distintividad y marca frente a convención (T2): sé convencional en estructura y diferénciate en contenido y tono.
- Tensiona con: SIS-04 Navaja de Occam — «simplificar» puede eliminar pistas convencionales (navegación escondida).
- Tensiona con: MEM-05 Posición serial — la convención de plataforma prevalece para navegación global (T13).
- Tensiona con: MOT-05 Regla pico-final — buscar un momento memorable mediante novedad.
- Se confunde a menudo con: consistencia interna — Jakob trata de la coherencia con el ecosistema, no dentro del producto.

## Fuentes

- Laws of UX (Jon Yablonski): https://lawsofux.com/jakobs-law/ — síntesis divulgativa.
- Primarias:
  - Nielsen, J. (2000, 23 de julio). End of Web Design. Alertbox (useit.com), hoy en NN/g. https://www.nngroup.com/articles/end-of-web-design/ (versión original archivada: https://web.archive.org/web/2001/http://www.useit.com/alertbox/20000723.html)
  - Nielsen, J. (1996, act. 2011). Top 10 Mistakes in Web Design. NN/g. https://www.nngroup.com/articles/top-10-mistakes-web-design/
  - Nielsen, J. (2017). Jakob's Law of Internet User Experience (vídeo). NN/g. https://www.nngroup.com/videos/jakobs-law-internet-ux/
  - Newell, A. & Rosenbloom, P. S. (1981). Mechanisms of skill acquisition and the law of practice. En J. R. Anderson (Ed.), *Cognitive Skills and Their Acquisition* (pp. 1–55). Erlbaum.
  - Heathcote, A., Brown, S. & Mewhort, D. J. K. (2000). The power law repealed: The case for an exponential law of practice. *Psychonomic Bulletin & Review*, 7(2), 185–207. DOI 10.3758/BF03212979 (40 conjuntos de datos, 475 sujetos: la exponencial ajusta mejor en todos los datos sin promediar)
- Secundarias consultadas:
  - Budiu, R. (2016). The Power Law of Learning. https://www.nngroup.com/articles/power-law-learning/
  - NN/g, vídeo sobre interfaces inconsistentes. https://www.nngroup.com/videos/inconsistent-ui-design/
  - Yablonski, J. (2024). Familiar vs Novel. https://lawsofux.com/articles/2024/familiar-vs-novel/
  - Chan, M. (2024). Mental Models in User Experience Design. https://www.nngroup.com/articles/mental-models/
  - https://en.wikipedia.org/wiki/Power_law_of_practice
