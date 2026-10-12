# H4 · Justificar una decisión de diseño ante terceros

**Objetivo:** construir un argumento sólido para negocio, ingeniería o dirección, apoyado en
leyes y evidencia, honesto sobre la incertidumbre.
**Salida:** ficha de decisión (`07-plantillas/ficha-decision.md`).

## Estructura del argumento (5 piezas)

1. **Decisión**: qué se propone, en una frase.
2. **Problema y coste actual**: dato, observación o riesgo (tiempo, errores, abandono, soporte).
3. **Mecanismo**: qué ley(es) explican el problema y **por qué** la propuesta lo resuelve.
   Incluye nivel de evidencia y fuente primaria (`08-fuentes/`).
4. **Trade-offs**: qué se sacrifica (tensiones), qué se descartó y por qué.
5. **Cómo sabremos que funcionó**: métrica, umbral y plazo; plan de reversión si no.

## Adaptar al público

| Público | Énfasis |
|---|---|
| Negocio / producto | Métricas (conversión, retención, soporte), riesgo, coste de oportunidad. Pareto y pico-final suelen resonar. |
| Ingeniería | Coste de implementación, Tesler ("una semana de ingeniería vs. un minuto de millones de personas"), Postel, Doherty (rendimiento medible). |
| Dirección / marca | Confianza, percepción de calidad (estética-usabilidad), diferenciación vs. Jakob. |
| Legal / cumplimiento | Accesibilidad (WCAG 2.2, EAA en la UE), patrones oscuros (DSA, DMA, FTC). |

## Reglas

- No exageres: una ley E3 no "demuestra" nada; "sugiere" y "conviene probar".
- Cita fuentes primarias para afirmaciones fuertes; Laws of UX como síntesis divulgativa.
- Si la evidencia interna (datos del producto) contradice la ley, gana la evidencia interna;
  explícalo.
